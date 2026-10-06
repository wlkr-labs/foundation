# Postiz hosting handoff prompt

Copy the text below into the chat that will execute the deployment:

```text
Set up the free self-hosted Postiz edition for WLKR Labs on my existing 0o10 / Octal8 server, operated by octal8. Start in /Users/shanewalker/Desktop/dev/WLKRLABS and follow docs/postiz-octal8-setup-checklist.md, including the owning 0o10 instructions it references.

Use https://social.wlkrlabs.com as the intended URL and social@wlkrlabs.com for the owner login. Coordinate with docs/social-setup-handoff.md. Store credentials in my existing 1Password account associated with scwlkr, in its dedicated owner-only “WLKR Labs Social” vault, using separate Hosting items for application secrets.

Complete inspection, isolated deployment, shared-Caddy routing, scoped DNS, owner access, persistence, backups, isolated restore verification and rollback instructions. Reuse system Docker, private application/database networks, Tailscale management and the assigned backed-up drive. Preserve PatriSearch, Minecraft, existing Caddy routes, firewall rules and backups. Use current upstream Compose with compatible pinned images; do not purchase services, enable paid APIs/AI, replace the hosting architecture or reboot the shared host just for this setup.

Configure available free social integrations and test read/draft operations. A synthetic scheduled post may go only to an explicitly identified owner-only test destination; do not publish publicly or message other people. Work autonomously through the scoped setup, asking only for missing access, consequential ambiguity or unavoidable owner actions. Give exact steps for each blocker, continue independent work, and distinguish core hosting checks from unverified publishing, external reachability, IP-change and host-reboot recovery.
```
