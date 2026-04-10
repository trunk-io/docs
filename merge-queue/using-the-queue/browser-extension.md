---
description: Use the Trunk browser extension to manage merge queue status directly from GitHub
---

# Browser Extension

The Trunk Merge Queue browser extension brings merge queue controls into GitHub. You can submit PRs to the queue, check status, and view the merge graph without leaving GitHub.

## Supported browsers

The extension works on Chrome and other Chromium-based browsers (Edge, Brave, Arc).

## Installation

Install the extension from the Chrome Web Store and sign in with your Trunk account.

Once installed, the extension activates automatically when you visit a GitHub repository that uses Trunk Merge Queue.

## Features

### PR page integration

When you open a pull request on GitHub, the extension adds a Trunk merge queue panel near the merge button. The panel shows:

- The current status of the PR in the queue (queued, testing, passed, failed, or merged)
- A link to the full merge queue details in the Trunk app
- Buttons to submit the PR to the queue or cancel it

The panel updates in real time while your PR is in progress. You do not need to refresh the page to see status changes.

### Repo merge queue tab

The extension adds a **Merge Queue** tab to the GitHub repository navigation bar. The tab shows an overview of the queue for that repo, including how many PRs are currently queued.

## Authentication

The extension uses your Trunk session to authenticate. If you are signed in to the Trunk app in the same browser, the extension picks up that session automatically. If not, the extension will prompt you to sign in.

## Submitting and canceling PRs

From a PR page, click **Add to merge queue** in the Trunk panel to submit the PR. To remove it, click **Cancel**.

These actions are equivalent to posting `/trunk merge` or `/trunk cancel` as a GitHub comment. See [Submit and cancel pull requests](reference.md) for other submission methods.

## Status indicators

The extension uses icons to show the current state of a PR in the queue:

| Icon | Status |
|------|--------|
| Pending | The PR is waiting for queue capacity |
| Testing | CI is running against the PR |
| Tests passed | CI passed; waiting for upstream PRs to merge |
| Failed | The PR failed testing and was removed from the queue |
| Merged | The PR was successfully merged |

## Troubleshooting

**The extension does not appear on a PR page.**
Confirm the repository has Trunk Merge Queue configured. The extension only activates for repos connected to Trunk.

**The status is not updating.**
The extension polls for status changes. If the panel appears stale, reload the page to force a refresh.

**I am prompted to sign in repeatedly.**
Make sure you are signed in to the Trunk app in the same browser profile. The extension reads the Trunk session cookie and will not persist authentication across browser profiles.
