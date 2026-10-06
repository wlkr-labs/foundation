# GitHub organization setup proposal

Updated October 6, 2026. The approved first stage is executed: Free `wlkr-labs`, public profile, private website history import and original public planning repository transferred to `foundation`. Both personal accounts and product ownership/visibility/licensing remain in place. No hosted checks were dispatched and $0 was spent.

## Ownership at the initial inspection

| Account | Type / controlled session | Owned repositories visible through authenticated owner inventory |
| --- | --- | --- |
| `WLKRLABS` | Personal User; existing CLI credential confirmed this identity | 3 public, 0 private: `WLKRLABS`, `buoy`, `tall-talents` |
| `scwlkr` | Personal User; existing CLI credential confirmed this identity | 63 total: 28 public, 35 private |

All eight foundation/catalog/supporting repositories inspected report their respective personal owner as administrator and sole returned collaborator. No repository webhooks, deploy keys, Actions secrets or Actions variables were returned for those eight. That does not establish absence of external integration credentials, vendor connections, packages or OAuth grants.

Detailed repo names, metadata and dependency indexes are local only in ignored `private/foundation/github-inventory.json` and `local-dependency-index.json`. Account-level app installation/package reads returned 403; account SSH/signing-key reads returned 404 under the existing token scopes. Private branch-protection/ruleset reads returned 403. Do not infer “none” from inaccessible reads. No extra scopes were requested and no secret values or key material were collected.

A local high-signal scan of reachable text blobs (up to 2 MB each) found no credential-pattern or sensitive-filename candidates in either the foundation or website history. Its private report records the exact scope and counts. This bounded scan is preparation evidence, not a complete privacy/content approval for a new remote.

## Adopted first stage

Created **separate GitHub Free organization `wlkr-labs`**, display name **WLKR Labs**, owned by `scwlkr`, using Shane’s selected administrative contact. Public organization type: community/initiative, without claiming recognized charity status. Add a second trusted human owner when one is identified and approves that access; this is not a blocker for an empty organization.

`wlkr-labs` and fallback `wlkrlabs-foundation` did not resolve through GitHub's user endpoint on October 6. The form subsequently accepted `wlkr-labs`; creation and Free plan were read back. The exact `WLKRLABS` handle is occupied by the personal account. Keep both personal accounts and their authentication working.

