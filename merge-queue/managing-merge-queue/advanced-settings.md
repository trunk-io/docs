---
description: >-
  Explanation of settings for states, timeouts, concurrency, and branch
  protection.
---

# Settings and configurations

All of the following settings are specific to individual Merge Queues and can be accessed in two ways:

* From the **Settings** menu: Navigate to `Settings > Repositories > Repo-Name > Merge Queue`&#x20;
* From the **Merge Queue** tab: Select your repository, then click the **Settings** tab

{% hint style="info" %}
Note that you must be an Organization admin to adjust any of these settings.
{% endhint %}

***

## Merge Queue state

You can change the state of your Merge Queue to control whether new PRs can enter the queue and whether tested PRs will merge. PRs already testing will always complete their tests regardless of state. Below are the possible states:

{% columns %}
{% column %}
**State**
{% endcolumn %}

{% column %}
**Will PRs Enter the Queue?**
{% endcolumn %}

{% column %}
**Will PRs Merge After Testing?**
{% endcolumn %}

{% column %}
**Example use case**
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column width="25%" %}
`Running`
{% endcolumn %}

{% column width="25%" %}
Yes :white\_check\_mark:
{% endcolumn %}

{% column %}
Yes :white\_check\_mark:
{% endcolumn %}

{% column %}
**Everyday merging:** protect your mainline and merges successful PRs.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
`Paused`
{% endcolumn %}

{% column %}
No :x:
{% endcolumn %}

{% column %}
No :x:
{% endcolumn %}

{% column %}
**CI failure recovery**: stop merges and testing in the queue until failure is resolved.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
`Draining`
{% endcolumn %}

{% column %}
No :x:
{% endcolumn %}

{% column %}
Yes :white\_check\_mark:
{% endcolumn %}

{% column %}
**Code freeze**: merge PRs currently in the queue but don't start testing additional PRs.
{% endcolumn %}
{% endcolumns %}

**Note:** The Merge Queue may automatically enter a `Switching Modes` state, which functions exactly like `Draining`. This occurs when you switch the queue mode while PRs are still being tested.

### When to change merge queue state?

The `Running` state is the default state of your merge queue, and will be the normal, day-to-day state of your queue.

`Paused` is useful for CI incident response and failure recovery. For example, if there is a test infrastructure outage, a queue can be `Paused` until recovery is complete. The ordering of PRs in the queue is preserved, but no PRs are tested or merged.

`Draining` is useful for managing events like code freezes. PRs currently in the queue will be tested and merged, but no new PRs will start testing.

***

## Merge Queue mode

> Merge Queues operate in one of two modes, **Single** (default) or [**Parallel**](../concepts-and-optimizations/parallel-queues/)**.**&#x20;

