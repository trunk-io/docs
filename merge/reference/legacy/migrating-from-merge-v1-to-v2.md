---
description: >-
  An explanation of how to move an older Trunk merge queue to the latest and
  greatest.
---

# Migrating From Merge V1 To V2

{% hint style="info" %}
This article only applies to customers currently using an older Trunk  merge queue. Older versions will not have a "Graph" tab in the Merge UI, as seen below - if you do not have this tab, you are running on Merge V1. A banner will also show up on the Merge UI alerting you to this planned migration if you are on Merge V1.
{% endhint %}

<figure><img src="../../../.gitbook/assets/image (2).png" alt=""><figcaption><p>Trunk Merge Queues that do not show the "Graph" tab on the UI are currently using a V1 Merge Queue.</p></figcaption></figure>

{% hint style="warning" %}
On **July 20th, 2024**, Trunk will migrate all merge queues created before November 16th, 2023. Below details this process and how to manually migrate your own merge queue.
{% endhint %}

## Background

On November 16th, 2023, Trunk released a newer version of Merge that supports a wide range of newer features, like:

1. [Parallel mode](https://docs.trunk.io/merge#single-mode-vs.-parallel-mode) to dynamically create queues only for PRs that affect each other (no more README changes waiting behind backend changes)
2. [PR Prioritization](https://docs.trunk.io/merge/pr-prioritization) to get the PRs that matter tested and merged faster
3. [Anti-flake Protection](https://docs.trunk.io/merge/anti-flake-protection) to stop random false failures from wreaking havoc on your merge times and CI
4. [Batching](https://docs.trunk.io/merge/batching) to group multiple PRs together to handle high throughputs and cut down on CI costs

Merge queues created before this date will not be able to access these features.

## Does This Apply To Me?

As noted above, this only applies to you if you cannot see the "Graph" tab in the Merge UI.&#x20;

## What Do I Need To Do?

If you do nothing, Trunk will automatically migrate you over on July 20th, 2024 and everything will continue to run as expected after that.

If you wish to migrate yourself over before this date, you can do so by deleting and re-creating your merge queue:

1. Ensure your merge queue is empty and [pause](https://docs.trunk.io/merge/legacy/configuration#paused-running) it.
   1. This is to make sure that no pull requests get submitted to the queue while you are performing these steps
2. Delete the merge queue from the settings page for your repo
3. Go back to the Merge tab for your repository and re-create it. Select "Single" mode, as that matches exactly how your older merge queue operated and does not require additional setup
4. If your merge queue is currently sending slack notifications to a specific channel, you will need to reconnect your merge queue to slack. The process for doing this is no different than when this was initially set up for your mergequeue, and can be found [here](https://docs.trunk.io/merge/set-up-trunk-merge/integration-for-slack#merge-queue-specific-notifications)

If you have any questions, reach out on our [slack](https://join.slack.com/t/trunkcommunity/shared\_invite/zt-2ij902iie-QeVEgHfyIJP76XdlFuJz5g)!
