---
description: >-
  Information on all the different ways Merge can be configured to fit your
  needs.
layout:
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: false
  outline:
    visible: false
  pagination:
    visible: true
---

# Configuration

We offer some knobs and dials when configuring Merge. All of the following settings are specific to individual Merge graphs, and can be applied can be applied at [app.trunk.io](https://app.trunk.io) in the Settings > Repositories > Repo-Name page.

### Graph State

You can change the state of your Merge graph, which will affect behavior around PRs entering the graph and merging. PRs will always continue testing no matter what state the Merge graph is in. Below are the possible different states:

<table><thead><tr><th width="149">State</th><th>Will PRs Enter the Graph?</th><th>Will PRs Merge After Testing?</th></tr></thead><tbody><tr><td><code>Running</code></td><td>Yes <span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td><td>Yes <span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td></tr><tr><td><code>Paused</code></td><td>No <span data-gb-custom-inline data-tag="emoji" data-code="274c">❌</span></td><td>No <span data-gb-custom-inline data-tag="emoji" data-code="274c">❌</span></td></tr><tr><td><code>Draining</code></td><td>No <span data-gb-custom-inline data-tag="emoji" data-code="274c">❌</span></td><td>Yes <span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td></tr></tbody></table>

There is an additional state, `Switching Modes`, that functions exactly like `Draining`. The Merge graph enters this state when you switch the mode of the graph while PRs are still testing.

### Supported Modes

Merge can support two different modes - `Queue` and `Graph` mode. The mode affects how PRs are enqueued when they enter the graph and what is required for a PR to begin testing.

#### Graph Mode

In this mode, when PR is submitted to the Merge graph, you will also be required to provide a list of list of impacted targets that result from code changes in the PR (see [impacted-targets.md](impacted-targets.md "mention") for more details as well as how to generate the list of impacted targets). The graph will then examine the provided list of impacted targets for all PRs in the graph and only make your PR depend in the other PRs it actually affects.

For example, the following PRs:

* PR 1 with impacted target list `[src/protos/]`
* PR 2 with impacted target list `[src/user_service/, src/protos/]`
* PR 3 with impacted target list `[docs/]`

Would look like this in the Merge graph in `Graph` mode

<figure><img src="../.gitbook/assets/image (19).png" alt="" width="332"><figcaption></figcaption></figure>

#### Queue Mode

In this mode, PRs will always be queued directly behind one another, regardless of what parts of code your PR actually affects. Uploading impacted targets is not required in this mode.

For example, the above 3 PRs would look like this in the Merge graph in `Queue` mode

<figure><img src="../.gitbook/assets/image (20).png" alt=""><figcaption></figcaption></figure>

#### Switching Modes

Merge can be swapped between `Graph` and `Queue` mode at any time. If there are no PRs in the graph when switching, the switch will be immediate. If there are PRs in the graph, then Merge will go into the `Switching Modes` state, where it'll wait for all currently testing PRs to merge before switching modes. During this time, PRs will not be able to enter the graph.

### Timeout for Tests to Complete

Configure how long a PR's test can run before auto-cancelling while testing in the Merge graph. If a long-running test is detected, Merge will automatically cancel the test.

{% hint style="info" %}
If you're unsure about what timeout to set, you can use our [CI Analytics](https://trunk.io/products/ci-analytics) to analyze the runtime of your CI.
{% endhint %}

For example, assuming a timeout of 4 hours:

* At 3:00, Bob submits PR 456 to the MergeQueue.
* At 3:05, PR 456 starts testing using Bob's CI system.
* At 7:05, Trunk cancels PR 456, since PR 456 is still testing.

### Concurrency

Configure how many PRs may test in parallel. A larger number may increase throughput, since more PRs are tested in parallel, but at the expense of CI, since more jobs are running in parallel. When the graph is at capacity, PRs will still be submitted to it, but they will not begin testing until a PR leaves the graph.

{% hint style="info" %}
If your testing workload contains some flaky tests, a deeper queue (i.e. a higher concurrency) may struggle. Running Merge in `Graph` mode can help with this, as it will reduce the average depth of your merge graph, since all PRs won't be queued directly behind each other.
{% endhint %}

For example, assuming a concurrency of 3:

* At 12:00, Alice submits PR 1000 to the MergeQueue, and it starts testing.
* At 12:05, Bob submits PR 888 to the MergeQueue, and it starts testing.
* At 12:10, Charlie submits PR 777 to the MergeQueue, and it starts testing.
* At 12:15, Alice submits PR 1001 to the MergeQueue. Tests do not start, because the MergeQueue is at its concurrency limit.
