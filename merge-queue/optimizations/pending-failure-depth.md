# Pending failure depth

### What it is

Pending failure depth allows pull requests to wait until other pull requests behind them in the queue complete testing before getting removed from the queue.

By default, a PR that fails testing will be evicted from the queue. The **Pending Failure Depth** feature allows a failed PR to remain in the queue for pull requests behind it so that testing can be finished before this eviction occurs. The number of PRs that the queue will wait for is the _Pending Failure Depth._ This depth is configurable and reflects the number of pull requests behind this one that should complete testing before eviction is assessed.

### Why use it

* **Prevent queue stalls** - When a PR fails, the queue doesn't grind to a halt. Other PRs continue testing, assuming the failure was isolated. Keeps merge velocity high even during issues.
* **Faster failure recovery** - If PR #3 fails but PR #4 fixes the issue, both can be processed quickly because they tested in parallel. Without pending failure depth, you'd wait for #3 to fail, then wait for #4 to test sequentially.
* **Optimize for your team size** - Small teams benefit from lower values (fewer wasted tests), large teams benefit from higher values (maintain throughput despite occasional failures).
* **Balance risk vs. throughput** - Tune the setting to match your team's tolerance for wasted CI resources vs. need for high queue velocity.

### How to enable

{% hint style="info" %}
Pending failure depth is **set to zero by default** and should be enabled after you're confident in your basic queue setup.
{% endhint %}

Configure Pending Failure Depth in **Settings** > **Repositories** > your repository > **Merge Queue** > select a value from the **Pending Failure Depth** dropdown.

### Configuration options

{% hint style="info" %}
Just getting started with tuning Pending Failure Depth? Try a value of 2, and work from there with your team to find the right balance.
{% endhint %}

**Start with a small value** and observe:

* If your queue frequently stalls when PRs fail → Increase value
* If you see lots of wasted test runs (many PRs test then all fail) → Decrease value
* If your CI infrastructure is constrained → Use lower value (3-4)
* If you have abundant CI capacity → Use higher value (7-10)

#### Verify it's working

When a PR fails, watch for:

* ✅ Multiple other PRs continue testing (up to your configured depth)
* ✅ Queue doesn't stop entirely
* ✅ Failed PR is removed, but others keep going

### Tradeoffs and considerations

#### What you gain

* **Queue never fully stops** - Failures don't block all subsequent PRs
* **Faster recovery** - Independent PRs can merge while others fail
* **Tunable throughput** - Adjust for your team's needs
* **Better CI utilization** - Tests keep running instead of stopping

#### What you give up or risk

* **Wasted CI resources** - PRs may test against a state that includes failing PRs, then need to retest
* **Cascading failures** - If one PR breaks something, multiple subsequent PRs might fail before the issue is caught
* **Complexity** - More PRs testing simultaneously = harder to understand queue state

#### When to decrease pending failure depth

Lower the value (3-4) if:

* **Your tests are flaky (>5% flake rate)** - Flaky tests cause false failures, leading to wasted retests
* **CI resources are expensive/limited** - Lower parallelism reduces waste
* **PRs frequently conflict** - Related changes often fail together, so testing them in parallel wastes resources
* **You're seeing excessive retests** - Many PRs testing, failing, retesting pattern

#### When to increase pending failure depth

Raise the value (7-10) if:

* **Your queue stalls frequently when PRs fail** - Low depth is blocking throughput
* **PRs are mostly independent** - Failures are isolated, not cascading
* **You have abundant CI capacity** - Waste isn't a concern
* **Large team, high PR volume** - Need parallelism to maintain velocity

#### Understanding the cost

**Example cost calculation:**

Scenario: Pending failure depth = 5, PR #101 fails testing

* PRs #102, #103, #104, #105, #106 all test against a state including #101
* All 5 fail because #101 broke something
* All 5 retest after #101 is removed
* **Wasted**: 5 test runs

**But consider:**

* Without pending failure depth, PRs would test sequentially (much slower)
* In most cases, failures ARE independent, so PRs merge successfully
* Occasional waste is preferable to frequent queue stalls

**Typical waste rate:** 5-10% of test runs are wasted retests in well-configured queues

#### Common misconceptions

* **Misconception:** "Higher pending failure depth always means faster queue"&#x20;
  * **Reality:** Too high = wasted CI resources and cascading failures. Too low = queue stalls. The sweet spot depends on your team size and test stability.
* **Misconception:** "Pending failure depth should be set to 1 to avoid waste"&#x20;
  * **Reality:** Value of 1 means queue stops on every failure (defeats the purpose of predictive testing). Start at 5 and adjust.
* **Misconception:** "This setting isn't important"&#x20;
  * **Reality:** Poorly tuned pending failure depth can either waste significant CI resources or cause frequent queue stalls. It's worth monitoring and adjusting.

### Next Steps

**Initial setup:**

1. Start with a small value (2)
2. Monitor queue behavior
3. Check metrics for wasted test runs
4. Adjust based on observations

**Optimize the value:**

* Queue stalls frequently? → Increase depth
* Excessive retests (>15%)? → Decrease depth
* Make small adjustments and observe impact

**Monitor performance:**

* [Metrics and monitoring](../administration/metrics.md) - Track retest rate and queue throughput
* Watch for patterns: Do failures cascade? Are they independent?
* Adjust pending failure depth based on data

**Combine with other optimizations:**

* [Anti-flake protection](anti-flake-protection.md) - Reduce false failures first
* [Batching](batching.md) - Understand how pending failure depth affects batch splitting
* [Predictive testing](predictive-testing.md) - Read the full explanation of how these work together

**Troubleshooting:**

* Too many wasted tests → Lower pending failure depth
* Queue stops on every failure → Increase pending failure depth
* Unclear which value to use → Start at 2, monitor for a week
