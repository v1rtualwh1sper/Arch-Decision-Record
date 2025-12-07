#!/usr/bin/env python3
"""
scripts/generate_adr_summary.py

Version simplifiée sans arguments :
- dossier ADR par défaut : doc/adr/
- sortie : doc/adr/SUMMARY.md
"""

from pathlib import Path
import re
from datetime import datetime

ADR_DIR = Path("doc/adr")
SUMMARY_FILE = Path("doc") / "SUMMARY.md"
MAX_CONTEXT_LEN = 140

TITLE_RE = re.compile(r"^#\s*(\d+)\.\s*(.+)", re.IGNORECASE)
STATUS_HEADER_RE = re.compile(r"^##\s*Statut\s*$", re.IGNORECASE)
CONTEXTE_HEADER_RE = re.compile(r"^##\s*Contexte\s*$", re.IGNORECASE)

def parse_adr(path: Path):
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    num, title, status, context_snippet = None, None, None, ""

    # Title
    for line in lines[:15]:
        m = TITLE_RE.match(line.strip())
        if m:
            num = m.group(1)
            title = m.group(2).strip()
            break

    # Status
    for i, line in enumerate(lines):
        if STATUS_HEADER_RE.match(line):
            j = i+1
            while j < len(lines) and lines[j].strip() == "":
                j += 1
            if j < len(lines):
                status = lines[j].strip()
            break

    # Contexte
    for i, line in enumerate(lines):
        if CONTEXTE_HEADER_RE.match(line):
            j = i+1
            paras, cur = [], []
            while j < len(lines):
                l = lines[j]
                if l.strip().startswith("##"):
                    if cur:
                        paras.append(" ".join([s.strip() for s in cur if s.strip()]))
                    break
                if l.strip() == "":
                    if cur:
                        paras.append(" ".join([s.strip() for s in cur if s.strip()]))
                        cur = []
                else:
                    cur.append(l)
                j += 1
            if cur and not paras:
                paras.append(" ".join([s.strip() for s in cur if s.strip()]))
            if paras:
                context_snippet = paras[0]
            break

    return {
        "file": path.name,
        "num": int(num) if num and num.isdigit() else None,
        "title": title or "",
        "status": status or "",
        "context": context_snippet or ""
    }

def escape_pipe(s: str) -> str:
    return s.replace("|", "\\|")

def main():
    if not ADR_DIR.exists() or not ADR_DIR.is_dir():
        print(f"Erreur: dossier '{ADR_DIR}' introuvable.")
        return

    md_files = sorted([p for p in ADR_DIR.glob("*.md") if p.name.lower() != SUMMARY_FILE.name.lower()])
    if not md_files:
        SUMMARY_FILE.write_text("# Sommaire des ADR\n\n_Aucun ADR trouvé._\n", encoding="utf-8")
        print("Aucun ADR trouvé.")
        return

    entries = [parse_adr(md) for md in md_files]
    entries.sort(key=lambda e: (e["num"] is None, e["num"] if e["num"] is not None else e["file"]))

    lines = [
        "# Sommaire des ADR",
        "",
        f"_Généré le {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%SZ')}_",
        "",
        "Ce fichier liste les ADR disponibles dans `doc/adr/`.",
        "",
        "| # | Titre | Statut | Fichier | Contexte (extrait) |",
        "|---:|---|---|---|---|"
    ]

    for e in entries:
        num = e["num"] if e["num"] is not None else "-"
        title = escape_pipe(e["title"] or e["file"])
        status = escape_pipe(e["status"] or "-")
        filelink = f"[{e['file']}](./{e['file']})"
        context = e["context"]
        if len(context) > MAX_CONTEXT_LEN:
            truncated = context[:MAX_CONTEXT_LEN-1]
            if " " in truncated:
                truncated = truncated.rsplit(" ",1)[0]
            context = truncated + "…"
        context = escape_pipe(context or "-")
        lines.append(f"| {num} | {title} | {status} | {filelink} | {context} |")

    SUMMARY_FILE.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Sommaire généré : {SUMMARY_FILE}")

if __name__ == "__main__":
    main()

