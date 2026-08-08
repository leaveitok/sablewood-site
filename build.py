#!/usr/bin/env python3
"""
Build the City of Sablewood demonstration site.

WHY A GENERATOR AND NOT 16 HAND-WRITTEN FILES. The English and Spanish trees must
stay STRUCTURALLY IDENTICAL - same headings, same table shapes, same landmark
order - because the crawler chunks on structure. If the Spanish pages drift into a
different shape, a Spanish answer and an English answer stop being comparable and
"bilingual independence" quietly becomes "we also have some Spanish pages".

The content below is the single source of truth. `crawl.py` reads the PUBLISHED
HTML, not this file - the same path a real city's site takes.

FICTIONAL. Sablewood is not a real municipality. Phone numbers use the reserved
555-01xx range. No real seal, wordmark, photograph or stylesheet is reproduced.
"""

from __future__ import annotations

import html
import pathlib
import re

ROOT = pathlib.Path(__file__).parent

CITY = {
    "en": {
        "name": "City of Sablewood",
        "state": "Texas",
        "tagline": "Sablewood, Texas",
        "hall": "100 Civic Plaza, Sablewood, TX 76077",
        "main": "(940) 555-0100",
        "hours": "Monday–Friday, 8:00 a.m. – 5:00 p.m.",
        "search": "Search sablewood.gov",
        "search_btn": "Search",
        "skip": "Skip to main content",
        "lang_label": "Español",
        "lang_href": "es/index.html",
        "home": "Home",
    },
    "es": {
        "name": "Ciudad de Sablewood",
        "state": "Texas",
        "tagline": "Sablewood, Texas",
        "hall": "100 Civic Plaza, Sablewood, TX 76077",
        "main": "(940) 555-0100",
        "hours": "Lunes a viernes, 8:00 a.m. – 5:00 p.m.",
        "search": "Buscar en sablewood.gov",
        "search_btn": "Buscar",
        "skip": "Saltar al contenido principal",
        "lang_label": "English",
        "lang_href": "../index.html",
        "home": "Inicio",
    },
}

# Paths here are SITE-ROOT-RELATIVE. rel(depth, path) converts them for the page
# being written, so one nav definition serves every depth in both trees.
NAV = {
    "en": [
        ("Government", "government/departments.html"),
        ("Services", "services/utility-billing.html"),
        ("Permits", "services/building-permits.html"),
        ("Parks", "services/parks-recreation.html"),
        ("Agendas", "government/council-agendas.html"),
        ("Contact", "government/departments.html"),
    ],
    "es": [
        ("Gobierno", "es/gobierno/departamentos.html"),
        ("Servicios", "es/servicios/facturacion-de-agua.html"),
        ("Permisos", "es/servicios/permisos-de-construccion.html"),
        ("Parques", "es/servicios/parques-y-recreacion.html"),
        ("Agendas", "es/gobierno/agendas-del-consejo.html"),
        ("Contacto", "es/gobierno/departamentos.html"),
    ],
}

# Chrome links, site-root-relative, per language.
CHROME_LINKS = {
    "en": {"home": "index.html", "contact": "government/departments.html",
           "a11y": "accessibility.html", "contact_label": "Contact Us",
           "a11y_label": "Accessibility", "nav_label": "Primary"},
    "es": {"home": "es/index.html", "contact": "es/gobierno/departamentos.html",
           "a11y": "es/accesibilidad.html", "contact_label": "Contáctenos",
           "a11y_label": "Accesibilidad", "nav_label": "Principal"},
}

BANNER = {
    "en": ("This is a fictional city.", "Sablewood, Texas does not exist. This site is a "
           "demonstration built by OpticVector AI to show a grounded municipal concierge "
           "working on a realistic city website. Nothing here is an official government "
           "record and no service on it is real."),
    "es": ("Esta es una ciudad ficticia.", "Sablewood, Texas no existe. Este sitio es una "
           "demostración creada por OpticVector AI para mostrar un asistente municipal "
           "fundamentado en un sitio web municipal realista. Nada aquí es un registro "
           "gubernamental oficial y ningún servicio en él es real."),
}

