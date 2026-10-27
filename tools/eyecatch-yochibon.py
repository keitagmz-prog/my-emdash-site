import sys,html
from playwright.sync_api import sync_playwright
# usage: yb.py OUT CATEGORY_SLUG "EYEBROW" "TITLE(| = line break)" "SUBTITLE" ICON LAYOUT(a|b|c) [BIG e.g. 6選]
o,cat,ey,ti,su,ic,lay=sys.argv[1:8];big=sys.argv[8] if len(sys.argv)>8 else "";E=html.escape;W="#fff"
P={"rakuten-affiliate":("#e2542b","#fff1ea"),"us-affiliate":("#2f8a7a","#e9f5f1"),"development":("#3b5b8c","#edf1f8")}
A,BG=P.get(cat,("#f28a2e","#fbf5ea"));R="#e2542b"
I={"kitchen":'<rect x="70" y="150" width="120" height="70" rx="14" fill="{f}"/><rect x="185" y="172" width="55" height="12" rx="6" fill="{f}"/><rect x="60" y="138" width="140" height="16" rx="8" fill="{f}"/><path d="M110 120c0-18 14-18 14-36M135 120c0-18 14-18 14-36" stroke="{f}" stroke-width="8" fill="none" stroke-linecap="round"/>',
"storage":'<rect x="70" y="175" width="160" height="55" rx="10" fill="{f}"/><rect x="85" y="115" width="130" height="55" rx="10" fill="{f}"/><rect x="100" y="60" width="100" height="50" rx="10" fill="{f}"/><rect x="130" y="196" width="40" height="10" rx="5" fill="{b}"/><rect x="132" y="136" width="36" height="10" rx="5" fill="{b}"/><rect x="134" y="80" width="32" height="10" rx="5" fill="{b}"/>',
"ai":'<rect x="45" y="95" width="95" height="65" rx="10" fill="{f}"/><text x="92" y="140" font-size="30" font-weight="900" text-anchor="middle" fill="{b}" font-family="Noto Sans CJK JP">US</text><rect x="160" y="140" width="95" height="65" rx="10" fill="{f}"/><circle cx="207" cy="172" r="18" fill="#e2542b"/><path d="M115 200q25 30 55 18M185 100q-25-30-55-18" stroke="{f}" stroke-width="8" fill="none" stroke-linecap="round"/>',
"bag":'<path d="M80 115h140l-12 120H92z" fill="{f}"/><path d="M115 115v-20a35 35 0 0 1 70 0v20" stroke="{f}" stroke-width="10" fill="none"/><circle cx="150" cy="175" r="16" fill="{b}"/>',
"chart":'<rect x="70" y="170" width="38" height="60" rx="6" fill="{f}"/><rect x="131" y="130" width="38" height="100" rx="6" fill="{f}"/><rect x="192" y="85" width="38" height="145" rx="6" fill="{f}"/><path d="M70 140 130 100 170 115 230 60" stroke="{f}" stroke-width="9" fill="none" stroke-linecap="round" stroke-linejoin="round" opacity=".6"/>',
"code":'<rect x="55" y="80" width="190" height="140" rx="14" fill="{f}"/><path d="M110 125 85 150l25 25M190 125l25 25-25 25M162 115l-24 70" stroke="{b}" stroke-width="10" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'}
def ico(f,b,size,circle=None):
 c=f'<circle cx="150" cy="150" r="150" fill="{circle}"/>' if circle else ""
 return f'<svg viewBox="0 0 300 300" width="{size}" height="{size}">{c}{I.get(ic,I["bag"]).format(f=f,b=b)}</svg>'
t="<br>".join(E(x) for x in ti.split("|"));J="font-family:'Noto Sans CJK JP'"
stripe=f'<div style="position:absolute;top:0;left:0;right:0;height:22px;background:repeating-linear-gradient(90deg,{A} 0 46px,#fff 46px 92px)"></div>'
pill=lambda bg,fg:f'<div style="display:inline-block;background:{bg};color:{fg};font-weight:700;font-size:26px;padding:8px 22px;border-radius:999px;letter-spacing:2px">{E(ey)}</div>'
if lay=="b":
 h=f'''<body style="margin:0;width:1200px;height:675px;overflow:hidden;{J};background:{A};color:#fff;position:relative;text-align:center">
<div style="position:absolute;top:0;left:0;right:0;height:22px;background:repeating-linear-gradient(90deg,#fff 0 46px,transparent 46px 92px);opacity:.9"></div>
<div style="padding-top:70px">{ico("#fff",A,120)}</div>
<div style="margin-top:14px">{pill("#fff",A)}</div>
<div style="font-size:72px;font-weight:900;line-height:1.22;margin-top:24px">{t}</div>
<div style="font-size:28px;margin-top:22px;opacity:.92">{E(su)}</div>
<div style="position:absolute;left:0;right:0;bottom:36px;font-size:24px;font-weight:900">よちぼん市場</div></body>'''
elif lay=="c":
 left=f'<div style="font-size:150px;font-weight:900;color:#fff;line-height:1">{E(big)}</div>' if big else ico("#fff",A,300)
 h=f'''<body style="margin:0;width:1200px;height:675px;overflow:hidden;{J};background:{BG};color:#2b2118;display:flex;position:relative">
<div style="width:440px;background:{A};display:flex;align-items:center;justify-content:center;position:relative">{left}
<div style="position:absolute;top:0;left:0;right:0;height:22px;background:repeating-linear-gradient(90deg,#fff 0 46px,transparent 46px 92px);opacity:.9"></div></div>
<div style="flex:1;padding:80px 64px;display:flex;flex-direction:column">
<div>{pill(A,"#fff")}</div>
<div style="font-size:66px;font-weight:900;line-height:1.25;margin-top:28px">{t}</div>
<div style="width:90px;height:8px;background:{A};border-radius:4px;margin:30px 0 20px"></div>
<div style="font-size:27px;font-weight:500;color:#5c4e40">{E(su)}</div>
<div style="flex:1"></div><div style="font-size:24px;font-weight:900">よちぼん市場</div></div></body>'''
else:
 h=f'''<body style="margin:0;width:1200px;height:675px;overflow:hidden;{J};background:{BG} radial-gradient(rgba(0,0,0,.08) 1.5px,transparent 1.6px) 0 0/22px 22px;position:relative;color:#2b2118">{stripe}
<div style="position:absolute;right:-20px;top:120px">{ico("#fff",A,330,A)}</div>
<div style="position:absolute;left:80px;top:90px;width:760px">{pill(A,"#fff")}
<div style="font-size:78px;font-weight:900;line-height:1.22;margin-top:30px">{t}</div>
<div style="width:90px;height:8px;background:{A};border-radius:4px;margin:34px 0 22px"></div>
<div style="font-size:28px;font-weight:500;color:#5c4e40">{E(su)}</div></div>
<div style="position:absolute;left:80px;bottom:44px;font-size:24px;font-weight:900">よちぼん市場</div></body>'''
with sync_playwright() as p:
 b=p.chromium.launch();g=b.new_page(viewport={"width":1200,"height":675});g.set_content(h);g.wait_for_timeout(300);g.screenshot(path=o,type="jpeg",quality=88);b.close()