**Single Queue** processes all pull requests in one line, testing each PR predictively against all changes ahead of it. Multiple PRs can be tested and merged simultaneously based on your [Testing Concurrency](advanced-settings.md#testing-concurrency) and [Batching](advanced-settings.md#batching) settings.

**Parallel Queues** dynamically creates multiple independent testing lanes based on each PR's impacted targets (the parts of the codebase it changes). PRs affecting different parts of the code can be tested in separate lanes, reducing wait times for repositories with distinct, independently-testable components.

**Requirements for Parallel mode:**

* Requires configuring a workflow to calculate and upload impacted targets for each PR
* The queue will wait for impacted targets before processing PRs

Read more about [Trunk's implementation of Parallel merge queues](../concepts-and-optimizations/parallel-queues/), supported build systems ([Bazel](../../flaky-tests/get-started/frameworks/bazel.md), [Nx](../concepts-and-optimizations/parallel-queues/nx.md), or [custom AP](../concepts-and-optimizations/parallel-queues/api.md)I), and [what impacted targets are](../concepts-and-optimizations/parallel-queues/#what-are-impacted-targets).

***

## Testing concurrency

> Testing concurrency can be set to any value, options are **5 (average)**, **25 (high)**, **50 (very high),** and **Custom**.

Configure how many PRs may be tested in parallel. A larger number may increase throughput since more PRs are tested in parallel, but at the expense of CI since more jobs are running in parallel. When the queue is at capacity, PRs will still be submitted to it, but they will not begin testing until a PR leaves the queue.

{% hint style="info" %}
If your testing workload contains some flaky tests, a deeper queue (i.e., a higher concurrency) may struggle. Running Merge in Parallel mode can help with this, as it will reduce the average depth of your merge queue since all PRs won't be queued directly behind each other.
{% endhint %}

For example, assuming a concurrency of 3:

* At 12:00, Alice submits PR 1000 to the Merge Queue, and it starts testing.
* At 12:05, Bob submits PR 888 to the Merge Queue, and it starts testing.
* At 12:10, Charlie submits PR 777 to the Merge Queue, and it starts testing.
* At 12:15, Alice submits PR 1001 to the Merge Queue. Tests do not start because the Merge Queue is at its concurrency limit.

***

## Timeout for tests to complete

> Select the number of hours from the dropdown, default is **5 hours**.

Configure how long a PR's test can run before auto-cancelling while testing in the Merge Queue. If a long-running test is detected, Merge will automatically cancel the test.

For example, assuming a timeout of 4 hours:

* At 3:00, Bob submits PR 456 to the Merge Queue.
* At 3:05, PR 456 starts testing using Bob's CI system.
* At 7:05, Trunk cancels PR 456 since PR 456 is still testing.

***

## Optimistic Merge Queue

> Toggle this feature **Enabled** or **Disabled**. Default is **Disabled**.

[**Optimistic Merging**](../concepts/optimistic-merging.md) allows multiple PRs to merge together at once when testing completes out of order. When [Testing Concurrency](advanced-settings.md#testing-concurrency) allows multiple PRs to test simultaneously, a PR later in the queue may finish before PRs ahead of it. Since that PR's tests include all the changes ahead of it, the system can safely merge all verified PRs together instead of waiting for each one individually, reducing merge time.

***

## Pending Failure Depth

> Pending Failure Depth can be set to any value, options are **0** (default), **1**, **2**, **3**, and **Custom**.

[**Pending Failure Depth**](../concepts/pending-failure-depth.md) allows a failed PR to remain in the queue temporarily while a configurable number of PRs behind it complete testing. Since predictive testing means the failed PR's code is retested as part of later PRs, this gives flaky tests multiple chances to pass before the PR is evicted from the queue.

When set to **0** (default), failed PRs are immediately evicted from the queue. Any PRs behind the failed PR that were already testing will be restarted, since they were testing against a predicted future state of the branch that is no longer accurate.

***

## Draft pull request creation

> Toggle this feature **Enabled** or **Disabled**. Default is **Enabled**.

[**Draft PR Creation**](../set-up-trunk-merge/branch-protection-and-required-status-checks.md#draft-prs) determines whether Trunk Merge Queue creates draft PRs or push-triggered branches when testing changes. When enabled (default), the queue creates draft PRs to trigger your existing PR-based CI checks. When disabled, the queue creates `trunk-merge/` branches instead, requiring you to configure push-triggered workflows to run your required status checks.

***

## GitHub comments

> Toggle this feature **Enabled** or **Disabled**. Default is **Enabled**.

When enabled, Trunk posts comments on pull requests with merge queue status updates and instructions (e.g., "To merge this pull request, check the box to the left or comment `/trunk merge`").

**When to disable:**

* **Testing and evaluation** - Validate the merge queue works with your CI setup without notifying your development team. Once configured and ready, re-enable comments to roll out to developers.
* **Custom tooling** - You're building your own bot or integration that will provide merge queue instructions to developers, making Trunk's default comments redundant.

<figure><img src="../../.gitbook/assets/merge-github-comment (1).png" alt=""><figcaption></figcaption></figure>

***

## GitHub commands

> Toggle this feature **Enabled** or **Disabled**. Default is **Enabled**.

Whether or not GitHub slash commands like `/trunk merge` are enabled for this merge queue.

**When to disable:**

* **API-only workflows** - You want all queue submissions to go through the public API (e.g., via a bot or custom automation) rather than individual developer commands.
* **Holding pattern** - You're temporarily restricting queue submissions while investigating issues, performing maintenance, or coordinating with your team. (Note: Consider using the Paused or Draining queue state if you want to stop all new PRs from entering the queue.)

***

## Notifications

[Integrate Trunk Merge Queue with Slack ](integration-for-slack.md)to deliver real-time updates about your pull requests and queue status. You can configure notifications at two levels:&#x20;

* per-queue notifications sent to a Slack channel, or&#x20;
* per-user notifications sent as direct messages for PRs you authored.&#x20;

Customize which events trigger notifications, such as testing completion, failures, queue configuration changes, and successful merges.

***

## Batching

> Toggle this feature **Enabled** or **Disabled**. Default is **Disabled**.

[**Batching**](../concepts/batching.md) tests multiple pull requests as a single unit instead of individually, dramatically reducing CI costs.&#x20;

***

## Delete Merge Integration

{% hint style="danger" %}
CAUTION: Any queued merge requests will not be merged and all data will be lost.

**Before deleting:** Ensure all important PRs in the queue are either merged manually or that you're prepared to resubmit them to a new queue.
{% endhint %}

This setting will delete the Merge Queue configuration and any queued merge requests will not be merged and all data will be lost.

**When to use this:**

* **Switching target branches** - If you need to change which branch the queue merges into (e.g., switching from a test branch during POC to `main` for production use), you must delete the current queue and create a new one pointing to your desired branch.
* **Removing Merge Queue** - You're decommissioning Merge Queue for this repository entirely.
* **Starting fresh** - You want to reset all configuration.

