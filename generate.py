#!/usr/bin/env python3
"""
POOF Junk Removal & Cleanouts - static site generator.

This file is the SOURCE OF TRUTH. Do not edit the generated .html files
directly - edit this script and re-run it:

    python3 generate.py

Then commit and push. GitHub Pages publishes in about a minute.
"""

import time
import html as _html

# ---------------------------------------------------------------------------
# SITE CONSTANTS
# ---------------------------------------------------------------------------
# NOTE: PHONE and EMAIL below are PLACEHOLDERS. They are not real and must be
# replaced before this site is promoted anywhere. Search for "PLACEHOLDER".

SITE = {
    "name": "POOF",
    "full_name": "POOF Junk Removal & Cleanouts",
    "tagline": "Poof, it's gone.",
    "secondary_tagline": "We make your junk disappear.",
    "phone": "(000) 000-0000",          # PLACEHOLDER - Google Voice number pending
    "phone_href": "tel:+10000000000",   # PLACEHOLDER
    "sms_href": "sms:+10000000000",     # PLACEHOLDER - Google Voice supports SMS
    "contact_verb": "Call or text",
    "email": "hello@example.com",       # PLACEHOLDER - domain not registered yet
    "base_zip": "20151",
    "region": "Northern Virginia",
    "base_city": "Chantilly / Fairfax",
}

VERSION = str(int(time.time()))

SERVICE_AREAS = [
    "Chantilly", "Fairfax", "Centreville", "Oakton", "Vienna", "McLean",
    "Great Falls", "Reston", "Herndon", "Falls Church", "Arlington",
    "Burke", "Springfield", "Alexandria", "Sterling", "Ashburn",
    "Lorton", "Manassas", "Woodbridge", "Dumfries",
]


# ---------------------------------------------------------------------------
# SHARED SHELL
# ---------------------------------------------------------------------------

def head(title, description, page_class=""):
    return f"""<!DOCTYPE html>
<html lang="en" class="{page_class}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{_html.escape(title)}</title>
<meta name="description" content="{_html.escape(description)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700;12..96,800&family=Instrument+Sans:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css?v={VERSION}">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
"""


def logo(variant="nav"):
    """Real logo files, exported from the Canva source.

    nav  = wordmark only (POOF, no descriptor) for the sticky header
    foot = full lockup with the JUNK REMOVAL & CLEANOUTS pill
    """
    src = {
        "nav":  ("assets/logo-nav-lockup.png", "POOF Junk Removal & Cleanouts"),
        "foot": ("assets/logo-lockup.png", "POOF Junk Removal & Cleanouts"),
    }[variant]
    return (f'<img class="logo logo--{variant}" src="{src[0]}?v={VERSION}" '
            f'alt="{src[1]}" width="1031" height="560">'
            if variant == "nav" else
            f'<img class="logo logo--{variant}" src="{src[0]}?v={VERSION}" '
            f'alt="{src[1]}" width="963" height="520">')


def nav(active=""):
    def cls(name):
        return ' class="on"' if name == active else ""
    return f"""<header class="nav">
  <div class="wrap nav__in">
    <a class="nav__logo" href="index.html">{logo("nav")}</a>
    <nav aria-label="Main">
      <a href="index.html#services"{cls("services")}>Services</a>
      <a href="index.html#area"{cls("area")}>Service area</a>
      <a href="estimate.html"{cls("estimate")}>Get an estimate</a>
    </nav>
    <a class="btn btn--sm nav__call" href="{SITE['phone_href']}"><span class="nav__call-label">{SITE['contact_verb']}</span> {SITE['phone']}</a>
  </div>
</header>
"""


