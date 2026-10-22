# WLKR Labs workspace

This repository owns the foundation plans, brand masters, social and Postiz handoffs, and sanitized deployment tooling. Product code stays in its existing repositories. Start with [README.md](README.md), the [implementation checklist](docs/implementation-checklist.md), and the [October 22 maintenance record](docs/closeout-2026-10-22.md).

## Work and access

- Shane owns account recovery, public release decisions and future content choices. Operators maintain the checks and record exact results; preserve unrelated product and shared-host work.
- Read the [social handoff](docs/social-setup-handoff.md) and [Postiz status](docs/postiz-deployment-status.md) before changing accounts or hosting. The [deployment runbook](deploy/postiz/README.md) covers backup, isolated restore and rollback.
- Credentials belong in the existing owner-only password manager. Record only item names and durable references; never secret values in this repository.
- Exact account actions and receipts stay in ignored `private/social/`; server commands and recovery evidence stay in ignored `private/postiz/`. Local check and cleanup receipts stay in ignored `.local/`.
- `website` is an ignored shortcut to the existing website checkout. Read its own `AGENTS.md` and `MAINTENANCE.md` before website work. A foundation document commit does not deploy the website.
- Keep dated evidence distinct from current checks. Record unverified recovery steps and provider approvals as open work. Missing traffic, income or usage data is unknown, not zero.

## Checks

Run `./project --help` for available commands. Use `./project docs:check` for public documentation, `./project postiz:check` for deployment tooling and `./project brand:check` for brand assets. Use the website's own checks for website work. Run `git diff --check` before committing; keep private material excluded.

Wstack 0.2.0 applies when invoked. Every code change needs an implementation subagent and a fresh independent read-only reviewer before delivery. Preserve useful continuing work and remove only owned disposable test resources.

<!-- wstack:begin setup -->
Wstack: 0.2.0
Features: [FEATURES.md](FEATURES.md)
Terms: [GLOSSARY.md](GLOSSARY.md)
CLI: `./project --help`
<!-- wstack:end setup -->
