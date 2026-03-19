---
description: >-
  Send merge queue updates to multiple Slack channels and receive personal DM
  notifications — all powered by the Trunk Slack app.
---

# Slack Integration

Trunk Merge Queue integrates with Slack to send real-time notifications about queue activity and pull request state changes. You can route notifications to **multiple Slack channels** per repository, each with its own set of enabled topics, and receive **personal DMs** about your own PRs directly in Slack.

<!-- TODO: replace with updated overview screenshot showing new multi-channel UI -->

<figure><img src="../.gitbook/assets/Screenshot 2025-10-21 at 4.32.54 PM.png" alt=""><figcaption></figcaption></figure>

## Installing the Trunk Slack App

Before you can set up channel notifications or personal DMs, a Slack workspace admin must install the Trunk Slack app for your organization. This is a one-time setup that enables all Slack integration features.

### Steps to Install

1. In the Trunk web app, navigate to **Settings > Organization > Slack**.
2. Click **Add to Slack**.
3. Review and approve the requested permissions on the Slack OAuth screen.
4. You'll be redirected back to Trunk. The page will show your workspace as **Connected** along with the workspace name.

<!-- TODO: add screenshot of Settings > Organization > Slack page showing Add to Slack button -->

<!-- TODO: add screenshot of Slack OAuth permission review screen -->

<!-- TODO: add screenshot of connected state showing workspace name and Reconnect/Disconnect options -->

### Managing the Connection

Once connected, you can **Reconnect** (to reauthorize) or **Disconnect** the workspace from the same settings page.

{% hint style="warning" %}
**Migrating from legacy Slack integration?** If your organization previously connected Slack through the per-repo "Connect with Slack" flow, you still need to complete this new workspace-level installation to access multi-channel notifications and the new personal DM features. After installing, you can set up channel connections and personal notifications using the new workflows described below.
{% endhint %}

## Channel Notifications

Send merge queue updates to one or more shared Slack channels to keep your team informed about queue activity. Each channel can have its own set of enabled notification topics.

### Connecting Slack Channels

