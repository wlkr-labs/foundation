# Voluntary support launch proposal

Prepared October 6, 2026. This is a finished setup proposal, not an activated account. No provider session, live profile ownership, payment recipient, bank destination, or receipt has been verified. The website contains no payment link. The mission itself is established.

## Recommended arrangement

- Ko-fi Free, USD, ordinary one-time voluntary support; use one processor that Shane already controls and that is verified for this activity.
- Public display name: **WLKR Labs**. Actual recipient: **Shane Walker operating WLKR Labs**, subject to verification against the processor account.
- No monthly subscription, Gold upgrade, membership, shop, commissions, rewards, restricted incorporation campaign, or mandatory contribution.
- General support for software, maintenance, education, formation preparation, reasonable development/teaching compensation, and applicable operating obligations. No fixed compensation amount or percentage.
- Keep the $300 net formation-reserve target internal initially. Publish no balance, fundraising progress, gross goal, or promised filing date until actual records support it.

Ko-fi lists 0% platform fees on Free one-time tips, with processor fees still applying. Its help pages call the default optional fee setting Standard/Contributor/Get all of Ko-fi; opt out in Settings → Payment and read back the actual account setting. [Fees](https://help.ko-fi.com/hc/en-us/articles/360002506494-Does-Ko-fi-take-a-fee), [Contributor setting](https://help.ko-fi.com/hc/en-us/articles/25143210488477-Contributor-status).

## Ready profile copy

Display name: **WLKR Labs**

Headline: **Free software. Useful technology. Biblical purpose.**

Website field: `https://wlkrlabs.com`

About field:

> WLKR Labs builds and maintains excellent free software, helps people gain practical access to technology, and teaches them to use and create it. Rooted in biblical faith, we put Scripture access and study through PatriBible at the center of our work.
>
> Voluntary support helps maintain our software, produce practical education, and prepare for future nonprofit formation. Core public tools and education are intended to remain available without mandatory payment.
>
> Contributions go to Shane Walker operating WLKR Labs. WLKR Labs has not incorporated or received 501(c)(3) recognition. These payments are not tax-deductible charitable donations.

The final paragraph becomes factual launch copy only after the recipient is verified. Use the existing WLKR Labs brandmark after checking its rendering; no new paid design work is needed.

## Ready public funding terms

> Support is voluntary and does not purchase a product, reward, service, or ownership interest. Funds may support software development and maintenance, educational resources, formation preparation, reasonable compensation for the work, and related operating obligations. Founder compensation will be reported separately.
>
> If nonprofit formation is delayed or does not proceed, general support will continue to serve the software and educational work described here. We will report actual funding use and formation progress without publishing supporter identities. We do not promise a formation date or tax exemption.
>
> For an accidental or duplicate payment, request a refund through the Ko-fi page's Send a Message option, with its date and transaction reference. We aim to review requests within seven days. Approved refunds go through the original payment provider; timing and any provider limits apply. This policy does not limit rights available through your payment provider or applicable law.

This refund response target is a proposed operational commitment requiring Shane's approval. Creator responsibility and the refund controls are documented in [Ko-fi's refund guide](https://help.ko-fi.com/hc/en-us/articles/7733731935773-How-to-issue-a-refund). The current [IRS contribution guidance](https://www.irs.gov/taxtopics/tc506) does not make personal payments charitable deductions.

## Exact missing account details

Use the empty [account verification record](../templates/support-account-verification.md) in `private/`. Record references and masked identifiers only; enter sensitive identity/bank information directly with the provider.

| Field | Needed to settle it | Current state |
| --- | --- | --- |
| Existing account or new account | Controlled Ko-fi login and confirmed account email; MFA/recovery handled by Shane | Unknown |
| Public profile | Actual full profile URL, visible name, About text, and ownership confirmed in authenticated settings | Unknown; no guessed URL |
| Processor | Choose controlled PayPal or Stripe account; identify account country, account type, USD currency, and permission for this activity | Unknown |
| Legal recipient | Exact legal name matches Shane's actual identity and processor records; select the truthful individual/sole-proprietor status, not nonprofit | Proposed, unverified |
| Identity verification | Provider's actual onboarding may request legal name, address, birth date, phone, taxpayer identifier and ID; Shane completes these directly | Not started |
| Payout destination | Confirm the existing bank/account holder and currency; privately record last four digits and a secure record reference | Unknown |
| Public receipt/descriptor | Preview actual recipient name, support contact and statement descriptor a supporter will see | Unknown |
| Fees/features | Read back Free one-time tips, optional fee mode off, subscriptions/features disabled, processor fees and refund/chargeback terms | Unverified |
| Tax/record handling | Preserve exports and receipts, confirm actual treatment, and choose a tax reserve before spending receipts | No receipts or balance established |
| Private backup | Choose an existing encrypted backup location for account metadata, financial exports and receipt references | Not established |

The processor determines exact onboarding requirements from country, account type and capabilities; this table is the information to have ready, not a claim that every field is always requested. [Stripe verification requirements](https://docs.stripe.com/connect/required-verification-information).

## Approval and owner-only steps

1. Approve this general-support policy, Ko-fi Free, recipient Shane Walker, refund response target, and the chosen existing processor. Approve the provider/processor terms before accepting them; [Ko-fi terms](https://more.ko-fi.com/terms) were checked October 6 (effective July 13, 2026).
2. Sign in to Ko-fi or create the account directly. Shane handles password creation, MFA, identity/tax information, bank information, and any financial-account opening or connection consent. Do not buy an upgrade or transact money.
3. In Settings → Payment, connect the verified processor, use USD, and disable the optional 5% one-time-tip fee setting. Confirm the real account and payout destination. Save a redacted readback privately.
4. Insert the prepared profile and funding terms, choose one-time support, and verify both the authenticated profile URL and its public view. Before activating public collection, obtain the activation approval for that specific profile/recipient/processor.
5. Review the checkout up to the final payment step, checking recipient, descriptor, currency, one-time selection, terms, and contact. Do not submit a test payment under the $0 constraint. End-to-end charge, payout and refund remain unverified until an authorized real receipt exists.
6. Only after verified readbacks and activation approval, add the single actual URL to `website/src/pages/support.astro` with **Support WLKR Labs**. Replace the “not open yet” copy with the verified recipient disclosure and terms; run the website's checks and publish only after release approval.

The current no-payment website draft can be released independently. Account activation, identity verification and payment publication are not prerequisites for reviewing that draft.
