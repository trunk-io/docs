---
description: >-
  Test pull requests with a predicted view of your stable branch by including
  all the changes in the pull requests ahead of it.
---

# Predictive testing

The core concept of any merge queue solution is **predictive testing**. The idea here is to test your pull request against the head of your protected branch (e.g. `main` , `master`, `dev`) and all the pull requests ahead of your own in the queue. &#x20;

### What's Happening? The "Happy Path"

This example shows how pull requests (PRs) are tested in a queue. PR `B` is tested with the changes from `A`, and `C` is tested with the changes from both `A` and `B`.

{% embed url="https://share.vidyard.com/watch/31gaLwGNSYTn2ec2BSQjkn" %}
Test your pull request with the changes ahead of it in the queue
{% endembed %}

<table><thead><tr><th width="331">What's Happening?</th><th>Queue</th></tr></thead><tbody><tr><td><strong>A</strong> begins testing</td><td><code>main</code> &#x3C;- <mark style="background-color:orange;"><strong>A</strong></mark></td></tr><tr><td><strong>B</strong> begins predictive testing by including the changes in <strong>A</strong></td><td><code>main</code> &#x3C;- <strong>A</strong> &#x3C;- <mark style="background-color:orange;"><strong>B</strong>+a</mark> &#x3C;- <strong>C</strong>+ba</td></tr><tr><td><strong>C</strong> begins predictive testing by including the changes in both <strong>A</strong> and B</td><td><code>main</code> &#x3C;- <strong>A</strong> &#x3C;- <strong>B+a</strong>  &#x3C;- <mark style="background-color:orange;"><strong>C</strong>+ba</mark></td></tr><tr><td>as testing completes - pull requests can merge safely</td><td><code>merge</code> <strong>A</strong>, <strong>B</strong>, <strong>C</strong></td></tr></tbody></table>

#### **What's the point of predictive testing?**

Normally, pull requests are tested against a snapshot of the head of `main` when the pull request is posted to your source control provider. This can mean that by the time the pull request is actually merged - the results of the automated testing are **stale**. \
\
When you merge a pull request with stale results, you are effectively merging in **un-tested code**. The changes to the protected branch since the test was run create a blind spot in your testing regimen. With predictive testing, you no longer have a blind spot because the merge queue ensures that the pull request is tested against the state of `main` that will exist when your pull request is merged.&#x20;

### The "Unhappy Path": How the Queue Handles Test Failures

Predictive testing is powerful, but it creates a new challenge: **failure cascades**.

In the "Happy Path" example, if PR `A` introduces a failing test, the predictive tests for `B` and `C` are _also_ guaranteed to fail, because they both include the broken code from `A`.

A simple queue would kick `B` and `C` as soon as their tests failed. This would disrupt their authors, who did nothing wrong, and force them to restart their PRs multiple times, wasting valuable CI time .

This is solved by **Pending Failure**.

#### How Pending Failure Works

The main purpose of "pending failure" is to **minimize disruptions to the queue** by intelligently finding the _**true**_ source of a failure.

Instead of immediately kicking a PR just because its test run failed, the queue follows this logic:

1. **A Test Fails**: Let's say PR `C`'s test run fails.
2. **Enter** `Pending Failure` **State**: `C` is _not_ kicked. It enters a `Pending Failure` state and _waits_ for the PRs it depends on (`A` and `B`) to finish testing.
3. **Identify the Root Cause:** The queue's goal is to determine: "Did this PR fail because of its own code, or did it fail because of a change in a PR ahead of it?".
   * `C` (failed) waits for `B`.
   * `B` (also fails) waits for `A`.
   * When `A` (at the top of the queue) fails, the queue knows it _must_ be the PR that introduced the failure, as it only depends on `main`.
4. **Minimize Disruption:** The queue only kicks the first faulty PR (`A`).
5. **Automatic Recovery:** PRs `B` and `C` (which are likely healthy) stay in the queue. They are automatically re-scheduled for testing with a new predicted state that _excludes_ the bad PR (e.g., `B` now tests against `main`, and `C` tests against `main + B`).

**Pending Failure** is the essential recovery mechanism that makes **Predictive Testing** practical. It ensures the queue is resilient and that engineers are not disrupted by test failures they didn't cause.

