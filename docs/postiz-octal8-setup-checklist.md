# Postiz on 0o10 / Octal8: setup checklist

Executed October 6, 2026. Hosting target: **0o10 / Octal8**, operated by **octal8**. Application: **https://social.wlkrlabs.com**. Core deployment, owner access, independent HTTPS reachability, persistence, consistent secondary-drive backup and isolated restore are verified. See the [deployment runbook](../deploy/postiz/README.md) and [execution status](postiz-deployment-status.md). The [copyable prompt](../templates/postiz-octal8-setup-prompt.md) remains available for continuation.

## Outcome and operating contract

Run the free self-hosted Postiz edition on the existing server, ready for the [social-account handoff](social-setup-handoff.md). Owner login: `social@wlkrlabs.com`. Store owner credentials, application secrets and provider keys in the same owner-only **1Password / WLKR Labs Social** vault, using distinct `Hosting` items rather than reusing social-account passwords.

Read the host's owning instructions before any change:

- `/Users/shanewalker/Documents/ChatGPT/0o10 2/AGENTS.md`
- `/Users/shanewalker/Documents/ChatGPT/0o10 2/README.md`
- `/Users/shanewalker/Documents/ChatGPT/0o10 2/docs/hosting.md`
- `/Users/shanewalker/Documents/ChatGPT/0o10 2/docs/backend-policy.md`
- `/Users/shanewalker/Documents/ChatGPT/0o10 2/deploy/ddns/README.md`

If these paths have moved, locate the actual owning 0o10 checkout. Do not substitute the separate `homelab` dashboard project for the Octal8 hosting instructions.

The required shape is **system Docker + a separate Postiz Compose project + the existing shared Caddy edge**. Management stays on Tailscale. Persistent state goes on the assigned backed-up data drive. Preserve current firewall rules, private routes, host backups, PatriSearch and Minecraft; record pre-existing outages before deployment. No second Docker daemon, second edge proxy, Tunnel/Funnel substitution, global cleanup or unrelated host upgrade.

Postiz keeps its required upstream Node runtime; the host's Rust-first policy applies to new first-party backend code, not a rewrite of this third-party application. Avoid building custom services unless a concrete deployment gap requires one.

## Social setup coordination checkpoint — October 6, 2026

The existing owner-only vault and social mailbox were reused. The shared Caddy container was present but had failed at host startup before this task. Its existing routes and ports were recovered, then the isolated Postiz route was added. Bluesky and Mastodon are connected; two synthetic drafts remain DRAFT with no queued or published posts. Provider apps and owner/provider gates have separate status in the execution record.
## 1. Inspect and prepare

- [x] Confirm authorized Tailscale/SSH access to 0o10, actual host identity, deployment account and administrator capability. Keep IPs, credentials and private operator paths outside Git.
- [x] Verify the selected Docker daemon is system Docker, enabled at boot. Clear an obsolete Docker context for this session if necessary; do not alter unrelated contexts or install another daemon.
- [x] Inventory existing Compose projects, Caddy routes/networks, reserved ports, storage mounts and backup coverage. Save a private baseline and rollback copy of the affected edge configuration.
- [x] Check memory, CPU and disk headroom under the existing workload. Postiz's documented light-use floor is 2 GB RAM / 2 vCPU; that is not spare capacity proof on a shared server. Budget at least 4 GB available for this stack where practical and allow room for media. [System requirements](https://docs.postiz.com/self-host/installation/system-requirements)
- [x] Identify the assigned persistent storage and verify mount ordering before container startup. Follow the existing data-drive dependency; do not change host-wide boot configuration unnecessarily.
- [x] Confirm `social@wlkrlabs.com` delivery and the 1Password account/vault from the social handoff. Existing mailbox/SMTP credentials remain in their original secure items.
- [x] Identify the owning deployment repository. Keep actual sanitized Compose, release pins, deployment and recovery instructions there; use this document as the checklist. Do not commit runtime secrets or machine-specific operator data.

## 2. Assemble the stack