def footer():
    areas = " &middot; ".join(SERVICE_AREAS)
    return f"""<footer class="foot">
  <div class="wrap">
    <div class="foot__top">
      <div class="foot__brand">
        {logo("foot")}
        <p class="foot__tag">{SITE['secondary_tagline']}</p>
      </div>
      <div class="foot__col">
        <h3>Get in touch</h3>
        <p><a href="{SITE['phone_href']}">{SITE['phone']}</a></p>
        <p class="muted">Call or text, including photos</p>
        <p><a href="mailto:{SITE['email']}">{SITE['email']}</a></p>
        <p class="muted">Serving {SITE['region']}</p>
      </div>
      <div class="foot__col">
        <h3>Pages</h3>
        <p><a href="index.html">Home</a></p>
        <p><a href="index.html#services">Services</a></p>
        <p><a href="estimate.html">Get an estimate</a></p>
      </div>
    </div>
    <p class="foot__areas">{areas}</p>
    <p class="foot__legal">&copy; {time.strftime('%Y')} {SITE['full_name']}. Serving Virginia.</p>
  </div>
</footer>
<script src="app.js?v={VERSION}"></script>
</body>
</html>
"""


# ---------------------------------------------------------------------------
# PAGE: HOME
# ---------------------------------------------------------------------------

SERVICES = [
    ("Garage cleanouts",
     "Years of accumulation cleared in a single visit, floor swept when we leave."),
    ("Basement &amp; attic cleanouts",
     "Tight stairs and low clearances are routine. We bring the manpower for it."),
    ("Estate cleanouts",
     "Whole-property clearing handled discreetly, at whatever pace the family needs."),
    ("Furniture &amp; appliances",
     "Sectionals, safes, treadmills, refrigerators. Disassembly included when needed."),
    ("Commercial &amp; office",
     "Lease turnovers, cubicle teardowns, and retail fit-outs, scheduled after hours."),
    ("Property turnovers",
     "Pre-listing clearing and post-tenant cleanouts on a timeline that holds."),
]

STEPS = [
    ("Tell us what's going",
     "Describe it in a sentence, or just text us a photo of the pile. That's enough for us to price it."),
    ("We confirm and schedule",
     "You get an arrival window and a price before anyone touches anything."),
    ("Poof, it's gone",
     "We load, sweep the space, and sort the load for donation and recycling on the way out."),
]


