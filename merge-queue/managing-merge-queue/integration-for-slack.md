---
description: >-
  Push updates about your queue status to a slack channel to keep your team
  informed.
---

# Integration for Slack

Trunk Merge Queue integrates with Slack to push relevant information to a specified slack channel so you can stay up to date with the status of your pull requests.

## Setup integration with Slack

After you have Merge Queue set up and running in your repository, you can set up Slack notifications to get alerts on a variety of actions.

### Merge Queue specific notifications

After you have Merge set up and running in your repository, you can set up your integration with Slack in `Settings > Repositories > the specific repository > Merge Queue`&#x20;

<figure><img src="../../.gitbook/assets/image (44).png" alt=""><figcaption></figcaption></figure>

Click **Connect** to install the Trunk Slack application and receive Merge Queue notifications in a specific channel. Once you have authorized the app to post to a channel, you will be redirected to your settings page.

<figure><img src="../../.gitbook/assets/image (48).png" alt=""><figcaption></figcaption></figure>

## Configuring your integration with Slack

After you have connected to a Slack channel, you can select which notifications you would like to receive. By default, all Merge notifications are enabled.

| Notification                                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Merge is updated                                  | The merge queue's configuration was changed. This covers anything that changes how the queue acts, including: pausing or draining the queue, changing its mode, changing testing concurrency, and so on.                                                                                                                                                                                                                                                                      |
| Pull request is submitted for merging             | A pull request has been [submitted to the queue](https://docs.trunk.io/merge-queue/set-up-trunk-merge#submit-pull-requests)                                                                                                                                                                                                                                                                                                                                                   |
| Pull request is ready for testing                 | A pull request has been admitted to the queue and will begin testing as soon as it can                                                                                                                                                                                                                                                                                                                                                                                        |
| Pull request is testing                           | Trunk merge has begun testing a pull request                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Pull request has passed tests                     | Testing has passed on a pull request. The PR will be merged when it reached the top of the queue                                                                                                                                                                                                                                                                                                                                                                              |
| Pull request is merged                            | A pull request submitted to the queue has successfully been merged into its target branch                                                                                                                                                                                                                                                                                                                                                                                     |
| Pull request fails                                | Testing failed on a pull request and it was removed from the queue or Trunk failed to merge the PR into its target branch                                                                                                                                                                                                                                                                                                                                                     |
| Pull request is canceled                          | A pull request has been canceled, either manually or due to it [reaching a configured testing timeout](https://docs.trunk.io/merge-queue/set-up-trunk-merge/advanced-settings#timeout-for-tests-to-complete)                                                                                                                                                                                                                                                                  |
| Pull request is waiting for earlier pull requests | <p>A pull request failed testing, but the pull request is currently waiting before being kicked. This can happen for one of two reasons:<br>1. The pull request is not at the head of the queue, so it is waiting to determine if it is the source of the failure or if a PR it depends on is<br>2. <a href="https://docs.trunk.io/merge-queue/pending-failure-depth">Pending Failure Depth is enabled</a> and the PR is waiting for other PRs below it to finish testing</p> |
|                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
