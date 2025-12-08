# Batching

### What it is

Batching allows Trunk Merge Queue to test multiple pull requests together as a single unit, rather than testing them one at a time.&#x20;

When batching is enabled, Trunk intelligently groups compatible PRs and runs your test suite once for the entire batch. If the batch passes, all PRs in the batch merge together, dramatically reducing total test time.

### Why use it

* **Reduce total test time by 60-80%** - Instead of running your full test suite 10 times for 10 PRs, you run it 2-3 times for the same PRs grouped into batches. More PRs merged with less CI time.
* **Increase merge throughput** - Process 3-5x more PRs per hour compared to testing individually. A queue that handled 20 PRs/hour can now handle 60-100 PRs/hour with batching.
* **Lower CI costs** - Fewer test runs means lower CI/CD infrastructure costs. Teams report 50-70% reduction in CI minutes consumed by merge queue testing.
* **Faster time-to-production** - PRs spend less time waiting in queue. What used to take hours can now take minutes, getting features and fixes to production faster.

### How to enable

{% hint style="info" %}
Batching is **disabled by default** and must be explicitly enabled.
{% endhint %}

Batching is enabled in the Merge Settings of your repo at **Settings** > **Repositories** > your repository > **Merge Queue** > **Batching** and toggle batching **On**.

### Configuration options

With Batching enabled, you can configure two options:

* **Maximum wait time** - The maximum amount of time the Merge Queue should wait to fill the target batch size before beginning testing. A higher maximum wait time will cause the Time-In-Queue metric to increase but have the net effect of reducing CI costs per pull request.
* **Target batch size** - The largest number of entries in the queue that will be tested in a single batch. A larger target batch size will help reduce CI cost per pull request but require more work to be performed when progressive failures necessitate bisection.

{% hint style="info" %}
A good place to start is with the defaults, Maximum wait time set to 0 (zero) and Target batch size set to 5.
{% endhint %}

### Fine tuning batch sizes

**Signs your batch size is too large:**

* Batches frequently fail and need to be split
* Long wait times to form full batches
* Test suite times out or becomes unstable

**Signs your batch size is too small:**

* Not seeing significant throughput improvement
* Batches form immediately (could handle more PRs)
* Still consuming lots of CI resources

**Optimal batch size depends on:**

* Test suite speed (faster tests = larger batches)
* Test stability (more flaky tests = smaller batches)
* PR submission rate (more PRs = larger batches)

### Tradeoffs and considerations

The downsides here are very limited. Since batching combines multiple pull requests into one, you essentially give up the proof that every pull request in complete isolation can safely be merged into your protected branch.&#x20;

In the unlikely case that you have to revert a change from your protected branch or do a rollback, you will need to retest that revert or submit it to the queue to ensure nothing has broken. In practice, this re-testing is required in almost any case, regardless of how it was originally merged, and the downsides are fairly limited.

#### Common misconceptions

* **Misconception:** "Batching merges multiple PRs into a single commit"&#x20;
  * **Reality:** No! Each PR is still merged as a separate commit. Batching only affects testing, not merging.
* **Misconception:** "If a batch fails, all PRs in the batch fail"&#x20;
  * **Reality:** Trunk automatically splits the batch and retests to identify only the failing PR(s). Passing PRs still merge.
* **Misconception:** "Batching always makes the queue faster"&#x20;
  * **Reality:** Batching is most effective with stable tests and high PR volume. For low-traffic repos or flaky tests, the overhead may outweigh benefits.

### Related features

Batching works exceptionally well with these optimizations:

**Predictive testing** - Batching builds on predictive testing. Batches are tested against the projected future state of main, just like individual PRs. These features complement each other perfectly.

**Optimistic merging** - While a batch is testing, the next batch can begin forming and testing optimistically. Combining batching with optimistic merging provides maximum throughput. Configure both for best results.

**Pending failure depth** - When a batch fails and is being split/retested, pending failure depth controls how many other PRs can test simultaneously. Higher pending failure depth helps maintain throughput during batch failures.

**Anti-flake protection** - Essential companion to batching. Reduces false batch failures caused by flaky tests, making batching more reliable and efficient.

### Batching + Optimistic Merging and Pending Failure Depth

Enabling batching along with Pending Failure Depth and Optimistic Merging can help you realize the major cost savings of batching while still reaping the [anti-flake](anti-flake-protection.md) protection of optimistic merging and pending failure depth.

{% embed url="https://share.vidyard.com/watch/BsPi6f1KHvsa6wE18ySAJf" %}
example of testing pull requests in batches of 3
{% endembed %}

<table><thead><tr><th width="331">event</th><th>queue</th></tr></thead><tbody><tr><td>Enqueue <strong>A</strong>, <strong>B</strong>, <strong>C, D, E, F, G</strong></td><td><code>main</code> &#x3C;- <strong>ABC</strong> &#x3C;- <strong>DEF</strong> +abc</td></tr><tr><td>Batch ABC fails</td><td><code>main</code> &#x3C;- <mark style="color:red;"><strong>ABC</strong></mark></td></tr><tr><td>pending failure depth keeps <strong>ABC</strong> from being evicted while <strong>DEF</strong></td><td><code>main</code> &#x3C;- <mark style="color:red;"><strong>ABC</strong></mark> (hold) &#x3C;- <strong>DEF</strong>+abc</td></tr><tr><td><strong>DEF</strong> passes</td><td><code>main</code> &#x3C;- <mark style="color:red;"><strong>ABC</strong></mark> &#x3C;- <mark style="color:green;"><strong>DEF</strong>+abc</mark></td></tr><tr><td>optimistic merging allows <strong>ABC</strong> and <strong>DEF</strong> to merge</td><td><code>merge</code> <strong>ABC</strong>, <strong>DEF</strong></td></tr></tbody></table>

Combined, Pending Failure Depth, Optimistic Merging, and Batching can greatly improve your CI performance because now Merge can optimistically merge whole batches of PRs with far less wasted testing.

### Next steps

**Start with batching:**

1. Enable batching with conservative settings (batch size: 3-5)
2. Monitor for a few days and observe behavior
3. Gradually increase batch size as you gain confidence
4. Check [Metrics and monitoring](../administration/metrics.md) to measure impact

**Optimize further:**

* [Optimistic merging](optimistic-merging.md) - Combine with batching for maximum throughput
* [Anti-flake protection](anti-flake-protection.md) - Reduce false batch failures
* [Pending failure depth](pending-failure-depth.md) - Tune behavior during batch failures

**Monitor performance:**

* [Metrics and monitoring](../administration/metrics.md) - Track throughput improvements and CI cost savings
* Watch batch failure rate (should be <10%)
* Measure time-to-merge improvements

**Troubleshoot issues:**

* If batches fail frequently → Lower batch size or enable [Anti-flake protection](anti-flake-protection.md)
* If not seeing improvements → Check PR volume and test stability
* For detailed help → [Troubleshooting](../reference/troubleshooting.md)
