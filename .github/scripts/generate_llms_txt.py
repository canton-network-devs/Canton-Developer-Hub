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
    style = """
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@300;400;500;600&display=swap" rel="stylesheet" />
<style>
  :root {
    --yellow: #F3FF97; --black: #030206; --white: #FFFFFC;
    --lilac: #D5A5E3; --purple: #875CFF; --taupe: #A89F91;
    --bg: #FFFFFC; --border: rgba(3,2,6,0.18);
    --text: #030206; --muted: #5a5860; --hint: #9a97a0;
  }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'IBM Plex Sans', system-ui, sans-serif; background: var(--bg); color: var(--text); -webkit-font-smoothing: antialiased; }
  a { color: var(--purple); text-decoration: none; }
  a:hover { text-decoration: underline; }
  .site-header { background: var(--black); padding: 0 2rem; height: 56px; display: flex; align-items: center; justify-content: space-between; }
  .logo { color: var(--white); font-size: 16px; font-weight: 500; }
  .header-btn { font-size: 13px; padding: 6px 14px; border-radius: 100px; border: 1px solid rgba(255,255,252,0.2); color: var(--white); }
  .header-btn:hover { border-color: rgba(255,255,252,0.5); text-decoration: none; }
  .hero { background: var(--black); padding: 2.5rem 2rem 2rem; }
  .hero-inner, .main { max-width: 960px; margin: 0 auto; }
  .hero-eyebrow { font-size: 12px; font-weight: 500; letter-spacing: 0.1em; text-transform: uppercase; color: var(--taupe); margin-bottom: 0.5rem; }
  .hero h1 { font-size: clamp(24px, 4vw, 36px); font-weight: 300; color: var(--white); margin-bottom: 0.5rem; }
  .hero p { font-size: 15px; font-weight: 300; color: var(--taupe); max-width: 600px; line-height: 1.6; }
  .hero p a { color: var(--yellow); }
  .main { padding: 2rem 1rem 4rem; }
  h2.section { font-size: 13px; font-weight: 700; letter-spacing: 0.03em; text-transform: uppercase; color: var(--muted); margin: 2rem 0 0.9rem; padding-top: 1rem; border-top: 1px solid var(--border); }
  h2.section:first-of-type { border-top: none; padding-top: 0; margin-top: 0; }
  .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 14px; }
  .card { background: var(--bg); border: 1px solid var(--border); border-radius: 14px; padding: 1.4rem; display: flex; flex-direction: column; gap: 8px; }
  .card-top { display: flex; justify-content: space-between; align-items: flex-start; gap: 8px; }
  .card-name { font-size: 15px; font-weight: 500; }
  .card-maker { font-size: 12.5px; color: var(--hint); font-weight: 600; }
  .badge { font-size: 12px; font-weight: 600; padding: 3px 9px; border-radius: 100px; white-space: nowrap; flex-shrink: 0; }
  .badge.official { background: var(--yellow); color: var(--black); }
  .badge.partner { background: rgba(213,165,227,0.25); color: #4a2060; }
  .badge-devfund { display: inline-block; font-size: 11.5px; font-weight: 600; padding: 2px 9px; border-radius: 100px; background: rgba(76,175,80,0.12); color: #2e7d32; border: 1px solid rgba(76,175,80,0.35); }
  .card-desc { font-size: 13px; color: var(--muted); line-height: 1.6; }
  .card-meta { font-size: 11.5px; color: #313130; }
  .card-links { display: flex; flex-wrap: wrap; gap: 6px; }
  .card-links a { font-size: 11.5px; font-weight: 600; padding: 2px 9px; border-radius: 100px; border: 1px solid var(--border); color: var(--muted); text-decoration: none; }
  .card-links a:hover { border-color: var(--hint); color: var(--black); }
  .site-footer { background: var(--black); padding: 1.75rem; text-align: center; font-size: 13px; color: var(--taupe); font-weight: 300; }
  .site-footer a { color: var(--yellow); }
</style>"""

    parts = [
        "<!DOCTYPE html>",
        '<html lang="en"><head><meta charset="utf-8">',
        '<meta name="viewport" content="width=device-width, initial-scale=1">',
        "<title>Canton Developer Hub</title>",
        '<meta name="description" content="Static, crawlable index of Canton '
        'Network ecosystem tools, SDKs, and APIs for AI assistants and search engines.">',
        style,
        "</head><body>",
        '<header class="site-header"><div class="logo">Build on Canton</div>'
        '<a class="header-btn" href="https://canton-network-devs.github.io/Canton-Developer-Hub/">Interactive version &#8594;</a></header>',
        '<section class="hero"><div class="hero-inner">',
        '<p class="hero-eyebrow">All Open-Source</p>',
        "<h1>Ecosystem Tool Catalog</h1>",
        "<p>Canton Developer Hub is the community-maintained catalog of ecosystem "
        "tooling for building on Canton Network: official Canton Network SDKs/APIs, "
        "Canton Foundation Dev Fund-funded projects, and other community built tools. "
        'For filtering and search, use the <a href="https://canton-network-devs.github.io/'
        'Canton-Developer-Hub/">interactive Dev Hub</a>.</p>',
        "</div></section>",
        '<main class="main">',
    ]
    for category in sorted(by_category):
        parts.append(f'<h2 class="section">{html.escape(category)}</h2>')
        parts.append('<div class="grid">')
        for t in sorted(by_category[category], key=lambda x: x["name"]):
            name = html.escape(t["name"])
            maker = html.escape(t.get("maker", "Unknown"))
            desc = html.escape(t.get("desc", ""))
            dev_fund_badge = '<span class="badge-devfund">Dev Fund</span>' if t.get("dev_fund") else ""
            ttype = t.get("type", "partner")
            badge_label = "Official" if ttype == "official" else "Partner tooling"
            links = t.get("links") or []
            link = html.escape(links[0]["url"]) if links else "#"
            # The name already carries the first link. The rest were being
            # dropped: 19 of the entries in tools.json declare more than one,
            # and a tool whose demo, package or spec lives behind link two was
            # listed with no way to reach it.
            extra = "".join(
                f'<a href="{html.escape(l["url"])}" target="_blank" rel="noopener">'
                f'{html.escape(l.get("label") or "Link")}</a>'
                for l in links[1:] if l.get("url")
            )
            extra_html = f'<div class="card-links">{extra}</div>' if extra else ""
            updated = html.escape(t.get("last_updated", ""))
            parts.append(
                '<div class="card">'
                '<div class="card-top">'
                f'<div><div class="card-name"><a href="{link}">{name}</a></div>'
                f'<div class="card-maker">{maker}</div></div>'
                f'<span class="badge {html.escape(ttype)}">{badge_label}</span>'
                "</div>"
                f"<div>{dev_fund_badge}</div>"
                f'<div class="card-desc">{desc}</div>'
                f"{extra_html}"
                f'<div class="card-meta">Last updated: {updated}</div>'
                "</div>"
            )
        parts.append("</div>")
    parts.append("</main>")
    parts.append(
        f'<footer class="site-footer">Generated automatically from tools.json on '
        f'{date.today().isoformat()}. Maintained by <a href="https://canton.foundation/" '
        'target="_blank">Canton Foundation</a>.</footer>'
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
