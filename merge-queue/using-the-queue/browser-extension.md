---
description: See merge queue status and manage PRs directly from GitHub
---

# Browser Extension

The Trunk Merge Queue browser extension adds queue visibility and controls to GitHub without leaving the PR page. Install it once and your entire team gets merge queue status inline in their normal GitHub workflow.

### What it does

On any GitHub pull request page, the extension:

* Shows the PR's current position and status in the merge queue
* Lets you submit a PR to the merge queue or cancel it without opening the Trunk dashboard
* Links directly to the PR's detail page in Trunk
* Displays status icons that update in real time (pending, testing, bisecting, merged, failed)

On any GitHub repository page, a **Merge Queue** tab appears in the repo nav showing a queue overview and PR count.

### Install the extension

The extension supports Chrome and other Chromium-based browsers (Edge, Brave, Arc).

1. Install the extension from the Chrome Web Store (link available at [trunk.io](https://trunk.io))
2. Click the extension icon to open the popup
3. Log in with your Trunk account
4. Navigate to any GitHub PR in a repo that uses Trunk Merge Queue — queue status appears automatically

### Queue status indicators

| Status | Meaning |
|--------|---------|
| Pending | PR submitted, waiting to enter the queue |
| Testing | PR is actively being tested |
| Bisecting | Queue is isolating a failure |
| Merged | PR merged successfully |
| Failed | PR failed testing and was removed from the queue |

### Submitting and canceling

On a PR page, use the Trunk controls next to GitHub's merge button to submit the PR to the queue or cancel an existing submission. The extension polls the queue state automatically and reflects changes within a few seconds.

### Options and debugging

Open the extension options page (right-click the extension icon, select **Options**) to:

* View your connected Trunk organization and repository
* Access debug logs if you're troubleshooting unexpected behavior
* Sign out

### Permissions

The extension requires access to `github.com` pages and communicates with `api.trunk.io` to fetch queue state. No GitHub tokens are stored by the extension — authentication uses your existing Trunk session.
