---
description: >-
  Submit, cancel, and track Trunk Merge Queue pull requests directly from
  GitHub with the Trunk Chrome Extension.
---

# Chrome Extension

The Trunk Chrome Extension overlays merge queue controls and status onto your normal GitHub experience, so you can submit a PR to the queue, cancel it, and watch its testing progress without leaving the pull request page.

{% hint style="info" %}
The extension is a companion to Trunk Merge Queue — you still need a [configured queue](getting-started/) for your repository. The extension only surfaces controls and status for queues your Trunk organization already owns.
{% endhint %}

<!-- TODO: hero screenshot of the extension overlay on a GitHub PR page -->

<figure><img src="../.gitbook/assets/chrome-extension-overview.png" alt=""><figcaption>The Trunk overlay on a GitHub pull request page.</figcaption></figure>

## Install the extension

1. Open the [Trunk Merge Queue listing](https://chromewebstore.google.com/detail/liggeliamkammmieidmmfmmdnjilabgn) in the Chrome Web Store.
2. Click **Add to Chrome** and approve the requested permissions.
3. Pin the Trunk icon to your toolbar so the popup is one click away.
4. Click the Trunk icon and sign in. The extension uses your existing browser session at [app.trunk.io](https://app.trunk.io) — if you're already logged in, no additional sign-in is needed. See [Authentication and security](#authentication-and-security) for details.

{% hint style="info" %}
**Rolling the extension out to a team?** Chrome admins can force-install the Trunk extension for everyone in a Google Workspace organization using the [Chrome Web Store ID](https://chromewebstore.google.com/detail/liggeliamkammmieidmmfmmdnjilabgn) `liggeliamkammmieidmmfmmdnjilabgn`. See Google's [Automatically install apps and extensions](https://support.google.com/chrome/a/answer/6306504?hl=en) guide for the admin console steps.
{% endhint %}

<!-- TODO: screenshot of Chrome Web Store listing -->

<figure><img src="../.gitbook/assets/chrome-extension-install.png" alt=""><figcaption></figcaption></figure>

The extension activates automatically on `github.com` pull request pages for repositories that have a Trunk Merge Queue configured.

## Submit a pull request to the queue

On any pull request in a queue-enabled repository, the extension adds a **Merge Queue** panel alongside GitHub's native merge controls.

1. Open the pull request on GitHub.
2. In the Trunk panel, click **Add to Merge Queue**.
3. Optionally choose a [priority](optimizations/priority-merging.md) before submitting.

<!-- TODO: screenshot of the Add to Merge Queue button on a GitHub PR -->

<figure><img src="../.gitbook/assets/chrome-extension-submit.png" alt=""><figcaption>Submitting a PR to the queue from the GitHub PR page.</figcaption></figure>

Submission goes through the same backend as the `/trunk merge` comment and the Trunk web app, so behavior is identical — see [Submit and cancel pull requests](using-the-queue/reference.md) for the full lifecycle.

## Remove a pull request from the queue

If a PR is already in the queue, the panel shows a **Cancel** action.

1. Click **Cancel** in the Trunk panel on the PR page.
2. The PR is removed from the queue immediately, the same as running `/trunk cancel`.

<!-- TODO: screenshot of the Cancel control in the extension panel -->

<figure><img src="../.gitbook/assets/chrome-extension-cancel.png" alt=""><figcaption></figcaption></figure>

## Track testing progress

Once a PR is in the queue, the extension panel updates in real time as it moves through [each state](using-the-queue/reference.md#pull-request-states):

* **Queued** — waiting for prerequisites such as branch protection or mergeability
* **Pending** — admitted to the queue, waiting for capacity
* **Testing** — actively running required status checks against a merge candidate
* **Tests Passed** — waiting for upstream PRs before merging
* **Merged**, **Failed**, or **Cancelled** — terminal states

The panel shows the current state, time spent in queue, and any upstream PRs whose results this PR depends on. A link jumps to the full PR detail page in the Trunk web app for deeper context.

<!-- TODO: screenshot of the in-progress testing view inside the panel -->

<figure><img src="../.gitbook/assets/chrome-extension-testing.png" alt=""><figcaption>Live testing progress shown directly on the GitHub PR page.</figcaption></figure>

## Authentication and security

The extension does **not** ask you for credentials, API tokens, or a separate password. It authenticates by reusing your existing browser session at [app.trunk.io](https://app.trunk.io) — the same session you already use for the Trunk web app.

* **Session-based auth.** When you take an action in the extension, the request is sent to the Trunk API with the cookies your browser already holds for `app.trunk.io`. If you aren't signed in, the extension prompts you to sign in once via the normal Trunk login flow; from then on it piggybacks on that session.
* **No new credentials are stored.** The extension does not generate, store, or transmit a long-lived token. Signing out of [app.trunk.io](https://app.trunk.io) signs the extension out as well.
* **Permissions are unchanged.** The extension can only see queues and act on PRs that your Trunk user already has access to — it cannot escalate permissions. Every action is recorded against your Trunk user, just as it would be from the web app or CLI.
* **Scoped to GitHub PR pages.** The content script runs on `github.com` pull request URLs so it can render the overlay; it does not read or transmit page contents beyond the repository and PR identifiers needed to query the Trunk API.
* **Same transport guarantees as the rest of Trunk.** All extension traffic to Trunk uses TLS, and your data is handled per the [Trunk Security policy](../setup-and-administration/security.md).

If you want to revoke the extension's access, sign out of [app.trunk.io](https://app.trunk.io) or remove the extension from Chrome — there is no separate token to rotate.

## Frequently asked questions

<details>

<summary><strong>Do I need to install anything besides the extension?</strong></summary>

Yes — the extension is a UI on top of Trunk Merge Queue. Your repository must have the [Trunk GitHub App installed and a queue configured](getting-started/) before the overlay does anything useful.

</details>

<details>

<summary><strong>Why don't I see the overlay on a PR?</strong></summary>

The overlay only appears on pull requests in repositories that your Trunk organization has configured a queue for. If you're signed in and still don't see it, confirm the repository in **Settings → Repositories** in the Trunk web app.

</details>

<details>

<summary><strong>Does the extension work in other Chromium browsers?</strong></summary>

The extension targets Chrome. Chromium-based browsers (Edge, Brave, Arc) generally work via the Chrome Web Store, but only Chrome is officially supported.

</details>

<details>

<summary><strong>How does the extension differ from the `/trunk merge` comment?</strong></summary>

Both go through the same Trunk Merge Queue backend. The extension is a faster, in-page surface for the same actions and adds live status without polling the PR comments.

</details>
