# Optimistic merging

### What it is

Optimistic merging allows pull requests that fail tests to still get merged if pull requests behind them in the queue pass _their_ tests. The assumption is that the queue has proof that while one specific PR might fail tests, it passes them when combined with a pull request that is going to merge soon behind it.

The foundation of our merge queue starts with [predictive testing](/broken/pages/BAKgbuxqWos5o4kna99T). When a predictive test is being run, concurrent tests sometimes finish before the work ahead of it. This creates a situation where the system knows that all code ahead of it collectively `passes` tests, and it is safe to merge all those changes into your protected branch (`main)`.\
\
With optimistic merging enabled, we can leverage results from pull requests later in the queue to merge faster. In the illustration below you can see that pull request 'c' includes the verified testing results of pull requests 'b' and 'a'. As soon as 'c' passes testing, we can safely merge 'a', 'b', and 'c' and know they will all work correctly together.

{% embed url="https://share.vidyard.com/watch/5iy2KdNFKHM1Nc13zDv8g8?" %}
Optimistic merging to merge faster
{% endembed %}

### Why use it

* **Eliminate idle time** - The queue doesn't sit idle waiting for merges to complete. As soon as a PR enters the "merging" phase, the next PR begins testing. Result: 20-30% reduction in average PR wait time.
* **Increase throughput** - More PRs can be in-flight simultaneously. Queues using optimistic merging process 1.5-2x more PRs per hour compared to sequential testing.
* **Faster time-to-production** - PRs merge faster because they don't wait for the previous PR to fully complete. What used to take 30 minutes might now take 20 minutes.
* **Better resource utilization** - Your CI infrastructure isn't sitting idle between tests. Continuous testing means more efficient use of your CI capacity.

### How to enable

{% hint style="info" %}
Optimistic merging is **disabled by default** and should be enabled after you're confident in your basic queue setup.
{% endhint %}

Enable Optimistic merging in **Settings** > **Repositories** > your repository > **Merge Queue** > toggle **On** **Optimistic Merge Queue**.

#### Verify it's working

After enabling, watch your queue:

* ✅ Multiple PRs should show "Testing" status simultaneously
* ✅ New PR starts testing before previous PR shows "Merged"
* ✅ In your CI, you'll see overlapping test runs

**Start conservative:** Enable optimistic merging after you've validated basic queue functionality. Don't enable it on day one.

### Tradeoffs and considerations

The downsides here are very limited. You essentially give up the proof that every pull request in complete isolation can safely be merged into your protected branch.&#x20;

In the unlikely case that you have to revert a change from your protected branch, you will need to retest that revert or submit it to the queue to ensure nothing has broken. In practice, this re-testing is required in almost any case, regardless of how it was originally merged, and the downsides are fairly limited.

#### What you gain

* **faster average merge time** - Less idle time between tests
* **higher throughput** - More PRs processing simultaneously
* **Better CI utilization** - Continuous testing instead of start-stop
* **Faster incident response** - Critical PRs merge quicker

#### What you give up or risk

* **Wasted CI on retests (rare)** - If an optimistically-tested PR needs to retest, you've used some CI resources unnecessarily
* **More complex queue state** - Multiple PRs in "testing" can be confusing initially
* **Requires stable tests** - Flaky tests cause more retests with optimistic merging

#### When NOT to use optimistic merging

Don't enable optimistic merging if:

* **Your tests are highly flaky (>5% flake rate)** - Retests will negate the benefits
* **Your queue is rarely busy** - If you only have 1-2 PRs per hour, there's nothing to optimize
* **You're still learning the queue** - Get comfortable with basic functionality first
* **Your merges frequently fail** - If PRs often fail during merge (not testing), optimistic assumptions will be wrong often

#### Best practices

**Start without it:** Use Trunk Merge Queue for a week or two before enabling optimistic merging. Understand normal flow first.

**Enable when stable:** Once your queue is working reliably and you have consistent PR volume, optimistic merging provides significant benefits.

**Combine with other optimizations:** Optimistic merging works best alongside:

* [Batching](batching.md) - Test batches optimistically
* [Predictive testing](predictive-testing.md) - Required foundation for optimistic merging
* [Anti-flake protection](/broken/pages/eP3tevVEeuSPwyO2f6yo) - Reduces unnecessary retests

#### Common misconceptions

* **Misconception:** "Optimistic merging is risky - it might merge broken code"&#x20;
  * **Reality:** No! Trunk still requires all tests to pass. Optimistic merging only affects _when_ testing starts, not _whether_ testing happens. Safety is never compromised.
* **Misconception:** "Optimistic merging causes lots of wasted retests"&#x20;
  * **Reality:** Retests are rare (< 5% of PRs in typical queues). The throughput gains far outweigh the occasional retest cost.
* **Misconception:** "I should enable every optimization immediately"&#x20;
  * **Reality:** Start with just predictive testing. Add batching once stable. Add optimistic merging last. Build confidence in each layer.

### Next Steps

**Before enabling optimistic merging:**

1. Ensure basic queue is working well
2. Verify test stability (< 5% flake rate recommended)
3. Enable [Anti-flake protection](anti-flake-protection.md) first
4. Check that you have consistent PR volume

**After enabling:**

* [Metrics and monitoring](../administration/metrics.md) - Track throughput improvements
* Watch for retest rate (should be < 5%)
* Measure time-to-merge improvements

**Optimize further:**

* [Batching](batching.md) - Combine with optimistic merging for maximum effect
* [Pending failure depth](pending-failure-depth.md) - Fine-tune simultaneous testing behavior

**Troubleshooting:**

* If seeing frequent retests → Check test stability or disable temporarily
* If not seeing improvements → Check PR volume and queue activity
* For detailed help → [Troubleshooting](../reference/troubleshooting.md)