def home():
    services = "\n".join(
        f"""      <article class="card">
        <h3>{t}</h3>
        <p>{d}</p>
      </article>""" for t, d in SERVICES)

    steps = "\n".join(
        f"""      <li class="step">
        <span class="step__n">{i}</span>
        <div>
          <h3>{t}</h3>
          <p>{d}</p>
        </div>
      </li>""" for i, (t, d) in enumerate(STEPS, 1))

    areas = "\n".join(f'        <li>{a}</li>' for a in SERVICE_AREAS)

    return head(
        f"{SITE['full_name']} | {SITE['region']}",
        "Premium junk removal and cleanouts across Northern Virginia. Garages, "
        "basements, estates, and commercial properties. Donation and recycling "
        "first.",
    ) + nav() + f"""
<main id="main">

  <section class="hero">
    <div class="wrap hero__in">
      <div class="hero__copy">
        <p class="eyebrow">{SITE['region']}</p>
        <h1 class="hero__h1">Poof,<br>it's gone.</h1>
        <p class="hero__sub">
          Junk removal and full-property cleanouts for homes, estates, and
          commercial spaces. We do the carrying, the loading, and the sorting.
          You point at what's going.
        </p>
        <div class="hero__cta">
          <a class="btn btn--lg" href="estimate.html">Get an estimate</a>
          <a class="btn btn--ghost btn--lg" href="{SITE['phone_href']}">{SITE['contact_verb']} {SITE['phone']}</a>
        </div>
        <p class="hero__text-note">
          Faster still: text photos of the pile to that same number and we'll
          price it from there.
        </p>
      </div>

      <aside class="starter" aria-labelledby="starter-h">
        <h2 class="starter__h" id="starter-h">What are you getting rid of?</h2>
        <form class="starter__form" action="estimate.html" method="get">
          <label class="sr" for="startq">Describe what needs to go</label>
          <textarea id="startq" name="q" rows="3"
            placeholder="A sectional, two dressers, and about ten boxes in the garage"></textarea>
          <button class="btn btn--full" type="submit">Start my estimate</button>
        </form>
        <p class="starter__note">Takes about a minute. No account, no phone call required.</p>
      </aside>
    </div>
  </section>

  <section class="band">
    <div class="wrap band__in">
      <p>Upfront pricing</p>
      <p>Donation &amp; recycling first</p>
      <p>We do the heavy lifting</p>
      <p>Swept clean before we go</p>
    </div>
  </section>

  <section class="sec" id="services">
    <div class="wrap">
      <p class="eyebrow">What we clear</p>
      <h2 class="sec__h">One visit, whatever the scale.</h2>
      <div class="grid">
{services}
      </div>
      <p class="sec__foot">
        Also taken: mattresses, electronics, exercise equipment, hot tubs, yard
        waste, and renovation debris. If you're unsure whether something
        qualifies, just ask. The answer is usually yes.
      </p>
    </div>
  </section>

  <section class="sec sec--dark" id="how">
    <div class="wrap">
      <p class="eyebrow">How it works</p>
      <h2 class="sec__h">We make it disappear in three steps.</h2>
      <ol class="steps">
{steps}
      </ol>
    </div>
  </section>

  <section class="sec split" id="where">
    <div class="wrap split__in">
      <div>
        <p class="eyebrow">Where it goes</p>
        <h2 class="sec__h">The landfill is our last stop, not our first.</h2>
        <p class="lede">
          Most junk removal ends at a transfer station because that's the fast
          option. We sort every load first. Furniture and household goods go to
          local donation partners, metal and electronics go to recycling, and
          only what's genuinely spent goes to disposal.
        </p>
        <p class="muted">
          We'll tell you where your load ended up if you want to know.
        </p>
      </div>
      <ul class="routes">
        <li><span>01</span><div><h3>Donate</h3><p>Furniture, housewares, and working appliances in usable condition.</p></div></li>
        <li><span>02</span><div><h3>Recycle</h3><p>Metal, electronics, cardboard, and clean wood.</p></div></li>
        <li><span>03</span><div><h3>Dispose</h3><p>Everything left over, handled at a licensed facility.</p></div></li>
      </ul>
    </div>
  </section>

  <section class="sec" id="area">
    <div class="wrap">
      <p class="eyebrow">Service area</p>
      <h2 class="sec__h">Working across Northern Virginia.</h2>
      <ul class="areas">
{areas}
      </ul>
      <p class="sec__foot">
        Outside this list? Call or text us anyway. We travel for larger jobs.
      </p>
    </div>
  </section>

  <section class="cta">
    <div class="wrap cta__in">
      <h2>Let's make it disappear.</h2>
      <p>Call or text us a photo of the pile. We'll send a price back.</p>
      <div class="cta__btns">
        <a class="btn btn--dark btn--lg" href="estimate.html">Get an estimate</a>
        <a class="btn btn--ghost-dark btn--lg" href="{SITE['phone_href']}">{SITE['contact_verb']} {SITE['phone']}</a>
      </div>
    </div>
  </section>

</main>
""" + footer()


# ---------------------------------------------------------------------------
# PAGE: ESTIMATE
# ---------------------------------------------------------------------------

