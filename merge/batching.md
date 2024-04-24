---
description: Speed up your testing and merging workflow with Merge Batching
---

# Batching

Normally, even when PRs depend on each other, they are always tested and merged individually. In a high velocity codebase it can make more sense to group PRs into batches. This is called Batching.

{% hint style="info" %}
Note that batching only works when Merge is set to single queue mode.
{% endhint %}

## Without Batching

Without batching enabled, Merge will test PRs individually in order. For example, suppose we have a queue with four PRs called A, B, C, and D that is set to test four PRs at a time (in other words, has a [concurrency](https://docs.trunk.io/merge/set-up-trunk-merge/advanced-settings#concurrency) of 4):

**main <- A <- B <- C <- D**

A, B, C, and D will all begin testing individually. For D to merge, A, B, and C must pass and merge themselves (or be kicked from the queue when they fail).&#x20;

In this scenario, it is highly likely that the same tests will be run multiple times, once for each PR.  Additionally, if A, B, or C fails, it will cause other PRs in the queue to restart.

## With Batching

Merge will group PRs together into Batches based on the **Minimum Batch Size**. In the example above, if the **batch size** was set to **4** then all of the PRs would be grouped into a single branch and tested as a whole, resulting in 1/4th the testing work.

**main <- ABCD**

### Batch Size and Timeouts

The Target Batch Size controls how many PRs merge puts into a single batch.  When batches are enabled Merge will wait until the batch is filled before processing any of the PRs. For example: if the target batch size was set to 4 with the PRs A, B, C the queue would look like this

**main <- A <- B <- C**&#x20;

Merge will not create a batch until a fourth PR comes in. Since this could be a while, you can set a **Maximum Wait Time.** Merge will wait up until the wait time, and then will process the partially filled batch.

## Handling Failures

If a batch fails then Merge will move the batch to a separate queue for bisection analysis.  In this queue the batch will be split in various ways and tested in isolation in order to determine the PRs in the batch that introduced the failure. PRs that pass this way will be moved back to the main queue for re-testing. PRs that are believed to have caused the failure are kicked from the queue.

### Optimistic Merging and Pending Failure Depth

{% hint style="info" %}
The [_Optimistic Merging_](optimistic-merging.md#optimistic-merging) and [_Pending Failure Depth_](optimistic-merging.md#pending-failure-depth) features of Merge work together to make batching much more performant.
{% endhint %}

The **Pending Failure Depth** makes the queue hold onto failed PRs before kicking them out of the queue. **Optimistic Merging** makes the queue merge a failed PR if the one after it succeeds. These features apply to both batches and individual PRs.

For example: suppose the batch size is set to 4, Optimistic Merging is enabled, and the Pending Failure Depth is set to 1.  There are eight PRs in the queue like this:

**main <- A <- B <- C <- D <- E <- F <- G <- H**

With batching the queue will be converted into two batches.

**main <- ABCD <- EFGH**

Now suppose **ABCD** fails. Because Pending Failure Depth is set to 1 the batch stays in the queue until **EFGH** is tested.

If **EFGH** fails then both will be kicked from the queue. However, if **EFGH** passed then **ABCD** was probably a transient failure. With Optimistic Merging turned on, both ABCD and EFGH will be merged.

These two features apply to the main queue as well as the bisection queue.

Combined, Pending Failure Depth, Optimistic Merging, and Batching can greatly improve your CI performance because now Merge can optimistically merge whole batches of PRs, with far less wasted testing.



## Enable Batching

Batching is enabled in the Merge Settings of your repo in the [Trunk webapp](https://app.trunk.io/).

<figure><img src="../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>





