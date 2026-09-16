from html import escape
from pathlib import Path
import os
from app import total_ht

out = Path("public")
out.mkdir(exist_ok=True)
titre = escape(os.getenv("APP_TITLE", "Formation SOLYTI"))
version = escape(os.getenv("CI_COMMIT_SHORT_SHA", "local"))
page = (
    '<!doctype html><html lang="fr"><meta charset="utf-8">'
    f'<title>{titre}</title><h1>{titre}</h1>'
    f'<p>Exemple HT : {total_ht(3, 20)} euros</p>'
    f'<p>Version : {version}</p></html>'
)
(out / "index.html").write_text(page, encoding="utf-8")
print("Fichier genere : public/index.html")
