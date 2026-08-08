# City of Sablewood — demonstration municipal website

**Sablewood, Texas is fictional.** It does not exist and never has. This site is a
demonstration property built by OpticVector AI so the GovAssist concierge can be shown
working on a realistic city website, end to end, without touching a real municipality's
content or asking a real city for permission.

Every page carries a persistent banner saying so, in the site chrome — not in the footer.

---

## Why this exists

The concierge backend answers, cites and defers, and that has been provable in production
since release 00.73. What it has never had is **a host page**. The widget was built to be
embedded on a city's own site and had nowhere to be embedded.

It also fixes something subtler. Before this site existed, **no citation the system produced
resolved to anything** — the demo tenant cited `demo.example.gov`, a domain that does not
exist. Here, the citation opens **the actual page the answer came from**. A buyer clicking a
citation and landing on the source is the entire auditable-grounding argument in one gesture.

## The deliberate omission — do not "fix" it

Nothing on this site says anything about **short-term rentals**. That is not an oversight.

Residents ask about short-term rentals constantly, and plenty of real cities have never
published a policy. Asking the concierge *"do I need a permit for a short-term rental?"* is
therefore the live demonstration of **cite-or-defer**: a correct system must say it does not
have a published answer and hand over the department, rather than assembling a confident one
out of the building-permits page.

A demo that can only show the happy path is not showing the product.

**If you ever add a short-term rental page, the defer demonstration dies.** Remove a
different topic in the same commit.

## Design provenance

The **layout conventions** — utility bar, seal-and-wordmark masthead, full-bleed hero,
"How do I…" action tiles, department grid, notices and agenda modules — are standard
municipal web practice, chosen because a demo has to feel like a city website to be worth
anything.

**No third party's seal, wordmark, photography, stylesheet or markup is reproduced.** The
seal in `assets/seal.svg` and the stylesheet in `assets/style.css` are original work for this
site. Telephone numbers use the `555-01xx` range reserved for fictional use. The domain in
email addresses is `sablewood.example`, which is reserved by RFC 2606 and can never resolve.

## The hero is the concierge

The assistant is placed as the **first content section, full width, directly under the
header** — not as a floating bubble in the corner. That placement is what makes a municipal
digital assistant read as the city's front door instead of a support widget, and it mirrors
how production city deployments actually do it.

The stage renders a **poster state**. No avatar session is minted and no vendor minute is
billed until a resident chooses to start one — a city pays per avatar minute, and streaming
to someone who scrolled past is money spent on nobody.

## Bilingual

English and Spanish are **independent page trees**, not a translation widget bolted onto
English pages. Every Spanish page carries the same headings, the same fee tables and the same
department contact as its English counterpart; `build.py` enforces that parity.

This matters because the common competitor pattern is a Google Website Translator script on
an English page. If the claim is that English and Spanish are independent paths, the
demonstration corpus has to actually contain independent Spanish.

## Building

```
python3 build.py
```

`build.py` holds the templates and chrome; `pages.py` holds the content. Regenerating
overwrites every `.html` file — **edit the Python, never the HTML**, or your change is lost on
the next build.

Verification run after every build:

- every internal link resolves (440 checked, 0 broken)
- English and Spanish counterparts match on `h1` / `h2` / table counts
- the short-term rental omission is genuinely absent
- the AI-disclosure strip never overlaps or clips the start control, checked at six
  viewports in both languages

That last one earned its place: the disclosure was pinned with `position:absolute` and
padded away from the button, which held at exactly one size and covered the control
everywhere else. A TRAIGA disclosure that can obscure the control it is disclosing about is
worse than no layout at all. It is now in normal flow, and the stage uses `min-height`
rather than `aspect-ratio` — the ratio version clipped the **Spanish** disclosure and not the
English one, because Spanish runs about 20% longer here. A bug that only appears in the
language nobody proofreads.

## Hosting

Static. Any host works. For GitHub Pages, the `.nojekyll` file is required so that paths are
served as-is.

## Not yet wired

- The concierge widget script tag is **not** on these pages yet. The buttons carry
  `data-govassist-open` so the widget can bind to them without markup changes.
- The crawler that turns these published pages into the retrieval corpus is a separate piece.
- The tenant, Vertex data store and search app are not provisioned.

---

*Built by OpticVector AI. Demonstration only.*