- [x] Start from the [official Postiz Compose repository](https://github.com/gitroomhq/postiz-docker-compose) at a recorded commit. Read its current services and compatible release instructions before adapting it; do not copy an old online Compose snippet.
- [x] Give the application a distinct Compose project, such as `wlkrlabs-postiz`. Pin all deployed images to compatible releases or digests; remove shipped sample credentials and avoid floating `latest` images.
- [x] Include the upstream Postiz application/worker services, PostgreSQL, Redis and Temporal services required by that release. Persist their required database/workflow state and uploaded media on the assigned drive. Use local media storage initially; no new paid storage or AI services.
- [x] Replace upstream development host-port mappings with private Docker networking. Only Postiz's web-facing service joins a dedicated network shared with Caddy; databases, Redis, Temporal and admin UIs stay private. Publish no application/database/workflow ports to WAN or LAN.
- [x] Generate independent database and application secrets securely. Preserve encryption/signing secrets needed to recover stored provider credentials. Store recoverable copies in the vault and inject through protected, untracked configuration; never log rendered secrets.
- [x] Set public URL values for the chosen hostname: `MAIN_URL` and `FRONTEND_URL` use `https://social.wlkrlabs.com`; the browser API URL uses its documented `/api` route. Set internal backend/worker URLs from the actual upstream service layout, not guessed ports.
- [x] Configure uploads, worker connectivity, restart behavior and health checks according to the chosen release. Leave paid AI, Stripe/billing and unused provider integrations unset. Keep production security protections enabled. [Configuration reference](https://docs.postiz.com/self-host/configuration/reference)
- [x] Validate Compose without printing resolved environment values; check for collisions, placeholder secrets, wrong public URLs and unintended published ports. Stage and verify before DNS cutover.

## 3. Route HTTPS and DNS

- [x] Add only the Postiz hostname to the existing shared Caddy project. Preserve its current bind addresses, networks, certificate state and all other routes; no broad recreation as a routine deployment step.
- [x] Validate Caddy before reload. Proxy to the private Docker service's web port; `localhost` inside a Caddy container is not the Postiz container. Use trusted public TLS for this domain, not the documentation's internal-CA example. [Caddy guidance](https://docs.postiz.com/self-host/reverse-proxies/caddy)
- [x] Confirm the existing eero TCP 80/443 forwards and public reachability. Add no Postiz port forward. If an eero action is necessary, the owner uses Settings → Advanced networking → Reservations & port forwarding.
- [x] Inspect existing Cloudflare records for the new hostname. Use a scoped record change matching the host's direct-DNS architecture; preserve website/mail records and avoid an unverified AAAA record.
- [x] Account for a changing public IP. The existing updater targets one configured existing DNS-only A record; it does not automatically cover a new hostname. Reuse its supported bounded mechanism with separate Postiz configuration if needed, preserving the current job and records.
- [x] Verify current record identity, updater execution, timer status and result readback. Distinguish correct DNS today from recovery after an actual IP change; do not claim the latter without a real test. No disruptive router/IP-change experiment is required for initial setup.
- [x] Verify HTTP-to-HTTPS redirect, trusted certificate, UI, `/api`, uploads and an OAuth callback from an independent external path. Record external checks as pending if only an on-host/home-network path is available.

## 4. Establish owner access

- [x] Keep first-run registration private or otherwise inaccessible to strangers until the intended owner is established. Create the first owner with `social@wlkrlabs.com` and a generated vault-stored password.
- [x] Disable unintended public registration and verify the selected release's actual login behavior. Test logout/login and confirm a stranger cannot create an organization. Do not treat an environment flag alone as verification.
- [x] Configure transactional email with the existing permitted SMTP provider if supported and needed. Verify activation/recovery behavior; do not assume login success proves password recovery. Use `social@` as sender only after send-as is verified.
- [x] Set display timezone to **America/Chicago**; verify that a chosen local scheduling time maps correctly to UTC and daylight-saving behavior. **List view correctly displays both DST test dates; upstream Day view has a future-date offset-label defect. See execution status.**
- [x] Create an API credential only if needed for agent access; save it as a separate vault item. Point the documented Postiz CLI/MCP at this instance and verify a read/draft operation. This does not authorize an unattended public-posting automation.

## 5. Connect and test

- [x] Coordinate account IDs, handles and vault references with the social handoff. Start with an available free connection such as Bluesky or Mastodon; add approved Meta and LinkedIn Page apps progressively. [Provider setup](https://docs.postiz.com/self-host/providers/overview)
- [x] Use exact current OAuth redirect URIs for this hostname. Store provider credentials in the vault and protected configuration. Confirm intended scopes and account identity before connecting.
- [x] Keep X disconnected from paid API access. Keep Pinterest, Tumblr and TikTok permanently excluded. Record YouTube and Reddit approval restrictions accurately; native posting remains an available account-level route.
- [x] Verify login, draft creation/editing, media upload, channel connection and worker/workflow readiness. A saved draft or healthy worker does not establish successful scheduled publication.
- [ ] If an owner-only test destination is available, explicitly scope a synthetic scheduled-delivery test to it, verify the result and check for duplicates. Do not send to other people or publish publicly without publishing instructions. Otherwise record scheduled delivery as unverified with its exact next test. **Unverified: no owner-only test destination was identified; no synthetic post was scheduled.**
- [x] Restart only the Postiz project and verify persistence and recovery. Recheck the existing services against the baseline; report pre-existing failures separately.

## 6. Backup, rollback and finish

- [x] Verify consistent PostgreSQL backups plus uploaded media, required Temporal state, release/configuration records and securely stored recovery secrets. Confirm retention, restore procedure and actual coverage on the existing backed-up drive.
- [x] Restore a backup into an isolated test project with outbound publishing disabled and no usable live channel credentials. Verify restored records/media without triggering duplicate posts or changing production.
- [x] Write exact rollback steps for the chosen release, database migrations, Caddy route and scoped DNS change. Retain compatible database backups and old images; an image downgrade alone may not reverse a migration.
- [x] Verify restart policy and storage dependencies. Do not reboot the whole shared host solely for this setup. Mark actual host-reboot recovery as pending unless independently tested.
- [x] Keep offsite backup explicitly deferred under the host's existing policy; do not claim local backups cover loss of the host/data drive.
- [x] Finish with the application URL, deployed image digests, verified checks, credential item references, connected/pending channels, backup/restore result and exact owner actions. Store sensitive evidence privately.

Complete the hosting handoff when the core deployment, owner access, HTTPS, persistence, isolation and recoverability are proven. Report end-to-end publishing, external reachability, IP-change recovery and host-reboot recovery separately wherever unverified. Never equate a running container with a finished deployment.

Run the owning project's proportional local checks before pushing/deploying; record the exact commit SHA, comparison base, commands and results. Do not add or wait for hosted CI. Run `./project docs:check` for changes to this planning packet.
