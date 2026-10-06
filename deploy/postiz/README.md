# WLKR Labs Postiz on Octal8

This directory owns the free self-hosted deployment at https://social.wlkrlabs.com.
Follow the [setup checklist](../../docs/postiz-octal8-setup-checklist.md) and
[social handoff](../../docs/social-setup-handoff.md). Execution evidence, actual
operator paths, account/channel IDs and credential item IDs are in ignored
`private/postiz/`. No public posting automation is enabled by this deployment.

## Release and architecture

Upstream Compose: `gitroomhq/postiz-docker-compose` commit
`dd4969e5e694cd009619a0d53cff14c21104580b`. Application: Postiz `v2.25.0`.
Every application/dependency image is pinned in `images.env`; optional Temporal
administration tools/UI require the `operations` profile and expose no ports.
The current upstream application image contains frontend, API and workflow workers.
This third-party Node runtime is retained under the owning 0o10 Rust-first policy;
small shell scripts coordinate existing Compose/systemd interfaces.

Use system Docker, project `wlkrlabs-postiz`, assigned mounted data/backup drives,
and shared Caddy `octal8-edge`. Application and workflow networks are separate;
workflow is internal. Only Postiz and Caddy join external `octal8-postiz`.
No application/database/Temporal ports are published. Caddy keeps its reserved
LAN bind, fixed frontend address, certificate storage, existing routes and
Tailscale management. No new firewall/router rules are required.

Compared with upstream: remove sample credentials, fixed container names, host
port mappings, spotlight and production-inappropriate development cache refresh;
use project-scoped networks, bind persistent state to the assigned data drive,
use local uploads, single-owner registration, SMTP, bounded logs and digest pins.
Stripe, AI, paid storage and unused provider keys remain unset. SSRF and production
cookie protections stay enabled. Database credentials and JWT are independent.

## Operator configuration and startup

Keep a mode-0700 project root and `operator/` outside Git on the assigned drive.
The mode-0600 `operator.env` supplies `POSTIZ_ROOT`, `POSTIZ_DATA_MOUNT` and
`POSTIZ_BACKUP_MOUNT`; none belongs in public source. `operator/postiz.env`
supplies DATABASE_URL, JWT_SECRET, EMAIL_USER, EMAIL_PASS and approved provider
keys. `postgres.env` and `temporal-postgres.env` supply their POSTGRES_PASSWORD;
`temporal.env` supplies POSTGRES_PWD. Their recoverable originals are distinct
Hosting items in the owner-only WLKR Labs Social vault. SMTP stays in its
existing mailbox Login; do not move or replace it.

Stage a clean committed copy of this directory under `releases/<commit>/`.
Create state directories for config, uploads, postgres, redis, temporal-postgres
and elasticsearch. Elasticsearch writes as UID 1000. Confirm the existing
Docker `RequiresMountsFor` and `After` include the assigned mount. The wrapper
also refuses an absent/wrong mount before any Compose operation.

```sh
export POSTIZ_OPERATOR_ENV='<protected operator.env>'
./project config --quiet
./project up -d --wait --wait-timeout 300
./project ps
```

Create the first LOCAL owner privately before adding Caddy/DNS. Registration
is disabled from first boot: upstream permits the first organization only.
Verify `/api/auth/can-register` becomes false and a second registration is rejected.
SMTP activation and password recovery need separate mail receipt checks. Keep
activation/recovery tokens out of logs. Owner login is `social@wlkrlabs.com`.
Display timezone uses the browser's America/Chicago zone; container TZ alone
does not set a browser preference. Recheck UTC conversion across DST.

## Shared edge and DNS

Create internal network `octal8-postiz`; add `edge.override.yml` to the existing
edge Compose invocation, retaining every prior override. `POSTIZ_RELEASE_ROOT`
points to the staged committed directory. Mount `postiz.caddy` using that override;
validate the complete Caddy configuration before reload. Adding the new network
and bind mount may require recreating only Caddy once. Keep all existing fixed
addresses, routes and certificate volumes. Future route-content changes use
`caddy reload`; do not routinely recreate the edge.

Use one DNS-only CNAME, `social.wlkrlabs.com` → `search-origin.patribible.com`.
This follows the existing dashboard's direct-DNS alias pattern and shares the
already-bounded Octal8 DDNS target. The updater still modifies only its existing
Search A record; it gains no credentials, record scope or new timer. Verify the
alias, target A, lack of AAAA, fresh updater execution and enabled timer together.
An actual IP-change test remains separate. Keep website/mail/Minecraft DNS intact.
Confirm HTTP redirect, trusted TLS, API and uploads; home-network checks alone
do not establish independent external reachability.

## Backups and isolated restore

`backup.sh` briefly stops only Postiz/Temporal/Elasticsearch/Redis, makes logical
PostgreSQL dumps of application and both Temporal databases, and archives cold
Elasticsearch/Redis files, media, configuration, secrets and releases. It restarts
only this stack and requires health readiness. Protected bundles retain 14 runs
on the data drive and secondary backup drive, verified by SHA-256. The existing
host nightly snapshot additionally includes the entire data drive and retains
seven snapshots; no existing backup job is changed. Offsite backup is deferred.

```sh
./backup.sh
./install-backup-timer.sh '<absolute release directory>' "$POSTIZ_OPERATOR_ENV"
./restore-check.sh '<backup UTC timestamp>'
systemctl --user status wlkrlabs-postiz-backup.timer
```

The restore creates two database containers on a dedicated internal network,
restores all three SQL dumps with errors fatal, clears live channel/API/user
credentials, and extracts media and cold workflow files. It runs no application
or worker, exposes no ports, and removes its containers/network on exit. Test
state/evidence stays on the assigned drive. Compare restored record counts and
media hashes with production. SQL/media restore does not prove scheduled delivery
or service-level Elasticsearch/Redis workflow resumption. Rehearse full recovery
with publishing blocked before using it for a real outage.

## Rollback

Before an upgrade, keep its compatible SQL/media/workflow bundle, old release
and images. Stop only `wlkrlabs-postiz`; never run `down -v` or prune shared Docker.
Image downgrade alone cannot reverse Prisma migrations.

For a fresh-install rollback, remove only the Postiz Caddy import mount and
network override from the edge invocation, validate and reload/recreate only
Caddy as needed, retaining all previous overrides. Remove only the new `social`
CNAME. Disable `wlkrlabs-postiz-backup.timer`, stop the Postiz project and retain
its state, backup bundles and vault items for recovery. Keep the restored shared
edge running; do not restore the pre-existing failed edge container state.

For a release rollback, stop Postiz workers first. Restore the matching SQL dumps
into empty databases using matching major-version images; restore cold workflow
files and uploads from that same bundle, along with its protected environment
and release. Start dependencies, verify Temporal/database health, then start the
application and confirm owner login, drafts/media and channel identity. Check
Temporal's existing workflows before resuming scheduling to avoid duplicates.
Keep outbound publishing blocked until that audit is complete. The private receipt
contains exact staged paths, DNS record identity and the pre-change edge snapshot.

Actual host reboot, public-IP-change recovery and live scheduled publication are
separate checks. Do not reboot or force an IP change for initial qualification.
