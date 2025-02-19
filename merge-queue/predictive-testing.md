---
description: >-
  Test pull requests with a predicted view of your stable branch by including
  all the changes in the pull requests ahead of it.
---

# Predictive Testing

The core concept of any merge queue solution is predictive testing. The idea here is to test your pull request against the head of your protected branch `main` and all the pull requests ahead of your own in the queue.  \


{% embed url="https://share.vidyard.com/watch/31gaLwGNSYTn2ec2BSQjkn" %}
test your pull request withj the changes ahead of it in the queue
{% endembed %}



<table><thead><tr><th width="331">What's Happening?</th><th>Queue</th></tr></thead><tbody><tr><td><strong>A</strong> begins testing</td><td><code>main</code> &#x3C;- <mark style="background-color:orange;"><strong>A</strong></mark></td></tr><tr><td><strong>B</strong> begins predictive testing by including the changes in <strong>A</strong></td><td><code>main</code> &#x3C;- <strong>A</strong> &#x3C;- <mark style="background-color:orange;"><strong>B</strong>+a</mark> &#x3C;- <strong>C</strong>+ba</td></tr><tr><td><strong>C</strong> begins predictive testing by including the changes in both <strong>A</strong> and B</td><td><code>main</code> &#x3C;- <strong>A</strong> &#x3C;- <strong>B+a</strong>  &#x3C;- <mark style="background-color:orange;"><strong>C</strong>+ba</mark></td></tr><tr><td>as testing completes - pull requests can merge safely</td><td><code>merge</code> <strong>A</strong>, <strong>B</strong>, <strong>C</strong></td></tr></tbody></table>

**What's the point of predictive testing?**

Normally pull requests are tested against a snapshot of the head of `main` when the pull request is posted to your source control provider. This can mean that by the time the pull request is actually merged - the results of the automated testing are stale. \
\
When you merge a pull request with stale results you are effectively merging in un-tested code. The changes to the protected branch since the test was run create a blind spot in your testing regimen. With predictive testing, you no longer have a blind spot because the merge queue ensures that the pull request is tested against the state of `main` that will exist when your pull request is merged. \
\
No blind spots === no build breakages.