def estimate():
    return head(
        f"Get an estimate | {SITE['full_name']}",
        "Describe what needs to go and get a ballpark estimate for junk removal "
        "in Northern Virginia.",
        page_class="page-estimate",
    ) + nav("estimate") + f"""
<main id="main">
  <section class="est">
    <div class="wrap est__in">

      <div class="est__intro">
        <p class="eyebrow">Instant estimate</p>
        <h1 class="est__h1">Tell us what's going.</h1>
        <p class="lede">
          The more you tell us, the tighter the number. A photo of the pile
          does more than any list, so upload one if you can.
        </p>
        <p class="est__text-alt">
          Rather not fill in a form? {SITE['contact_verb']} us at
          <a href="{SITE['phone_href']}">{SITE['phone']}</a> and send your
          photos straight over. Same answer, fewer steps.
        </p>
        <div class="notice">
          <h2>This is an estimate, not a quote</h2>
          <p>
            It's a ballpark based on what you describe. The final price is
            confirmed on site, before any work starts and before you owe
            anything.
          </p>
        </div>
      </div>

      <form class="est__form" id="estimate-form" novalidate>

        <fieldset>
          <legend>What needs to go</legend>

          <div class="field">
            <label for="items">Describe the items</label>
            <textarea id="items" name="items" rows="4" required
              placeholder="A sectional sofa, two dressers, a mattress, and roughly ten boxes"></textarea>
            <p class="hint">Rough is fine. Piece counts and rough sizes help most.</p>
          </div>

          <div class="row">
            <div class="field">
              <label for="pieces">Roughly how many pieces</label>
              <select id="pieces" name="pieces">
                <option value="">Select</option>
                <option>1-3 items</option>
                <option>4-10 items</option>
                <option>11-25 items</option>
                <option>26+ items</option>
                <option>Full room or more</option>
                <option>Whole property</option>
              </select>
            </div>
            <div class="field">
              <label for="space">Where is it</label>
              <select id="space" name="space">
                <option value="">Select</option>
                <option>Garage</option>
                <option>Basement</option>
                <option>Attic</option>
                <option>Single room</option>
                <option>Whole house</option>
                <option>Yard or driveway</option>
                <option>Office or commercial space</option>
              </select>
            </div>
          </div>

          <div class="field">
            <label for="access">Anything that makes it harder to get out?</label>
            <select id="access" name="access">
              <option value="">Select</option>
              <option>Ground floor, easy access</option>
              <option>Stairs involved</option>
              <option>Long carry to the truck</option>
              <option>Needs disassembly</option>
              <option>Elevator building</option>
            </select>
          </div>

          <div class="field">
            <label for="photos">Photos <span class="opt">optional</span></label>
            <input type="file" id="photos" name="photos" accept="image/*" multiple>
            <p class="hint">A wide shot of the whole space beats close-ups.</p>
          </div>
        </fieldset>

        <fieldset>
          <legend>Where to send your estimate</legend>
          <p class="legend-note">
            We'll email it to you. The ZIP and timing help us price it accurately.
          </p>
          <div class="row">
            <div class="field">
              <label for="name">Name</label>
              <input type="text" id="name" name="name" autocomplete="name">
            </div>
            <div class="field">
              <label for="email">Email</label>
              <input type="email" id="email" name="email" autocomplete="email" required>
            </div>
          </div>
          <div class="row">
            <div class="field">
              <label for="zip">ZIP code</label>
              <input type="text" id="zip" name="zip" inputmode="numeric"
                     maxlength="5" placeholder="20151" autocomplete="postal-code">
              <p class="hint">Used to work out travel distance.</p>
            </div>
            <div class="field">
              <label for="when">When do you need it gone</label>
              <select id="when" name="when">
                <option value="">Select</option>
                <option>As soon as possible</option>
                <option>This week</option>
                <option>Next week</option>
                <option>Just planning ahead</option>
              </select>
            </div>
          </div>
        </fieldset>

        <button class="btn btn--lg btn--full" type="submit">Send me my estimate</button>
        <p class="est__fine">
          We use your email to send the estimate and follow up once. Nothing else.
        </p>

        <div class="status" id="form-status" role="status" aria-live="polite"></div>
      </form>

    </div>
  </section>
</main>
""" + footer()


# ---------------------------------------------------------------------------
# BUILD
# ---------------------------------------------------------------------------

PAGES = {
    "index.html": home,
    "estimate.html": estimate,
}


def build():
    for filename, fn in PAGES.items():
        with open(filename, "w", encoding="utf-8") as f:
            f.write(fn())
        print(f"wrote {filename}")
    print(f"cache-bust version: {VERSION}")


if __name__ == "__main__":
    build()
