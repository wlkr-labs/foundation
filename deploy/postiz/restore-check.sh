#!/usr/bin/env bash
# No application or worker starts; the restore network has no outbound route.
set -euo pipefail
cd "$(dirname "$0")"
umask 077
set -a
source images.env
source "${POSTIZ_OPERATOR_ENV:?Set operator.env}"
set +a
stamp=${1:?Backup timestamp required}
[[ "$stamp" =~ ^[0-9]{8}T[0-9]{6}Z$ ]]
mountpoint -q "$POSTIZ_DATA_MOUNT"
mountpoint -q "$POSTIZ_BACKUP_MOUNT"
[[ "$(findmnt -n -o TARGET --target "$POSTIZ_ROOT")" == "$POSTIZ_DATA_MOUNT" ]]
testroot="$POSTIZ_ROOT/restore-check-$stamp"
[[ ! -e "$testroot" ]]
mkdir -p "$testroot"
# Read the secondary drive without changing its protected backup permissions.
docker --host unix:///var/run/docker.sock run --rm --network none \
  --mount "type=bind,src=$POSTIZ_BACKUP_MOUNT/postiz-snapshots/$stamp,dst=/backup,readonly" \
  --mount "type=bind,src=$testroot,dst=/restore" \
  -e OPERATOR_UID="$(id -u)" -e OPERATOR_GID="$(id -g)" \
  "$POSTIZ_POSTGRES_IMAGE" sh -ec \
  'cp -a /backup /restore/backup; chown -R "$OPERATOR_UID:$OPERATOR_GID" /restore/backup'
backup="$testroot/backup"
(cd "$backup" && sha256sum -c SHA256SUMS)
network="wlkrlabs-postiz-restore-$stamp"
docker --host unix:///var/run/docker.sock network create --internal "$network" >/dev/null
cleanup() {
  docker --host unix:///var/run/docker.sock rm -f "postiz-restore-$stamp" "temporal-restore-$stamp" "redis-restore-$stamp" "elasticsearch-restore-$stamp" >/dev/null 2>&1 || true
  docker --host unix:///var/run/docker.sock network rm "$network" >/dev/null
}
trap cleanup EXIT
for role in postiz temporal; do
  image=$POSTIZ_POSTGRES_IMAGE
  [[ "$role" == temporal ]] && image=$TEMPORAL_POSTGRESQL_IMAGE
  mkdir -p "$testroot/$role-postgres"
  docker --host unix:///var/run/docker.sock run -d --name "$role-restore-$stamp" \
    --network "$network" -e POSTGRES_HOST_AUTH_METHOD=trust \
    --mount "type=bind,src=$testroot/$role-postgres,dst=/var/lib/postgresql/data" "$image" >/dev/null
  for attempt in $(seq 1 60); do
    docker --host unix:///var/run/docker.sock exec "$role-restore-$stamp" pg_isready -U postgres >/dev/null 2>&1 && break
    sleep 1
  done
done
pg() { docker --host unix:///var/run/docker.sock exec -i "postiz-restore-$stamp" "$@"; }
tp() { docker --host unix:///var/run/docker.sock exec -i "temporal-restore-$stamp" "$@"; }
pg createdb -U postgres postiz
pg pg_restore -U postgres -d postiz --no-owner --no-privileges --exit-on-error < "$backup/postiz.dump"
# Invalidate live channel, user, API, webhook and OAuth credentials before reads.
pg psql -U postgres -d postiz -v ON_ERROR_STOP=1 <<'SQL'
UPDATE "Integration" SET token='', "refreshToken"=NULL, disabled=true, "customInstanceDetails"=NULL;
UPDATE "Organization" SET "apiKey"=NULL;
UPDATE "User" SET password=NULL, "providerId"=NULL;
TRUNCATE "OAuthAuthorization", "OAuthSelfHostedAuthorization", "Webhooks", "IntegrationsWebhooks", "ThirdParty" CASCADE;
SELECT count(*) AS restored_users FROM "User";
SELECT count(*) AS restored_drafts FROM "Post" WHERE state='DRAFT';
SELECT count(*) AS usable_channel_credentials FROM "Integration" WHERE token<>'' OR "refreshToken" IS NOT NULL;
SQL
for database in temporal; do
  tp createdb -U postgres "$database"
  tp pg_restore -U postgres -d "$database" --no-owner --no-privileges --exit-on-error < "$backup/$database.dump"
  tp psql -U postgres -d "$database" -Atc "SELECT count(*) FROM information_schema.tables WHERE table_schema='public';"
done
docker --host unix:///var/run/docker.sock run --rm --network none \
  --mount "type=bind,src=$backup,dst=/backup,readonly" \
  --mount "type=bind,src=$testroot,dst=/restore" \
  "$POSTIZ_POSTGRES_IMAGE" sh -ec 'tar xzf /backup/files.tar.gz -C /restore state/uploads state/redis state/elasticsearch; find /restore/state/uploads -type f -exec sha256sum {} \; > /restore/media-sha256.txt'
docker --host unix:///var/run/docker.sock run -d --name "redis-restore-$stamp" \
  --network "$network" --mount "type=bind,src=$testroot/state/redis,dst=/data" \
  "$POSTIZ_REDIS_IMAGE" redis-server --appendonly yes >/dev/null
docker --host unix:///var/run/docker.sock run -d --name "elasticsearch-restore-$stamp" \
  --network "$network" --mount "type=bind,src=$testroot/state/elasticsearch,dst=/usr/share/elasticsearch/data" \
  -e discovery.type=single-node -e xpack.security.enabled=false \
  -e ES_JAVA_OPTS='-Xms512m -Xmx512m' "$TEMPORAL_ELASTICSEARCH_IMAGE" >/dev/null
ready=false
for attempt in $(seq 1 90); do
  if docker --host unix:///var/run/docker.sock exec "elasticsearch-restore-$stamp" \
    curl -fsS 'http://localhost:9200/_cluster/health?wait_for_status=yellow&timeout=2s' > "$testroot/elasticsearch-health.json"; then
    ready=true
    break
  fi
  sleep 2
done
[[ "$ready" == true ]]
docker --host unix:///var/run/docker.sock exec "redis-restore-$stamp" redis-cli ping | grep -qx PONG
docker --host unix:///var/run/docker.sock exec "redis-restore-$stamp" redis-cli dbsize
docker --host unix:///var/run/docker.sock exec "elasticsearch-restore-$stamp" \
  curl -fsS 'http://localhost:9200/_cat/indices?v'
echo "Isolated SQL, media, Redis and Elasticsearch restore passed; no application/worker or live credentials started."
echo "Publishing workflow execution remains untested."
