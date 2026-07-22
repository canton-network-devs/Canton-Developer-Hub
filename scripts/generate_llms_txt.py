#!/usr/bin/env python3

"""
Generates a static, JavaScript-free llms.txt from Dev Hub's tools.json so Mintlify's assistant (or any AI crawler that can't execute JS) can index the full tool catalog. Run from the repo root:
python3 scripts/generate_llms_txt.py
"""
import json
from collections import defaultdict
from datetime import date, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SOURCE = REPO_ROOT / "Github Page" / "tools.json"
DEST = REPO_ROOT / "Github Page" / "llms.txt"

def main():
    tools = json.loads(SOURCE.read_text())
    by_category = defaultdict(list)
    for t in tools:
        by_category[t.get("category", "Other")].append(t)
    lines = [
        "# Canton Developer Hub — Ecosystem Tool Catalog",
        "",
        "> Canton Developer Hub (dev-hub.canton.foundation) is the community-maintained "
        "catalog of ecosystem tooling for building on Canton Network — official Canton "
        "Network SDKs/APIs, Canton Foundation Dev Fund-funded projects, and other "
        "community-built tools. This is a plain-text index for AI assistants; the "
        "interactive version with filtering is at https://dev-hub.canton.foundation.",
        "",
    ]
    for category in sorted(by_category):
        lines.append(f"## {category}")
        lines.append("")
        for t in sorted(by_category[category], key=lambda x: x["name"]):
            name = t["name"]
            maker = t.get("maker", "Unknown")
            desc = t.get("desc", "")
            dev_fund = " (Canton Foundation Dev Fund)" if t.get("dev_fund") else ""
            ttype = t.get("type", "")
            primary_link = t["links"][0]["url"] if t.get("links") else ""
            updated = t.get("last_updated", "")
            lines.append(
                f"- [{name}]({primary_link}): {desc} — Maker: {maker}{dev_fund}. "
                f"Type: {ttype}. Last updated: {updated}."
            )
        lines.append("")
    lines.append("---")
    lines.append("Generated automatically from tools.json. Do not edit.")
    lines.append(f"Generated: {date.today().isoformat()}")
    DEST.write_text("\n".join(lines))
    print(f"Wrote {DEST} — {len(tools)} tools across {len(by_category)} categories")
if __name__ == "__main__":
    main()
