---
description: Speed up your testing and merging workflow with Merge Batching
---

# Batching

Batching allows multiple pull requests in the queue to be tested as a single unit. Given the same CI resources, a system with batching enabled can achieve higher throughput while also reducing the net amount of CI time spent per pull request. \
\
By enabling batching, the cost per pull request in the Merge Queue can be reduced by almost 90%. For example, in the table below, you can see how batching affects the amount spent testing pull requests in the queue.&#x20;

{% embed url="https://share.vidyard.com/watch/BsPi6f1KHvsa6wE18ySAJf" %}
example of testing pull requests in batches of 3
{% endembed %}

<table><thead><tr><th data-type="number">Batch Size</th><th width="323">Pull Requests</th><th>Testing Cost</th><th>Savings</th></tr></thead><tbody><tr><td>1</td><td><strong>A</strong>, <strong>B</strong>, <strong>C</strong>, <strong>D</strong>, <strong>E</strong>, <strong>F</strong>, <strong>G</strong>, <strong>H, I, J, K, L</strong></td><td><code>12x</code></td><td>0%</td></tr><tr><td>2</td><td><strong>AB, CD, EF, GH, IJ</strong></td><td><code>6x</code></td><td>50%</td></tr><tr><td>4</td><td><strong>ABCD</strong>, <strong>EFGH, IJKL</strong></td><td><code>3x</code></td><td>75%</td></tr><tr><td>8</td><td><strong>ABCDEFGH, IJKL</strong></td><td><code>1.5x</code></td><td>87.5%</td></tr><tr><td>12</td><td><strong>ABCDEFGHIJKL</strong></td><td><code>1x</code></td><td>92%</td></tr></tbody></table>

#### Configuring Batching

The behavior of batching is controlled by two settings in the Merge Queue:\
\
**Target Batch Size:** The largest number of entries in the queue that will be tested in a single batch. A larger target batch size will help reduce CI cost per pull request but require more work to be performed when progressive failures necessitate bisection.\
\
**Maximum Wait Time:** The maximum amount of time the Merge Queue should wait to fill the target batch size before beginning testing. A higher maximum wait time will cause the Time-In-Queue metric to increase but have the net effect of reducing CI costs per pull request.

<table><thead><tr><th>Time (mm:ss)</th><th width="323">Batching 4;  Maximum Wait 5 minutes</th><th>Testing</th></tr></thead><tbody><tr><td>00:00</td><td><strong>enqueue A</strong></td><td><code>----</code></td></tr><tr><td>01:00</td><td><strong>enqueue B</strong></td><td><code>----</code></td></tr><tr><td>02:30</td><td><strong>enqueue C</strong></td><td><code>----</code></td></tr><tr><td>05:00</td><td>5 min maximum wait time reached</td><td><code>Begin testing ABC</code></td></tr></tbody></table>

#### What happens when a batch fails testing?

If a batch fails, Trunk Merge will move it to a separate queue for bisection analysis. In this queue, the batch will be split in various ways and tested in isolation to determine the PRs in the batch that introduced the failure. PRs that pass this way will be moved back to the main queue for re-testing. PRs that are believed to have caused the failure are kicked from the queue.

#### Batching + Optimistic Merging and Pending Failure Depth

By enabling batching along with [pending failure depth](pending-failure-depth.md) and [optimistic merging](optimistic-merging.md) you can realize the major cost savings of batching while still reaping the [anti-flake ](anti-flake-protection.md)protection of optimistic merging and pending failure depth.\


<table><thead><tr><th width="331">event</th><th>queue</th></tr></thead><tbody><tr><td>Enqueue  <strong>A</strong>, <strong>B</strong>, <strong>C, D, E, F, G</strong></td><td><code>main</code> &#x3C;- <strong>ABC</strong> &#x3C;- <strong>DEF</strong> +abc </td></tr><tr><td>Batch ABC fails</td><td><code>main</code> &#x3C;- <mark style="color:red;"><strong>ABC</strong></mark></td></tr><tr><td>pending failure depth keeps <strong>ABC</strong> from  being evicted while <strong>DEF</strong></td><td><code>main</code> &#x3C;- <mark style="color:red;"><strong>ABC</strong></mark> (hold) &#x3C;- <strong>DEF</strong>+abc</td></tr><tr><td><strong>DEF</strong> passes</td><td><code>main</code> &#x3C;- <mark style="color:red;"><strong>ABC</strong></mark>  &#x3C;- <mark style="color:green;"><strong>DEF</strong>+abc</mark></td></tr><tr><td>optimistic merging allows <strong>ABC</strong> and <strong>DEF</strong> to merge</td><td><code>merge</code> <strong>ABC</strong>, <strong>DEF</strong></td></tr></tbody></table>

Combined, Pending Failure Depth, Optimistic Merging, and Batching can greatly improve your CI performance because now Merge can optimistically merge whole batches of PRs, with far less wasted testing.

**What are the risks of batching?**

The downsides here are very limited. Since batching combines multiple pull requests into one, you essentially give up the proof that every pull request in complete isolation can safely be merged into your protected branch. In the unlikely case that you have to revert a change from your protected branch or do a rollback, you will need to retest that revert or submit it to the queue to ensure nothing has broken. In practice, this re-testing is required in almost any case, regardless of how it was originally merged, and the downsides are fairly limited.

## Enable Batching

Batching is enabled in the Merge Settings of your repo in the [Trunk webapp](https://app.trunk.io/).

<figure><img src="../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>





