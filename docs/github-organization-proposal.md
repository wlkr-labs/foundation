# GitHub organization setup proposal

Prepared from authenticated, read-only inventory on October 6, 2026. No accounts were renamed or converted, repositories transferred, visibility changed, tokens replaced, integrations installed, workflows dispatched, or money spent.

## Verified ownership

| Account | Type / controlled session | Owned repositories visible through authenticated owner inventory |
| --- | --- | --- |
| `WLKRLABS` | Personal User; existing CLI credential confirmed this identity | 3 public, 0 private: `WLKRLABS`, `buoy`, `tall-talents` |
| `scwlkr` | Personal User; existing CLI credential confirmed this identity | 63 total: 28 public, 35 private |

All eight foundation/catalog/supporting repositories inspected report their respective personal owner as administrator and sole returned collaborator. No repository webhooks, deploy keys, Actions secrets or Actions variables were returned for those eight. That does not establish absence of external integration credentials, vendor connections, packages or OAuth grants.

Detailed repo names, metadata and dependency indexes are local only in ignored `private/foundation/github-inventory.json` and `local-dependency-index.json`. Account-level app installation/package reads returned 403; account SSH/signing-key reads returned 404 under the existing token scopes. Private branch-protection/ruleset reads returned 403. Do not infer “none” from inaccessible reads. No extra scopes were requested and no secret values or key material were collected.

A local high-signal scan of reachable text blobs (up to 2 MB each) found no credential-pattern or sensitive-filename candidates in either the foundation or website history. Its private report records the exact scope and counts. This bounded scan is preparation evidence, not a complete privacy/content approval for a new remote.

## Concrete recommendation

Create a **separate GitHub Free organization**, suggested handle **`wlkr-labs`**, display name **WLKR Labs**, owned initially by `scwlkr`. Use a controlled administrative contact chosen by Shane, not an inferred historical mailbox. Public organization type: community/initiative, without claiming recognized charity status. Add a second trusted human owner when one is identified and approves that access; this is not a blocker for an empty organization.

`wlkr-labs` and fallback `wlkrlabs-foundation` did not resolve through GitHub's user endpoint on October 6. Neither is reserved or guaranteed available; the creation form must validate the approved handle. The exact `WLKRLABS` handle is occupied by the personal account. Keep both personal accounts and their authentication working.

