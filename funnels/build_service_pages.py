"""Builds the Meta-ad landing pages for Fiverr services (logo, web).
Run: python3 funnels/build_service_pages.py  -> writes public/<slug>/index.html
Each page: Meta pixel 2153021785300175, headline A/B variants (?v=), events tagged with
service, round, variant, creative. CTA goes to the Fiverr gig and fires Lead + InitiateCheckout.
"""
import json, pathlib

PIXEL = "2153021785300175"
BASE = "https://avielcarlos.github.io/ascension-site"

PAGES = {
  "logo": dict(
    title="Logo & brand identity by Aviel",
    desc="A logo and a full brand kit that feels like you. From US$25 on Fiverr.",
    order="https://www.fiverr.com/mrandromeda/design-your-logo-and-full-brand-identity-kit",
    price="US$25", palette=dict(bg="#f4ede2", bg2="#ebe2d3", panel="#fbf7f0", ink="#1b1712", muted="#6b5f50", accent="#7a5a22", accent_ink="#fffaf0", line="rgba(27,23,18,.12)"),
    kicker="Logo & brand identity",
    variants=[("a","A brand that feels like you <em>before anyone reads a word.</em>"),
              ("b","Look like the business <em>you're becoming.</em>"),
              ("c","Your logo, colours and fonts <em>in one kit.</em>")],
    lede="I design your logo and the full kit around it ~ colours, type, social icons and print files ~ so everything you put out looks like one brand.",
    hero="ebv.jpg", hero_alt="Event Beautification Victoria logo and brand system",
    proof_title="Real brands I've built",
    proof=[("ebv.jpg","Event Beautification Victoria","Event décor in Victoria, BC. Logo, mascot, palette, type and web kit."),
           ("aventi.jpg","Aventi","A local events app. Stark mark, dark palette and type."),
           ("greenisland.jpg","Green Island","A local farm in Saanich. Sprout mark, green palette and type.")],
    steps=[("Tell me about your business","Who you serve, the feeling you want, and anything you already love or hate."),
           ("I design concepts","Two logo directions, then I refine the one that feels right."),
           ("You get the whole kit","Final logo files plus colours, fonts, social icons and print files.")],
    gets=["2 logo concepts, then your final logo","PNG, SVG, vector and print files","Brand colours and fonts, written down","Social media kit and stationery designs"],
    faqs=[("How much is it?","Logos start at US$25 on Fiverr. Bigger brand kits are in the higher packages there."),
          ("Why Fiverr?","Your payment is protected there, and you can message me before you order. I answer every message myself."),
          ("How long does it take?","About 3 days for the logo package. I'll tell you up front if your project needs longer."),
          ("Do I own it?","Yes. You get your final logo plus the source and vector files.")],
    cta="Start your brand", close_h="Ready to look like yourself?", close_sub="Tell me about your business. I'll take care of the rest."),
  "web": dict(
    title="Websites & web apps by Aviel",
    desc="A fast, mobile-ready website you can actually run. From US$80 on Fiverr.",
    order="https://www.fiverr.com/mrandromeda/build-and-manage-your-website-or-web-app-fast-and-mobile-ready",
    price="US$80", palette=dict(bg="#0c1412", bg2="#101b18", panel="#13201c", ink="#eef6f2", muted="#9fb5ad", accent="#3ddc97", accent_ink="#06261a", line="rgba(220,255,240,.12)"),
    kicker="Websites & web apps",
    variants=[("a","A website that loads fast, <em>looks right on a phone</em>, and gets you booked."),
              ("b","Stop losing customers <em>to a slow website.</em>"),
              ("c","Your business, <em>online in days.</em>")],
    lede="I design, build and look after websites and web apps ~ landing pages that turn visitors into bookings, all the way to full apps.",
    hero="aventi.jpg", hero_alt="Aventi events app built by Aviel",
    proof_title="Real sites I've built",
    proof=[("ebv-desktop.jpg","Event Beautification Victoria","Booking site with a free mock-up quote flow, live in Victoria, BC."),
           ("aventi.jpg","Aventi","A local events app. Mobile first, installable, in beta."),
           ("ebv-mobile.jpg","Built for phones first","Most of your customers will see your site on a phone. I design for that first.")],
    steps=[("Tell me what you need","Your business, your customers, and what the site should get them to do."),
           ("I build it fast","A working, mobile-ready site with forms, payments and speed tuned in."),
           ("Launch and grow","I set up hosting and can keep improving it with you over time.")],
    gets=["A responsive page that works on every phone","Contact, signup or booking form","Payments and email list hooked up","Speed tuning and hosting setup"],
    faqs=[("How much is it?","A landing page starts at US$80 on Fiverr. Multi-page sites and web apps are in the higher packages there."),
          ("Why Fiverr?","Your payment is protected there, and you can message me before you order. I answer every message myself."),
          ("How long does it take?","About 4 days for a landing page. Bigger builds get a clear timeline before you order."),
          ("Can you manage it after?","Yes. I can keep it updated and keep improving it as your business grows.")],
    cta="Start your website", close_h="Ready for a site that works for you?", close_sub="Tell me what you need. I'll take care of the rest."),
}

TPL = open(pathlib.Path(__file__).with_name("service_page.html")).read()

def render(slug, c):
    p = c["palette"]
    proof = "\n".join(f'<figure class="pf"><img src="{img}" alt="{t}" loading="lazy"><figcaption><b>{t}</b><span>{d}</span></figcaption></figure>' for img,t,d in c["proof"])
    steps = "\n".join(f'<div class="step"><h3>{h}</h3><p>{d}</p></div>' for h,d in c["steps"])
    gets = "\n".join(f"<li>{g}</li>" for g in c["gets"])
    faqs = "\n".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q,a in c["faqs"])
    funnel = dict(pixel=PIXEL, service=slug, order=c["order"], round="r1-headline",
                  variants=[dict(key=k, weight=1, headline=h) for k,h in c["variants"]])
    out = TPL
    for k,v in dict(TITLE=c["title"], DESC=c["desc"], OG=f"{BASE}/{slug}/og.jpg", FUNNEL=json.dumps(funnel, ensure_ascii=False),
                    KICKER=c["kicker"], H1=c["variants"][0][1], LEDE=c["lede"], HERO=c["hero"], HERO_ALT=c["hero_alt"],
                    PRICE=c["price"], CTA=c["cta"], PROOF_TITLE=c["proof_title"], PROOF=proof, STEPS=steps, GETS=gets,
                    FAQS=faqs, CLOSE_H=c["close_h"], CLOSE_SUB=c["close_sub"], **{f"C_{a.upper()}":b for a,b in p.items()}).items():
        out = out.replace("{{"+k+"}}", v)
    assert "{{" not in out, slug
    path = pathlib.Path(__file__).parent.parent / "public" / slug / "index.html"
    path.write_text(out)
    print("wrote", path)

for s,c in PAGES.items(): render(s,c)
