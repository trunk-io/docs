---
description: >-
  Using optimistic merging and pending-failure-depth to protect your Merge Queue
  from flaky failures
---

# Anti-Flake Protection

Sometimes, a pull request (PR) fails testing for reasons outside of the actual code change - [a test was flaky](../flaky-tests/), a CI runner was disconnected, etc..  If a second PR that depends on the first **does** pass, then it is very likely that the first PR was actually good and simply experienced a transient failure.  Trunk Merge can use the combination of [**Optimistic Merging** ](optimistic-merging.md)and [Pending Failure Depth](anti-flake-protection.md#pending-failure-depth) to merge pull requests that would otherwise be rejected from the queue. \
\
In the video below you can see an example of this anti-flake protection:

{% embed url="https://share.vidyard.com/watch/5YxXzJ5Szy7vP4F7awgTsc" %}
anti-flake protection with optimistic merging + pending failure depth
{% endembed %}

<table><thead><tr><th width="331">what's happening?</th><th>queue</th></tr></thead><tbody><tr><td><strong>A</strong>, <strong>B</strong>, <strong>C</strong> begin predictive testing</td><td><code>main</code> &#x3C;- <strong>A</strong> &#x3C;- <strong>B</strong>+a &#x3C;- <strong>C</strong>+ba </td></tr><tr><td><strong>B</strong> fails testing </td><td><code>main</code> &#x3C;- <strong>A</strong> &#x3C;- <mark style="color:red;"><strong>B</strong>+a</mark> &#x3C;- <strong>C</strong>+ba</td></tr><tr><td>predictive failure depth keeps <strong>B</strong> from  being evicted while <strong>C</strong> tests</td><td><code>main</code> &#x3C;- <strong>A</strong> &#x3C;- <mark style="color:red;"><strong>B</strong>+a</mark> (hold) &#x3C;- <strong>C</strong>+ba</td></tr><tr><td><strong>C</strong> passes </td><td><code>main</code> &#x3C;- <strong>A</strong> &#x3C;- <mark style="color:red;"><strong>B</strong>+a</mark>  &#x3C;- <mark style="color:green;"><strong>C</strong>+ba</mark></td></tr><tr><td>optimistic merging allows <strong>A</strong>, <strong>B</strong>, <strong>C</strong> to merge</td><td><code>merge</code> <strong>A B C</strong></td></tr></tbody></table>

{% hint style="info" %}
Optimistic Merging only works when the [Pending Failure Depth](anti-flake-protection.md#pending-failure-depth) is set to **a value greater than zero**. When zero or disabled, Merge will not hold any failed tests in the queue.
{% endhint %}

#### Enabling anti-flake protection

Achieve anti-flake protection works by enabling [**Optimistic Merge**](optimistic-merging.md) and setting [**Pending Failure Depth**](pending-failure-depth.md) greater than 0 in the [Merge UI](using-the-webapp.md) settings:

<figure><img src="../.gitbook/assets/pika-1715033350907-2x.png" alt=""><figcaption><p>setting to enable anti-flake protection</p></figcaption></figure>

**The Fine Print**\
There is a small tradeoff to be made when optimistic merging is used. You can get into a situation where an actually broken test in say change 'B' is corrected by a change in 'C'. In this case if you later reverted 'C' your build would be broken.&#x20;
