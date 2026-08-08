#!/usr/bin/env python3
"""
Content for the City of Sablewood demonstration site.

TWO RULES THIS FILE FOLLOWS DELIBERATELY.

1. THE SPANISH IS A REAL PAGE, NOT A TRANSLATED SHELL. Every Spanish page carries
   the same headings, the same fee tables and the same department contact as its
   English counterpart. The competitor pattern - and it is the pattern on the very
   site that inspired this project - is a Google Website Translator script bolted
   onto an English page. That is machine translation of a page, not a Spanish path.
   If our claim is "English and Spanish operate as independent paths", the demo
   corpus has to actually contain independent Spanish.

2. ONE COMMON QUESTION IS DELIBERATELY LEFT UNPUBLISHED: SHORT-TERM RENTALS.
   Residents ask about it constantly and plenty of cities have not written it down.
   Nothing on this site answers it. That is not an oversight - it is the live
   demonstration of cite-or-defer. Ask "do I need a permit for a short-term
   rental?" and a correct system must say it does not know and hand over the
   department, rather than assembling a confident answer out of the permits page.
   A demo that can only show the happy path is not showing the product.

   IF YOU EVER ADD A SHORT-TERM RENTAL PAGE, the defer demo dies. Add a different
   omission in the same commit.
"""

MAIN_HOURS_EN = "Monday–Friday, 8:00 a.m. – 5:00 p.m."
MAIN_HOURS_ES = "Lunes a viernes, 8:00 a.m. – 5:00 p.m."


