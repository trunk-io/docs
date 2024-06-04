---
description: >-
  Explanation of settings for states, timeouts, concurrency, and branch
  protection.
---

# Settings

We offer some knobs and dials when configuring Merge. All of the following settings are specific to individual Merge Queues, and can be applied can be applied at [app.trunk.io](https://app.trunk.io) in the `Settings > Repositories > Repo-Name` page.

## Merge Queue States

You can change the state of your Merge Queue, which will affect behavior around PRs entering the queue and merging. PRs will always continue testing no matter what state the Merge Queue is in. Below are the possible different states:

<table><thead><tr><th width="149">State</th><th>Will PRs Enter the Queue?</th><th>Will PRs Merge After Testing?</th></tr></thead><tbody><tr><td><code>Running</code></td><td>Yes <span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td><td>Yes <span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td></tr><tr><td><code>Paused</code></td><td>No <span data-gb-custom-inline data-tag="emoji" data-code="274c">❌</span></td><td>No <span data-gb-custom-inline data-tag="emoji" data-code="274c">❌</span></td></tr><tr><td><code>Draining</code></td><td>No <span data-gb-custom-inline data-tag="emoji" data-code="274c">❌</span></td><td>Yes <span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td></tr></tbody></table>

There is an additional state, `Switching Modes`, that functions exactly like `Draining`. The Merge Queue enters this state when you switch the mode of the queue while PRs are still testing.

## Timeout for Tests to Complete

Configure how long a PR's test can run before auto-cancelling while testing in the Merge Queue. If a long-running test is detected, Merge will automatically cancel the test.

{% hint style="info" %}
If you're unsure about what timeout to set, you can use our [CI Analytics](https://trunk.io/products/ci-analytics) to analyze the runtime of your CI.
{% endhint %}

For example, assuming a timeout of 4 hours:

* At 3:00, Bob submits PR 456 to the Merge Queue.
* At 3:05, PR 456 starts testing using Bob's CI system.
* At 7:05, Trunk cancels PR 456, since PR 456 is still testing.

## Concurrency

Configure how many PRs may test in parallel. A larger number may increase throughput, since more PRs are tested in parallel, but at the expense of CI, since more jobs are running in parallel. When the queue is at capacity, PRs will still be submitted to it, but they will not begin testing until a PR leaves the queue.

{% hint style="info" %}
If your testing workload contains some flaky tests, a deeper queue (i.e. a higher concurrency) may struggle. Running Merge in Parallel mode can help with this, as it will reduce the average depth of your merge queue, since all PRs won't be queued directly behind each other.
{% endhint %}

For example, assuming a concurrency of 3:

* At 12:00, Alice submits PR 1000 to the Merge Queue, and it starts testing.
* At 12:05, Bob submits PR 888 to the Merge Queue, and it starts testing.
* At 12:10, Charlie submits PR 777 to the Merge Queue, and it starts testing.
* At 12:15, Alice submits PR 1001 to the Merge Queue. Tests do not start, because the Merge Queue is at its concurrency limit.

## Branch Protection

Trunk Merge, since it will eventually merge your PR on GitHub, is still **bound by any protection rules set in GitHub** that affect the branch Trunk Merge will merge into or that affect your Trunk Merge branch. For example, if a PR requires at least one review to merge, then Trunk Merge would display `'not mergable GitHub yet'` until that PR has a review.

If you have trouble with merge queueing PRs, check if there is any kind of additional branch protection set up on your repo. Existing branch protection rules must be changed in order to **not** protect branches in the form of `trunk-temp/*` and `trunk-merge/*` . If either of those branches are considered protected in any way according to GitHub (e.g., if there is a `*/*` branch protection rule), then Merge will not be able to run tests properly due to GitHub permission errors.

If there are any questions or help is needed, reach out on our  questions or help is needed, reach out on our [community slack](https://slack.trunk.io/)!



###
