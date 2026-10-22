"""Gera index.html (site publicável) a partir de loja.html.
Uso: python montar-site.py   -> depois suba index.html + pasta img/ para a hospedagem."""
from pathlib import Path
base = Path(__file__).parent
corpo = (base / "loja.html").read_text(encoding="utf-8")
html = ('<!doctype html>\n<html lang="pt-BR">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        '<style>:root{padding:env(safe-area-inset-top,0px) 0 env(safe-area-inset-bottom,0px)}body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>\n'
        '</head>\n<body>\n' + corpo + '\n</body>\n</html>\n')
(base / "index.html").write_text(html, encoding="utf-8")
print("index.html gerado")
