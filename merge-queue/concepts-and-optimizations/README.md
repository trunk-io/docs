# Concepts and Optimizations

The core concept of any merge queue is **predictive testing**: testing your pull request against the head of the `main` branch, including all pull requests ahead of it in the queue.

While this is the foundation, achieving the scale necessary to merge thousands of PRs per day requires more advanced strategies. Trunk Merge Queue introduces a suite of powerful concepts designed to maximize throughput and maintain velocity, even in complex, high-traffic repositories. In fact, hitting a high scale is nearly impossible without leveraging features like optimistic merging, pending failure depth, and batching.

This section explains each of these key concepts:

#### Throughput & Speed

* [**Batching**](../concepts/batching.md): Groups multiple compatible pull requests together into a single test run. This significantly increases merge throughput and can dramatically reduce CI costs by validating an entire batch with a single test run instead of one for each individual pull request. It is an essential feature for achieving high throughput.
* [**Parallel Queues**](parallel-queues/): Allows for the creation of multiple independent queues that test and merge PRs in parallel. This feature is necessary for high-scale simulations and transforms the queue from a simple "line" into a more complex and efficient "graph".

#### Resilience & Flake Handling

* [**Pending Failure Depth**](../concepts/pending-failure-depth.md): Allows the queue to continue testing subsequent pull requests even if an earlier one fails. Because predictive testing re-tests the failed PR's code along with the subsequent PRs, this feature gives the failed PR additional chances to pass. This prevents a single flaky test from halting all forward progress and makes the queue more resilient to intermittent failures.
* [**Optimistic Merging**](../concepts/optimistic-merging.md): Increases merge speed by leveraging test results from pull requests that are later in the queue. When a pull request (e.g., pull request 'c') passes testing, its success also verifies the changes from the pull requests ahead of it ('a' and 'b'). This allows the entire group of pull requests to be safely merged at once.
* [**Anti-Flake Protection**](../concepts/anti-flake-protection.md): Combining Optimistic Merging and Pending Failure Depth makes the queue more resilient to flaky tests. This inherent outcome allows the successful test of a later pull request to retroactively validate an earlier one that failed due to a transient issue.

#### Prioritization

* [**Priority Merging**](pr-prioritization.md): Provides the ability to prioritize certain pull requests, allowing urgent changes or hotfixes to bypass the standard queue order and be tested and merged more quickly.

<table data-view="cards"><thead><tr><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Predictive Testing</strong></td><td><a href="../concepts/predictive-testing.md">predictive-testing.md</a></td></tr><tr><td><strong>Batching</strong></td><td><a href="../concepts/batching.md">batching.md</a></td></tr><tr><td> <strong>Priority</strong></td><td><a href="pr-prioritization.md">pr-prioritization.md</a></td></tr><tr><td><strong>Optimistic Merging</strong></td><td><a href="../concepts/optimistic-merging.md">optimistic-merging.md</a></td></tr><tr><td><strong>Pending Failure Depth</strong></td><td><a href="../concepts/pending-failure-depth.md">pending-failure-depth.md</a></td></tr><tr><td><strong>Anti-Flake Protection</strong></td><td><a href="../concepts/anti-flake-protection.md">anti-flake-protection.md</a></td></tr><tr><td><strong>Parallel Queues</strong></td><td><a href="parallel-queues/">parallel-queues</a></td></tr><tr><td><strong>Parallel Queues with Bazel</strong></td><td><a href="parallel-queues/bazel.md">bazel.md</a></td></tr><tr><td><strong>Parallel Queues with Nx</strong></td><td><a href="parallel-queues/nx.md">nx.md</a></td></tr></tbody></table>
