# Website plan and starter copy

Status: published with Shane's approval, October 6, 2026. The established mission is reflected in Home/About, metadata, Work context, principles and the mission note. The updated logo assets, verified Buy Me a Coffee link, adopted Support terms and Privacy notice are live. Release `d03d3c4e3dfe175e2a6a7a9eaf9c195aea2697d1` matches both hostnames; 64 served asset/route checks pass and the existing Worker version is at 100%. Product visibility and licenses are unchanged.

## Keep the existing site simple

Keep the static Astro site, established design, and four-project catalog. Use the existing pages and content model instead of adding a new application, CMS, or database.

| Location | Proposed change |
| --- | --- |
| Home | Add one short mission line and an accurate aspiration/status sentence; keep access to actual software prominent |
| About | Explain the mission, founder, biblical foundation, current legal status, and intention to form a nonprofit |
| Principles | Integrate free access, teaching, stewardship, and sustainable work with the existing twelve craft principles |
| Work | Give PatriBible prominence; preserve accurate capabilities and source visibility in the four existing records |
| Notes | Publish an initial mission note and subsequent useful education/progress reports |
| Support | Prepared static page for free ways to help and accurate current status; activate a payment link only after actual recipient/profile and terms are approved and verified |

Use one verified support link. Explain support at the point where a visitor decides to pay. Keep the free core resources accessible regardless of contribution.

## Homepage copy

> Excellent free software, practical education, and biblical purpose.
>
> WLKR Labs builds tools that help people learn, create, and use technology. PatriBible is at the heart of our work: making Scripture easier to access and study.
>
> We are preparing for a future nonprofit structure while continuing to build and maintain useful software today.

Preserve the existing “Software, systems, and design—built as one discipline” line as a craft principle or supporting sentence if it fits the page.

## About copy

> WLKR Labs is an independent initiative built in Texas by Shane Walker. Our aim is to make excellent software freely available, help people gain practical access to technology, and produce education that helps them use and create it.
>
> Biblical faith is central to this work. PatriBible is our flagship project, alongside practical tools and programming education.
>
> We are working toward becoming a nonprofit. Today, WLKR Labs has not incorporated or received 501(c)(3) recognition. We are developing the mission, organizational plans, and funding needed for that next step.
>
> We want the work to last. Funding should primarily support software development, maintenance, access, and education, including reasonable compensation for the people doing that work.

## Support copy to finalize before launch

> Help keep useful software free.
>
> Your support helps maintain WLKR Labs projects, produce educational resources, and prepare for nonprofit formation. Our initial formation reserve target is $300 in available funds, subject to the application's eligibility and actual costs.
>
> Contributions currently go to Shane Walker operating WLKR Labs. WLKR Labs is not an incorporated or IRS-recognized charity, and these payments are not tax-deductible charitable donations.
>
> We will report funding use and formation progress. If formation is delayed or does not proceed, general support will continue to serve the software and educational work described here.

Button label: **Support WLKR Labs**. Connect it only to a confirmed live profile with matching recipient and terms. The [funding plan](funding-and-operations.md) defines the proposed bookkeeping and disclosure approach. [IRS contribution rules](https://www.irs.gov/taxtopics/tc506).

Do not show an invented progress total, a guaranteed approval date, nonprofit badges, or an unsupported source-license claim. Source code remains public or private according to each project's actual rights and decisions.

## Implementation locations

Use `website/src/pages/index.astro` and `about.astro` for initial copy; `src/data/principles.ts` for principles; `content/products/*.yaml` for catalog facts; and `content/notes/` for public writing. A Support page can be a small `src/pages/support.astro` when launch prerequisites are met.

Read the website's `AGENTS.md` and `MAINTENANCE.md` before editing. The current source is reached through the local shortcut; do not deploy the old Vite prototype.

## Publication steps

1. Approve the exact public language and confirm the status facts remain true.
2. For a support link, approve provider, payout identity, fee settings, terms, and funding use; verify the link and payment flow.
3. Make the smallest copy/content changes within the existing design.
4. Run the site's required local checks, then review desktop/mobile layout, keyboard navigation, and links.
5. Commit and verify that exact clean commit before any release.
6. Publish through the existing Cloudflare workflow after a release decision and check the served build record and pages.

The mission/status copy can be published independently of a fundraising launch. Payment configuration does not need to delay useful public writing.
