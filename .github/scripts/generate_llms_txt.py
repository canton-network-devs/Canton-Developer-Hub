#!/usr/bin/env python3

import html
import json
from collections import defaultdict
from datetime import date
from pathlib import Path

SOURCE = Path("Github Page") / "tools.json"
DEST_TXT = Path("Github Page") / "llms.txt"
DEST_HTML = Path("Github Page") / "catalog.html"

def load_by_category(tools):
    by_category = defaultdict(list)
    for t in tools:
        by_category[t.get("category", "Other")].append(t)
    return by_category

def generate_txt(tools, by_category):
    lines = [
        "# Canton Developer Hub",
        "",
        "> Canton Developer Hub (dev-hub.canton.foundation) is the community maintained catalog of ecosystem tooling for building on Canton Network. This is a plain-text index for AI assistants; the interactive version with filtering is at https://dev-hub.canton.foundation.",
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
    return "\n".join(lines)

def generate_html(tools, by_category):
    parts = [
        "<!DOCTYPE html>",
        '<html lang="en"><head><meta charset="utf-8">',
        "<title>Canton Developer Hub</title>",
        '<meta name="description" content="Static, crawlable index of Canton '
        'Network ecosystem tools, SDKs, and APIs for AI assistants and search engines.">',
        "</head><body>",
        "<h1>Canton Developer Hub</h1>",
        "<p>Canton Developer Hub is the community-maintained catalog of ecosystem "
        "tooling for building on Canton Network: official Canton Network SDKs/APIs, "
        "Canton Foundation Dev Fund-funded projects, and other community built tools. "
        'The interactive version is at <a href="https://canton-network-devs.github.io/'
        'Canton-Developer-Hub/">the Canton Developer Hub</a>.</p>',
    ]
    for category in sorted(by_category):
        parts.append(f"<h2>{html.escape(category)}</h2>")
        parts.append("<ul>")
        for t in sorted(by_category[category], key=lambda x: x["name"]):
            name = html.escape(t["name"])
            maker = html.escape(t.get("maker", "Unknown"))
            desc = html.escape(t.get("desc", ""))
            dev_fund = " (Canton Foundation Dev Fund)" if t.get("dev_fund") else ""
            ttype = html.escape(t.get("type", ""))
            link = html.escape(t["links"][0]["url"]) if t.get("links") else "#"
            updated = html.escape(t.get("last_updated", ""))
            parts.append(
                f'<li><a href="{link}">{name}</a>: {desc} — Maker: {maker}{dev_fund}. '
                f"Type: {ttype}. Last updated: {updated}.</li>"
            )
        parts.append("</ul>")
    parts.append(
        f"<hr><p><em>Generated automatically from tools.json on {date.today().isoformat()}. "
        "Do not edit.</em></p>"
    )
    parts.append("</body></html>")
    return "\n".join(parts)

def main():
    tools = json.loads(SOURCE.read_text())
    by_category = load_by_category(tools)

    DEST_TXT.write_text(generate_txt(tools, by_category))
    DEST_HTML.write_text(generate_html(tools, by_category))
    print(f"Wrote {DEST_TXT} and {DEST_HTML} — {len(tools)} tools across {len(by_category)} categories")

if __name__ == "__main__":
    main()
