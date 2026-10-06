#!/usr/bin/env bash
# Quiesce only this stack; logical SQL dumps and cold workflow/media files agree.
set -euo pipefail
cd "$(dirname "$0")"
umask 077
set -a
source images.env
source "${POSTIZ_OPERATOR_ENV:?Set operator.env}"
set +a
mountpoint -q "$POSTIZ_DATA_MOUNT"
mountpoint -q "$POSTIZ_BACKUP_MOUNT"
[[ "$(findmnt -n -o TARGET --target "$POSTIZ_ROOT")" == "$POSTIZ_DATA_MOUNT" ]]
exec 9>"$POSTIZ_ROOT/backup.lock"
flock -n 9
stamp=$(date -u +%Y%m%dT%H%M%SZ)
destination="$POSTIZ_ROOT/backups/$stamp"
mkdir -p "$destination"
resume() { ./project up -d >/dev/null; }
trap resume EXIT
./project stop postiz temporal temporal-elasticsearch postiz-redis
./project exec -T postiz-postgres pg_dump -U postiz-user -d postiz-db-local -Fc > "$destination/postiz.dump"
for database in temporal temporal_visibility; do
  ./project exec -T temporal-postgresql pg_dump -U temporal -d "$database" -Fc > "$destination/$database.dump"
done
docker --host unix:///var/run/docker.sock run --rm --network none \
  --mount "type=bind,src=$POSTIZ_ROOT,dst=/source,readonly" \
  --mount "type=bind,src=$destination,dst=/backup" \
  -e OPERATOR_UID="$(id -u)" -e OPERATOR_GID="$(id -g)" \
  "$POSTIZ_POSTGRES_IMAGE" sh -ec \
  'umask 077; tar czf /backup/files.tar.gz -C /source state/config state/uploads state/redis state/elasticsearch operator releases; chown "$OPERATOR_UID:$OPERATOR_GID" /backup/files.tar.gz'
(
  cd "$destination"
  sha256sum ./*.dump files.tar.gz > SHA256SUMS
)
docker --host unix:///var/run/docker.sock run --rm --network none \
  --mount "type=bind,src=$destination,dst=/source,readonly" \
  --mount "type=bind,src=$POSTIZ_BACKUP_MOUNT,dst=/backup-drive" \
  -e BACKUP_STAMP="$stamp" "$POSTIZ_POSTGRES_IMAGE" sh -ec \
  'umask 077; mkdir -p /backup-drive/postiz-snapshots; cp -a /source /backup-drive/postiz-snapshots/"$BACKUP_STAMP"; cd /backup-drive/postiz-snapshots/"$BACKUP_STAMP"; sha256sum -c SHA256SUMS'
printf '%s\n' "$stamp" > "$POSTIZ_ROOT/backups/latest"
./project up -d --wait --wait-timeout 240
trap - EXIT
# Retain 14 successful daily backups; older local snapshots follow host policy.
mapfile -t old < <(find "$POSTIZ_ROOT/backups" -mindepth 1 -maxdepth 1 -type d -name '20*T*Z' | sort -r | tail -n +15)
for directory in "${old[@]}"; do rm -rf -- "$directory"; done
docker --host unix:///var/run/docker.sock run --rm --network none \
  --mount "type=bind,src=$POSTIZ_BACKUP_MOUNT,dst=/backup-drive" \
  "$POSTIZ_POSTGRES_IMAGE" sh -ec \
  'find /backup-drive/postiz-snapshots -mindepth 1 -maxdepth 1 -type d -name "20*T*Z" | sort -r | tail -n +15 | while read -r directory; do rm -rf -- "$directory"; done'
echo "Consistent Postiz backup complete: $stamp"
