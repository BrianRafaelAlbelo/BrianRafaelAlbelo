from pathlib import Path
import json, urllib.request, os, html
ROOT = Path(__file__).resolve().parents[1]
USERNAME='BrianRafaelAlbelo'
def fetch():
    headers={'Accept':'application/vnd.github+json','User-Agent':'cyberpunk-profile-readme'}
    if os.getenv('GH_PROFILE_TOKEN'):
        headers['Authorization']='Bearer '+os.getenv('GH_PROFILE_TOKEN')
    try:
        req=urllib.request.Request('https://api.github.com/users/'+USERNAME,headers=headers)
        with urllib.request.urlopen(req,timeout=10) as r: return json.load(r)
    except Exception as ex:
        print('GitHub API unavailable:',ex)
        return {}

def esc(value): return html.escape(str(value),quote=True)
def make():
    data=fetch()
    stats=[('REPOS',str(data.get('public_repos','--'))),('FOLLOWERS',str(data.get('followers','--'))),('FOLLOWING',str(data.get('following','--')))]
    scan_lines=['                  .-====-.                 ',
'               .==++++++++==.             ',
'             .=++==------==++=.           ',
'            =++=--::::::::--=++=          ',
'           =++--::........::--++=         ',
'          =++-::..  ____  ..::-++=        ',
'          ++-::..  / __ \\  ..::-++       ',
'         =++-:..  | /  \\ |  ..:-++=      ',
'         ++-:...  | |  | | ...:-++       ',
'         ++-:...  | |__| | ...:-++       ',
'         ++-::..   \\____/  ..::-++       ',
'         =++-::...  |  |  ...::-++=      ',
'          =++--::.. /____\\ ..::--++=      ',
'           =++=--::/|    |\\::--=++=      ',
'            =+++===/|____|\\===+++=       ',
'          .==+++====|____|====+++==.      ',
'        .==+++++++==|____|==+++++++==.    ',
'      .==++++++==--======--==++++++==.   ',
'     .==++++==--::::::::::::--==++++==.  ']
    lines='\n'.join(f'<text x="90" y="{243+i*16}" class="ascii" xml:space="preserve">{esc(line)}</text>' for i,line in enumerate(scan_lines))
    meta='\n'.join(f'<text x="754" y="{332+i*60}" class="key">{k}</text><text x="1060" y="{332+i*60}" class="value">{esc(v)}</text>' for i,(k,v) in enumerate(stats))
    svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="740" viewBox="0 0 1280 740" role="img" aria-labelledby="title desc">
<title id="title">Brian Albelo — Cyberpunk Profile Scan</title><desc id="desc">Interfaz cyberpunk original con retrato ASCII estilizado e indicadores del perfil GitHub.</desc>
<defs>
 <linearGradient id="frame" x1="0" x2="1" y1="0" y2="1"><stop stop-color="#28ffe1"/><stop offset=".55" stop-color="#08aa9a"/><stop offset="1" stop-color="#bb5cff"/></linearGradient>
 <linearGradient id="surface" x1="0" x2="0" y1="0" y2="1"><stop stop-color="#092627"/><stop offset="1" stop-color="#071017"/></linearGradient>
 <filter id="glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="7" result="blur"/><feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
 <pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse"><path d="M 32 0 L 0 0 0 32" fill="none" stroke="#00e6ce" stroke-opacity=".075"/></pattern>
 <pattern id="scanlines" width="4" height="4" patternUnits="userSpaceOnUse"><rect width="4" height="1" fill="#bfffee" opacity=".035"/></pattern>
 <clipPath id="portrait"><rect x="58" y="192" width="565" height="436" rx="13"/></clipPath>
