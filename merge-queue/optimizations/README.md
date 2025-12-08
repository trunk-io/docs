# Optimizations

The core concept of any merge queue is [**Predictive Testing**](predictive-testing.md): testing your pull request against the head of the `main` branch, including all pull requests ahead of it in the queue.

While this is the foundation, achieving the scale necessary to merge thousands of PRs per day requires more advanced strategies. Trunk Merge Queue introduces a suite of powerful concepts designed to maximize throughput and maintain velocity, even in complex, high-traffic repositories. In fact, hitting a high scale is nearly impossible without leveraging features like optimistic merging, pending failure depth, and batching.

This section explains each of these key concepts:

#### Throughput and speed

* [**Batching**](batching.md): Groups multiple compatible pull requests together into a single test run. This significantly increases merge throughput and can dramatically reduce CI costs by validating an entire batch with a single test run instead of one for each individual pull request. It is an essential feature for achieving high throughput.
* [**Parallel Queues**](parallel-queues/): Allows for the creation of multiple independent queues that test and merge PRs in parallel. This feature is necessary for large monorepos and transforms the queue from a simple "line" into a more complex and efficient "graph".
* [**Testing Concurrency**](../administration/advanced-settings.md#testing-concurrency): A setting that defines the maximum number of pull requests that can be tested simultaneously. Fine-tuning this number is a powerful way to maximize merge velocity. It ensures a continuous flow of validated pull requests by keeping your CI runners fully utilized.

#### Resilience and flake handling

* [**Optimistic Merging**](optimistic-merging.md): Increases merge speed by leveraging test results from pull requests that are later in the queue. When a pull request (e.g., pull request 'c') passes testing, its success also verifies the changes from the pull requests ahead of it ('a' and 'b'). This allows the entire group of pull requests to be safely merged at once.
* [**Pending Failure Depth**](pending-failure-depth.md): Allows the queue to continue testing subsequent pull requests even if an earlier one fails. Because predictive testing re-tests the failed PR's code along with the subsequent PRs, this feature gives the failed PR additional chances to pass. This prevents a single flaky test from halting all forward progress and makes the queue more resilient to intermittent failures.
* [**Anti-Flake Protection**](anti-flake-protection.md): Combining Optimistic Merging and Pending Failure Depth makes the queue more resilient to flaky tests. This inherent outcome allows the successful test of a later pull request to retroactively validate an earlier one that failed due to a transient issue.

{% hint style="success" %}
**Note on flaky tests**

While Anti-Flake Protection provides resilience to flaky tests through queue mechanics, they still delay merges. Trunk Flaky Tests addresses the root cause by automatically [detecting](../../flaky-tests/detection.md) and [quarantining](../../flaky-tests/quarantining.md) flaky tests at runtime while maintaining test visibility. For maximum throughput, [integrate Flaky Tests](../../flaky-tests/get-started/) to work alongside Anti-Flake Protection.
{% endhint %}

* [**Flaky Tests Quarantining**](../../flaky-tests/quarantining.md) (via [Flaky Tests](../../flaky-tests/overview.md)): Automatically detects and quarantines flaky tests to prevent their failures from blocking the merge queue. Quarantined tests continue running and uploading results for visibility, allowing your team to identify and fix them while eliminating false-negative blockages. This foundation of clean test signals is essential for achieving maximum queue throughput.

#### Prioritization

* [**Priority Merging**](priority-merging.md): Provides the ability to prioritize certain pull requests, allowing urgent changes or hotfixes to bypass the standard queue order and be tested and merged more quickly.