DISCLOSURE = {
    "en": ("You are interacting with an AI assistant.", "It answers only from information "
           "published on this website, shows you the page each answer came from, and refers "
           "you to a department when the answer is not published."),
    "es": ("Está interactuando con un asistente de inteligencia artificial.", "Responde "
           "únicamente con información publicada en este sitio web, le muestra la página de "
           "la que proviene cada respuesta y lo remite a un departamento cuando la respuesta "
           "no está publicada."),
}

FOOTER_NOTE = {
    "en": "Sablewood is a fictional city created for demonstration purposes by OpticVector AI. "
          "Telephone numbers use the 555-01xx range reserved for fictional use. Any resemblance "
          "to a real municipality is unintended.",
    "es": "Sablewood es una ciudad ficticia creada con fines de demostración por OpticVector AI. "
          "Los números de teléfono usan el rango 555-01xx reservado para uso ficticio. Cualquier "
          "parecido con un municipio real no es intencional.",
}


def esc(s: str) -> str:
    return html.escape(s, quote=False)


def rel(depth: int, path: str) -> str:
    return ("../" * depth) + path


def chrome(lang: str, depth: int, current: str) -> tuple[str, str]:
    c = CITY[lang]
    k = CHROME_LINKS[lang]
    other = "es" if lang == "en" else "en"
    b_title, b_body = BANNER[lang]
    nav = "".join(
        '<li><a href="{href}"{cur}>{label}</a></li>'.format(
            href=rel(depth, h),
            label=esc(t),
            cur=' aria-current="page"' if t == current else "",
        )
        for t, h in NAV[lang]
    )
    # THE LANGUAGE SWITCH POINTS AT THE OTHER TREE'S HOME, not at a translated
    # copy of this page. Pretending every page has a counterpart when it does not
    # is how a bilingual site strands a Spanish speaker on an English 404.
    lang_href = rel(depth, CHROME_LINKS[other]["home"])

    head = f"""<a class="skip" href="#main">{esc(c['skip'])}</a>
<div class="demo-banner" role="note">
  <div class="wrap"><span class="dot" aria-hidden="true">&#9888;</span>
    <p style="margin:0"><strong>{esc(b_title)}</strong> {esc(b_body)}</p></div>
</div>
<div class="utility">
  <div class="wrap">
    <span class="lang"><a href="{lang_href}" hreflang="{other}" lang="{other}"
      >{esc(c['lang_label'])}</a></span>
    <a href="{rel(depth, k['contact'])}">{esc(k['contact_label'])}</a>
    <a href="{rel(depth, k['a11y'])}">{esc(k['a11y_label'])}</a>
  </div>
</div>
<header class="masthead">
  <div class="wrap">
    <img class="seal" src="{rel(depth, 'assets/seal.svg')}" alt="" width="66" height="66">
    <a class="wordmark" href="{rel(depth, k['home'])}">
      <span class="l1">{'Official Website' if lang == 'en' else 'Sitio Oficial'}</span>
      <span class="l2">{esc(c['name'])}</span>
      <span class="l3">{esc(c['tagline'])}</span>
    </a>
    <span class="spacer"></span>
    <form class="mast-search" role="search" onsubmit="return false">
      <label class="sr-only" for="q">{esc(c['search'])}</label>
      <input id="q" type="search" placeholder="{esc(c['search'])}">
      <button type="submit">{esc(c['search_btn'])}</button>
    </form>
  </div>
</header>
<nav class="mainnav" aria-label="{esc(k['nav_label'])}">
  <div class="wrap"><ul>{nav}</ul></div>
</nav>"""

    foot = f"""<footer class="footer">
  <div class="wrap">
    <div class="cols">
      <div>
        <h2>{esc(c['name'])}</h2>
        <p>{esc(c['hall'])}<br>{esc(c['main'])}<br>{esc(c['hours'])}</p>
      </div>
      <div>
        <h2>{'Services' if lang == 'en' else 'Servicios'}</h2>
        <ul>{''.join(f'<li><a href="{rel(depth, h)}">{esc(t)}</a></li>' for t, h in NAV[lang][:4])}</ul>
      </div>
      <div>
        <h2>{'Government' if lang == 'en' else 'Gobierno'}</h2>
        <ul>{''.join(f'<li><a href="{rel(depth, h)}">{esc(t)}</a></li>' for t, h in NAV[lang][4:])}</ul>
      </div>
    </div>
    <div class="legal">
      <p>{esc(FOOTER_NOTE[lang])}</p>
      <p>&copy; 2026 OpticVector AI &#183; {'Demonstration site' if lang == 'en' else 'Sitio de demostración'}</p>
    </div>
  </div>
</footer>"""
    return head, foot


