# Configuration

We offer some knobs and dials when configuring a MergeQueue. The following
configuration can be applied at app.trunk.io, in the Settings > <repoName> page.

## Timeout for Tests to Start

For every PR in the MergeQueue, Trunk creates a new testing branch, validating that main is protected. CI should be configured to run tests when that branch is created: see [getting started](getting-started.md) for some examples. However, CI can have transient failures, and tests may not start. Trunk will cancel any PRs that have requested tests to start, but have not yet heard back from CI.

For example, assuming a timeout of one hour:
- At 12:00, Alice submits PR 123 to the MergeQueue.
- At 12:10, PR 123 passes all required readiness checks, and a testing branch is created using Alice's CI system.
- At 1:10, Trunk's MergeQueue has not yet heard back from Alice's CI system about the testing branch. Trunk cancels PR 123.

## Timeout for Tests to Complete

When a PR is running tests in the MergeQueue, a runaway test can halt throughput of the MergeQueue. For example, if we know the P99 of our test time is 4 hours, we can configure a testing timeout to auto-cancel PRs if they have taken longer than 4 hours. Although this may cause tests restarts downstream, we allow the MergeQueue to keep processing subsequent items. 

:hint: If you're unsure about what timeout to set, you can use our CI Analytics to analyze the runtime of your CI. 

For example, assuming a timeout of 4 hours:
- At 3:00, Bob submits PR 456 to the MergeQueue.
- At 3:05, PR 456 starts testing using Bob's CI system.
- At 7:05, Trunk cancels PR 456, since PR 456 is still testing.

## Concurrency

Trunk offers control over how many tests you may want to run concurrently. A larger number may increase throughput, since more PRs are tested in parallel, but at the expense of CI, since more jobs are running in parallel. 

:hint: If your testing workload contains some flaky tests, a deeper queue (i.e. a higher concurrency) may struggle. We strongly suggest you take a look into our MergeGraph offering to reduce the average depth of your merging solution. Please contact us at [Slack](slack.trunk.io), or via [email](support@trunk.io), and we're happy to help!

For example, assuming a concurrency of 3:
- At 12:00, Alice submits PR 1000 to the MergeQueue, and it starts testing.
- At 12:05, Bob submits PR 888 to the MergeQueue, and it starts testing.
- At 12:10, Charlie submits PR 777 to the MergeQueue, and it starts testing.
- At 12:15, Alice submits PR 1001 to the MergeQueue. Tests do not start, because the MergeQueue is at its concurrency limit.