Organizations are collaboration accounts and Free supports public/private repositories; some private-repository protections and review features require paid plans. Do not buy those features or expose private code to obtain them. [Organization model](https://docs.github.com/en/organizations/collaborating-with-groups-in-organizations/about-organizations).

Personal-account conversion is a poor first step: it is irreversible and removes personal login/access patterns; SSH keys, OAuth tokens and installed Apps do not carry over. Retaining the exact `WLKRLABS` namespace would require a separate owner-approved namespace decision after complete account/dependency review. [Conversion effects](https://docs.github.com/en/account-and-profile/reference/personal-account-reference).

## Proposed first stage — identity and review only

1. Approve the exact handle, Free plan, `scwlkr` owner, and controlled contact address. Shane accepts GitHub's terms and any required email/MFA steps at creation. Do not convert or rename either account.
2. Set display name and description: “Excellent free software, accessible technology, education, and biblical purpose. PatriBible is our flagship. Working toward becoming a nonprofit.”
3. Use the [prepared organization profile](../templates/github-profile.md) as `profile/README.md` in a new public `.github` repository only after publication approval. Default member repository permission should be **None**; grant specific access when needed. Enable available owner security measures without new subscriptions.
4. Make a separate private `website` repository only after a full-history/content review and owner visibility approval. Import the existing website Git history; do not copy a snapshot or replace it with the old prototype. No remote is added by this proposal.
5. First transfer candidate: existing public planning repository `WLKRLABS/WLKRLABS`, retaining its history and current visibility, optionally naming it `foundation` at the destination. Approve that exact transfer separately. Its current README doubles as the personal account profile, so prepare a short replacement profile linking the new organization before moving it.

The first stage can stop after creating the empty organization. Public profile publication, website-history import, and each repository transfer are separate reviewable actions.

## Dependency map and deferred migration order

| Repository / asset | Observed dependency | Required verification before any transfer | Proposal |
| --- | --- | --- | --- |
| Foundation `WLKRLABS/WLKRLABS` | Personal-account profile README; local SSH account alias; no provider deployments or releases returned | Complete history backup, confirm destination name, preserve personal profile, verify owner permissions and clone/push | First pilot after specific approval |
| Website | Existing manual Cloudflare static Worker; no Git remote or Git-connected build | Review full history for private material; preserve maintenance paths, source bundles and existing deployment; connect only the approved private remote | Import history separately; no hosting/DNS change |
| tellygrab | Public MIT source; install instructions with owner-qualified Git URLs; one existing check workflow | Resolve/coordinate unrelated edits, preserve LICENSE, update downstream install URLs, verify packaged CLI and existing tooling locally | Lowest product complexity; possible second transfer |
| WalkLang | Apache-2.0 source, 27 releases, binaries; live GitHub Pages custom domain and `github-pages` environment; Pages workflow | Archive all refs/release assets, review Pages/domain proof and install/editor URLs, local compiler checks, verify domain/HTTPS and releases after pilot | Defer until a Pages continuity plan is approved |
| OpenJob | 13 releases, CLI tarball install URL; Cloudflare, Firebase and Apple/Google authentication and native release configuration in source | Confirm external ownership/connections, release URLs, OAuth consent/callbacks and native service bindings with provider owners; clarify absent source license independently | Defer; retain public visibility and existing rights |
| PatriBible and supporting search | Private source; Cloudflare web release, Apple/Xcode Cloud bindings and search service references in local documentation | Review App Store Connect/Xcode Cloud repository access, actual provider permissions, private release links, corpus/text permissions and search deployment continuity | Keep private and under current ownership for now |
| `buoy`, `tall-talents` | Existing public releases/workflows, outside approved showcase | Inventory dependent release/installation URLs if future stewardship is requested | No initial transfer |
| Other `scwlkr` repositories | Personal/client/other work outside approved scope | Separate explicit project decision | No transfer |

Source references identify review dependencies; external vendor permissions were not requalified by the GitHub API inventory. WalkLang Pages configuration and HTTPS were read from GitHub; no Pages build was dispatched.

## Transfer execution packet to use later

Before the pilot, export the approved repository's full refs/history, release assets, issue/PR metadata and configuration into an existing encrypted backup. The two local foundation/website Git bundles are history backups, not a complete backup of GitHub issues, release assets or provider accounts. For each later repo, record exact old/new owner/name, unchanged visibility/license, downstream URLs, provider contacts, expected access and abort criteria.

Then use the repository's Settings → General → Danger Zone → Transfer only for the explicitly approved repository/destination. Confirm Free-plan feature effects before proceeding, acceptance requirements, no destination-name conflict, inherited permissions, and the exact new owner. Repository transfers normally preserve history, issues/PRs and releases and provide redirects, but integrations/access may need updates. [Transfer behavior](https://docs.github.com/en/repositories/creating-and-managing-repositories/transferring-a-repository).

After acceptance, update only that repository's approved remotes and dependent public source links. Verify clone, push permission, refs/tags, release downloads, licenses, private access boundaries and affected hosted workflows. Avoid reusing the old namespace because that can break redirects. Stop before the next transfer until the pilot's evidence is saved. A transfer back is another consequential account action and needs approval; do not call it an automatic rollback.

## Exact owner actions still needed

- Approve `wlkr-labs` (fallback only if separately selected), Free, owner `scwlkr`, and provide a controlled administrative email.
- In **each personal account → Settings**, review **SSH and GPG keys**, **Applications** (installed GitHub Apps and authorized OAuth Apps), **Developer settings** (tokens), **Packages**, and security/recovery settings. Record names, permissions and affected projects privately; do not paste tokens, keys or recovery codes into chat.
- For later private transfers, inspect current branch protections/rulesets and vendor repository grants in their authenticated settings; existing API permissions cannot prove them.
- Approve each proposed destination/visibility and transfer only when its dependency packet is complete. None is necessary for the current local website draft.
