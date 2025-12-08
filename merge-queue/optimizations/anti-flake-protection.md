# Anti-flake protection

### What it is

Some CI jobs fail for reasons unrelated to a PR's code change, such as due to [flaky tests](https://trunk.io/blog/the-ultimate-guide-to-flaky-tests) or a CI runner disconnecting. These failures are usually cleared when the CI job is rerun. If a second PR that depends on the first **does** pass, it is very likely that the first PR was good and simply experienced a transient failure.&#x20;

Trunk Merge Queue can use the combination of [**Optimistic Merging** ](optimistic-merging.md)and [**Pending Failure Depth**](pending-failure-depth.md) to merge pull requests that would otherwise be rejected from the queue.

{% hint style="success" %}
If you have a lot of flaky tests in your projects, you should track and fix them with [Trunk Flaky Tests](../../flaky-tests/overview.md). Anti-flake protection helps reduce the impact of flaky tests but doesn't help you detect, track, and eliminate them.
{% endhint %}

In the video below, you can see an example of this anti-flake protection:

{% embed url="https://share.vidyard.com/watch/5YxXzJ5Szy7vP4F7awgTsc" %}
Anti-flake protection with optimistic merging + pending failure depth
{% endembed %}

<table><thead><tr><th width="331">what's happening?</th><th>queue</th></tr></thead><tbody><tr><td><strong>A</strong>, <strong>B</strong>, <strong>C</strong> begin predictive testing</td><td><code>main</code> &#x3C;- <strong>A</strong> &#x3C;- <strong>B</strong>+a &#x3C;- <strong>C</strong>+ba</td></tr><tr><td><strong>B</strong> fails testing</td><td><code>main</code> &#x3C;- <strong>A</strong> &#x3C;- <mark style="color:red;"><strong>B</strong>+a</mark> &#x3C;- <strong>C</strong>+ba</td></tr><tr><td>predictive failure depth keeps <strong>B</strong> from being evicted while <strong>C</strong> tests</td><td><code>main</code> &#x3C;- <strong>A</strong> &#x3C;- <mark style="color:red;"><strong>B</strong>+a</mark> (hold) &#x3C;- <strong>C</strong>+ba</td></tr><tr><td><strong>C</strong> passes</td><td><code>main</code> &#x3C;- <strong>A</strong> &#x3C;- <mark style="color:red;"><strong>B</strong>+a</mark> &#x3C;- <mark style="color:green;"><strong>C</strong>+ba</mark></td></tr><tr><td>optimistic merging allows <strong>A</strong>, <strong>B</strong>, <strong>C</strong> to merge</td><td><code>merge</code> <strong>A B C</strong></td></tr></tbody></table>

{% hint style="info" %}
Optimistic Merging only works when the [Pending Failure Depth](anti-flake-protection.md#pending-failure-depth) is set to **a value greater than zero**. When zero or disabled, Merge will not hold any failed tests in the queue.
{% endhint %}

### Why use it

* **Eliminate false negatives** - Flaky tests cause 20-40% of PR failures in typical pipelines. Anti-flake protection helps get these under control, so developers don't waste time investigating non-issues.
* **Maintain developer confidence** - When the queue rejects PRs for real reasons (not flaky tests), developers trust the system. Reduces "it's probably just flaky" dismissiveness of real failures.
* **Reduce manual retries** - Developers don't need to manually resubmit PRs or click "retry" when tests flake. Trunk handles it automatically, saving time and frustration.
* **Keep queue moving** - Flaky tests don't stall the queue. PRs that would have been blocked by transient failures merge successfully, increasing overall throughput.

### How to enable

{% hint style="info" %}
Anti Flake Protection is active when [**Optimistic Merge Queue**](optimistic-merging.md) is **On** and [**Pending Failure Depth**](pending-failure-depth.md) is **set to a value greater than zero**
{% endhint %}

Enable Optimistic merging in **Settings** > **Repositories** > your repository > **Merge Queue** > toggle **On** **Optimistic Merge Queue**.

Configure Pending Failure Depth in **Settings** > **Repositories** > your repository > **Merge Queue** > select a value from the **Pending Failure Depth** dropdown.

### Tradeoffs and considerations

#### What you gain

* **80-90% reduction in flaky test blocks** - Most flaky failures are caught and handled automatically
* **Developer time saved** - No manual retries or investigation of flaky failures
* **Higher queue throughput** - Flaky tests don't stall the queue
* **Better developer experience** - Less frustration with non-deterministic failures

#### What you give up or risk

* **Increased CI cost** - Retrying tests costs additional CI resources (typically 10-20% increase)
* **Slightly longer merge times** - PRs that fail then retry take longer than PRs that pass first time
* **Potential false positives** - Occasionally a legitimate failure might be retried (though Trunk is conservative)
* **Masks underlying problems** - Flaky tests indicate test quality issues; retrying treats symptom, not cause

#### When NOT to use anti-flake protection

Don't enable anti-flake protection if:

* **Your tests are not flaky (< 2% flake rate)** - No benefit, only cost
* **CI resources are extremely limited** - Retries double test costs for flaky PRs
* **You're actively fixing flaky tests** - Better to fix than to mask
* **Flaky tests indicate real issues** - Sometimes "flaky" failures reveal race conditions or timing issues in your code

#### When to use anti-flake protection

Do enable anti-flake protection when:

* **Flaky tests are blocking PRs (5-15% flake rate)** - Clear benefit outweighs cost
* **Fixing flaky tests will take time** - Use this as interim solution while improving test quality
* **Infrastructure flakiness** - Network timeouts, resource contention you can't control
* **Third-party dependencies are flaky** - External APIs or services cause transient failures

#### The right long-term solution

{% hint style="warning" %}
️ **Anti-flake protection is a band-aid, not a cure.**
{% endhint %}

**The right approach:**

1. **Enable anti-flake protection** - Unblock your team immediately
2. **Identify flaky tests** - Use CI analytics to find which tests flake most
3. **Fix the root causes** - Make tests deterministic, add retries at test level, improve infrastructure
4. **Reduce flake rate over time** - Goal should be < 2% flake rate
5. **Consider disabling** - Once tests are stable, anti-flake protection becomes unnecessary

**Red flags indicating systemic issues:**

* Flake rate > 20% (your tests are broken)
* Same tests flake repeatedly (specific tests need fixing)
* All flakes are in one area (infrastructure or test framework issue)

#### Common misconceptions

* **Misconception:** "Anti-flake protection lets me ignore flaky tests"&#x20;
  * **Reality:** NO! This is a temporary solution. Flaky tests are a code/test quality problem that must be fixed. Anti-flake protection buys you time to fix them properly.
* **Misconception:** "It retries all failures automatically"&#x20;
  * **Reality:** Trunk is selective. Only failures that match flaky patterns are retried. Legitimate failures still block PRs immediately.
* **Misconception:** "Anti-flake protection wastes tons of CI resources"&#x20;
  * **Reality:** Typical cost increase is 10-20% for teams with moderate flake rates. This is far less than the developer time wasted investigating flaky failures.
* **Misconception:** "I should set retry limit to 10 to catch all flakes"&#x20;
  * **Reality:** If you need 10 retries, your tests are catastrophically broken. Fix the tests! Retry limit should be 1-3 max.

### Next Steps

If you have a lot of flaky tests in your projects, you should track and fix them with [Trunk Flaky Tests](../../flaky-tests/overview.md). Anti-flake protection helps reduce the impact of flaky tests but doesn't help you detect, track, and eliminate them.