</defs>
<style>
 .heading{{font:700 28px 'DejaVu Sans Mono',monospace;fill:#dffff8;letter-spacing:2px}} .small{{font:13px 'DejaVu Sans Mono',monospace;fill:#74d4cb;letter-spacing:2px}} .key{{font:18px 'DejaVu Sans Mono',monospace;fill:#49cdbf}} .value{{font:700 18px 'DejaVu Sans Mono',monospace;fill:#ecfff9}} .ascii{{font:700 14px 'DejaVu Sans Mono',monospace;fill:#5afbe0;letter-spacing:0px}} .accent{{fill:#7effea}}
 @keyframes blink{{0%,47%{{opacity:1}}50%,100%{{opacity:0}}}} .cursor{{animation:blink 1.2s step-end infinite}}
 @keyframes sweep{{0%{{transform:translateY(-430px);opacity:0}}12%{{opacity:.65}}85%{{opacity:.65}}100%{{transform:translateY(430px);opacity:0}}}} .scanner{{animation:sweep 6s linear infinite}}
 @keyframes pulse{{0%,100%{{opacity:.45}}50%{{opacity:1}}}} .pulse{{animation:pulse 3s ease-in-out infinite}}
 @media (prefers-reduced-motion:reduce){{.cursor,.scanner,.pulse{{animation:none}}}}
</style>
<rect width="1280" height="740" fill="#04090e"/><rect width="1280" height="740" fill="url(#grid)"/>
<rect x="24" y="24" width="1232" height="692" rx="22" fill="none" stroke="#00efd6" stroke-opacity=".3" stroke-width="12" filter="url(#glow)"/>
<rect x="24" y="24" width="1232" height="692" rx="22" fill="url(#surface)" stroke="url(#frame)" stroke-width="2"/>
<rect x="37" y="37" width="1206" height="666" rx="17" fill="none" stroke="#54fdea" stroke-opacity=".23"/>
<circle cx="64" cy="67" r="7" fill="#ff6b88"/><circle cx="89" cy="67" r="7" fill="#fbd16a"/><circle cx="114" cy="67" r="7" fill="#49ecb3"/>
<text x="160" y="74" class="small">~/PROFILE_SCAN.EXE</text><text x="1160" y="73" class="small">v1.0</text>
<line x1="50" y1="96" x2="1230" y2="96" stroke="#55f7df" stroke-opacity=".45"/>
<text x="58" y="145" class="heading">PROFILE SCAN <tspan fill="#65fae6">//</tspan> BRIAN ALBELO</text><text x="1175" y="144" class="small pulse">● ONLINE</text>
<rect x="58" y="192" width="565" height="436" rx="13" fill="#06191d" stroke="#35dfcc" stroke-width="1.5"/>
<rect x="648" y="192" width="574" height="436" rx="13" fill="#071a1d" stroke="#35dfcc" stroke-width="1.5"/>
<text x="81" y="222" class="small">VISUAL_MAP  /  SUBJECT_001</text><text x="672" y="222" class="small">SYSTEM_INFO  /  IDENTITY</text>
<g clip-path="url(#portrait)">{lines}
<rect x="60" y="0" width="561" height="4" fill="#79ffe5" opacity=".6" class="scanner"/>
</g>
<text x="82" y="600" class="small">[ ANONYMOUS CYBER AVATAR / ASCII MODE ]</text>
<text x="677" y="275" class="key">NAME</text><text x="846" y="275" class="value">Brian Albelo</text>
{meta}
<text x="754" y="518" class="key">ROLE</text><text x="930" y="518" class="value">Analista Funcional</text>
<text x="754" y="560" class="key">STACK</text><text x="930" y="560" class="value">SQL · APIs · BPMN</text>
<text x="754" y="602" class="key">LOCATION</text><text x="930" y="602" class="value">Argentina</text>
<line x1="58" y1="660" x2="1222" y2="660" stroke="#57f5de" stroke-opacity=".3"/>
<text x="62" y="686" class="small">&gt; SYSTEM READY. WAITING FOR NEXT CHALLENGE<tspan class="cursor">_</tspan></text>
<rect width="1280" height="740" fill="url(#scanlines)" pointer-events="none"/>
</svg>'''
    (ROOT/'assets/profile-scan.svg').write_text(svg,encoding='utf-8')
    print('Created SVG; stats:',stats)
if __name__=='__main__': make()
