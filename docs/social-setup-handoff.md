# WLKR Labs social setup handoff

Updated October 7, 2026. Execution status: email delivery and the dedicated owner-only vault are verified, ten public profiles are established and linked from the website, and the two-week launch draft pack is saved privately. The remaining authenticator recovery, YouTube approval and provider-connection gates are documented privately. Postiz core hosting, recovery, secondary-drive restore and Bluesky/Mastodon/Threads/DEV drafts are verified; see the [Postiz execution status](postiz-deployment-status.md). The existing Meta app is reused for Pages/Instagram; no duplicate was created. LinkedIn’s Overview, developer app/Page association and Mastodon’s reciprocal website verification are complete; LinkedIn organization API access is still pending. The current account inventory, evidence and exact remaining actions are in ignored `private/social/`. Start with the [copyable prompt](../templates/social-setup-prompt.md) when continuing.

## Outcome

Establish WLKR Labs' professional presence across the free platforms below. Use **social@wlkrlabs.com** for new brand registrations, notifications and recovery wherever supported. Organize credentials in the existing **1Password** account associated with **scwlkr**, in an owner-only **WLKR Labs Social** vault. Account creation and Postiz integration have separate completion states. Pinterest, Tumblr and TikTok are permanently excluded at the owner's direction on October 6, 2026; do not create accounts, connections or launch drafts for them.

## Identity and ownership

| Field | Use |
| --- | --- |
| Display name | WLKR Labs |
| Preferred handle | `wlkrlabs`; check availability before claiming |
| Handle fallback | `wlkr_labs`, then `wlkrlabsHQ`, where allowed |
| Website | `https://wlkrlabs.com` |
| Registration/contact email | `social@wlkrlabs.com` |
| Short bio | Free software. Useful technology. Biblical purpose. |
| Longer bio | WLKR Labs builds free software, makes technology more accessible, and teaches people to use and create it. Rooted in biblical faith, with PatriBible at the center of our work. |
| Owner | Shane Walker; use the existing `scwlkr` browser profile when available |

Read [mission and programs](mission-and-programs.md), [setup guidance](setup-and-github.md) and the [brand guide](../brand/README.md). Preserve existing product accounts and the established `wlkr-labs` GitHub organization. Current documents describe an independent initiative preparing for possible future nonprofit formation; use that description rather than claiming incorporation or recognized charity status.

Use `brand/icons/avatar-light.png` or `avatar-dark.png`. Existing LinkedIn, X and YouTube graphics are under `brand/social/`; generate missing crops from the approved masters. Keep one consistent avatar, name and website across profiles.

## 1. Verify email first

- [x] Read the owning email workspace: `/Users/shanewalker/Desktop/dev/email/AGENTS.md`, `README.md`, `inventory.yaml` and `MIGRATION.md`. Respect its excluded domains and existing senders.
- [x] Confirm `social@wlkrlabs.com` reaches the owner's intended WLKR inbox. October 2 records show Purelymail catch-all delivery to the existing Shane inbox; that is historical evidence, not a current delivery test.
- [x] If necessary, add only the `social@` alias through the existing Purelymail administration. Reuse the current mailbox; a separate mailbox is unnecessary unless delivery or account requirements justify it. Preserve all other routes, MX, SPF, DKIM and DMARC.
- [x] Send an owner-scoped synthetic verification message to `social@`; verify receipt and a reply from that address with authentication passing. Keep message contents private.
- [x] Confirm platform verification and recovery messages arrive before completing account setup. Do not change personal Meta, Google or LinkedIn account emails just to match the brand address.

## 2. Organize credentials

The owner confirmed **1Password** for this setup. Confirm the account connected to `scwlkr`; a browser profile name does not prove which 1Password account is selected.

