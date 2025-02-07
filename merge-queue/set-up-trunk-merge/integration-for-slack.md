---
description: Push updates about your queue status to Slack to keep your team informed.
---

# Integration for Slack

Trunk Merge Queue integrates with Slack to push relevant information to your team so you can stay up to date with the status of your pull requests.

## Setup Integration with Slack

After you have Merge set up and running in your repository you can set up Slack notifications. There are two ways to configure where notifications are delivered: per queue and per user. You can have all notifications from a specific Merge Queue sent to a Slack channel. You can also have notifications for PRs authored by you, regardless of which queue they are going through, sent as a DM to you.

### Merge Queue Specific Notifications

After you have Merge set up and running in your repository, you can set up your integration with Slack in `Settings > Repositories > the specific repository` with the Merge Queue.

<figure><img src="../../.gitbook/assets/enable-parallel-mode" alt=""><figcaption></figcaption></figure>

Click **Connect** to install the Trunk Slack application and receive Merge notifications in a specific channel. Once you have authorized the app to post to a channel, you will be redirected to your settings page.

<figure><img src="../../.gitbook/assets/image (45).png" alt=""><figcaption></figcaption></figure>

### User Specific Notifications

To have notifications for **PRs you authored** regardless of what Merge Queue they're going through sent **as a DM to you**, you go to `Settings > Account > Connect`

Note: For user-specific notifications you **must** have your GitHub account connected to your Slack account. The button to do this is in the `Settings > Account > Link GitHub Account` section.

<figure><img src="../../.gitbook/assets/image-6.png" alt=""><figcaption></figcaption></figure>

## Configuring Your Integration with Slack

After you have connected to a Slack channel, you can select which notifications you would like to receive. By default, all Merge notifications are enabled.

| Notification                                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Merge is updated                                  | The merge queue's configuration was changed. This covers anything that changes how the queue acts, including: pausing or draining the queue, changing its mode, changing testing concurrency, and so on.                                                                                                                                                                                                                                                                |
| Pull request is submitted for merging             | A pull request has been [submitted to the queue](https://docs.trunk.io/merge-queue/set-up-trunk-merge#submit-pull-requests)                                                                                                                                                                                                                                                                                                                                                   |
| Pull request is ready for testing                 | A pull request has been admitted to the queue and will begin testing as soon as it can                                                                                                                                                                                                                                                                                                                                                                                  |
| Pull request is testing                           | Trunk merge has begun testing a pull request                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Pull request has passed tests                     | Testing has passed on a pull request. The PR will be merged when it reached the top of the queue                                                                                                                                                                                                                                                                                                                                                                        |
| Pull request is merged                            | A pull request submitted to the queue has successfully been merged into its target branch                                                                                                                                                                                                                                                                                                                                                                               |
| Pull request fails                                | Testing failed on a pull request and it was removed from the queue or Trunk failed to merge the PR into its target branch                                                                                                                                                                                                                                                                                                                                               |
| Pull request is canceled                          | A pull request has been canceled, either manually or due to it [reaching a configured testing timeout](https://docs.trunk.io/merge-queue/set-up-trunk-merge/advanced-settings#timeout-for-tests-to-complete)                                                                                                                                                                                                                                                                  |
| Pull request is waiting for earlier pull requests | <p>A pull request failed testing, but the pull request is currently waiting before being kicked. This can happen for one of two reasons:<br>1. The pull request is not at the head of the queue, so it is waiting to determine if it is the source of the failure or if a PR it depends on is<br>2. <a href="https://docs.trunk.io/merge-queue/pending-failure-depth">Pending Failure Depth is enabled</a> and the PR is waiting for other PRs below it to finish testing</p> |
|                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