{% hint style="info" %}
**Prerequisite:** The Trunk Slack app must be [installed for your organization](integration-for-slack.md#installing-the-trunk-slack-app) before you can connect channels.
{% endhint %}

1. Navigate to **Settings > Repositories > \[your repository] > Merge Queue**.
2. Under **Slack Notifications**, click **Add Channel**.
3. In the **Add Slack Channel** modal, select a channel from the dropdown.
4. Toggle the notification topics you want enabled for that channel.
5. Click **Connect**.

You can connect **multiple channels**, each with a different set of enabled topics. For example, you might send all notifications to a `#merge-notifications` channel while only sending failure alerts to a `#merge-queue-failures` channel.

<!-- TODO: add screenshot of Slack Notifications panel showing connected channels list with Add Channel and Disconnect buttons -->

<!-- TODO: add screenshot of Add Slack Channel modal with channel dropdown and notification topic toggles -->

The channel list displays each connected channel along with a summary of how many notification topics are enabled (e.g., "6/9 enabled"). To remove an individual channel, click the trash icon next to it. To remove all channel connections for the repository, click **Disconnect**.

### Managing Channel Notification Preferences

Each connected channel has its own independent set of notification topics. You can expand any channel in the list to view and toggle its topics on or off. Changes take effect immediately.

See [Available Notification Topics](integration-for-slack.md#available-notification-topics) below for descriptions of each notification type.

{% hint style="info" %}
**Tip:** Want to receive notifications about your own PRs as personal DMs instead of in a shared channel? Check out the [Personal Slack Notifications](integration-for-slack.md#personal-slack-notifications) setup guide.
{% endhint %}

## Personal Slack Notifications

Get direct messages in Slack about your PRs in the merge queue, keeping you informed without adding noise to team channels.

Personal Slack notifications deliver DMs when your PRs are queued, start testing, pass tests, get merged, or encounter issues. This keeps you up-to-date on the progress of your code through the merge queue without needing to check the web UI or monitor shared channels.

### Setting up Personal Notifications

Personal notification setup is done entirely from the **Trunk Slack app's Home tab** — no part of this flow is completed from the Trunk web UI.

1. Open the **Trunk** app in Slack. If you don't see it in your sidebar, add it via **Apps > Manage > Browse Apps** in Slack.
2. Go to the **Home** tab.
3. Click **Link Account** to connect your Trunk account to Slack.
4. Connect your **GitHub account** from the Home tab. This is required for PR tracking and most notifications.
5. Configure your notification preferences using the toggles on the Home tab.

<!-- TODO: add screenshot of Slack Home tab showing Link Account button -->

{% hint style="info" %}
**Tip:** After the Trunk Slack app is installed for your workspace, individual users may still need to manually add the app to their Slack account. In Slack, go to **Apps > Manage > Browse Apps** and search for "Trunk" to add it.
{% endhint %}

### Using the Trunk Web UI

The Trunk notifications page (**Settings > Account > Notifications**) still exists as a convenience entry point, but it directs you to complete setup in Slack:

* **Step 1: Connect your Slack workspace** — Shows whether your workspace is connected. If not, a **Go to Slack settings** button takes you to the organization Slack settings page.
* **Step 2: Complete setup in Slack** — An **Open in Slack** button takes you to the Trunk app's Home tab to link your account and configure notifications.

<!-- TODO: add screenshot of Trunk web UI notifications page showing the two-step redirect flow -->

{% hint style="warning" %}
**Slack app not installed?** If the Trunk Slack app hasn't been installed for your organization yet, the Home tab in Slack will display a warning: "The Trunk app isn't fully installed for this workspace yet, so personal notifications can't be set up here." It will direct a Slack admin to go to **Settings > Organization** in Trunk and install the app. See [Installing the Trunk Slack App](integration-for-slack.md#installing-the-trunk-slack-app).
{% endhint %}

{% hint style="info" %}
**Tip:** Want to send notifications to a shared team channel instead? Check out the [Channel Notifications](integration-for-slack.md#channel-notifications) setup guide.
{% endhint %}

## Slack App Home Dashboard

The Trunk Slack app's **Home** tab provides a personal merge queue dashboard directly in Slack. Open the Trunk app in Slack and click the **Home** tab to see an overview of your merge queue activity across all repositories.

### What You'll See

The Home tab displays the following sections:

* **Refresh** — A button at the top of the Home tab to update the view with the latest queue data, along with a "Last refreshed" timestamp.
* **Account connection status** — Shows your connected identity (e.g., "Connected as **Your Name**"), an **Unlink Account** button, and your GitHub account connection status. You can connect your GitHub account directly from the Home tab if it isn't linked yet.
* **Not Ready** — PRs you've submitted that are waiting for prerequisites (e.g., GitHub mergeability) before entering the queue. Grouped by repository and branch.
* **PRs in Queue** — Your PRs that are currently in the queue, with real-time status indicators (e.g., "Testing"). Grouped by repository and branch.
* **Recently Merged PRs** — Your most recently merged PRs with merge dates. Grouped by repository and branch.
* **Failed PRs** — Your PRs that failed in the queue. Grouped by repository and branch.
* **Notification Preferences** — Toggle buttons for all 9 notification topics. You can enable or disable individual notifications directly from Slack without visiting the web UI.

Each PR entry shows the PR title, number, and a link to the GitHub PR. All data is scoped to your PRs via your linked GitHub account and is shown across **all merge queues** you submit to.

<!-- TODO: add screenshot of Home tab connected state showing account info and PR sections -->

<!-- TODO: add screenshot of Home tab Notification Preferences toggles -->

### Linking Your Account

1. Open the Trunk app in Slack and go to the **Home** tab.
2. Click **Link Account** to connect your Trunk account.
3. Connect your **GitHub account** (required for PR tracking and most notifications).

{% hint style="info" %}
After the workspace-level Slack app installation, individual users may still need to add the Trunk app to their Slack account. In Slack, go to **Apps > Manage > Browse Apps** and search for "Trunk."
{% endhint %}

### Managing Notification Preferences

You can toggle notification topics on or off directly from the Home tab — no need to visit the Trunk web UI. Changes take effect immediately. The available topics are the same as those listed in [Available Notification Topics](integration-for-slack.md#available-notification-topics).

## Frequently Asked Questions

<details>

<summary><strong>Do I need both GitHub and Slack connected to receive personal notifications?</strong></summary>

Yes, both connections are required. Connect your GitHub account from the Trunk Slack app's **Home** tab — this links your PRs to your Trunk user account. Your Slack connection is established when you link your account from the Home tab, enabling direct messaging.

</details>

<details>

<summary><strong>What's the difference between personal notifications and channel notifications?</strong></summary>

[Personal notifications](integration-for-slack.md#personal-slack-notifications) are sent directly to you via Slack DM and only include updates about your own PRs. They are set up from the Trunk Slack app's Home tab.

[Channel notifications](integration-for-slack.md#channel-notifications) are sent to one or more shared team channels and include updates about all PRs in the merge queue. You can connect multiple channels per repository, each with different notification topics.

You can use both simultaneously to stay informed personally while keeping your team updated.

</details>

<details>

<summary><strong>Can I customize which notifications I receive?</strong></summary>

Yes. For personal notifications, toggle topics on or off from the Trunk Slack app's **Home** tab. For channel notifications, configure topics per channel under **Settings > Repositories > \[your repository] > Merge Queue** in the Trunk web app.

</details>

<details>

<summary><strong>What happens if I disconnect my accounts?</strong></summary>

You can unlink your account from the Trunk Slack app's Home tab using the **Unlink Account** button. Disconnecting stops personal Slack notifications. You can reconnect at any time by returning to the Home tab and clicking **Link Account**.

</details>

<details>

<summary><strong>How do I add the Trunk app to my Slack account?</strong></summary>

After a Slack workspace admin has installed the Trunk app for your organization, individual users may still need to add it to their Slack account. In Slack, go to **Apps > Manage > Browse Apps**, search for "Trunk," and add the app. Once added, it will appear in your Slack sidebar under **Apps**.

</details>

## Available Notification Topics

Both channel and personal Slack notifications support the same notification topics. You can customize which events trigger notifications for each channel or for your personal DMs.

<figure><img src="../.gitbook/assets/SCR-20260202-neph.png" alt=""><figcaption></figcaption></figure>

| Notification                                                                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| --------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Merge is updated                                                            | The merge queue's configuration was changed. This covers anything that changes how the queue acts, including: pausing or draining the queue, changing its mode, changing testing concurrency, and so on.                                                                                                                                                                                                                                                                      |
| Pull request is submitted for merging                                       | A pull request has been [submitted to the queue](https://docs.trunk.io/merge-queue/set-up-trunk-merge#submit-pull-requests)                                                                                                                                                                                                                                                                                                                                                   |
| Pull request is admitted to the queue and is waiting to be tested           | A pull request has been admitted to the queue and will begin testing as soon as it can                                                                                                                                                                                                                                                                                                                                                                                        |
| Pull request is testing                                                     | Trunk merge has begun testing a pull request                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Pull request has passed tests                                               | Testing has passed on a pull request. The PR will be merged when it reached the top of the queue                                                                                                                                                                                                                                                                                                                                                                              |
| Pull request is merged                                                      | A pull request submitted to the queue has successfully been merged into its target branch                                                                                                                                                                                                                                                                                                                                                                                     |
| Pull request fails                                                          | Testing failed on a pull request and it was removed from the queue or Trunk failed to merge the PR into its target branch                                                                                                                                                                                                                                                                                                                                                     |
| Pull request is canceled                                                    | A pull request has been canceled, either manually or due to it [reaching a configured testing timeout](https://docs.trunk.io/merge-queue/set-up-trunk-merge/advanced-settings#timeout-for-tests-to-complete)                                                                                                                                                                                                                                                                  |
| Pull request failed and is waiting for PRs in front of it to finish testing | <p>A pull request failed testing, but the pull request is currently waiting before being kicked. This can happen for one of two reasons:<br>1. The pull request is not at the head of the queue, so it is waiting to determine if it is the source of the failure or if a PR it depends on is<br>2. <a href="https://docs.trunk.io/merge-queue/pending-failure-depth">Pending Failure Depth is enabled</a> and the PR is waiting for other PRs below it to finish testing</p> |
