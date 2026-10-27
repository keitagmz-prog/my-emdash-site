import sys,html
from playwright.sync_api import sync_playwright
# usage: rn.py OUT CATEGORY_SLUG "EYEBROW" "TITLE" "SUBTITLE" LAYOUT(a|b|c) [NUMBER]
o,cat,ey,ti,su,lay=sys.argv[1:7];num=sys.argv[7] if len(sys.argv)>7 else "";E=html.escape
P={"lighting":("#f7efdc","#c98a1e","#3a2a12","lamp"),"walls":("#eef1ea","#5d7a5c","#1f3b2d","frame"),
"small-space-storage":("#f5ece2","#b0663f","#3b2416","shelf"),"room-ideas":("#eaf0f2","#4f6f82","#1d3140","sofa")}
bg,ac,tx,ic=P.get(cat,("#f4efe7","#c8794a","#1f3b2d","house"))
def icon(fg,bgc):
 d={"lamp":f'<path d="M20 10h24l8 22H12z" fill="{fg}"/><rect x="30" y="32" width="4" height="18" fill="{fg}"/><rect x="20" y="50" width="24" height="5" rx="2.5" fill="{fg}"/>',
 "frame":f'<rect x="10" y="12" width="44" height="40" rx="3" fill="none" stroke="{fg}" stroke-width="5"/><path d="M16 46l11-14 8 9 6-6 9 11z" fill="{fg}"/><circle cx="42" cy="23" r="4" fill="{fg}"/>',
 "shelf":f'<rect x="12" y="10" width="40" height="46" rx="3" fill="none" stroke="{fg}" stroke-width="5"/><path d="M12 26h40M12 41h40" stroke="{fg}" stroke-width="4"/><rect x="18" y="15" width="7" height="11" fill="{fg}"/><rect x="27" y="17" width="6" height="9" fill="{fg}"/><rect x="36" y="31" width="11" height="10" rx="2" fill="{fg}"/><rect x="18" y="45" width="12" height="11" rx="2" fill="{fg}"/>',
 "sofa":f'<rect x="14" y="20" width="36" height="16" rx="5" fill="{fg}"/><rect x="8" y="28" width="48" height="16" rx="6" fill="{fg}"/><rect x="12" y="44" width="5" height="8" fill="{fg}"/><rect x="47" y="44" width="5" height="8" fill="{fg}"/>',
 "house":f'<path d="M32 12 10 31h6v20h32V31h6z" fill="{fg}"/>'}[ic]
 return d
def svg(fg,size,bgc=None,rx=14):
 r=f'<rect width="64" height="64" rx="{rx}" fill="{bgc}"/>' if bgc else ""
 return f'<svg viewBox="0 0 64 64" width="{size}" height="{size}">{r}<g transform="translate(6 6) scale(.8125)">{icon(fg,bgc)}</g></svg>'
mono="font-family:'DejaVu Sans Mono';letter-spacing:5px;text-transform:uppercase"
serif="font-family:Lora,serif;font-weight:700"
brand=f'<span style="{serif}">Rent &amp; Nest</span>'
if lay=="b":
 body=f'''<body style="margin:0;width:1200px;height:675px;overflow:hidden;background:{ac};color:#fff;font-family:Inter;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;box-sizing:border-box;padding:0 120px">
<div style="opacity:.95">{svg("#fff",96)}</div>
<div style="{mono};font-size:22px;margin-top:18px;opacity:.85">{E(ey)}</div>
<div style="{serif};font-size:68px;line-height:1.1;margin-top:22px">{E(ti)}</div>
<div style="font-size:28px;margin-top:26px;opacity:.9">{E(su)}</div>
<div style="position:absolute;bottom:34px;font-size:24px">{brand}</div></body>'''
elif lay=="c":
 left=f'<div style="{serif};font-size:230px;line-height:1;color:#fff">{E(num)}</div>' if num else svg("#fff",230)
 body=f'''<body style="margin:0;width:1200px;height:675px;overflow:hidden;background:{bg};color:{tx};font-family:Inter;display:flex">
<div style="width:430px;background:{ac};display:flex;align-items:center;justify-content:center">{left}</div>
<div style="flex:1;padding:80px 70px;display:flex;flex-direction:column">
<div style="{mono};font-size:22px;color:{ac}">{E(ey)}</div>
<div style="{serif};font-size:64px;line-height:1.1;margin-top:26px">{E(ti)}</div>
<div style="width:90px;height:7px;background:{ac};margin:30px 0 22px;border-radius:4px"></div>
<div style="font-size:28px;line-height:1.35;color:#4a4540">{E(su)}</div>
<div style="flex:1"></div><div style="font-size:24px">{brand}</div></div></body>'''
else:
 body=f'''<body style="margin:0;width:1200px;height:675px;overflow:hidden;background:{bg};font-family:Inter;color:{tx};position:relative">
<div style="position:absolute;right:90px;top:200px">{svg("#fffaf3",260,ac)}</div>
<div style="position:absolute;left:90px;top:70px;width:720px">
<div style="{mono};font-size:24px;color:{ac}">{E(ey)}</div>
<div style="{serif};font-size:72px;line-height:1.08;letter-spacing:-1px;margin-top:30px">{E(ti)}</div>
<div style="width:110px;height:8px;background:{ac};margin:32px 0 24px;border-radius:4px"></div>
<div style="font-size:30px;line-height:1.35;color:#4a4540;font-weight:500">{E(su)}</div></div>
<div style="position:absolute;left:90px;bottom:40px;font-size:28px">{brand}</div></body>'''
with sync_playwright() as p:
 b=p.chromium.launch();g=b.new_page(viewport={"width":1200,"height":675});g.set_content(body);g.wait_for_timeout(300);g.screenshot(path=o,type="jpeg",quality=88);b.close()
