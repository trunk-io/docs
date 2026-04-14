---
description: >-
  Keep failed PRs in the queue while successor PRs test, giving transient
  failures a chance to pass.
---

# Pending failure depth

### What it is

When a group's test run fails in the merge queue, it doesn't immediately get evicted. Instead, it enters a **Pending Failure** state — a holding state where the system hasn't yet decided whether to mark the group as failed or, if [batching](batching.md) is enabled, to bisect the batch to isolate the culprit.

{% hint style="info" %}
Throughout this page, "group" means either a batch of PRs (when [batching](batching.md) is enabled) or an individual PR (when it's not).
{% endhint %}

#### Waiting for Predecessors

A group in Pending Failure always waits for predecessor groups (the PRs ahead of it in the queue) to finish testing. This is how the system determines root cause:

* If a predecessor also failed, the current group's failure may have been caused by the predecessor. The current group will be retested once the bad predecessor is removed.
* If all predecessors passed, the failure is attributable to the current group itself.

This predecessor-waiting happens regardless of the Pending Failure Depth setting.

#### Waiting for Successors (Controlled by Pending Failure Depth)

**Pending Failure Depth** is a configuration value (integer, default 0) that controls how many levels of **successor** test runs (PRs behind the failed group in the queue) the system also waits on before transitioning the group out of the Pending Failure state.

* **When set to 0 (default):** The successor check is skipped. The group transitions as soon as the predecessor condition is met.
* **When set to a value greater than 0:** The system additionally waits for successor groups within that many hops to finish testing before transitioning.

#### Why Wait for Successors?

The value of waiting for successors depends on whether [optimistic merging](optimistic-merging.md) is enabled:

* **With optimistic merging (primary use case):** If the failure was caused by a flake rather than a real code problem, a successor further down the queue may pass its tests. Because that successor's test run includes the failed group's changes, a passing result is proof that those changes work. Optimistic merging uses this to retroactively clear the failed group and merge it. The Pending Failure Depth window gives those successors time to finish testing before the system prematurely fails or bisects the group. This is the automated [anti-flake protection](anti-flake-protection.md) path.
* **Without optimistic merging:** The hold window gives you time to manually inspect the failure and restart the test run if it looks transient, before the system auto-transitions the group to Failed (or bisection, if [batching](batching.md) is enabled). This is the only benefit without optimistic merging.

{% hint style="warning" %}
Pending Failure Depth only helps with transient (flaky) failures. For legitimate failures that propagate to successors, those successors will also fail, and the hold window expires without clearing the failure.
{% endhint %}

#### Example: Anti-Flake Protection in Action

This example shows how Pending Failure Depth works together with optimistic merging to automatically recover from a flaky failure:

<table><thead><tr><th width="331">What's Happening?</th><th>Queue</th></tr></thead><tbody><tr><td><strong>A</strong>, <strong>B</strong>, <strong>C</strong> begin predictive testing</td><td><code>main</code> &#x3C;- <strong>A</strong> &#x3C;- <strong>B</strong>+a &#x3C;- <strong>C</strong>+ba</td></tr><tr><td><strong>B</strong> fails testing (a flake)</td><td><code>main</code> &#x3C;- <strong>A</strong> &#x3C;- <mark style="color:red;"><strong>B</strong>+a</mark> &#x3C;- <strong>C</strong>+ba</td></tr><tr><td>Pending Failure Depth keeps <strong>B</strong> in the queue while <strong>C</strong> finishes testing</td><td><code>main</code> &#x3C;- <strong>A</strong> &#x3C;- <mark style="color:red;"><strong>B</strong>+a</mark> (hold) &#x3C;- <strong>C</strong>+ba</td></tr><tr><td><strong>C</strong> passes — proving <strong>B</strong>'s failure was a flake</td><td><code>main</code> &#x3C;- <strong>A</strong> &#x3C;- <mark style="color:red;"><strong>B</strong>+a</mark> &#x3C;- <mark style="color:green;"><strong>C</strong>+ba</mark></td></tr><tr><td>Optimistic merging clears <strong>B</strong> and merges <strong>A</strong>, <strong>B</strong>, <strong>C</strong></td><td><code>merge</code> <strong>A B C</strong></td></tr></tbody></table>

Without Pending Failure Depth, **B** would have been immediately evicted or bisected when its tests failed — even though the failure was transient and **C**'s passing result proves the changes work.

### Why use it

* **Automated flake recovery with optimistic merging** - When combined with [optimistic merging](optimistic-merging.md), a passing successor automatically clears a flaky failure without any manual intervention. This is the [anti-flake protection](anti-flake-protection.md) mechanism.
* **Manual inspection window without optimistic merging** - Even without optimistic merging, the hold gives you a grace period to inspect the failure and manually restart the test run if it looks transient, before the system auto-transitions the group to Failed (or bisection, if [batching](batching.md) is enabled).
* **Reduce developer disruption** - PRs that failed due to flakes are not unnecessarily evicted, so authors don't need to re-enqueue or investigate non-issues.
* **Prevent premature bisection of batches** - When [batching](batching.md) is enabled, the hold prevents the system from immediately bisecting a batch that may have only failed due to a transient issue.

### How to enable

{% hint style="info" %}
Pending Failure Depth is **set to 0 by default** (successor-waiting disabled). We recommend enabling it after you have [optimistic merging](optimistic-merging.md) configured and your basic queue setup is working.
{% endhint %}

Configure Pending Failure Depth in **Settings** > **Repositories** > your repository > **Merge Queue** > select a value from the **Pending Failure Depth** dropdown.

You can also configure it via Terraform using the `pending_failure_depth` attribute.

### Recommendations

* **Not using optimistic merging?** We don't recommend enabling Pending Failure Depth out of the box. Without optimistic merging, the only benefit is a manual inspection window, which most teams don't need.
* **Using optimistic merging?** Start with a depth of 1. This gives one successor a chance to pass and clear a flaky failure automatically.
* **Optimistic merging not kicking in as often as expected?** If you're seeing PRs get evicted for flakes that a successor _would_ have cleared — but the hold expired before the successor finished testing — increase the depth to give more successors time to complete.

### Tradeoffs and considerations

#### What you gain

* **Grace period for flake recovery** - Failed groups are held while successors finish testing, giving optimistic merging a chance to clear transient failures.
* **Fewer unnecessary evictions** - PRs that would have been evicted due to flakes can instead be automatically cleared and merged.
* **Avoids premature batch bisection** - When [batching](batching.md) is enabled, the hold prevents the system from immediately bisecting a batch that failed due to a transient issue.

#### What you give up or risk

* **Delayed failure feedback** - Legitimate failures take longer to surface because the system waits for successors to finish testing before transitioning the group. The higher the depth, the longer the wait.
* **No automatic benefit for real failures** - If the failure is legitimate (not a flake), successors that include the same broken code will also fail. The hold window expires without clearing the failure — the group transitions to Failed (or bisection) just as it would have, only later.
* **Limited value without optimistic merging** - Without optimistic merging enabled, there is no automated mechanism to clear the failure during the hold. The only benefit is the manual inspection window.

### Next Steps

* [Anti-flake protection](anti-flake-protection.md) - Understand the combined mechanism of optimistic merging + Pending Failure Depth
* [Optimistic merging](optimistic-merging.md) - The companion feature that enables automated flake clearing
* [Batching](batching.md) - How Pending Failure Depth interacts with batch groups and bisection
* [Predictive testing](predictive-testing.md) - The foundation that makes successor test runs include predecessor changes
