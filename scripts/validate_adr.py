#!/usr/bin/env python3
"""
scripts/validate_adr.py
Vérifie que chaque ADR suit le template minimal.
Retourne code 0 si ok, 1 sinon.
"""
import re, sys, pathlib

REQUIRED_HEADERS = [
    r"^#\d+\.\s+.+",         # #<Numero>.<Titre>
    r"^##Statut\s*$",
    r"^##Contexte\s*$",
    r"^##Decision\s*$",
    r"^##Alternatives envisagees\s*$",
    r"^##Consequences\s*$"
]

def check_file(path: pathlib.Path):
    text = path.read_text(encoding="utf-8")
    # Normalize line endings
    lines = text.splitlines()
    joined = "\n".join(lines)
    missing = []
    for hdr in REQUIRED_HEADERS:
        if not re.search(hdr, joined, re.MULTILINE):
            missing.append(hdr)
    return missing

def main():
    base = pathlib.Path("doc/adr")
    if not base.exists():
        print("No doc/adr directory found.", file=sys.stderr)
        return 1
    ok = True
    for md in sorted(base.glob("*.md")):
        missing = check_file(md)
        if missing:
            ok = False
            print(f"ERROR: {md} is missing required headers:")
            for m in missing:
                print(f"  - {m}")
            print()
    if not ok:
        print("One or more ADR files are invalid.", file=sys.stderr)
        return 1
    print("All ADR files are valid.")
    return 0

if __name__ == "__main__":
    sys.exit(main())

