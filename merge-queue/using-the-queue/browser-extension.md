---
description: Install the Trunk browser extension to manage the merge queue directly from GitHub
---

# Browser Extension

The Trunk browser extension adds merge queue controls directly into the GitHub interface. You can submit PRs to the queue, cancel them, and see real-time queue status without leaving GitHub.

## Install

The extension is available for Chrome and Chromium-based browsers (Edge, Brave, Arc).

1. Visit the [Trunk for GitHub extension](https://chromewebstore.google.com/detail/trunk-for-github/trunk) page in the Chrome Web Store.
2. Click **Add to Chrome**.
3. Pin the extension to your toolbar for quick access to the queue overview popup.

## Sign in

The extension uses your existing Trunk session. If you are already signed in to [app.trunk.io](https://app.trunk.io), the extension detects your session automatically. If not, click the extension popup and follow the sign-in prompt.

## What it adds

### PR page: merge queue status

On any GitHub PR page for a repository that uses Trunk Merge Queue, the extension injects a status indicator next to the merge button. The indicator shows the current queue state:

| Status | Meaning |
|---|---|
| Pending | PR is queued but not yet testing |
| Testing | PR is running CI tests in the queue |
| Bisecting | A batch failure is being isolated |
| Tests passed | PR passed CI and is waiting for upstream PRs |
| Failed | PR failed tests and was removed from the queue |
| Merged | PR merged successfully |

You can submit a PR to the queue or cancel it directly from this indicator — no GitHub comment or CLI command required.

### Repository tab: queue overview

The extension adds a **Merge Queue** tab to GitHub repository navigation. The tab shows:

- All PRs currently in the queue
- Each PR's position and status
- A count of PRs by state

This gives the same overview as the Trunk dashboard without leaving GitHub.

### Extension popup

Click the Trunk icon in the browser toolbar to open the popup. It shows the queue state for any Trunk-connected repository you recently visited, along with a link to the full Trunk dashboard.

## Supported browsers

| Browser | Supported |
|---|---|
| Chrome | Yes |
| Edge | Yes |
| Brave | Yes |
| Arc | Yes |
| Firefox | No |
| Safari | No |

## Disable or remove

To disable the extension temporarily, click the extensions menu in your browser, find **Trunk for GitHub**, and toggle it off. To remove it entirely, select **Remove from Chrome**.

Removing the extension does not affect your merge queue configuration or any PRs currently in the queue.