def build(g):
    esc, rel, interior, chrome, write = (
        g["esc"], g["rel"], g["interior"], g["chrome"], g["write"])
    contact_box, related_box, PAGE, CITY, DISCLOSURE = (
        g["contact_box"], g["related_box"], g["PAGE"], g["CITY"], g["DISCLOSURE"])

    # ------------------------------------------------------------------ #
    # HOME - the hero IS the concierge. First content section, full width.
    # ------------------------------------------------------------------ #
    def home(lang, depth):
        c = CITY[lang]
        head, foot = chrome(lang, depth, "")
        d_title, d_body = DISCLOSURE[lang]
        t = {
            "en": dict(
                eyebrow="Ask the city anything",
                h1="Find a city service in one question.",
                lede=("Sablewood's digital assistant answers from the city's own published "
                      "pages, shows you the page the answer came from, and refers you to the "
                      "right department when the answer has not been published."),
                start="Start a conversation", browse="Browse services",
                avatar_name="Vera", stage_h="Meet Vera",
                stage_p="Your Sablewood digital assistant. Ask in English or Spanish.",
                howdo="How do I…", howdo_p="The requests residents make most.",
                tiles=[("&#128167;", "Pay my water bill", "Online, by phone, or in person",
                        "services/utility-billing.html"),
                       ("&#9851;", "Check my trash day", "Collection and recycling schedule",
                        "services/trash-recycling.html"),
                       ("&#128736;", "Pull a building permit", "Fees, forms and inspections",
                        "services/building-permits.html"),
                       ("&#127795;", "Reserve a park pavilion", "Facilities and recreation",
                        "services/parks-recreation.html"),
                       ("&#128221;", "Report a code violation", "Tall grass, junk, signage",
                        "services/code-compliance.html"),
                       ("&#128197;", "Read a council agenda", "Meetings, minutes and packets",
                        "government/council-agendas.html")],
                notices_h="City notices", agenda_h="Upcoming meetings",
                notices=[("March 2, 2026", "Spring brush collection begins March 16",
                          "services/trash-recycling.html"),
                         ("February 24, 2026", "Utility billing office closed for system upgrade",
                          "services/utility-billing.html"),
                         ("February 18, 2026", "Permit fee schedule updated for fiscal year 2026",
                          "services/building-permits.html")],
                agendas=[("March 10, 2026", "City Council Regular Meeting, 6:00 p.m.",
                          "government/council-agendas.html"),
                         ("March 17, 2026", "Planning &amp; Zoning Commission, 6:30 p.m.",
                          "government/council-agendas.html"),
                         ("March 24, 2026", "Parks Advisory Board, 5:30 p.m.",
                          "government/council-agendas.html")],
                depts_h="City departments", depts_p="Who to call, and when they answer.",
            ),
            "es": dict(
                eyebrow="Pregúntele a la ciudad",
                h1="Encuentre un servicio municipal con una sola pregunta.",
                lede=("El asistente digital de Sablewood responde con las páginas publicadas por "
                      "la ciudad, le muestra la página de la que proviene la respuesta y lo "
                      "remite al departamento correspondiente cuando la respuesta no está "
                      "publicada."),
                start="Iniciar una conversación", browse="Ver servicios",
                avatar_name="Vera", stage_h="Conozca a Vera",
                stage_p="Su asistente digital de Sablewood. Pregunte en español o en inglés.",
                howdo="¿Cómo puedo…?", howdo_p="Las solicitudes más frecuentes de los residentes.",
                tiles=[("&#128167;", "Pagar mi factura de agua", "En línea, por teléfono o en persona",
                        "es/servicios/facturacion-de-agua.html"),
                       ("&#9851;", "Consultar el día de recolección", "Calendario de basura y reciclaje",
                        "es/servicios/basura-y-reciclaje.html"),
                       ("&#128736;", "Obtener un permiso de construcción", "Tarifas, formularios e inspecciones",
                        "es/servicios/permisos-de-construccion.html"),
                       ("&#127795;", "Reservar un pabellón en un parque", "Instalaciones y recreación",
                        "es/servicios/parques-y-recreacion.html"),
                       ("&#128221;", "Reportar una violación de código", "Césped alto, chatarra, letreros",
                        "es/servicios/cumplimiento-de-codigos.html"),
                       ("&#128197;", "Leer una agenda del Concejo", "Reuniones, actas y paquetes",
                        "es/gobierno/agendas-del-consejo.html")],
                notices_h="Avisos de la ciudad", agenda_h="Próximas reuniones",
                notices=[("2 de marzo de 2026", "La recolección de ramas de primavera comienza el 16 de marzo",
                          "es/servicios/basura-y-reciclaje.html"),
                         ("24 de febrero de 2026", "Oficina de facturación cerrada por actualización de sistema",
                          "es/servicios/facturacion-de-agua.html"),
                         ("18 de febrero de 2026", "Tarifas de permisos actualizadas para el año fiscal 2026",
                          "es/servicios/permisos-de-construccion.html")],
                agendas=[("10 de marzo de 2026", "Reunión ordinaria del Concejo Municipal, 6:00 p.m.",
                          "es/gobierno/agendas-del-consejo.html"),
                         ("17 de marzo de 2026", "Comisión de Planificación y Zonificación, 6:30 p.m.",
                          "es/gobierno/agendas-del-consejo.html"),
                         ("24 de marzo de 2026", "Junta Asesora de Parques, 5:30 p.m.",
                          "es/gobierno/agendas-del-consejo.html")],
                depts_h="Departamentos municipales", depts_p="A quién llamar y cuándo contestan.",
            ),
        }[lang]

        tiles = "".join(
            f'<a class="tile" href="{rel(depth, h)}"><span class="ico" aria-hidden="true">{i}</span>'
            f"<strong>{n}</strong><span>{s}</span></a>"
            for i, n, s, h in t["tiles"])
        notices = "".join(
            f'<li><span class="date">{d}</span><a href="{rel(depth, h)}">{n}</a></li>'
            for d, n, h in t["notices"])
        agendas = "".join(
            f'<li><span class="date">{d}</span><a href="{rel(depth, h)}">{n}</a></li>'
            for d, n, h in t["agendas"])

        body = f"""
<main id="main">

  <!-- ============================================================
       THE HERO IS THE CONCIERGE.
       Placed as the FIRST content section, full width, directly under
       the header - the placement production municipal digital assistants
       use, and the reason one reads as the city's front door instead of
       a support widget in the corner.

       The stage below is the POSTER state. No avatar session is minted
       and no vendor minute is billed until a resident chooses to start
       one. A city pays per avatar minute; streaming to someone who
       scrolled past is money spent on nobody.
       ============================================================ -->
  <section class="hero" aria-labelledby="hero-h">
    <div class="wrap">
      <div class="hero-copy">
        <span class="eyebrow">{t['eyebrow']}</span>
        <h1 id="hero-h">{t['h1']}</h1>
        <p>{t['lede']}</p>
        <div class="hero-actions">
          <button class="btn btn-primary" type="button"
                  data-govassist-open>{t['start']}</button>
          <a class="btn btn-ghost"
             href="{rel(depth, t['tiles'][0][3])}">{t['browse']}</a>
        </div>
      </div>

      <div class="concierge-stage" id="concierge-hero">
        <div class="poster">
          <div class="avatar-ring" aria-hidden="true">V</div>
          <h2>{t['stage_h']}</h2>
          <p>{t['stage_p']}</p>
          <button class="btn btn-primary" type="button" data-govassist-open>{t['start']}</button>
        </div>
        <p class="ai-disclosure"><strong>{d_title}</strong> {d_body}</p>
      </div>
    </div>
  </section>

  <section class="section wrap" aria-labelledby="howdo-h">
    <div class="section-head">
      <h2 id="howdo-h">{t['howdo']}</h2>
      <p>{t['howdo_p']}</p>
    </div>
    <div class="tiles">{tiles}</div>
  </section>

  <section class="band">
    <div class="section wrap split">
      <div>
        <div class="section-head"><h2>{t['notices_h']}</h2></div>
        <ul class="notice-list">{notices}</ul>
      </div>
      <div>
        <div class="section-head"><h2>{t['agenda_h']}</h2></div>
        <ul class="notice-list">{agendas}</ul>
      </div>
    </div>
  </section>

  <section class="section wrap" aria-labelledby="depts-h">
    <div class="section-head">
      <h2 id="depts-h">{t['depts_h']}</h2>
      <p>{t['depts_p']}</p>
    </div>
    <div class="cards">
      <div class="card"><h3>{'Utility Billing' if lang == 'en' else 'Facturación de Servicios'}</h3>
        <p>{'Water, sewer and solid waste accounts, payment arrangements and final bills.'
            if lang == 'en' else
            'Cuentas de agua, alcantarillado y residuos sólidos, planes de pago y facturas finales.'}</p>
        <p class="meta">(940) 555-0110</p></div>
      <div class="card"><h3>{'Public Works' if lang == 'en' else 'Obras Públicas'}</h3>
        <p>{'Streets, drainage, water distribution and residential collection.'
            if lang == 'en' else
            'Calles, drenaje, distribución de agua y recolección residencial.'}</p>
        <p class="meta">(940) 555-0120</p></div>
      <div class="card"><h3>{'Development Services' if lang == 'en' else 'Servicios de Desarrollo'}</h3>
        <p>{'Building permits, plan review, inspections and zoning.'
            if lang == 'en' else
            'Permisos de construcción, revisión de planos, inspecciones y zonificación.'}</p>
        <p class="meta">(940) 555-0130</p></div>
    </div>
  </section>

</main>"""
        return PAGE.format(
            lang=lang, title=("Home" if lang == "en" else "Inicio"), city=esc(c["name"]),
            desc=esc(t["lede"]), css=rel(depth, "assets/style.css"),
            seal=rel(depth, "assets/seal.svg"), head=head, body=body, foot=foot)

    write("index.html", home("en", 0))
    write("es/index.html", home("es", 1))

    # ------------------------------------------------------------------ #
    # UTILITY BILLING
    # ------------------------------------------------------------------ #
    write("services/utility-billing.html", interior(
        "en", 1, "Services", "Pay your water bill",
        "Ways to pay your City of Sablewood utility account, billing dates, and what "
        "happens when a payment is late.",
        [("Home", "index.html"), ("Services", "services/utility-billing.html"),
         ("Pay your water bill", "")],
        """
<h2>Ways to pay</h2>
<p>The City of Sablewood bills water, wastewater and solid waste on a single monthly
utility statement. You may pay any of the following ways.</p>
<ul>
  <li><strong>Online.</strong> Pay by bank draft or card through the resident portal at any
      time. Card payments carry a $2.15 vendor convenience fee; bank drafts are free.</li>
  <li><strong>By phone.</strong> Call the automated payment line at (940) 555-0111, available
      24 hours a day. You will need your 10-digit account number.</li>
  <li><strong>In person.</strong> At the Utility Billing counter, City Hall, 100 Civic Plaza,
      Monday–Friday, 8:00 a.m. – 5:00 p.m.</li>
  <li><strong>Drop box.</strong> A 24-hour drop box is located in the City Hall north parking
      lot. Do not place cash in the drop box.</li>
  <li><strong>By mail.</strong> City of Sablewood Utility Billing, P.O. Box 4120,
      Sablewood, TX 76077.</li>
</ul>

<h2>Billing and due dates</h2>
<p>Statements are mailed on the first business day of each month and are due on the
<strong>16th</strong>. If the 16th falls on a weekend or a city holiday, the due date moves
to the next business day.</p>
<table>
  <caption>Late payment and reconnection charges, effective October 1, 2025</caption>
  <thead><tr><th>Charge</th><th>Amount</th><th>When it applies</th></tr></thead>
  <tbody>
    <tr><td>Late penalty</td><td>10% of the past-due balance</td><td>The day after the due date</td></tr>
    <tr><td>Disconnection notice</td><td>$15.00</td><td>10 days past due</td></tr>
    <tr><td>Reconnection during business hours</td><td>$45.00</td><td>After service is disconnected</td></tr>
    <tr><td>Reconnection after hours</td><td>$85.00</td><td>Requested after 5:00 p.m. or on a weekend</td></tr>
    <tr><td>Returned payment</td><td>$25.00</td><td>Any payment returned by your institution</td></tr>
  </tbody>
</table>

<h2>Payment arrangements</h2>
<p>If you cannot pay in full, contact Utility Billing <em>before</em> your due date. Staff can
set up a deferred payment agreement spreading a past-due balance over up to three billing
cycles. An account with an active arrangement in good standing is not disconnected.</p>
<div class="callout">
  <p><strong>Medical needs.</strong> If someone in your household depends on electrically
  powered medical equipment, file a Critical Care affidavit with Utility Billing. It does not
  waive the bill, but it changes how and when service may be interrupted.</p>
</div>

<h2>Starting or stopping service</h2>
<p>New service requires a completed application, a government-issued photo ID and a deposit of
<strong>$75.00</strong> for an owner-occupied residence or <strong>$150.00</strong> for a rental.
Applications received before 3:00 p.m. are normally connected the next business day.</p>
<p>To stop service, give at least two business days' notice and provide a forwarding address.
Your final bill is issued within 15 days and any deposit is applied to it.</p>

<h2>Understanding a high bill</h2>
<p>The most common cause of a sudden increase is an irrigation system running on a controller
that was never adjusted for the season, followed by a leaking toilet flapper. Utility Billing
can pull 60 days of hourly consumption for your meter at no charge, which will usually show
whether the usage is continuous — the signature of a leak — or clustered at specific hours.</p>
""",
        contact_box("en", "Utility Billing", "(940) 555-0110",
                    "utilitybilling@sablewood.example", MAIN_HOURS_EN)
        + related_box("en", 1, [
            ("Trash and recycling collection", "services/trash-recycling.html"),
            ("Report a code violation", "services/code-compliance.html"),
            ("City departments", "government/departments.html")])))

    write("es/servicios/facturacion-de-agua.html", interior(
        "es", 2, "Servicios", "Pague su factura de agua",
        "Formas de pagar su cuenta de servicios públicos de la Ciudad de Sablewood, fechas de "
        "facturación y qué sucede cuando un pago se atrasa.",
        [("Inicio", "es/index.html"), ("Servicios", "es/servicios/facturacion-de-agua.html"),
         ("Pague su factura de agua", "")],
        """
<h2>Formas de pago</h2>
<p>La Ciudad de Sablewood factura el agua, el alcantarillado y los residuos sólidos en un solo
estado de cuenta mensual. Puede pagar de cualquiera de las siguientes maneras.</p>
<ul>
  <li><strong>En línea.</strong> Pague con débito bancario o tarjeta a través del portal para
      residentes en cualquier momento. Los pagos con tarjeta tienen un cargo por conveniencia
      de $2.15 del proveedor; los débitos bancarios son gratuitos.</li>
  <li><strong>Por teléfono.</strong> Llame a la línea automatizada de pagos al (940) 555-0111,
      disponible las 24 horas. Necesitará su número de cuenta de 10 dígitos.</li>
  <li><strong>En persona.</strong> En el mostrador de Facturación de Servicios, Ayuntamiento,
      100 Civic Plaza, de lunes a viernes, de 8:00 a.m. a 5:00 p.m.</li>
  <li><strong>Buzón de pagos.</strong> Hay un buzón disponible las 24 horas en el
      estacionamiento norte del Ayuntamiento. No deposite efectivo en el buzón.</li>
  <li><strong>Por correo.</strong> City of Sablewood Utility Billing, P.O. Box 4120,
      Sablewood, TX 76077.</li>
</ul>

<h2>Facturación y fechas de vencimiento</h2>
<p>Los estados de cuenta se envían el primer día hábil de cada mes y vencen el
<strong>día 16</strong>. Si el 16 cae en fin de semana o en un día festivo municipal, la fecha
de vencimiento pasa al siguiente día hábil.</p>
<table>
  <caption>Cargos por atraso y reconexión, vigentes desde el 1 de octubre de 2025</caption>
  <thead><tr><th>Cargo</th><th>Monto</th><th>Cuándo aplica</th></tr></thead>
  <tbody>
    <tr><td>Multa por atraso</td><td>10% del saldo vencido</td><td>El día siguiente al vencimiento</td></tr>
    <tr><td>Aviso de desconexión</td><td>$15.00</td><td>10 días después del vencimiento</td></tr>
    <tr><td>Reconexión en horario de oficina</td><td>$45.00</td><td>Después de la desconexión del servicio</td></tr>
    <tr><td>Reconexión fuera de horario</td><td>$85.00</td><td>Solicitada después de las 5:00 p.m. o en fin de semana</td></tr>
    <tr><td>Pago devuelto</td><td>$25.00</td><td>Cualquier pago devuelto por su institución</td></tr>
  </tbody>
</table>

<h2>Planes de pago</h2>
<p>Si no puede pagar el total, comuníquese con Facturación de Servicios <em>antes</em> de la
fecha de vencimiento. El personal puede establecer un acuerdo de pago diferido que distribuye
un saldo vencido en hasta tres ciclos de facturación. Una cuenta con un acuerdo activo y al
corriente no se desconecta.</p>
<div class="callout">
  <p><strong>Necesidades médicas.</strong> Si alguien en su hogar depende de equipo médico
  eléctrico, presente una declaración jurada de Cuidado Crítico ante Facturación de Servicios.
  No exime el pago de la factura, pero cambia cómo y cuándo se puede interrumpir el servicio.</p>
</div>

<h2>Iniciar o suspender el servicio</h2>
<p>El servicio nuevo requiere una solicitud completa, una identificación con fotografía emitida
por el gobierno y un depósito de <strong>$75.00</strong> para una vivienda ocupada por su
propietario o <strong>$150.00</strong> para una vivienda de alquiler. Las solicitudes recibidas
antes de las 3:00 p.m. normalmente se conectan el siguiente día hábil.</p>
<p>Para suspender el servicio, avise con al menos dos días hábiles de anticipación y
proporcione una dirección de reenvío. Su factura final se emite dentro de 15 días y cualquier
depósito se aplica a ella.</p>

<h2>Cómo entender una factura alta</h2>
<p>La causa más común de un aumento repentino es un sistema de riego que funciona con un
controlador que nunca se ajustó para la temporada, seguida por una válvula de inodoro con fuga.
Facturación de Servicios puede obtener 60 días de consumo por hora de su medidor sin costo, lo
que generalmente muestra si el consumo es continuo — la señal de una fuga — o concentrado en
horas específicas.</p>
""",
        contact_box("es", "Facturación de Servicios", "(940) 555-0110",
                    "utilitybilling@sablewood.example", MAIN_HOURS_ES)
        + related_box("es", 2, [
            ("Recolección de basura y reciclaje", "es/servicios/basura-y-reciclaje.html"),
            ("Reportar una violación de código", "es/servicios/cumplimiento-de-codigos.html"),
            ("Departamentos municipales", "es/gobierno/departamentos.html")])))

    # ------------------------------------------------------------------ #
    # TRASH & RECYCLING
    # ------------------------------------------------------------------ #
    write("services/trash-recycling.html", interior(
        "en", 1, "Services", "Trash and recycling collection",
        "Collection days, what goes in each cart, bulk and brush pickup, and holiday schedule "
        "changes for Sablewood residents.",
        [("Home", "index.html"), ("Services", "services/utility-billing.html"),
         ("Trash and recycling", "")],
        """
<h2>Collection days</h2>
<p>Residential collection runs Monday through Thursday. Your day depends on which quadrant of
the city you live in, divided by Sablewood Parkway (north–south) and Third Street (east–west).</p>
<table>
  <caption>Residential collection schedule</caption>
  <thead><tr><th>Quadrant</th><th>Garbage</th><th>Recycling</th></tr></thead>
  <tbody>
    <tr><td>Northwest</td><td>Monday</td><td>Every other Monday</td></tr>
    <tr><td>Northeast</td><td>Tuesday</td><td>Every other Tuesday</td></tr>
    <tr><td>Southwest</td><td>Wednesday</td><td>Every other Wednesday</td></tr>
    <tr><td>Southeast</td><td>Thursday</td><td>Every other Thursday</td></tr>
  </tbody>
</table>
<p>Carts must be at the curb by <strong>7:00 a.m.</strong> on your collection day, with wheels
toward the house and at least three feet of clearance from parked cars, mailboxes and each
other. Crews will not return for a cart set out late.</p>

<h2>What goes in each cart</h2>
<h3>Green cart — garbage</h3>
<p>Household waste, bagged. The lid must close. Extra bags placed beside the cart are not
collected on a regular route.</p>
<h3>Blue cart — recycling</h3>
<p>Accepted: cardboard (flattened), paper, mail, cartons, metal cans, and plastic bottles and
jugs marked #1 and #2.</p>
<p>Not accepted, and a frequent cause of a rejected load: plastic bags of any kind, foam
containers, food-soiled paper, garden hose, clothing, and household glass. <strong>Recycling
placed in a plastic bag is thrown away</strong>, because the bag cannot be opened safely at
the sorting facility.</p>

<h2>Bulk and brush</h2>
<p>Bulk waste is collected on the <strong>first collection day of each month</strong>. Place
items at the curb no earlier than the weekend before. The limit is one pickup-truck-bed volume,
roughly 8 cubic yards.</p>
<p>Brush must be cut to lengths of 4 feet or less and stacked with the cut ends facing the
street. Brush and bulk must be in separate piles — a mixed pile is collected as bulk and counts
against the monthly limit.</p>
<p>Not collected at the curb at any time: tires, paint, motor oil, batteries, appliances
containing refrigerant, and construction debris from a contracted job.</p>

<h2>Holiday schedule</h2>
<p>Collection does not run on New Year's Day, Memorial Day, Independence Day, Labor Day,
Thanksgiving Day and Christmas Day. When a holiday falls on a weekday, that day's route and
every route after it that week slide forward one day, and Thursday's route runs Friday.</p>

<h2>Missed collection</h2>
<p>Report a missed cart by 10:00 a.m. the following business day and a crew will return within
one business day at no charge. Reports made later are scheduled for the next regular route.</p>
""",
        contact_box("en", "Public Works — Solid Waste", "(940) 555-0120",
                    "solidwaste@sablewood.example", MAIN_HOURS_EN)
        + related_box("en", 1, [
            ("Pay your water bill", "services/utility-billing.html"),
            ("Report a code violation", "services/code-compliance.html"),
            ("City departments", "government/departments.html")])))

    write("es/servicios/basura-y-reciclaje.html", interior(
        "es", 2, "Servicios", "Recolección de basura y reciclaje",
        "Días de recolección, qué va en cada contenedor, recolección de artículos voluminosos y "
        "ramas, y cambios de horario por días festivos para los residentes de Sablewood.",
        [("Inicio", "es/index.html"), ("Servicios", "es/servicios/facturacion-de-agua.html"),
         ("Basura y reciclaje", "")],
        """
<h2>Días de recolección</h2>
<p>La recolección residencial se realiza de lunes a jueves. Su día depende del cuadrante de la
ciudad en el que viva, dividido por Sablewood Parkway (norte–sur) y Third Street (este–oeste).</p>
<table>
  <caption>Calendario de recolección residencial</caption>
  <thead><tr><th>Cuadrante</th><th>Basura</th><th>Reciclaje</th></tr></thead>
  <tbody>
    <tr><td>Noroeste</td><td>Lunes</td><td>Lunes cada dos semanas</td></tr>
    <tr><td>Noreste</td><td>Martes</td><td>Martes cada dos semanas</td></tr>
    <tr><td>Suroeste</td><td>Miércoles</td><td>Miércoles cada dos semanas</td></tr>
    <tr><td>Sureste</td><td>Jueves</td><td>Jueves cada dos semanas</td></tr>
  </tbody>
</table>
<p>Los contenedores deben estar en la acera antes de las <strong>7:00 a.m.</strong> del día de
recolección, con las ruedas hacia la casa y al menos tres pies de separación de autos
estacionados, buzones y entre sí. Las cuadrillas no regresan por un contenedor sacado tarde.</p>

<h2>Qué va en cada contenedor</h2>
<h3>Contenedor verde — basura</h3>
<p>Desechos domésticos, embolsados. La tapa debe cerrar. Las bolsas adicionales colocadas junto
al contenedor no se recogen en una ruta regular.</p>
<h3>Contenedor azul — reciclaje</h3>
<p>Se acepta: cartón (aplanado), papel, correo, envases de cartón, latas de metal y botellas y
jarras de plástico marcadas #1 y #2.</p>
<p>No se acepta, y es una causa frecuente de carga rechazada: bolsas de plástico de cualquier
tipo, envases de espuma, papel manchado de comida, mangueras de jardín, ropa y vidrio doméstico.
<strong>El reciclaje colocado en una bolsa de plástico se desecha</strong>, porque la bolsa no
puede abrirse de forma segura en la planta de clasificación.</p>

<h2>Artículos voluminosos y ramas</h2>
<p>Los artículos voluminosos se recogen el <strong>primer día de recolección de cada mes</strong>.
Coloque los artículos en la acera no antes del fin de semana previo. El límite es el volumen de
la caja de una camioneta, aproximadamente 8 yardas cúbicas.</p>
<p>Las ramas deben cortarse en tramos de 4 pies o menos y apilarse con los extremos cortados
hacia la calle. Las ramas y los artículos voluminosos deben estar en pilas separadas: una pila
mixta se recoge como voluminosos y cuenta para el límite mensual.</p>
<p>Nunca se recoge en la acera: llantas, pintura, aceite de motor, baterías, electrodomésticos
con refrigerante y escombros de construcción de un trabajo contratado.</p>

<h2>Horario de días festivos</h2>
<p>No hay recolección el Año Nuevo, el Día de los Caídos, el Día de la Independencia, el Día del
Trabajo, el Día de Acción de Gracias y el Día de Navidad. Cuando un día festivo cae entre semana,
la ruta de ese día y todas las rutas posteriores de esa semana se recorren un día, y la ruta del
jueves se realiza el viernes.</p>

<h2>Recolección omitida</h2>
<p>Reporte un contenedor omitido antes de las 10:00 a.m. del siguiente día hábil y una cuadrilla
regresará dentro de un día hábil sin costo. Los reportes hechos después se programan para la
siguiente ruta regular.</p>
""",
        contact_box("es", "Obras Públicas — Residuos Sólidos", "(940) 555-0120",
                    "solidwaste@sablewood.example", MAIN_HOURS_ES)
        + related_box("es", 2, [
            ("Pague su factura de agua", "es/servicios/facturacion-de-agua.html"),
            ("Reportar una violación de código", "es/servicios/cumplimiento-de-codigos.html"),
            ("Departamentos municipales", "es/gobierno/departamentos.html")])))

    # ------------------------------------------------------------------ #
    # BUILDING PERMITS  (note: says nothing about short-term rentals)
    # ------------------------------------------------------------------ #
    write("services/building-permits.html", interior(
        "en", 1, "Permits", "Building permits and inspections",
        "When a permit is required, current fees, how plan review works, and how to schedule "
        "an inspection in the City of Sablewood.",
        [("Home", "index.html"), ("Permits", "services/building-permits.html"),
         ("Building permits", "")],
        """
<h2>When you need a permit</h2>
<p>A permit is required before you begin work on any of the following:</p>
<ul>
  <li>New construction, additions, and any change to a structure's footprint</li>
  <li>Interior remodeling that moves or removes a wall, or alters plumbing, mechanical or
      electrical systems</li>
  <li>Roof replacement, including overlays</li>
  <li>Water heaters, HVAC replacement, and re-piping</li>
  <li>Fences over 6 feet, retaining walls over 4 feet, and any fence in a front yard</li>
  <li>Swimming pools, spas, and the barriers required around them</li>
  <li>Accessory structures over 120 square feet</li>
  <li>Driveway approaches and any work in the public right-of-way</li>
</ul>
<p>No permit is required for painting, floor covering, cabinet replacement, or a storage
building of 120 square feet or less that is not on a permanent foundation and has no plumbing
or electrical service.</p>

<h2>Fees</h2>
<table>
  <caption>Permit fees, fiscal year 2026</caption>
  <thead><tr><th>Permit type</th><th>Fee</th></tr></thead>
  <tbody>
    <tr><td>New single-family residence</td><td>$0.42 per square foot, $650 minimum</td></tr>
    <tr><td>Residential addition or remodel</td><td>$95 plus 1.1% of valuation over $5,000</td></tr>
    <tr><td>Roof replacement</td><td>$120 flat</td></tr>
    <tr><td>Mechanical, electrical or plumbing (standalone)</td><td>$85 each</td></tr>
    <tr><td>Fence or retaining wall</td><td>$65</td></tr>
    <tr><td>Swimming pool</td><td>$275</td></tr>
    <tr><td>Re-inspection after a failed inspection</td><td>$60</td></tr>
    <tr><td>Work started without a permit</td><td>Double the permit fee</td></tr>
  </tbody>
</table>

<h2>Plan review</h2>
<p>Residential plan review takes <strong>five to seven business days</strong> from a complete
submittal. Commercial review takes 10 to 15 business days and includes fire and engineering
review. The clock starts when the submittal is complete — an application missing a site plan or
a signed contractor registration is not in the queue, and this is the single most common reason
a permit takes longer than a resident expects.</p>

<h2>Contractor registration</h2>
<p>Every contractor pulling a permit must be registered with the city and carry general
liability coverage of at least $300,000. Registration runs $110 annually and expires
December 31 regardless of when it was issued. Electrical, plumbing and mechanical contractors
must also provide a current state license.</p>

<h2>Scheduling an inspection</h2>
<p>Request inspections through the permit portal or by calling (940) 555-0131 before
<strong>3:00 p.m.</strong> for next-business-day service. Same-day inspections are not offered.
Someone over 18 must provide access, and the approved plans and the permit card must be on
site — an inspector who cannot reach the work records a failed inspection and the re-inspection
fee applies.</p>
<div class="callout">
  <p><strong>Do not cover work before it is inspected.</strong> Framing, rough plumbing, rough
  electrical and mechanical rough-in must all be inspected while still exposed. Covered work
  will be ordered opened at the permit holder's expense.</p>
</div>

<h2>Expiration</h2>
<p>A permit expires if work has not started within 180 days of issuance, or if work is
abandoned for 180 days. One 90-day extension may be requested in writing before expiration.</p>
""",
        contact_box("en", "Development Services", "(940) 555-0130",
                    "permits@sablewood.example", MAIN_HOURS_EN)
        + related_box("en", 1, [
            ("Report a code violation", "services/code-compliance.html"),
            ("City departments", "government/departments.html"),
            ("Council agendas and minutes", "government/council-agendas.html")])))

    write("es/servicios/permisos-de-construccion.html", interior(
        "es", 2, "Permisos", "Permisos de construcción e inspecciones",
        "Cuándo se requiere un permiso, tarifas vigentes, cómo funciona la revisión de planos y "
        "cómo programar una inspección en la Ciudad de Sablewood.",
        [("Inicio", "es/index.html"), ("Permisos", "es/servicios/permisos-de-construccion.html"),
         ("Permisos de construcción", "")],
        """
<h2>Cuándo necesita un permiso</h2>
<p>Se requiere un permiso antes de comenzar cualquiera de los siguientes trabajos:</p>
<ul>
  <li>Construcción nueva, ampliaciones y cualquier cambio a la huella de una estructura</li>
  <li>Remodelación interior que mueva o elimine un muro, o que altere sistemas de plomería,
      mecánicos o eléctricos</li>
  <li>Reemplazo de techo, incluyendo sobrecapas</li>
  <li>Calentadores de agua, reemplazo de aire acondicionado y cambio de tuberías</li>
  <li>Cercas de más de 6 pies, muros de contención de más de 4 pies y cualquier cerca en el
      patio delantero</li>
  <li>Piscinas, spas y las barreras requeridas a su alrededor</li>
  <li>Estructuras accesorias de más de 120 pies cuadrados</li>
  <li>Accesos de entrada y cualquier trabajo en la vía pública</li>
</ul>
<p>No se requiere permiso para pintar, colocar pisos, reemplazar gabinetes, ni para una bodega
de 120 pies cuadrados o menos que no esté sobre cimentación permanente y no tenga servicio de
plomería ni eléctrico.</p>

<h2>Tarifas</h2>
<table>
  <caption>Tarifas de permisos, año fiscal 2026</caption>
  <thead><tr><th>Tipo de permiso</th><th>Tarifa</th></tr></thead>
  <tbody>
    <tr><td>Residencia unifamiliar nueva</td><td>$0.42 por pie cuadrado, mínimo $650</td></tr>
    <tr><td>Ampliación o remodelación residencial</td><td>$95 más 1.1% del valor sobre $5,000</td></tr>
    <tr><td>Reemplazo de techo</td><td>$120 fijo</td></tr>
    <tr><td>Mecánico, eléctrico o plomería (individual)</td><td>$85 cada uno</td></tr>
    <tr><td>Cerca o muro de contención</td><td>$65</td></tr>
    <tr><td>Piscina</td><td>$275</td></tr>
    <tr><td>Reinspección tras una inspección reprobada</td><td>$60</td></tr>
    <tr><td>Trabajo iniciado sin permiso</td><td>El doble de la tarifa del permiso</td></tr>
  </tbody>
</table>

<h2>Revisión de planos</h2>
<p>La revisión de planos residenciales toma de <strong>cinco a siete días hábiles</strong> desde
una presentación completa. La revisión comercial toma de 10 a 15 días hábiles e incluye revisión
de bomberos e ingeniería. El plazo comienza cuando la presentación está completa: una solicitud
sin plano del sitio o sin registro firmado del contratista no está en la fila, y esta es la razón
más común por la que un permiso tarda más de lo que un residente espera.</p>

<h2>Registro de contratistas</h2>
<p>Todo contratista que solicite un permiso debe estar registrado con la ciudad y contar con
cobertura de responsabilidad civil general de al menos $300,000. El registro cuesta $110 al año
y vence el 31 de diciembre sin importar cuándo se emitió. Los contratistas eléctricos, de
plomería y mecánicos también deben presentar una licencia estatal vigente.</p>

<h2>Programar una inspección</h2>
<p>Solicite inspecciones a través del portal de permisos o llamando al (940) 555-0131 antes de
las <strong>3:00 p.m.</strong> para servicio al siguiente día hábil. No se ofrecen inspecciones
el mismo día. Una persona mayor de 18 años debe dar acceso, y los planos aprobados y la tarjeta
del permiso deben estar en el sitio: un inspector que no pueda llegar al trabajo registra una
inspección reprobada y se aplica la tarifa de reinspección.</p>
<div class="callout">
  <p><strong>No cubra el trabajo antes de que sea inspeccionado.</strong> La estructura, la
  plomería en bruto, el sistema eléctrico en bruto y el trabajo mecánico en bruto deben
  inspeccionarse mientras aún estén expuestos. Se ordenará abrir el trabajo cubierto a costa del
  titular del permiso.</p>
</div>

<h2>Vencimiento</h2>
<p>Un permiso vence si el trabajo no comienza dentro de los 180 días posteriores a su emisión, o
si el trabajo se abandona por 180 días. Se puede solicitar por escrito una prórroga de 90 días
antes del vencimiento.</p>
""",
        contact_box("es", "Servicios de Desarrollo", "(940) 555-0130",
                    "permits@sablewood.example", MAIN_HOURS_ES)
        + related_box("es", 2, [
            ("Reportar una violación de código", "es/servicios/cumplimiento-de-codigos.html"),
            ("Departamentos municipales", "es/gobierno/departamentos.html"),
            ("Agendas y actas del Concejo", "es/gobierno/agendas-del-consejo.html")])))

    # ------------------------------------------------------------------ #
    # PARKS
    # ------------------------------------------------------------------ #
    write("services/parks-recreation.html", interior(
        "en", 1, "Parks", "Parks and recreation",
        "Park hours, pavilion and athletic field reservations, the Sablewood Aquatic Center, "
        "and rules that apply in every city park.",
        [("Home", "index.html"), ("Parks", "services/parks-recreation.html"),
         ("Parks and recreation", "")],
        """
<h2>Park hours</h2>
<p>City parks are open from <strong>6:00 a.m. to 11:00 p.m.</strong> daily unless posted
otherwise. Sablewood Nature Preserve closes at sunset year-round.</p>

<h2>Parks and facilities</h2>
<table>
  <caption>City parks</caption>
  <thead><tr><th>Park</th><th>Acres</th><th>Facilities</th></tr></thead>
  <tbody>
    <tr><td>Heritage Park</td><td>42</td><td>Two pavilions, playground, 1.2-mile loop trail, restrooms</td></tr>
    <tr><td>Millrace Park</td><td>18</td><td>Pavilion, splash pad (May–September), playground</td></tr>
    <tr><td>Sablewood Sports Complex</td><td>63</td><td>Six lighted athletic fields, concession building</td></tr>
    <tr><td>Nature Preserve</td><td>110</td><td>3.4 miles of unpaved trail, no restrooms</td></tr>
    <tr><td>Founders Green</td><td>4</td><td>Open lawn, band shell, seasonal market space</td></tr>
  </tbody>
</table>

<h2>Reserving a pavilion</h2>
<p>Pavilion reservations open <strong>90 days</strong> in advance and close 72 hours before the
date. Reserve online or at the Parks office.</p>
<table>
  <caption>Pavilion rates per four-hour block</caption>
  <thead><tr><th>Pavilion</th><th>Resident</th><th>Non-resident</th><th>Deposit</th></tr></thead>
  <tbody>
    <tr><td>Heritage Park, large</td><td>$75</td><td>$115</td><td>$50</td></tr>
    <tr><td>Heritage Park, small</td><td>$45</td><td>$70</td><td>$50</td></tr>
    <tr><td>Millrace Park</td><td>$45</td><td>$70</td><td>$50</td></tr>
  </tbody>
</table>
<p>The deposit is refunded within 10 business days if the pavilion is left clean and undamaged.
An unreserved pavilion is first-come, first-served; a printed confirmation is what settles a
dispute on the day.</p>

<h2>Athletic fields</h2>
<p>Fields at the Sports Complex are allocated to affiliated youth leagues first, and open for
public reservation on any date not allocated by March 1 for spring or August 1 for fall.
Field lights run until 10:00 p.m. and are billed at $22 per hour.</p>

<h2>Aquatic Center</h2>
<p>The Sablewood Aquatic Center opens the Saturday of Memorial Day weekend and closes the day
after Labor Day. Daily admission is $4 for residents and $7 for non-residents; children two and
under are admitted free. A resident season pass is $85 for an individual and $210 for a
household of up to five.</p>

<h2>Park rules</h2>
<ul>
  <li>Dogs must be leashed. The only off-leash area is the fenced run at Heritage Park.</li>
  <li>Glass containers are prohibited in all parks.</li>
  <li>Alcohol is prohibited except by permit at Founders Green during a permitted event.</li>
  <li>Motorized vehicles are restricted to paved parking areas. Trails are for foot and
      non-motorized traffic only.</li>
  <li>Amplified sound requires a permit and must end by 9:00 p.m.</li>
  <li>Charcoal grills are allowed only in the fixed grills provided. Open ground fires are
      prohibited year-round.</li>
</ul>
""",
        contact_box("en", "Parks and Recreation", "(940) 555-0140",
                    "parks@sablewood.example", MAIN_HOURS_EN)
        + related_box("en", 1, [
            ("Council agendas and minutes", "government/council-agendas.html"),
            ("City departments", "government/departments.html"),
            ("Report a code violation", "services/code-compliance.html")])))

    write("es/servicios/parques-y-recreacion.html", interior(
        "es", 2, "Parques", "Parques y recreación",
        "Horarios de los parques, reservaciones de pabellones y campos deportivos, el Centro "
        "Acuático de Sablewood y las reglas que aplican en todos los parques municipales.",
        [("Inicio", "es/index.html"), ("Parques", "es/servicios/parques-y-recreacion.html"),
         ("Parques y recreación", "")],
        """
<h2>Horario de los parques</h2>
<p>Los parques municipales están abiertos de <strong>6:00 a.m. a 11:00 p.m.</strong> todos los
días salvo indicación contraria. La Reserva Natural de Sablewood cierra al atardecer todo el
año.</p>

<h2>Parques e instalaciones</h2>
<table>
  <caption>Parques municipales</caption>
  <thead><tr><th>Parque</th><th>Acres</th><th>Instalaciones</th></tr></thead>
  <tbody>
    <tr><td>Heritage Park</td><td>42</td><td>Dos pabellones, juegos infantiles, sendero de 1.2 millas, baños</td></tr>
    <tr><td>Millrace Park</td><td>18</td><td>Pabellón, área de chorros de agua (mayo–septiembre), juegos infantiles</td></tr>
    <tr><td>Complejo Deportivo Sablewood</td><td>63</td><td>Seis campos deportivos iluminados, edificio de concesiones</td></tr>
    <tr><td>Reserva Natural</td><td>110</td><td>3.4 millas de sendero sin pavimentar, sin baños</td></tr>
    <tr><td>Founders Green</td><td>4</td><td>Césped abierto, concha acústica, espacio para mercado estacional</td></tr>
  </tbody>
</table>

<h2>Reservar un pabellón</h2>
<p>Las reservaciones de pabellones abren con <strong>90 días</strong> de anticipación y cierran
72 horas antes de la fecha. Reserve en línea o en la oficina de Parques.</p>
<table>
  <caption>Tarifas de pabellones por bloque de cuatro horas</caption>
  <thead><tr><th>Pabellón</th><th>Residente</th><th>No residente</th><th>Depósito</th></tr></thead>
  <tbody>
    <tr><td>Heritage Park, grande</td><td>$75</td><td>$115</td><td>$50</td></tr>
    <tr><td>Heritage Park, pequeño</td><td>$45</td><td>$70</td><td>$50</td></tr>
    <tr><td>Millrace Park</td><td>$45</td><td>$70</td><td>$50</td></tr>
  </tbody>
</table>
<p>El depósito se reembolsa dentro de 10 días hábiles si el pabellón se deja limpio y sin daños.
Un pabellón sin reservación se otorga por orden de llegada; una confirmación impresa es lo que
resuelve una disputa el día del evento.</p>

<h2>Campos deportivos</h2>
<p>Los campos del Complejo Deportivo se asignan primero a las ligas juveniles afiliadas, y quedan
disponibles para reservación pública en cualquier fecha no asignada antes del 1 de marzo para la
temporada de primavera o del 1 de agosto para la de otoño. Las luces de los campos funcionan
hasta las 10:00 p.m. y se cobran a $22 por hora.</p>

<h2>Centro Acuático</h2>
<p>El Centro Acuático de Sablewood abre el sábado del fin de semana del Día de los Caídos y
cierra el día después del Día del Trabajo. La entrada diaria cuesta $4 para residentes y $7 para
no residentes; los niños de dos años o menos entran gratis. El pase de temporada para residentes
cuesta $85 individual y $210 para un hogar de hasta cinco personas.</p>

<h2>Reglas de los parques</h2>
<ul>
  <li>Los perros deben estar con correa. La única área sin correa es el corral cercado de
      Heritage Park.</li>
  <li>Los envases de vidrio están prohibidos en todos los parques.</li>
  <li>El alcohol está prohibido salvo con permiso en Founders Green durante un evento
      autorizado.</li>
  <li>Los vehículos motorizados están restringidos a las áreas pavimentadas de estacionamiento.
      Los senderos son solo para tránsito a pie y no motorizado.</li>
  <li>El sonido amplificado requiere permiso y debe terminar a las 9:00 p.m.</li>
  <li>Las parrillas de carbón se permiten únicamente en las parrillas fijas provistas. Las
      fogatas en el suelo están prohibidas todo el año.</li>
</ul>
""",
        contact_box("es", "Parques y Recreación", "(940) 555-0140",
                    "parks@sablewood.example", MAIN_HOURS_ES)
        + related_box("es", 2, [
            ("Agendas y actas del Concejo", "es/gobierno/agendas-del-consejo.html"),
            ("Departamentos municipales", "es/gobierno/departamentos.html"),
            ("Reportar una violación de código", "es/servicios/cumplimiento-de-codigos.html")])))

    # ------------------------------------------------------------------ #
    # CODE COMPLIANCE
    # ------------------------------------------------------------------ #
    write("services/code-compliance.html", interior(
        "en", 1, "Services", "Report a code violation",
        "What the city enforces, how to file a complaint, how long the process takes, and what "
        "happens if a property is not brought into compliance.",
        [("Home", "index.html"), ("Services", "services/utility-billing.html"),
         ("Code compliance", "")],
        """
<h2>What we enforce</h2>
<p>Code Compliance responds to violations of the city's property maintenance, nuisance and
zoning ordinances. The most frequent are:</p>
<ul>
  <li><strong>High grass and weeds</strong> exceeding 12 inches on any developed lot</li>
  <li><strong>Junk, trash and debris</strong> visible from a public street or an adjoining lot</li>
  <li><strong>Junked vehicles</strong> — inoperable, unregistered or wrecked, and visible from
      a public place</li>
  <li><strong>Illegal signage</strong>, including signs in the right-of-way and portable signs
      without a permit</li>
  <li><strong>Substandard structures</strong> that are open, unsecured or structurally unsound</li>
  <li><strong>Prohibited outdoor storage</strong> in a residential front or side yard</li>
  <li><strong>Work without a permit</strong>, referred jointly with Development Services</li>
</ul>
<p>Some matters are not code violations and are handled elsewhere: barking dogs and loose animals
go to Animal Services, parking on a public street goes to the Police Department, and disputes
over a fence exactly on a property line are civil matters between owners.</p>

<h2>How to file a complaint</h2>
<p>Report online, by phone at (940) 555-0150, or in person at City Hall. Give the address and
what you observed. A complaint may be filed anonymously, though an anonymous complaint means we
cannot come back to you for detail, and a case that turns on a detail nobody can confirm is
usually closed.</p>
<div class="callout">
  <p><strong>Your name is not released to the property owner by the city.</strong> Complaint
  records are, however, government records and may be subject to release under the Texas Public
  Information Act.</p>
</div>

<h2>What happens next</h2>
<ol>
  <li><strong>Inspection</strong> — an officer inspects within three business days of the
      report.</li>
  <li><strong>Notice</strong> — if a violation exists, the owner receives written notice with a
      compliance deadline: 10 days for grass and weeds, 30 days for most structural items.</li>
  <li><strong>Re-inspection</strong> — the officer returns after the deadline.</li>
  <li><strong>Abatement or citation</strong> — for grass and weeds the city may mow and place
      the cost plus a $100 administrative fee as a lien against the property. Other violations
      are cited to municipal court, where each day of continued violation is a separate offense
      carrying a fine of up to $500, or up to $2,000 for a violation affecting public health
      and safety.</li>
</ol>

<h2>How long it takes</h2>
<p>A straightforward grass case closes in about three weeks: three days to inspect, ten days'
notice, and a re-inspection. Structural cases take considerably longer because the notice period
is longer and the owner has a right to be heard before a building standards panel.</p>
""",
        contact_box("en", "Code Compliance", "(940) 555-0150",
                    "code@sablewood.example", MAIN_HOURS_EN)
        + related_box("en", 1, [
            ("Building permits and inspections", "services/building-permits.html"),
            ("Trash and recycling collection", "services/trash-recycling.html"),
            ("City departments", "government/departments.html")])))

    write("es/servicios/cumplimiento-de-codigos.html", interior(
        "es", 2, "Servicios", "Reportar una violación de código",
        "Qué hace cumplir la ciudad, cómo presentar una queja, cuánto tarda el proceso y qué "
        "sucede si una propiedad no se pone en cumplimiento.",
        [("Inicio", "es/index.html"), ("Servicios", "es/servicios/facturacion-de-agua.html"),
         ("Cumplimiento de códigos", "")],
        """
<h2>Qué hacemos cumplir</h2>
<p>Cumplimiento de Códigos responde a violaciones de las ordenanzas municipales de mantenimiento
de propiedades, molestias públicas y zonificación. Las más frecuentes son:</p>
<ul>
  <li><strong>Césped y maleza altos</strong> que superen las 12 pulgadas en cualquier lote
      desarrollado</li>
  <li><strong>Chatarra, basura y escombros</strong> visibles desde una calle pública o desde un
      lote colindante</li>
  <li><strong>Vehículos chatarra</strong> — inservibles, sin registro o accidentados, y visibles
      desde un lugar público</li>
  <li><strong>Letreros ilegales</strong>, incluyendo letreros en la vía pública y letreros
      portátiles sin permiso</li>
  <li><strong>Estructuras deficientes</strong> que estén abiertas, sin asegurar o
      estructuralmente inseguras</li>
  <li><strong>Almacenamiento exterior prohibido</strong> en el patio delantero o lateral de una
      vivienda</li>
  <li><strong>Trabajo sin permiso</strong>, referido conjuntamente con Servicios de Desarrollo</li>
</ul>
<p>Algunos asuntos no son violaciones de código y se atienden en otra parte: los perros que
ladran y los animales sueltos corresponden a Servicios de Animales, el estacionamiento en la
calle pública al Departamento de Policía, y las disputas sobre una cerca exactamente en el límite
de propiedad son asuntos civiles entre propietarios.</p>

<h2>Cómo presentar una queja</h2>
<p>Reporte en línea, por teléfono al (940) 555-0150 o en persona en el Ayuntamiento. Indique la
dirección y lo que observó. Una queja puede presentarse de forma anónima, aunque una queja
anónima significa que no podemos contactarlo para obtener detalles, y un caso que depende de un
detalle que nadie puede confirmar normalmente se cierra.</p>
<div class="callout">
  <p><strong>La ciudad no divulga su nombre al propietario.</strong> Sin embargo, los registros
  de quejas son registros gubernamentales y pueden estar sujetos a divulgación bajo la Ley de
  Información Pública de Texas.</p>
</div>

<h2>Qué sucede después</h2>
<ol>
  <li><strong>Inspección</strong> — un oficial inspecciona dentro de los tres días hábiles
      siguientes al reporte.</li>
  <li><strong>Aviso</strong> — si existe una violación, el propietario recibe aviso por escrito
      con un plazo de cumplimiento: 10 días para césped y maleza, 30 días para la mayoría de los
      asuntos estructurales.</li>
  <li><strong>Reinspección</strong> — el oficial regresa después del plazo.</li>
  <li><strong>Remediación o citación</strong> — en casos de césped y maleza la ciudad puede podar
      y colocar el costo más una tarifa administrativa de $100 como gravamen sobre la propiedad.
      Otras violaciones se citan al tribunal municipal, donde cada día de violación continuada es
      una infracción separada con multa de hasta $500, o hasta $2,000 por una violación que
      afecte la salud y seguridad públicas.</li>
</ol>

<h2>Cuánto tarda</h2>
<p>Un caso sencillo de césped se cierra en unas tres semanas: tres días para inspeccionar, diez
días de aviso y una reinspección. Los casos estructurales tardan considerablemente más porque el
plazo de aviso es más largo y el propietario tiene derecho a ser escuchado ante un panel de
normas de construcción.</p>
""",
        contact_box("es", "Cumplimiento de Códigos", "(940) 555-0150",
                    "code@sablewood.example", MAIN_HOURS_ES)
        + related_box("es", 2, [
            ("Permisos de construcción e inspecciones", "es/servicios/permisos-de-construccion.html"),
            ("Recolección de basura y reciclaje", "es/servicios/basura-y-reciclaje.html"),
            ("Departamentos municipales", "es/gobierno/departamentos.html")])))

    # ------------------------------------------------------------------ #
    # COUNCIL AGENDAS
    # ------------------------------------------------------------------ #
    write("government/council-agendas.html", interior(
        "en", 1, "Agendas", "City Council agendas and minutes",
        "When the Sablewood City Council meets, how to read an agenda packet, and how to speak "
        "at a meeting.",
        [("Home", "index.html"), ("Government", "government/departments.html"),
         ("Council agendas", "")],
        """
<h2>Meeting schedule</h2>
<p>The City Council meets in regular session on the <strong>second and fourth Tuesday</strong> of
each month at <strong>6:00 p.m.</strong> in the Council Chambers, 100 Civic Plaza. Work sessions
begin at 5:00 p.m. when scheduled. Special meetings are posted at least 72 hours in advance as
required by the Texas Open Meetings Act.</p>
<table>
  <caption>Regular boards and commissions</caption>
  <thead><tr><th>Body</th><th>Meets</th><th>Time</th></tr></thead>
  <tbody>
    <tr><td>City Council</td><td>2nd and 4th Tuesday</td><td>6:00 p.m.</td></tr>
    <tr><td>Planning &amp; Zoning Commission</td><td>3rd Tuesday</td><td>6:30 p.m.</td></tr>
    <tr><td>Zoning Board of Adjustment</td><td>1st Thursday, as needed</td><td>6:00 p.m.</td></tr>
    <tr><td>Parks Advisory Board</td><td>4th Tuesday</td><td>5:30 p.m.</td></tr>
    <tr><td>Building Standards Commission</td><td>2nd Thursday, as needed</td><td>6:00 p.m.</td></tr>
  </tbody>
</table>

<h2>Agendas and packets</h2>
<p>Agendas are posted no later than <strong>72 hours</strong> before a meeting. The agenda packet
— the staff reports, ordinances, contracts and exhibits the Council will actually be reading —
is posted at the same time. Minutes are posted after the Council approves them, normally at the
following regular meeting, so the minutes of any given meeting appear about two weeks later.</p>

<h2>Speaking at a meeting</h2>
<p>Anyone may address the Council. Complete a speaker card and give it to the City Secretary
before the item is called. Each speaker has <strong>three minutes</strong>; a speaker
representing an organized group may be granted five.</p>
<p>During <strong>public comment</strong> you may raise any subject within the Council's
authority. The Council cannot deliberate or decide on a subject that is not posted on the agenda
— by law, not by preference — so expect an item raised in public comment to be referred to staff
or posted for a future meeting rather than answered from the dais.</p>
<p>During a <strong>public hearing</strong>, comment is limited to the subject of the hearing.</p>

<h2>Executive session</h2>
<p>The Council may meet in closed session on the limited matters allowed by the Texas Open
Meetings Act — consultation with its attorney, real property, personnel and security devices
among them. Any final action must be taken in open session.</p>

<h2>Requesting a record</h2>
<p>Agendas, packets, minutes and recordings are public records. For a record not posted online,
submit a public information request to the City Secretary at (940) 555-0160. The city responds
promptly and within 10 business days as the Public Information Act requires.</p>
""",
        contact_box("en", "City Secretary", "(940) 555-0160",
                    "citysecretary@sablewood.example", MAIN_HOURS_EN)
        + related_box("en", 1, [
            ("City departments", "government/departments.html"),
            ("Building permits and inspections", "services/building-permits.html"),
            ("Parks and recreation", "services/parks-recreation.html")])))

    write("es/gobierno/agendas-del-consejo.html", interior(
        "es", 2, "Agendas", "Agendas y actas del Concejo Municipal",
        "Cuándo se reúne el Concejo Municipal de Sablewood, cómo leer un paquete de agenda y cómo "
        "hablar en una reunión.",
        [("Inicio", "es/index.html"), ("Gobierno", "es/gobierno/departamentos.html"),
         ("Agendas del Concejo", "")],
        """
<h2>Calendario de reuniones</h2>
<p>El Concejo Municipal se reúne en sesión ordinaria el <strong>segundo y cuarto martes</strong>
de cada mes a las <strong>6:00 p.m.</strong> en la Sala del Concejo, 100 Civic Plaza. Las
sesiones de trabajo comienzan a las 5:00 p.m. cuando están programadas. Las reuniones especiales
se publican con al menos 72 horas de anticipación, como exige la Ley de Reuniones Abiertas de
Texas.</p>
<table>
  <caption>Juntas y comisiones ordinarias</caption>
  <thead><tr><th>Organismo</th><th>Se reúne</th><th>Hora</th></tr></thead>
  <tbody>
    <tr><td>Concejo Municipal</td><td>2.º y 4.º martes</td><td>6:00 p.m.</td></tr>
    <tr><td>Comisión de Planificación y Zonificación</td><td>3.er martes</td><td>6:30 p.m.</td></tr>
    <tr><td>Junta de Ajustes de Zonificación</td><td>1.er jueves, según necesidad</td><td>6:00 p.m.</td></tr>
    <tr><td>Junta Asesora de Parques</td><td>4.º martes</td><td>5:30 p.m.</td></tr>
    <tr><td>Comisión de Normas de Construcción</td><td>2.º jueves, según necesidad</td><td>6:00 p.m.</td></tr>
  </tbody>
</table>

<h2>Agendas y paquetes</h2>
<p>Las agendas se publican a más tardar <strong>72 horas</strong> antes de una reunión. El paquete
de la agenda — los informes del personal, ordenanzas, contratos y anexos que el Concejo realmente
leerá — se publica al mismo tiempo. Las actas se publican después de que el Concejo las aprueba,
normalmente en la siguiente reunión ordinaria, por lo que las actas de una reunión aparecen unas
dos semanas después.</p>

<h2>Hablar en una reunión</h2>
<p>Cualquier persona puede dirigirse al Concejo. Complete una tarjeta de orador y entréguela al
Secretario Municipal antes de que se anuncie el punto. Cada orador dispone de <strong>tres
minutos</strong>; un orador que represente a un grupo organizado puede recibir cinco.</p>
<p>Durante el <strong>comentario público</strong> puede plantear cualquier tema dentro de la
autoridad del Concejo. El Concejo no puede deliberar ni decidir sobre un tema que no esté
publicado en la agenda — por ley, no por preferencia — así que espere que un tema planteado en
comentario público se remita al personal o se publique para una reunión futura en lugar de
responderse desde el estrado.</p>
<p>Durante una <strong>audiencia pública</strong>, los comentarios se limitan al tema de la
audiencia.</p>

<h2>Sesión ejecutiva</h2>
<p>El Concejo puede reunirse a puerta cerrada sobre los asuntos limitados que permite la Ley de
Reuniones Abiertas de Texas — consultas con su abogado, bienes inmuebles, personal y dispositivos
de seguridad, entre otros. Toda acción final debe tomarse en sesión abierta.</p>

<h2>Solicitar un registro</h2>
<p>Las agendas, paquetes, actas y grabaciones son registros públicos. Para un registro que no
esté publicado en línea, presente una solicitud de información pública al Secretario Municipal
al (940) 555-0160. La ciudad responde con prontitud y dentro de 10 días hábiles, como exige la
Ley de Información Pública.</p>
""",
        contact_box("es", "Secretaría Municipal", "(940) 555-0160",
                    "citysecretary@sablewood.example", MAIN_HOURS_ES)
        + related_box("es", 2, [
            ("Departamentos municipales", "es/gobierno/departamentos.html"),
            ("Permisos de construcción e inspecciones", "es/servicios/permisos-de-construccion.html"),
            ("Parques y recreación", "es/servicios/parques-y-recreacion.html")])))

    # ------------------------------------------------------------------ #
    # DEPARTMENTS  - the deferral target. Every "we don't publish that"
    # answer sends a resident HERE, so it has to be genuinely useful.
    # ------------------------------------------------------------------ #
    dept_rows_en = """
    <tr><td>City Hall (main)</td><td>(940) 555-0100</td><td>General information, directions</td></tr>
    <tr><td>Utility Billing</td><td>(940) 555-0110</td><td>Water, sewer and solid waste accounts</td></tr>
    <tr><td>Automated payment line</td><td>(940) 555-0111</td><td>Pay a utility bill, 24 hours</td></tr>
    <tr><td>Public Works</td><td>(940) 555-0120</td><td>Streets, drainage, water distribution</td></tr>
    <tr><td>Solid Waste</td><td>(940) 555-0120</td><td>Carts, missed collection, bulk and brush</td></tr>
    <tr><td>Development Services</td><td>(940) 555-0130</td><td>Permits, plan review, zoning</td></tr>
    <tr><td>Inspection scheduling</td><td>(940) 555-0131</td><td>Book or cancel an inspection</td></tr>
    <tr><td>Parks and Recreation</td><td>(940) 555-0140</td><td>Reservations, athletics, aquatics</td></tr>
    <tr><td>Code Compliance</td><td>(940) 555-0150</td><td>Property maintenance, nuisance, signage</td></tr>
    <tr><td>City Secretary</td><td>(940) 555-0160</td><td>Agendas, minutes, public information requests</td></tr>
    <tr><td>Municipal Court</td><td>(940) 555-0170</td><td>Citations, fines, court dates</td></tr>
    <tr><td>Animal Services</td><td>(940) 555-0180</td><td>Loose animals, barking, licensing</td></tr>"""

    write("government/departments.html", interior(
        "en", 1, "Contact", "City departments and contacts",
        "Every City of Sablewood department, what it handles, and the number that reaches a "
        "person during business hours.",
        [("Home", "index.html"), ("Government", "government/departments.html"),
         ("Departments", "")],
        f"""
<h2>City Hall</h2>
<p>100 Civic Plaza, Sablewood, TX 76077<br>
Main line (940) 555-0100<br>
{MAIN_HOURS_EN}, closed on city holidays</p>

<h2>Departments</h2>
<table>
  <caption>Department directory</caption>
  <thead><tr><th>Department</th><th>Phone</th><th>Handles</th></tr></thead>
  <tbody>{dept_rows_en}</tbody>
</table>

<h2>After hours and emergencies</h2>
<p>For a life-threatening emergency, call 911.</p>
<p>For a water main break, sewer overflow, traffic signal failure or another hazard outside
business hours, call the Public Works after-hours line at (940) 555-0121. It is answered by a
dispatcher, not a recording.</p>

<h2>If you are not sure who to call</h2>
<p>Call the main line at (940) 555-0100 and describe the problem. Staff will route you rather
than transfer you blindly. If your question concerns something the city has not published on
this website, the department listed above is the authority on it — this directory is
deliberately the place every unanswered question ends up.</p>

<h2>Requesting records</h2>
<p>Public information requests go to the City Secretary. Submit in writing, by mail, in person,
or by email to citysecretary@sablewood.example. Describe the records you want rather than asking
a question — the Public Information Act obliges the city to produce existing records, not to
create new ones or to answer questions.</p>
""",
        contact_box("en", "City Hall", "(940) 555-0100",
                    "info@sablewood.example", MAIN_HOURS_EN)
        + related_box("en", 1, [
            ("Council agendas and minutes", "government/council-agendas.html"),
            ("Pay your water bill", "services/utility-billing.html"),
            ("Report a code violation", "services/code-compliance.html")])))

    dept_rows_es = """
    <tr><td>Ayuntamiento (principal)</td><td>(940) 555-0100</td><td>Información general, direcciones</td></tr>
    <tr><td>Facturación de Servicios</td><td>(940) 555-0110</td><td>Cuentas de agua, alcantarillado y residuos</td></tr>
    <tr><td>Línea automatizada de pagos</td><td>(940) 555-0111</td><td>Pagar una factura, 24 horas</td></tr>
    <tr><td>Obras Públicas</td><td>(940) 555-0120</td><td>Calles, drenaje, distribución de agua</td></tr>
    <tr><td>Residuos Sólidos</td><td>(940) 555-0120</td><td>Contenedores, recolección omitida, voluminosos</td></tr>
    <tr><td>Servicios de Desarrollo</td><td>(940) 555-0130</td><td>Permisos, revisión de planos, zonificación</td></tr>
    <tr><td>Programación de inspecciones</td><td>(940) 555-0131</td><td>Agendar o cancelar una inspección</td></tr>
    <tr><td>Parques y Recreación</td><td>(940) 555-0140</td><td>Reservaciones, deportes, centro acuático</td></tr>
    <tr><td>Cumplimiento de Códigos</td><td>(940) 555-0150</td><td>Mantenimiento de propiedades, molestias, letreros</td></tr>
    <tr><td>Secretaría Municipal</td><td>(940) 555-0160</td><td>Agendas, actas, solicitudes de información</td></tr>
    <tr><td>Tribunal Municipal</td><td>(940) 555-0170</td><td>Citaciones, multas, fechas de audiencia</td></tr>
    <tr><td>Servicios de Animales</td><td>(940) 555-0180</td><td>Animales sueltos, ladridos, licencias</td></tr>"""

    write("es/gobierno/departamentos.html", interior(
        "es", 2, "Contacto", "Departamentos y contactos municipales",
        "Cada departamento de la Ciudad de Sablewood, de qué se encarga y el número que conecta "
        "con una persona en horario de oficina.",
        [("Inicio", "es/index.html"), ("Gobierno", "es/gobierno/departamentos.html"),
         ("Departamentos", "")],
        f"""
<h2>Ayuntamiento</h2>
<p>100 Civic Plaza, Sablewood, TX 76077<br>
Línea principal (940) 555-0100<br>
{MAIN_HOURS_ES}, cerrado en días festivos municipales</p>

<h2>Departamentos</h2>
<table>
  <caption>Directorio de departamentos</caption>
  <thead><tr><th>Departamento</th><th>Teléfono</th><th>Atiende</th></tr></thead>
  <tbody>{dept_rows_es}</tbody>
</table>

<h2>Fuera de horario y emergencias</h2>
<p>Para una emergencia que ponga en peligro la vida, llame al 911.</p>
<p>Para una ruptura de tubería principal, un desbordamiento de alcantarillado, una falla de
semáforo u otro peligro fuera del horario de oficina, llame a la línea de Obras Públicas fuera
de horario al (940) 555-0121. Contesta un despachador, no una grabación.</p>

<h2>Si no sabe a quién llamar</h2>
<p>Llame a la línea principal al (940) 555-0100 y describa el problema. El personal lo dirigirá
en lugar de transferirlo a ciegas. Si su pregunta se refiere a algo que la ciudad no ha publicado
en este sitio web, el departamento indicado arriba es la autoridad en el tema: este directorio es
deliberadamente el lugar donde termina toda pregunta sin respuesta.</p>

<h2>Solicitar registros</h2>
<p>Las solicitudes de información pública se dirigen a la Secretaría Municipal. Preséntelas por
escrito, por correo, en persona o por correo electrónico a citysecretary@sablewood.example.
Describa los registros que desea en lugar de hacer una pregunta: la Ley de Información Pública
obliga a la ciudad a producir registros existentes, no a crear nuevos ni a responder preguntas.</p>
""",
        contact_box("es", "Ayuntamiento", "(940) 555-0100",
                    "info@sablewood.example", MAIN_HOURS_ES)
        + related_box("es", 2, [
            ("Agendas y actas del Concejo", "es/gobierno/agendas-del-consejo.html"),
            ("Pague su factura de agua", "es/servicios/facturacion-de-agua.html"),
            ("Reportar una violación de código", "es/servicios/cumplimiento-de-codigos.html")])))

    # ------------------------------------------------------------------ #
    # ACCESSIBILITY
    # ------------------------------------------------------------------ #
    write("accessibility.html", interior(
        "en", 0, "", "Accessibility",
        "How this site is built to be usable, and how to tell us when it is not.",
        [("Home", "index.html"), ("Accessibility", "")],
        """
<h2>Our commitment</h2>
<p>This site is built to meet <strong>WCAG 2.2 Level AA</strong>. In practice that means every
control can be reached and operated with a keyboard alone, headings describe the structure of
each page rather than its appearance, colour is never the only way information is conveyed,
tables carry captions and header cells, and animation is suppressed for anyone whose system
requests reduced motion.</p>

<h2>The digital assistant</h2>
<p>The assistant on the home page is usable as plain text chat with a keyboard and a screen
reader. The avatar is optional and never required to get an answer. Answers are announced in a
live region so a screen-reader user hears a reply arrive without hunting for it.</p>
<p>Under Texas House Bill 149, the Texas Responsible Artificial Intelligence Governance Act,
you are told plainly and before you interact that you are dealing with an AI system. That
disclosure is on the assistant itself, not buried in a policy page.</p>

<h2>Reporting a barrier</h2>
<p>If any part of this site or a city service is not accessible to you, contact City Hall at
(940) 555-0100 or info@sablewood.example. Tell us the page and what happened. The city responds
to accessibility reports within five business days, and a barrier that prevents you completing a
city transaction is treated as a service outage rather than a website bug.</p>
<p>You may also request any city information in an alternate format at no charge.</p>
""",
        contact_box("en", "City Hall", "(940) 555-0100",
                    "info@sablewood.example", MAIN_HOURS_EN)))

    write("es/accesibilidad.html", interior(
        "es", 1, "", "Accesibilidad",
        "Cómo está construido este sitio para ser utilizable, y cómo informarnos cuando no lo es.",
        [("Inicio", "es/index.html"), ("Accesibilidad", "")],
        """
<h2>Nuestro compromiso</h2>
<p>Este sitio está construido para cumplir con <strong>WCAG 2.2 Nivel AA</strong>. En la práctica
eso significa que todo control puede alcanzarse y operarse solo con el teclado, que los
encabezados describen la estructura de cada página y no su apariencia, que el color nunca es la
única forma de transmitir información, que las tablas incluyen títulos y celdas de encabezado, y
que la animación se suprime para quien tenga configurado su sistema con movimiento reducido.</p>

<h2>El asistente digital</h2>
<p>El asistente de la página principal puede usarse como chat de texto simple con teclado y
lector de pantalla. El avatar es opcional y nunca es necesario para obtener una respuesta. Las
respuestas se anuncian en una región activa para que una persona que use lector de pantalla
escuche la llegada de la respuesta sin tener que buscarla.</p>
<p>Conforme a la Ley 149 de la Cámara de Representantes de Texas, la Ley de Gobernanza
Responsable de Inteligencia Artificial de Texas, se le informa de manera clara y antes de
interactuar que está tratando con un sistema de inteligencia artificial. Esa divulgación está en
el propio asistente, no escondida en una página de políticas.</p>

<h2>Reportar una barrera</h2>
<p>Si alguna parte de este sitio o de un servicio municipal no le resulta accesible, comuníquese
con el Ayuntamiento al (940) 555-0100 o a info@sablewood.example. Indíquenos la página y lo que
ocurrió. La ciudad responde a los reportes de accesibilidad dentro de cinco días hábiles, y una
barrera que le impida completar un trámite municipal se trata como una interrupción del servicio
y no como un error del sitio web.</p>
<p>También puede solicitar cualquier información municipal en un formato alternativo sin costo.</p>
""",
        contact_box("es", "Ayuntamiento", "(940) 555-0100",
                    "info@sablewood.example", MAIN_HOURS_ES)))
