# Contributing Guide

Thanks for helping grow the Canton Developer Hub, This guide covers everything you need to know to add or update a tool listing.

There are two ways to contribute depending on what you want to do:

| What you want | How |
|---|---|
| Add/update a tool in the frontend catalogue/page | Open a **PR** to [`tools.json`](./Github%20Page/tools.json) and one MUST add their tool the same format as the others in the JSON File for it to be able to index properly. |
| Report a broken link or outdated info | Open an **Issue** with the Tool and Source of claim. |

## Info on Adding a Tool to the frontend Catalogue Page (PR to `tools.json`)

The filterable page at the Developer Hub is powered entirely by `tools.json` in the root of this repo. To get your tool listed, add a new entry to that file and open a PR.

### The entry format

```json
{
  "name": "Your Tool Name",
  "maker": "Your Company or GitHub handle",
  "type": "partner",
  "category": "APIs",
  "desc": "One to two sentences describing what the tool does and who it's for. Be specific — generic descriptions get sent back for revision.",
  "links": [
    { "label": "Docs", "url": "https://your-docs.com" },
    { "label": "Repo", "url": "https://github.com/you/your-tool" }
  ],
  "daml_sdk_version": "3.4.11",
  "maintained_by": "Your Company",
  "dev_fund": false/true, // Specify if your tool is funded from Canton Foundation Dev Fund.
  "last_updated": "2026-07-16" // Give the date of your latest release of the tool.
}
```

## The Daml SDK Version Requirement

> **This is a hard requirement. PRs that ignore it will not be merged.**

If your tool uses, depends on, or is built against the Daml SDK, you **must** specify the exact version in the `daml_sdk_version` field:

```json
"daml_sdk_version": "3.4.11"
```

### Why this matters

The Daml SDK is versioned, and Canton Network itself moves forward on a regular release cadence. A tool built against an outdated SDK version may produce incorrect results, fail to compile against newer DARs, or be incompatible with current participant nodes. Listing a tool with a stale SDK version misleads developers and reflects badly on the ecosystem.

### Your ongoing responsibility

**You are responsible for keeping your listing.** Specifically:

- When a new Daml SDK version is released and you update your tool to support it, you must open a new PR updating the `daml_sdk_version` field in your entry.
- PRs that update the SDK version should include a link to your tool's changelog, release notes, or commit that confirms the update.
- If your tool falls more than one major version behind the current Daml SDK and no update PR has been submitted, your listing may be marked as outdated or removed at the maintainers' discretion.
- You will not be notified individually when a new SDK version drops. It is your responsibility to track the [Canton Network releases](https://github.com/digital-asset/canton/releases) and the [DPM changelog](https://github.com/digital-asset/dpm/releases).


## PR Checklist

Before opening your PR, confirm all of the following:

- [ ] My entry is valid JSON.
- [ ] All URLs are live and return a working page
- [ ] `type` is exactly `"official"` or `"partner"` (no other values)
- [ ] `category` matches one of the valid categories listed above
- [ ] `description` is one to two sentences, specific, and free of marketing language
- [ ] If my tool uses the Daml SDK, `daml_sdk_version` is set to the current version my tool is built against **not** `null`
- [ ] `maintained_by` is filled in with the person or team responsible for keeping this up to date
- [ ] I understand I am responsible for submitting a new PR if the Daml SDK version changes and I update my tool

## What Gets Rejected

To save everyone's time, these things will get a PR closed without merge:

- Missing or `null` `daml_sdk_version` when the tool clearly uses the Daml SDK
- `type` set to `"official"` for tools not maintained by Digital Asset or Canton Foundation
- Broken or non-`https` links
- Invalid JSON
- Descriptions that are purely marketing copy with no technical substance
- Tools that are not functional or publicly accessible (no private-access-only tools)
- Duplicate entries for tools already listed

## Questions?

Join the [Canton Forum](https://forum.canton.network/) or open an Issue in this repo.
