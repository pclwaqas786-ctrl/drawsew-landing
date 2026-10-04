"""DrawSew — Embroidery Digitizing. Marketing landing page (Streamlit)."""
import base64
from pathlib import Path

import streamlit as st

# ---------------------------------------------------------------- constants
WA_LINK = (
    "https://wa.me/923323167915"
    "?text=Hi%20DrawSew!%20I%20want%20a%20trial%20design%20for%20my%20logo."
)
IG_URL = "https://instagram.com/drawsew1"
EMAIL = "drawsew1@gmail.com"
ASSETS = Path(__file__).parent / "assets"


def img_b64(name: str) -> str:
    return base64.b64encode((ASSETS / name).read_bytes()).decode()


st.set_page_config(
    page_title="DrawSew — Embroidery Digitizing | Your Logo, Perfectly Stitched",
    page_icon="🧵",
    layout="wide",
)

# ------------------------------------------------------------------- styles
st.markdown(
    """
<style>
:root { --gold: #d4af37; --gold-lt: #f0d878;
        --ink: #f2f2f2; --muted: #b9c4bd; --card: #16211c; }
html, body, [data-testid="stAppViewContainer"] { background: #101514; }
.block-container { max-width: 1100px; padding-top: 0; }
.ds-nav { position: sticky; top: 0; z-index: 999;
  background: rgba(16,21,20,.96); border-bottom: 1px solid #24352c;
  display: flex; align-items: center; justify-content: space-between;
  padding: 12px 20px; margin: 0 -20px; }
.ds-logo { font-weight: 900; letter-spacing: 3px; font-size: 1.25rem; color: var(--gold); }
.ds-links a { color: var(--muted); text-decoration: none; margin: 0 10px; font-size: .95rem; }
.ds-links a:hover { color: var(--gold-lt); }
.ds-btn { background: linear-gradient(135deg, var(--gold), #b8912a); color: #141414 !important;
  font-weight: 800; padding: 10px 22px; border-radius: 10px; text-decoration: none;
  display: inline-block; }
.ds-btn:hover { filter: brightness(1.08); }
.ds-btn-ghost { background: transparent; color: var(--gold-lt) !important;
  border: 1px solid var(--gold); font-weight: 700; padding: 10px 22px;
  border-radius: 10px; text-decoration: none; display: inline-block; }
.ds-hero { position: relative; border-radius: 18px; overflow: hidden;
  margin: 18px 0 8px; border: 1px solid #24352c; min-height: 420px;
  display: flex; align-items: center; }
.ds-hero-txt { position: relative; z-index: 2; padding: 8%; max-width: 640px; }
.ds-hero h1 { font-size: clamp(2rem, 5.5vw, 3.6rem); line-height: 1.05;
  color: #fff; margin: 0 0 12px; letter-spacing: 1px; }
.ds-hero h1 .gold { color: var(--gold-lt); }
.ds-hero p { color: var(--muted); font-size: 1.08rem; }
.ds-chips { margin-top: 14px; display: flex; gap: 10px; flex-wrap: wrap; }
.ds-chip { background: rgba(14,92,63,.55); border: 1px solid var(--gold);
  color: var(--gold-lt); padding: 7px 14px; border-radius: 999px;
  font-size: .88rem; font-weight: 600; }
.ds-cta-row { margin-top: 18px; display: flex; gap: 12px; flex-wrap: wrap; }
.ds-sec { padding: 44px 4px 8px; }
.ds-kicker { color: var(--gold); font-weight: 800; letter-spacing: 2.5px; font-size: .82rem; }
.ds-h2 { color: #fff; font-size: clamp(1.5rem, 3.4vw, 2.2rem); margin: 6px 0 18px; }
.ds-card { background: var(--card); border: 1px solid #24352c; border-radius: 14px;
  padding: 20px; }
.ds-card h4 { color: var(--gold-lt); margin: 0 0 8px; font-size: 1.05rem; }
.ds-card p { color: var(--muted); font-size: .94rem; margin: 0; }
.ds-fmt { display: inline-block; background: #0e241b; border: 1px solid #2c4a3a;
  color: var(--gold-lt); font-weight: 800; letter-spacing: 1px;
  padding: 10px 18px; border-radius: 10px; margin: 6px 8px 6px 0; }
.ds-step { display: flex; gap: 14px; align-items: flex-start; margin: 16px 0; }
.ds-step-n { width: 44px; height: 44px; border-radius: 50%; flex: none;
  background: linear-gradient(135deg, var(--gold), #b8912a); color: #141414;
  font-weight: 900; display: flex; align-items: center; justify-content: center;
  font-size: 1.15rem; }
.ds-step h4 { color: #fff; margin: 2px 0 4px; }
.ds-step p { color: var(--muted); margin: 0; font-size: .95rem; }
.ds-li { color: var(--muted); font-size: 1.02rem; margin: 10px 0; }
.ds-li b { color: #fff; }
.ds-li::before { content: "\\2714  "; color: var(--gold); font-weight: 900; }
.ds-contact-card { background: var(--card); border: 1px solid var(--gold);
  border-radius: 16px; padding: 30px; text-align: center; }
.ds-contact-card h3 { color: #fff; margin-top: 0; }
.ds-contact-card p { color: var(--muted); }
.ds-contact-card a { color: var(--gold-lt); }
.ds-footer { text-align: center; color: #7d8a82; font-size: .88rem;
  padding: 34px 0 26px; border-top: 1px solid #24352c; margin-top: 40px; }
.ds-footer b { color: var(--gold); }
.ds-cap { color: #7d8a82; font-size: .9rem; text-align: center; margin-top: 8px; }
@media (max-width: 640px){ .ds-links { display: none; } }
</style>
""",
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------- nav
st.markdown(
    f"""
<div class="ds-nav">
  <div class="ds-logo"><img src="data:image/png;base64,{img_b64('dp.png')}" style="height:38px;width:38px;border-radius:50%;vertical-align:middle;margin-right:8px;" />DRAWSEW</div>
  <div class="ds-links">
    <a href="#services">Services</a><a href="#portfolio">Portfolio</a>
    <a href="#process">Process</a><a href="#contact">Contact</a>
  </div>
  <a class="ds-btn" href="{WA_LINK}" target="_blank">Get Trial Design</a>
</div>
""",
    unsafe_allow_html=True,
)

# --------------------------------------------------------------------- hero
st.markdown(
    f"""
<div class="ds-hero" style="background:
  linear-gradient(90deg, rgba(8,20,15,.94) 25%, rgba(8,20,15,.35)),
  url('data:image/png;base64,{img_b64('hero-bg.png')}');
  background-size: cover; background-position: center;">
  <div class="ds-hero-txt">
    <h1>YOUR LOGO,<br><span class="gold">PERFECTLY STITCHED.</span></h1>
    <p>Professional embroidery digitizing — 800+ logos delivered in 6&ndash;12 hours,
       in every machine format you need.</p>
    <div class="ds-cta-row">
      <a class="ds-btn" href="{WA_LINK}" target="_blank">Get Trial Design</a>
      <a class="ds-btn-ghost" href="#portfolio">See Portfolio</a>
    </div>
    <div class="ds-chips">
      <span class="ds-chip">🧵 800+ logos digitized</span>
      <span class="ds-chip">⚡ 6&ndash;12 hr turnaround</span>
      <span class="ds-chip">💾 All machine formats</span>
    </div>
  </div>
</div>
""",
    unsafe_allow_html=True,
)

# --------------------------------------------------------------- wide banner
st.image(str(ASSETS / "fb-cover.png"), use_column_width=True)

# ----------------------------------------------------------------- services
st.markdown(
    '<div class="ds-sec" id="services">'
    '<div class="ds-kicker">OUR SERVICES</div>'
    '<div class="ds-h2">Digitizing, done right.</div></div>',
    unsafe_allow_html=True,
)
services = [
    ("🧵 Logo Digitizing", "Your logo converted to clean, machine-ready stitch files with sharp edges."),
    ("🧢 3D Puff Digitizing", "Raised foam-effect lettering and designs that pop off caps and jackets."),
    ("🛡️ Embroidered Patches", "Crisp patch designs with perfect borders, ready for any patch machine."),
    ("🧢 Cap Digitizing", "Centered, pucker-proof designs tuned for structured caps and hats."),
    ("🧥 Jacket Back Digitizing", "Large-format back designs with smooth fills and clean underlay."),
    ("✏️ Vector Art", "Clean vector redraws of your artwork — the perfect base for digitizing."),
]
cols = st.columns(3)
for i, (title, desc) in enumerate(services):
    with cols[i % 3]:
        st.markdown(
            f'<div class="ds-card"><h4>{title}</h4><p>{desc}</p></div>',
            unsafe_allow_html=True,
        )

# ---------------------------------------------------------------- portfolio
st.markdown(
    '<div class="ds-sec" id="portfolio">'
    '<div class="ds-kicker">PORTFOLIO</div>'
    '<div class="ds-h2">Real work, real stitches.</div></div>',
    unsafe_allow_html=True,
)
st.image(str(ASSETS / "fb-portfolio-post.png"), use_column_width=True)
st.markdown(
    '<div class="ds-cap">A sample of recent DrawSew digitizing work — patches, mascots &amp; detailed art.</div>',
    unsafe_allow_html=True,
)
c1, c2 = st.columns(2)
with c1:
    st.image(str(ASSETS / "slide2.png"), use_column_width=True)
with c2:
    st.image(str(ASSETS / "slide5.png"), use_column_width=True)

# ------------------------------------------------------------------ formats
st.markdown(
    '<div class="ds-sec">'
    '<div class="ds-kicker">FILE FORMATS</div>'
    '<div class="ds-h2">Every machine, covered.</div>',
    unsafe_allow_html=True,
)
fmts = "".join(f'<span class="ds-fmt">.{f}</span>' for f in
               ["DST", "PES", "EMB", "EXP", "JEF", "VP3", "XXX"])
st.markdown(
    f"{fmts}<p style='color:var(--muted);margin-top:10px;'>"
    "All formats included with every order — no extra charge.</p></div>",
    unsafe_allow_html=True,
)

# ------------------------------------------------------------------ process
st.markdown(
    '<div class="ds-sec" id="process">'
    '<div class="ds-kicker">HOW IT WORKS</div>'
    '<div class="ds-h2">From artwork to stitch file in 4 steps.</div></div>',
    unsafe_allow_html=True,
)
p1, p2 = st.columns([1.15, 1])
with p1:
    steps = [
        ("Send your artwork", "Upload your logo or design on WhatsApp or email — any clear image works."),
        ("Get your trial", "New clients get a trial design so you can see our quality first."),
        ("We digitize", "Vicky converts your art to clean stitch files, tuned for your machine."),
        ("Fast delivery", "Receive DST, PES and all formats in 6–12 hours, revisions friendly."),
    ]
    for n, (t, d) in enumerate(steps, 1):
        st.markdown(
            f'<div class="ds-step"><div class="ds-step-n">{n}</div>'
            f"<div><h4>{t}</h4><p>{d}</p></div></div>",
            unsafe_allow_html=True,
        )
with p2:
    st.image(str(ASSETS / "slide7.png"), use_column_width=True)

# ---------------------------------------------------------------- why us
st.markdown(
    '<div class="ds-sec">'
    '<div class="ds-kicker">WHY DRAWSEW</div>'
    '<div class="ds-h2">Stitch quality you can trust.</div>'
    '<div class="ds-li"><b>800+ logos digitized</b> — real experience across caps, jackets, patches &amp; more.</div>'
    '<div class="ds-li"><b>6–12 hour turnaround</b> — fast without cutting corners.</div>'
    '<div class="ds-li"><b>Clean stitch quality</b> — sharp edges, smooth fills, correct density &amp; underlay.</div>'
    '<div class="ds-li"><b>Friendly revisions</b> — we adjust until it sews the way you want.</div>'
    '<div class="ds-li"><b>All machine formats</b> — DST, PES, EMB, EXP, JEF, VP3, XXX included.</div>'
    "</div>",
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------- contact
st.markdown(
    f"""
<div class="ds-sec" id="contact">
  <div class="ds-kicker">GET IN TOUCH</div>
  <div class="ds-h2">Let's stitch your vision.</div>
  <div class="ds-contact-card">
    <h3>Trial design for new clients 🧵</h3>
    <p>Send your logo today — see the DrawSew quality before you commit.</p>
    <p><a class="ds-btn" href="{WA_LINK}" target="_blank">💬 WhatsApp: +92 332 3167915</a></p>
    <p>📸 Instagram: <a href="{IG_URL}" target="_blank">@drawsew1</a>
       &nbsp;·&nbsp; ✉️ <a href="mailto:{EMAIL}">{EMAIL}</a></p>
  </div>
</div>
""",
    unsafe_allow_html=True,
)

# ------------------------------------------------------------------ footer
st.markdown(
    '<div class="ds-footer">© 2026 <b>DrawSew</b> (Elite Draw Sew)<br>'
    "Vicky — Digitizing Specialist 🧵</div>",
    unsafe_allow_html=True,
)
