# Postiz deployment status — October 7, 2026

**Core hosting verified:** https://social.wlkrlabs.com/auth/login, owner `social@wlkrlabs.com`.
Credentials remain in the existing scwlkr 1Password account's owner-only
**WLKR Labs Social** vault. Owner Login, application signing secret, both database
passwords and organization API key have separate items. SMTP retains its original
mailbox Login. No services, API subscriptions, AI or storage were purchased.

## Deployed and verified

- Postiz **v2.25.0**, adapted from official Compose commit
  `dd4969e5e694cd009619a0d53cff14c21104580b`; all eight runtime/optional images
  have compatible immutable pins in [images.env](../deploy/postiz/images.env).
  Deployment tooling release: `b56b7d52ae189689a7423af5ac94879dcee9d321`.
- System Docker, six healthy runtime services, separate application/workflow
  networks, dedicated internal edge network, no app/database/workflow host ports.
  Persistent data uses the assigned mounted data drive. Docker's existing storage
  dependency and service restart policies are retained.
- Shared Caddy routing and trusted public TLS. Only one DNS-only CNAME was added:
  `social.wlkrlabs.com` → `search-origin.patribible.com`. The existing bounded
  DDNS target/timer remains enabled and a fresh execution succeeded. No AAAA,
  additional token scope, firewall changes or router forwards were added.
- Independent US and Switzerland probes reached login, API, uploaded media and
  the callback page with HTTP 200; plain HTTP returned 308. A real Mastodon OAuth
  callback completed. These checks establish current reachability.
- Private first-owner registration, activation email, browser logout/login and API login,
  secure HttpOnly cookies, recovery email and successful password reset verified.
  Public registration is false and a second registration was rejected.
- Bluesky `wlkrlabs.com`: dedicated non-privileged app password; email MFA retained.
  Mastodon `@wlkrlabs@mastodon.social`: profile read, posts write, media write.
  Threads `@wlkrlabs`: owner-approved tester and four requested scopes, real OAuth
  callback, CLI read and draft passed; developer app remains unpublished.
  DEV: owner-approved `scwlkr` author API key, connected read and a Postiz draft
  explicitly targeting the WLKR Labs organization. Its native organization draft
  is unpublished and returns 404 to an unauthenticated API read. This key also
  grants personal author access; select the organization on every draft.
  Developer credentials are distinct vault items.
- Official Postiz CLI **2.0.16** targets this instance's `/api` base. Channel reads,
  media upload, draft creation and draft editing passed. Four synthetic records
  remain **DRAFT**, with zero queued/published posts and null release URLs.
- Chicago 9:00 AM is stored as 14:00 UTC on October 7 and 15:00 UTC on November 3.
  List view displays both correctly and is selected for the owner.
- Project restart during the backup retained owner login, channels, drafts and
  uploaded media. Production and restored media SHA-256 hashes match.
- Consistent application/Temporal SQL dumps plus cold Redis/Elasticsearch, media,
  configuration, secrets and release files copied to the secondary backup drive.
  Own daily timer is enabled before the existing host snapshot; retention is
  14 successful bundles. Existing nightly backups and seven-snapshot policy remain.
- Secondary-drive isolated restore of the October 7 backup verified one owner,
  four drafts, zero usable
  channel credentials, 37 Temporal SQL tables, Redis startup and a green recovered
  visibility index. The restore ran no application/worker, had no host ports or
  outbound route, and removed its test containers/network afterward.

## Limits and continuation

| Check | Status / next action |
| --- | --- |
| Scheduled delivery / duplicates | **Unverified.** Identify an explicitly owner-only test destination, then approve a synthetic scheduled post to that destination only. No public post or message was sent. |
| Actual public-IP change | **Unverified.** CNAME and current DDNS execution/readback pass. Observe the next real IP change, target update and alias recovery; do not force a disruptive change. |
| Full shared-host reboot | **Unverified.** The pre-existing Caddy failure reported that its reserved LAN bind was unavailable at startup. Current routing was recovered without a reboot. Qualify LAN readiness and all services at an owner-planned reboot. |
| DST Day view | **Known upstream defect.** Its future-date row label uses today's offset. Use List view and verify UTC before scheduling across DST; no custom upstream image was introduced. |
| Facebook / Instagram | The existing WLKR Labs Postiz Meta app now includes Pages and Instagram alongside Threads, with exact callback URLs saved. No duplicate app was created. Main app-secret access awaits owner password reauthentication; actual account grants and read/draft tests remain pending. The app remains unpublished. |
| LinkedIn Page | Developer app created, Page association verified, callback and separate vault secret saved. Share on LinkedIn and OpenID Connect are provisioned; required organization permissions remain a provider gate. No inaccurate legal/business or advertising application was submitted. |
| Other providers | YouTube channel/API restrictions and Reddit approval remain separate provider/owner gates. Exact steps and eligibility limits are in the private receipt. |
| X / Hashnode | No paid API access enabled. Native account/publication routes remain. |
| Excluded platforms | Pinterest, Tumblr and TikTok remain permanently excluded. |
| Offsite / loss of both drives | **Deferred** under the existing host policy. Both verified backup copies are local. |

PatriSearch remains ready through the preserved authenticated Caddy route;
Minecraft server/origin and dashboard remain operational. Minecraft's public DNS
was already stale and was left outside this record change's scope. No shared
host reboot, global Docker cleanup or unrelated upgrade was performed.

The [deployment runbook](../deploy/postiz/README.md) describes architecture,
startup, backup, isolated restore and rollback. Exact protected paths, commands,
credential references and verification receipts remain in ignored `private/postiz/`;
the existing social inventory is coordinated in ignored `private/social/`.

Local validation of the deployment tooling and handoff on a clean commit, compared with
`e1c78281987b329e20793e183c053847310600c5`: `./project postiz:check`,
`./project docs:check`, and `git diff <base> --check` passed. Hosted CI was not used.