# --------------------------------------------------------------------------- #
# THE CONCIERGE EMBED. One script tag, exactly as a city's web team would paste
# it into their CMS.
#
# NO data-api ON PURPOSE. The widget defaults the API origin to the origin the
# SCRIPT was served from, which is the same host that serves /api/**. Requiring a
# city to paste a raw Cloud Run hostname puts infrastructure detail in the one
# field where a typo yields a widget that loads, looks healthy and answers
# nothing.
#
# data-avatar IS DELIBERATELY ABSENT. Without it the widget runs in text mode and
# spends ZERO vendor minutes. Turning it on requires BOTH this attribute and
# `avatar.enabled` on the tenant, which is currently False for sablewood because
# the widget's avatar path has never been executed once. Two switches, so nobody
# starts billing by editing one line of HTML.
# --------------------------------------------------------------------------- #
WIDGET_EMBED = (
    '<script src="https://govassist-prod-0001.web.app/widget/govassist-widget.js"\n'
    '        data-tenant="sablewood"\n'
    '        data-launch="Ask Vera"\n'
    '        data-accent="#C8912F"></script>'
)

PAGE = """<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} | {city}</title>
<meta name="description" content="{desc}">
<link rel="stylesheet" href="{css}">
<link rel="icon" href="{seal}" type="image/svg+xml">
</head>
<body>
{head}
{body}
{foot}
{widget}
</body>
</html>
"""


def interior(lang: str, depth: int, current: str, title: str, lede: str,
             crumbs: list[tuple[str, str]], prose: str, sidebar: str) -> str:
    c = CITY[lang]
    head, foot = chrome(lang, depth, current)
    crumb_html = " &rsaquo; ".join(
        f'<a href="{rel(depth, h)}">{esc(t)}</a>' if h else f"<span>{esc(t)}</span>"
        for t, h in crumbs
    )
    body = f"""<nav class="crumbs" aria-label="{'Breadcrumb' if lang == 'en' else 'Ruta'}">
  <div class="wrap">{crumb_html}</div>
</nav>
<div class="pagehead">
  <div class="wrap"><h1>{esc(title)}</h1><p>{esc(lede)}</p></div>
</div>
<main id="main" class="wrap layout">
  <article class="prose">{prose}</article>
  <aside class="sidebar" aria-label="{'Page details' if lang == 'en' else 'Detalles de la página'}">{sidebar}</aside>
</main>"""
    return PAGE.format(
        lang=lang, title=esc(title), city=esc(c["name"]), desc=esc(lede),
        css=rel(depth, "assets/style.css"), seal=rel(depth, "assets/seal.svg"),
        head=head, body=body, foot=foot, widget=WIDGET_EMBED,
    )


def contact_box(lang: str, dept: str, phone: str, email: str, hours: str) -> str:
    lbl = {"en": ("Department contact", "Phone", "Email", "Hours"),
           "es": ("Contacto del departamento", "Teléfono", "Correo electrónico", "Horario")}[lang]
    return f"""<div class="box contact">
  <h2>{esc(lbl[0])}</h2>
  <p><strong>{esc(dept)}</strong></p>
  <p>{esc(lbl[1])}: {esc(phone)}</p>
  <p>{esc(lbl[2])}: <a href="mailto:{email}">{email}</a></p>
  <p>{esc(lbl[3])}: {esc(hours)}</p>
</div>"""


def related_box(lang: str, depth: int, items: list[tuple[str, str]]) -> str:
    t = "Related pages" if lang == "en" else "Páginas relacionadas"
    li = "".join(f'<li><a href="{rel(depth, h)}">{esc(n)}</a></li>' for n, h in items)
    return f'<div class="box"><h2>{esc(t)}</h2><ul>{li}</ul></div>'


def write(path: str, content: str) -> None:
    p = ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8", newline="\n")
    print(f"  {path}  ({len(content):,} bytes)")


if __name__ == "__main__":
    import pages
    pages.build(globals())
    print("\nBuilt.")