Organizations are collaboration accounts and Free supports public/private repositories; some private-repository protections and review features require paid plans. Do not buy those features or expose private code to obtain them. [Organization model](https://docs.github.com/en/organizations/collaborating-with-groups-in-organizations/about-organizations).

Personal-account conversion is a poor first step: it is irreversible and removes personal login/access patterns; SSH keys, OAuth tokens and installed Apps do not carry over. Retaining the exact `WLKRLABS` namespace would require a separate owner-approved namespace decision after complete account/dependency review. [Conversion effects](https://docs.github.com/en/account-and-profile/reference/personal-account-reference).

## Executed first stage

1. Owner approved `wlkr-labs`, Free, `scwlkr` and the contact; explicit action-time terms approval was obtained and the organization created. Owner 2FA is enabled.
2. Display name, mission description and website set. Default member repository permission is None.
3. Approved [organization profile](../templates/github-profile.md) published in public `.github/profile/README.md`.
4. Approved private `website` created; complete existing history imported. An empty no-reply preservation commit was appended to the archived August branch after GitHub rejected its original tip for email privacy; all original commits remain unchanged. All local branch/tag SHAs were read back. Account email protection retained.
5. Original `WLKRLABS/WLKRLABS` transferred to public `wlkr-labs/foundation`, repository ID `1206532635` preserved. Original default history, license state and old URL redirect verified. Only this checkout’s remote was updated.
6. Destination creation permission required a temporary Member invitation to Shane’s other `WLKRLABS` account; Shane approved it and completed GitHub verification. After transfer, conversion to outside collaborator ended membership while preserving foundation Write access. Private website access returns 404 for that account; sole organization owner/member is `scwlkr`.
7. Hosted Actions disabled on the three foundation repositories. Existing workflow source/history retained; no extra OAuth scopes or hosted checks introduced.

The same-name personal profile README moved with the foundation repository. Keep the old namespace unused so repository redirects continue; the existing personal account remains intact, and the public organization profile provides the mission identity. No replacement same-name personal repository was created.

## Dependency map and deferred migration order

| Repository / asset | Observed dependency | Required verification before any transfer | Proposal |
| --- | --- | --- | --- |
| Foundation `WLKRLABS/WLKRLABS` | Personal-account profile README; local SSH account alias; no provider deployments or releases returned | Complete history backup, confirm destination name, preserve redirect/account identity, verify owner permissions and clone/push | Completed approved pilot |
| Website | Existing manual Cloudflare static Worker; no Git remote or Git-connected build | Review full history for private material; preserve maintenance paths, source bundles and existing deployment; connect only the approved private remote | Imported privately; hosting/DNS retained |
| tellygrab | Public MIT source; install instructions with owner-qualified Git URLs; one existing check workflow | Resolve/coordinate unrelated edits, preserve LICENSE, update downstream install URLs, verify packaged CLI and existing tooling locally | Lowest product complexity; possible second transfer |
| WalkLang | Apache-2.0 source, 27 releases, binaries; live GitHub Pages custom domain and `github-pages` environment; Pages workflow | Archive all refs/release assets, review Pages/domain proof and install/editor URLs, local compiler checks, verify domain/HTTPS and releases after pilot | Defer until a Pages continuity plan is approved |
| OpenJob | 13 releases, CLI tarball install URL; Cloudflare, Firebase and Apple/Google authentication and native release configuration in source | Confirm external ownership/connections, release URLs, OAuth consent/callbacks and native service bindings with provider owners; clarify absent source license independently | Defer; retain public visibility and existing rights |
| PatriBible and supporting search | Private source; Cloudflare web release, Apple/Xcode Cloud bindings and search service references in local documentation | Review App Store Connect/Xcode Cloud repository access, actual provider permissions, private release links, corpus/text permissions and search deployment continuity | Keep private and under current ownership for now |
| `buoy`, `tall-talents` | Existing public releases/workflows, outside approved showcase | Inventory dependent release/installation URLs if future stewardship is requested | No initial transfer |
| Other `scwlkr` repositories | Personal/client/other work outside approved scope | Separate explicit project decision | No transfer |

Source references identify review dependencies; external vendor permissions were not requalified by the GitHub API inventory. WalkLang Pages configuration and HTTPS were read from GitHub; no Pages build was dispatched.

## Evidence and packet for later transfers

The pilot’s full refs/history and GitHub configuration/issue/PR/release metadata were backed up on the MacBook and in the verified owner-only Drive recovery folder. No issues, PRs, releases or Pages dependency existed. Local bundles verify; Drive metadata/size and complete raw binary SHA-256 match the local archive. Local archive extraction and bundle validation provide recovery checks. Credentials and provider-account exports are outside these source-history backups. For later transfers, export actual release assets and nonempty issue/PR records as applicable. For each later repo, record exact old/new owner/name, unchanged visibility/license, downstream URLs, provider contacts, expected access and abort criteria.

Then use the repository's Settings → General → Danger Zone → Transfer only for the explicitly approved repository/destination. Confirm Free-plan feature effects before proceeding, acceptance requirements, no destination-name conflict, inherited permissions, and the exact new owner. Repository transfers normally preserve history, issues/PRs and releases and provide redirects, but integrations/access may need updates. [Transfer behavior](https://docs.github.com/en/repositories/creating-and-managing-repositories/transferring-a-repository).

After acceptance, update only that repository's approved remotes and dependent public source links. Verify clone, push permission, refs/tags, release downloads, licenses, private access boundaries and affected hosted workflows. Avoid reusing the old namespace because that can break redirects. Stop before the next transfer until the pilot's evidence is saved. A transfer back is another consequential account action and needs approval; do not call it an automatic rollback.

## Exact owner actions still needed

- No further approval is needed for the completed first stage. Select a second trusted human owner only when someone appropriate is available; another account belonging to Shane is not a second human owner.
- In **each personal account → Settings**, review **SSH and GPG keys**, **Applications** (installed GitHub Apps and authorized OAuth Apps), **Developer settings** (tokens), **Packages**, and security/recovery settings. Record names, permissions and affected projects privately; do not paste tokens, keys or recovery codes into chat.
- For later private transfers, inspect current branch protections/rulesets and vendor repository grants in their authenticated settings; existing API permissions cannot prove them.
- Approve each proposed destination/visibility and transfer only when its dependency packet is complete. No product transfer is required for the completed website/foundation setup.
