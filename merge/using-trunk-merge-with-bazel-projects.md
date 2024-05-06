---
description: >-
  This guide explains how Trunk Merge works with Bazel to build your codebase
  faster and safer.
---

# Using Trunk Merge with Bazel Projects

## Do you need a merge queue?

When testing and merging PRs to a main branch, your codebase will sometimes get what is called a _**logical**_** merge conflict**. This is when two PRs can each merge cleanly with the target branch, but together create a conflict. Git cannot resolve this type of a conflict, requiring manual intervention. Usually a engineer must merge one PR, rebase the second one, fix any conflicts, then submit again for testing. (for more see [What is a Logical Merge Conflict](https://trunk.io/learn/what-is-a-logical-merge-conflict)).&#x20;

Manually fixing logical merge conflicts is annoying but manageable. With a codebase developed by a small engineering team logical merge conflicts are rare enough to be manageable. The developers make changes, push PRs, and they gets merged into main after passing CI tests.&#x20;

As soon as your team has 40-50 engineers, or are working on multiple branches, you risk more frequent logical conflicts. As your team grows or your pace speeds up, more and more time is wasted on fixing these conflicts, increasing costs and wasting time that could be spent on features instead of wrangling with infrastructure. Enter the _merge queue_.

### What a merge queue fixes

A merge queue grabs PRs when they are ready to be merged and tests them individually against each other and the current head of your main branch. This ensures everything merges cleanly and all tests continue to pass on main as PRs keep getting merged. When something cannot be resolved automatically it is kicked back to the developer before allowing it to merge with the target branch. This means your dev team spends less time messing with surprise breakages. Everyone can get back to coding features and moving faster!

When a conflict happens without using a merge queue, the developer must rebase that PR against main, fix any changes, then submit it again and hope the CI tests finish before someone else’s that could trigger another round of conflicts and rebasing.  The time fixing conflicts grows, which is why the queue is a life saver with bigger codebases.

## The problems with traditional merge queues

A team of 100 developers can easily produce 50 to 60 PRs per day. When there are a lot of PRs, depending on how long a test run is, the queue can get backed up. Since each PR must be tested with every other PR, the test count and CI costs can grow rapidly.&#x20;

Traditional merge queues are also FIFO (First In First Out) queues, thus simple changes, or emergency fixes, must still wait at the end of the queue until everything before them finishes. There is no way to mark a PR as high priority.

## Trunk Merge, built for Bazel

Trunk Merge is a merge queue that works **with** your existing Bazel setup to understand the structure of your codebase and optimize the queue, resulting in faster development and cheaper CI. Trunk Merge does this in three ways:

### Concurrency

A smart merge queue can parallelize the testing work, but only if it knows which PRs truly depend on other PRs.  If one PR is for the GUI and another is for the backend, it is likely that the two PRs are independent of each other and could be tested and merged at the same time. However, the queue can only be 100% sure of this if it knows the structure of the code base dependencies.  This is where Bazel comes in.

In a codebase built with Bazel, the dependency graph is already defined by Bazel itself.  Trunk Merge can use this information from Bazel to intelligently parallelize the dependency graph. It can then be 100% sure that a PR for the frontend won’t conflict with the backend, and skip the tests that it now knows won’t fail.  This reduces the CI cost from O(N^2) to O(N+M), decreasing the actual time and monetary costs of tests. While Trunk Merge can operate without this information, or by supplying it in another form, Bazel already provides a dependency graph for the entire codebase, making the process seamless.

Trunk Merge also allows you to tune the amount of parallelization done to keep costs down. For some projects you might want 3 or for 4 simultaneous CI jobs. For other projects you might need only one.  In either case, Trunk Merge can use the dependency graph from Bazel to optimize the number of tests, even with only a single CI queue.

### Priority Management

Trunk Merge allows developers to set a priority on each PR if desired. If a PR is an emergency fix then you can mark it as high priority and it will move to the front of the queue.  Trunk Merge will still make sure it is run behind any dependent PRs, but it will skip any PRs that are guaranteed to not conflict. Again Bazel’s dependency graph makes this more effective.&#x20;

To make it even easier to set a PR priority you do not need to use a special UI. You can just [add the priority to a Github comment](pr-prioritization.md#github-comment) during code review to set the priority.

### Optimistic Merging and Batching

In certain cases Trunk Merge can [optimistically merge](anti-flake-protection.md) a PR, even if it failed testing, if a second PR after it passes. This is configurable and can help your dev process handle flaky tests better.&#x20;

Suppose a test fails 20% of the time due to a transient error (network delay, Chrome RAM usage, etc). With a traditional merge queue an engineer will have to investigate and at least hit a retry button. With Merge's intelligent _optimistic merging,_ if later PRs pass then the failure likely was transient and it can be safely merged without intervention. This minimizes the impact of flaky tests and keeps the developer pipeline running smoothly.

Trunk Merge can also [group PRs into batches](batching.md). With a batch size of 4 Merge will wait until four PR have been queued and then combine them into a single PR with all of the changes, testing and merging them as a single unit. This results in 1/4 the amount of time spent running tests, and 1/4th cost.

Trunk Merge with optimistic merging and batching greatly speed up your development pipeline.

### Pipeline Health

Trunk Merge proactively monitors the entire testing and merging process of your development pipeline. Whenever there are problems it will alert the team, even sending configurable Slack messages. When a PR fails Merge will remove it from the queue and immediately alert the team of a problem. Trunk Merge also provides a dashboard with statistics of the overall codebase health.

## Summary

Trunk Merge optimizes your development process and reduces CI costs by intelligently resolving conflicts, running tests in parallel, batching and optimistically merging PRs, and monitoring the health of your entire pipeline.

## Next Steps

More Questions? [Talk to a Developer](https://calendly.com/trunk/demo).

Ready to try it? See our [Quick Start](set-up-trunk-merge/) guide.

\