- [x] Reuse or create an owner-only vault named **WLKR Labs Social** in that account. Do not purchase a new plan or share the vault. If vault creation is unavailable, use the existing private vault with a `WLKR Labs/Social` tag and record the limitation. [1Password vault instructions](https://support.1password.com/create-share-vaults/)
- [x] Create one Login item per actual login, named `WLKR Labs — <Platform>`, with the correct login URL, handle, `social@` email and a generated unique password where supported. Record SSO and magic-link exceptions without inventing extra passwords.
- [x] For Facebook Pages, LinkedIn Pages or other assets controlled by an existing personal login, reference the controlling item; do not invent a separate Page password or move unrelated personal credentials.
- [ ] Save passkeys, MFA configuration and recovery codes in the appropriate secure items. Record which real account owns each asset and how to recover it.
- [x] Store developer credentials separately: `WLKR Labs — <Provider> Developer App`. Store Postiz owner access and deployment secrets as distinct items in the same vault, tagged `Hosting`.
- [x] Use secure autofill or documented password-manager integration. Keep secrets out of chat, Git, screenshots, command arguments and logs; do not export the vault. 1Password Environments are not a replacement for Login items.

## 3. Establish the accounts

Audit existing accounts before creating anything. Reuse owner-controlled profiles when appropriate; report handle conflicts instead of assuming ownership. Use free account features, with no ads, paid badges, subscriptions or paid API access.

| Platform | Presence to establish | Publishing route / dependency |
| --- | --- | --- |
| Facebook | WLKR Labs Page; existing real owner profile administers it | Meta Business Suite; Postiz after app/permission setup |
| Instagram | WLKR Labs Business account, linked to the Page | Meta Business Suite; Postiz after permissions |
| Threads | Matching WLKR Labs profile | Meta developer app for Postiz |
| LinkedIn | WLKR Labs organization Page, administered by Shane | Native posting initially; Page API access requires additional review |
| YouTube | WLKR Labs channel using a Brand Account | YouTube Studio; public API uploads require an audited API project |
| Bluesky | WLKR Labs account, then domain handle `wlkrlabs.com` | Free API connection using an app password |
| Mastodon | WLKR Labs account on a suitable existing free instance | Verify instance rules permit organizational use; connect its API |
| X | WLKR Labs account and available handle | Free native posting; leave paid API integration disconnected |
| Reddit | WLKR Labs brand account | Native participation within community rules; API access requires approval |
| Dev.to / Hashnode | Brand or organization presence where available | Optional technical articles; confirm current free plan and credential eligibility |
| Discord / Telegram | Owner-controlled server/channel if useful | Optional community presence; do not invite or message other people as part of setup |

Bluesky domain verification uses a scoped TXT record or the documented website route; read back the new handle. Add only the required record and preserve other DNS. [Bluesky guide](https://bsky.social/about/blog/4-28-2023-domain-handle-tutorial)

For business publishing, recheck [LinkedIn Page access](https://learn.microsoft.com/en-us/linkedin/marketing/community-management-app-review), [YouTube upload restrictions](https://developers.google.com/youtube/v3/docs/videos/insert), [Reddit access](https://support.reddithelp.com/hc/en-us/articles/14945211791892-Developer-Platform-Accessing-Reddit-Data) and [X API pricing](https://docs.x.com/x-api/getting-started/pricing). A free account does not establish free automated publishing.

Google Business Profile is conditional: online-only organizations are ineligible. Do not create a Maps listing unless WLKR Labs actually meets [Google's eligibility requirements](https://support.google.com/business/answer/13763036).

## 4. Verify profiles and connect publishing

- [ ] Save each profile's correct name, bio, website, avatar, header, category and supported contact email; inspect its public view.
- [ ] Enable supported MFA and verify secure credential storage and recovery settings. Record unsupported features explicitly.
- [x] Link only verified public profiles from the website, following `website/AGENTS.md` and `MAINTENANCE.md`. Do not publish placeholders or private administration links.
- [x] Coordinate Postiz connections with the [Octal8 setup checklist](postiz-octal8-setup-checklist.md). Register developer apps only for intended free publishing routes, using `social@` where supported.
- [x] Prepare an introduction and two weeks of platform-specific draft content from the established mission and actual released projects. Save drafts; public posts and automated replies require publishing instructions.
- [x] Continue independent platform setup while an approval or owner verification is pending. Do not repeatedly ask about already settled identity, email, budget or password organization.

## Record and handoff

Keep the real account inventory under ignored `private/social/`; credentials remain in the vault. Record only non-secret references, with one row per platform:

| Platform | Public URL / handle | Owner reference | Email confirmed | Credential item reference | MFA / recovery | Publishing method | Verified date / blocker |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `<platform>` | `<public profile>` | `<controlling login reference>` | `<yes/pending>` | `<item title, no secret>` | `<verified/pending>` | `<native/Postiz/pending>` | `<evidence or exact next action>` |

Use `Verified`, `Pending owner action`, `Pending provider approval`, `Unavailable` or `Deferred` accurately. A connected channel is not proof of delivery; draft saving is not a scheduled-post test.

Completion means every listed platform is either verified or has an exact documented reason and next step, `social@` delivery is proven, credentials and recovery are organized, profiles are checked publicly, and free publishing routes are identified. Report outstanding owner actions with the exact page and steps. Never claim an approval or account was completed without readback.

Run `./project docs:check` for documentation changes. Follow each owning repository's local checks and commit policy for implementation. Keep private account evidence outside public commits.
