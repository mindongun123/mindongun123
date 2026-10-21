import sys
out = sys.argv[1]
LOGO = '''<path d="M0,571 L266,571 L266,2672 L0,2672 Z M266,571 L761,1255 L761,1708 L266,1024 Z M761,0 L1027,0 L1027,2081 L761,2081 Z M483,158 L2253,158 L2253,424 L483,424 Z M1027,1262 L1524,571 L1524,1034 L1027,1716 Z M1524,571 L1790,571 L1790,2672 L1524,2672 Z M1987,424 L2253,424 L2253,1199 L1987,1235 Z M2253,1199 L1172,2685 L956,2528 L1987,1109 Z"/>'''
def star(cx, cy, r):
    import math
    pts = []
    for i in range(10):
        a = math.pi/2 + i*math.pi/5
        rr = r if i % 2 == 0 else r*0.45
        pts.append(f"{cx+rr*math.cos(a):.1f},{cy-rr*math.sin(a):.1f}")
    return " ".join(pts)
def make(dark):
    bg1, bg2 = ("#0B1220", "#10213A") if dark else ("#E0FBF7", "#E0F2FE")
    title = "#F8FAFC" if dark else "#0F172A"
    sub = "#94A3B8" if dark else "#334155"
    card = "#111C2E" if dark else "#FFFFFF"
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 320" width="1280" height="320" role="img" aria-label="MJ Game Studio — Casual &amp; Hyper-casual Mobile Games">
<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{bg1}"/><stop offset="1" stop-color="{bg2}"/></linearGradient>
  <linearGradient id="g" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#2DD4BF"/><stop offset=".55" stop-color="#0EA5E9"/><stop offset="1" stop-color="#2563EB"/></linearGradient>
  <linearGradient id="mj" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="0" y2="2686"><stop offset="0" stop-color="#5DE586"/><stop offset=".5" stop-color="#25A8B6"/><stop offset="1" stop-color="#0E88D3"/></linearGradient>
  <filter id="sh" x="-30%" y="-30%" width="160%" height="160%"><feDropShadow dx="0" dy="10" stdDeviation="12" flood-color="#0EA5E9" flood-opacity="{.35 if dark else .28}"/></filter>
  <clipPath id="clip"><rect width="1280" height="320" rx="28"/></clipPath>
</defs>
<style>
  .bob{{animation:bob 3.2s ease-in-out infinite;transform-box:fill-box;transform-origin:center}}
  .d1{{animation-delay:-.8s}} .d2{{animation-delay:-1.6s}} .d3{{animation-delay:-2.4s}}
  .spin{{animation:spin 9s linear infinite;transform-box:fill-box;transform-origin:center}}
  .pop{{animation:pop 2.4s cubic-bezier(.34,1.56,.64,1) infinite;transform-box:fill-box;transform-origin:center}}
  .logo{{animation:squash 2.4s ease-in-out infinite;transform-box:fill-box;transform-origin:50% 100%}}
  .in{{animation:in .9s cubic-bezier(.34,1.56,.64,1) both}}
  .in2{{animation-delay:.25s}} .in3{{animation-delay:.5s}}
  .t{{font-family:'Outfit','Segoe UI Rounded','Nunito','Segoe UI',system-ui,sans-serif;font-weight:800}}
  .s{{font-family:'Plus Jakarta Sans','Segoe UI',system-ui,sans-serif;font-weight:600}}
  @keyframes bob{{50%{{transform:translateY(-14px) rotate(6deg)}}}}
  @keyframes spin{{to{{transform:rotate(360deg)}}}}
  @keyframes pop{{0%,100%{{transform:scale(1)}}50%{{transform:scale(1.08)}}}}
  @keyframes squash{{0%,100%{{transform:translateY(0) scale(1,1)}}40%{{transform:translateY(-16px) scale(.96,1.04)}}55%{{transform:translateY(0) scale(1.06,.94)}}70%{{transform:scale(1,1)}}}}
  @keyframes in{{from{{opacity:0;transform:translateY(24px)}}to{{opacity:1;transform:none}}}}
  @media (prefers-reduced-motion:reduce){{*{{animation:none!important}}}}
</style>
<g clip-path="url(#clip)">
  <rect width="1280" height="320" fill="url(#bg)"/>
  <circle cx="1180" cy="-20" r="190" fill="url(#g)" opacity=".18"/>
  <circle cx="760" cy="350" r="130" fill="#D6B48C" opacity=".18"/>
  <!-- candy confetti -->
  <circle class="bob" cx="1010" cy="70" r="16" fill="#2DD4BF"/>
  <rect class="bob d1" x="1130" y="200" width="34" height="34" rx="10" fill="#0EA5E9"/>
  <polygon class="spin" points="{star(1215,110,22)}" fill="#FACC15"/>
  <circle class="bob d2" cx="930" cy="250" r="11" fill="#D6B48C"/>
  <rect class="bob d3" x="1050" y="130" width="22" height="22" rx="7" fill="#F472B6" opacity=".85"/>
  <polygon class="spin" points="{star(860,60,14)}" fill="#2DD4BF"/>
  <circle class="bob d1" cx="1240" cy="270" r="9" fill="#2563EB"/>
  <circle class="bob d3" cx="560" cy="40" r="8" fill="#F472B6" opacity=".7"/>
  <!-- logo card -->
  <g class="in">
    <g class="logo">
      <rect x="70" y="70" width="180" height="180" rx="44" fill="{card}" filter="url(#sh)"/>
      <g transform="translate(110 102) scale(.0447)" fill="url(#mj)">{LOGO}</g>
    </g>
    <ellipse cx="160" cy="282" rx="62" ry="8" fill="#0EA5E9" opacity=".15"/>
  </g>
  <!-- text -->
  <text class="t in in2" x="300" y="148" font-size="72" fill="{title}">MJ Game <tspan fill="url(#g)">Studio</tspan></text>
  <text class="s in in3" x="303" y="196" font-size="26" fill="{sub}">Casual &amp; Hyper-casual Mobile Games · Unity + C#</text>
  <g class="in in3">
    <g class="pop">
      <rect x="303" y="222" width="236" height="50" rx="25" fill="url(#g)"/>
      <text class="t" x="421" y="255" font-size="20" fill="#fff" text-anchor="middle" letter-spacing="2">▶ TAP TO PLAY</text>
    </g>
    <text class="s" x="560" y="254" font-size="20" fill="{sub}">Easy to play, hard to put down 🎮</text>
  </g>
</g>
</svg>
'''
open(out + "/banner-light.svg", "w", encoding="utf-8").write(make(False))
open(out + "/banner-dark.svg", "w", encoding="utf-8").write(make(True))
