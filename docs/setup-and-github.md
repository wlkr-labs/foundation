# Setup and GitHub plan

Verified October 6, 2026. The approved Free organization, profile, private website history import and planning-repository transfer are complete. Product migrations remain future decisions.

Implementation inventory now includes authenticated reads of both accounts. See the [organization proposal](github-organization-proposal.md) for counts, dependency gates, and the concrete first stage, and the [project inventory](project-inventory.md) for program scope. Detailed private account metadata stays under ignored `private/foundation/`.

## One organizing home

Use `/Users/shanewalker/Desktop/dev/WLKRLABS` for these plans and as the folder to open in an editor or add as a Codex project. It is the existing clone of the public `wlkr-labs/foundation` repository, transferred from `WLKRLABS/WLKRLABS` with its original history. Remote: `git@github-scwlkr:wlkr-labs/foundation.git`.

The `website` shortcut opens the existing Astro source at `/Users/shanewalker/Documents/Codex/2026-09-30/task/wlkrlabs.com`. That source retains independent Git history, with private remote `git@github-scwlkr:wlkr-labs/website.git`. Keep the shortcut local and ignored by Git. It preserves the source path used by the established maintenance procedure.

Do not use `/Users/shanewalker/Desktop/dev/wlkrlabs-website` for live-site changes: it is an older Vite/Three.js prototype. The approved support/identity release is `d03d3c4`; full verification is recorded in the implementation checklist and local receipts.

## What belongs where

| Material | Home | Publication |
| --- | --- | --- |
| Mission, roadmap, website copy, organization plans | `WLKRLABS/docs/` | Public-safe drafts; publish deliberately |
| Website source, project catalog, public notes, deployment procedure | `WLKRLABS/website/` shortcut | Follow the website's own Git and release process |
| Product implementation | Each existing product repository | Retain current visibility and licensing |
| Empty operating examples | `WLKRLABS/templates/` | Safe to share |
| Receipts, supporter identifiers, account inventory, payout records | `WLKRLABS/private/` | Ignored MacBook records; owner-only Drive backup |
| Check logs and exact commit receipts | `WLKRLABS/.local/` | Local only |
| Passwords, recovery codes, keys, taxpayer IDs | Existing password manager or appropriate secure system | Never Git or public website |

Git ignore rules prevent accidental tracking; they do not encrypt files or provide a backup. Shane approved MacBook storage and a private Drive backup. Sharing was verified owner-only; record its pointer privately. Credentials, identity documents, taxpayer IDs and bank numbers stay with the provider or existing secure system.

## Product inventory

| Project | Local source | Public source/status |
| --- | --- | --- |
| PatriBible | `/Users/shanewalker/Desktop/dev/PatriBible` | Public site and app; source remains private |
| PatriAI | `/Users/shanewalker/Desktop/dev/PatriAI` | Supporting implementation; retain private visibility |
| WalkLang | `/Users/shanewalker/Desktop/dev/WalkLang` | `scwlkr/WalkLang`; tracked Apache-2.0 LICENSE verified |
| OpenJob | `/Users/shanewalker/Desktop/dev/openjob` | `scwlkr/openjob`; no tracked LICENSE/COPYING or GitHub-detected license; no reuse rights promised |
| tellygrab | `/Users/shanewalker/Desktop/dev/tellygrab` | `scwlkr/tellygrab`; tracked MIT LICENSE verified |

These are location/visibility observations, not a transfer of ownership or a fresh qualification of every feature. Keep private source URLs out of public website copy.

Earlier email setup notes describe multiple historical arrangements. Treat `/Users/shanewalker/Desktop/dev/email` as the existing administration project, and verify current routing before changing contacts or DNS. Do not duplicate mail setup here.

## GitHub recommendation

An organization is a sensible eventual home for shared stewardship. GitHub Free supports organizations; legal nonprofit recognition is not needed to use that plan. A GitHub organization is a collaboration account, not legal incorporation. [GitHub organizations](https://docs.github.com/en/organizations/collaborating-with-groups-in-organizations/about-organizations).

Current public `WLKRLABS` account type is **User**. Its three public repositories are `WLKRLABS`, `buoy`, and `tall-talents`. The public site features projects held mainly under `scwlkr`, so inspect both namespaces before choosing transfers.

Preferred starting option: create a separate free organization under an approved available name and transfer selected repositories while preserving personal accounts. The exact `WLKRLABS` namespace is already occupied by the current user; retaining that exact name requires a deliberate namespace decision.

Automatic conversion preserves the brand namespace but is irreversible and changes personal-account access and attribution. SSH keys, OAuth tokens, and installed GitHub Apps do not carry over. Review that route only after an account inventory and backup. [GitHub account reference](https://docs.github.com/en/account-and-profile/reference/personal-account-reference), [moving work while keeping the personal account](https://docs.github.com/en/account-and-profile/concepts/account-management).

## Sequence for later migrations when ready

1. Confirm control of both accounts; inventory all repositories, integrations, releases, Pages, packages, and authentication dependencies, including private ones.
2. Save repository/history backups and recovery information in appropriate secure locations.
3. Approve the organization name and migration method. Use the verified personal account `scwlkr` as an owner; add another trusted human owner when available.
4. Create or convert only after that review, on the Free plan. Keep existing authentication working until the new access is verified.
5. Transfer one selected repository, update remotes and integrations, and verify clone/push, releases, and dependent sites before continuing.
6. Establish a foundation/planning repository and a separate website repository. Preserve website Git history; choose its visibility after reviewing its contents.
7. Use a public `.github` repository's `profile/README.md` for the organization's profile when desired. Keep private administration elsewhere.

Repository transfers can change permissions and integrations; verify each dependency. [GitHub transfer guidance](https://docs.github.com/en/repositories/creating-and-managing-repositories/transferring-a-repository).

The first stage retained both personal accounts, original histories and hosting/DNS. The original planning URL redirects to the foundation repository; do not recreate the old same-name personal profile repository, because reusing that namespace would break the redirect. The public organization profile is the mission’s current GitHub home. Hosted Actions are disabled on the foundation, website and profile repositories; use local checks.
