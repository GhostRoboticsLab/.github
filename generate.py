#!/usr/bin/env python3
"""Render profile/README.md from profile/README.template.md in any of the 9
palettes that ghostlabs.web.app ships in its Tweaks panel.

    python3 generate.py              # list palettes + show the active one
    python3 generate.py phosphor     # re-skin the README to "Phosphor CRT"
    python3 generate.py bone         # light-mode "Bone & Ink", etc.

The palette values mirror the site's PALETTES map (signal.jsx). Each token is a
hex string WITHOUT the leading '#', because that's the form the badge/render
services (shields.io, capsule-render, github-readme-stats) expect in URLs.
"""
import sys
from pathlib import Path

# token keys: bg / bg2 (surface-hi) / line / text / dim / accent / accent2
PALETTES = {
    "signal-lime":    ("Signal Lime",      "lime primary · peach secondary",           "0a0a0b", "1a1a1e", "26262c", "ececea", "9c9a94", "c8fb59", "fdba74"),
    "cobalt":         ("Cobalt Research",   "institutional blue · sky secondary",       "08090d", "171a23", "22262f", "ecedef", "9097a3", "5b8eff", "7ad8ff"),
    "phosphor":       ("Phosphor CRT",      "vintage terminal green · amber secondary", "050807", "0e1611", "1a241e", "d6f5e1", "7ea88c", "5cff95", "ffce5c"),
    "aurora":         ("Aurora Boreal",     "mint primary · peach · deep navy",         "0a1019", "152030", "1f2c40", "e9f1f7", "8fa5be", "7affc8", "ffba88"),
    "tungsten":       ("Tungsten Foundry",  "brass primary · steel-blue secondary",     "0f0c08", "221c16", "322a23", "f5ecdc", "a89c8c", "d4a93d", "6585a8"),
    "magenta-static": ("Magenta Static",    "magenta × cyan · high-energy punk",        "0a0810", "1d1626", "2c2238", "f4ebf6", "a995b3", "ff3d8c", "3df0ff"),
    "sodium":         ("Sodium Vapor",      "sodium-orange × electric blue",            "08070a", "19161d", "2a2530", "f0e8dc", "a89986", "ffae3c", "4a9eff"),
    "plum-atelier":   ("Plum Atelier",      "deep plum · brass · sage secondary",       "14101a", "241c30", "332a44", "ede6f2", "a695b5", "d4a93d", "8aab8b"),
    "bone":           ("Bone & Ink",        "LIGHT mode · oxblood × forest",            "f1ede4", "e0d8c2", "d6cfbd", "1a1814", "5e5a51", "6b1e1e", "3e5f4a"),
}

TOKENS = ("BG", "BG2", "LINE", "TEXT", "DIM", "ACCENT", "ACCENT2")

ROOT = Path(__file__).resolve().parent
TEMPLATE = ROOT / "profile" / "README.template.md"
OUTPUT = ROOT / "profile" / "README.md"


def palette_list_comment() -> str:
    """Indented bullet list of palettes for the generated file's header comment."""
    return "\n".join(
        f"       · {key:<15} {name} — {note}"
        for key, (name, note, *_rest) in PALETTES.items()
    )


def render(key: str) -> str:
    name, _note, bg, bg2, line, text, dim, accent, accent2 = PALETTES[key]
    values = dict(zip(TOKENS, (bg, bg2, line, text, dim, accent, accent2)))
    out = TEMPLATE.read_text(encoding="utf-8")
    out = out.replace("{{PALETTE_NAME}}", f"{name} ({key})")
    out = out.replace("{{PALETTE_LIST}}", palette_list_comment())
    for tok, val in values.items():
        out = out.replace("{{" + tok + "}}", val)
    return out


def usage() -> None:
    active = "unknown"
    if OUTPUT.exists():
        head = OUTPUT.read_text(encoding="utf-8")[:600]
        for key, (name, *_r) in PALETTES.items():
            if f"({key})." in head:
                active = f"{name} ({key})"
                break
    print(f"Active palette: {active}\n")
    print("Usage: python3 generate.py <palette>\n\nPalettes:")
    for key, (name, note, *_r) in PALETTES.items():
        print(f"  {key:<15} {name} — {note}")


def main() -> int:
    if len(sys.argv) != 2:
        usage()
        return 0
    key = sys.argv[1].strip().lower()
    if key not in PALETTES:
        print(f"Unknown palette: {key!r}\n")
        usage()
        return 1
    OUTPUT.write_text(render(key), encoding="utf-8")
    name = PALETTES[key][0]
    print(f"Wrote {OUTPUT.relative_to(ROOT)} · palette: {name} ({key})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
