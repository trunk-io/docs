# Output Formats

Reference for all outputs produced by the write-docs skill.

## Contents

- [PR body format](#pr-body-format)
- [Slack post format](#slack-post-format)
- [Report card format](#report-card-format)

## PR Body Format

PR title: `[TRUNK-XXXXX] Short descriptive title` (prefix with Linear ticket ID if one exists).

PR body sections:
- **Summary** — bullet list of changes
- **Linear tickets** — clickable links to all related tickets
- **Context links** — all Slack, Slite, Loom links from the notes
- **Files changed** — list of files created/modified
- **Open questions** — things that could not be confirmed from available context
- **Test plan** — checklist for reviewer (e.g., "check GitBook preview", "verify code example works")

## Slack Post Format

Write to `.claude/tmp/<draft-name>/slack.md`. Must be directly copy-pasteable into Slack.

**MUST use Slack mrkdwn syntax, NOT Markdown:**
- Bold: `*text*` (single asterisks, not double)
- Links: `<URL|display text>`
- Bullets: use the `*` character on a new line (Slack list style)
- No Markdown headers (`##`), links (`[text](url)`), or bold (`**text**`)

Template:
```
*[Feature Name] — docs update ready for review*

[1-2 sentence summary of what changed in the docs.]

* PR: <GitHub PR URL|#NNN>
* Linear: <Linear ticket URL|TRUNK-XXXXX>

*Open questions for the team:*
* [list any items needing eng confirmation]
```

## Report Card Format

Append an HTML card to `.claude/tmp/report.html`. If the file does not exist, create it with basic HTML styling.

Each card includes:
- PR link
- Linear link
- Change type badge
- Changes summary
- Context links
- Related tickets
- Review focus areas
- Open questions
