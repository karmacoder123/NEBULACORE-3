#!/usr/bin/env python3
"""Rigenera index.html (pagina compressa, <288 KB) dal sorgente leggibile.
Uso:   npm install        (una volta sola: installa three e esbuild)
       python3 build_index.py ../sorgente/NebulaCore_v2_20_Offline.html
Output: out/index.html (da pubblicare) e out/core.html (pagina espansa, per prove)."""
import gzip, base64, re, sys, subprocess, os
src_path = sys.argv[1]
os.makedirs('out', exist_ok=True)
s = open(src_path, encoding='utf-8').read()
a = s.rindex('<script>') + 8; b = s.rindex('</script>'); js = s[a:b]
names = sorted(set(re.findall(r'THREE\.([A-Za-z0-9_]+)', js)))      # solo le classi di three.js usate dall'app
open('out/three_entry.js', 'w').write("export { " + ", ".join(names) + " } from 'three';\n")
subprocess.run(["npx", "esbuild", "out/three_entry.js", "--bundle", "--format=iife", "--global-name=THREE", "--minify",
                "--legal-comments=none", "--outfile=out/three_min.js", "--log-level=warning"], check=True)
three = open('out/three_min.js', encoding='utf-8').read(); assert '</script' not in three
a = s.index('<script>') + 8; b = s.index('</script>', a)
inner = s[:a] + three + s[b:]
open('out/core.html', 'w', encoding='utf-8').write(inner)
b64 = base64.b64encode(gzip.compress(inner.encode('utf-8'), 9)).decode()
metas = ''.join(re.findall(r'<meta (?:name="(?:viewport|apple-mobile-web-app-capable|apple-mobile-web-app-status-bar-style|apple-mobile-web-app-title|theme-color)")[^>]*>\s*', inner))
loader = '''<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="UTF-8">
''' + metas + '''<title>NEBULA CORE</title>
</head>
<body style="margin:0;background:#020905;color:#88ffaa;font:14px monospace">
<p id="ld" style="padding:20px">Caricamento Nebula Core…</p>
<script>
/* Pagina compressa (gzip+base64) per restare sotto i limiti di dimensione dei file; si espande da sola all'avvio. */
(async () => {
  const b64 = "''' + b64 + '''";
  const bin = Uint8Array.from(atob(b64), c => c.charCodeAt(0));
  const html = await new Response(new Blob([bin]).stream().pipeThrough(new DecompressionStream("gzip"))).text();
  document.open(); document.write(html); document.close();
})().catch(e => { document.getElementById("ld").textContent = "Browser troppo vecchio per questa pagina (serve DecompressionStream, Safari 16.4+ / Chrome 80+ / Firefox 113+). " + e; });
</script>
</body>
</html>
'''
open('out/index.html', 'w', encoding='utf-8').write(loader)
print('out/index.html: %.1f KB (limite 288) | pagina espansa %d KB' % (len(loader.encode()) / 1024, len(inner) // 1024))
