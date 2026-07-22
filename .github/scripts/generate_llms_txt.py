#!/usr/bin/env python3

import json
from collections import defaultdict
from datetime import date
from pathlib import Path

SOURCE = Path("Github Page") / "tools.json"
DEST = Path("Github Page") / "llms.txt"

def main():
    tools = json.loads(SOURCE.read_text())
    by_category = defaultdict(list)
    for t in tools:
        by_category[t.get("category", "Other")].append(t)
    lines = [
        "# Canton Developer Hub — Ecosystem Tool Catalog",
        "",
        "> Canton Developer Hub (dev-hub.canton.foundation) is the foundation maintained catalog of ecosystem tooling for building on Canton Network."
        "This is a plain-text index for AI LLMs; the interactive version with filtering is at https://dev-hub.canton.foundation.",
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
    lines.append("Generated automatically from tools.json. Do not edit by hand.")
    lines.append(f"Generated: {date.today().isoformat()}")
    DEST.write_text("\n".join(lines))
    print(f"Wrote {DEST} — {len(tools)} tools across {len(by_category)} categories")
if __name__ == "__main__":
    main()
