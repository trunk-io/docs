---
description: >-
  Trunk Merge Graph is a beta Merge Queue solution. The MergeGraph parallelizes
  testing of independent PRs, increasing throughput to your repository while
  maintaining the correctness of tests.
---

# Merge Graph

## Getting Started

Trunk Merge Graph is coming out of beta soon. For a sneak peek, please contact us at our [Slack](https://slack.trunk.io/), and we'll help get your repository set up!

## How it Works

We suggest reading our docs on the [merge queue](../merge/graph/merge/) for prior art. A merge graph is like a merge queue, but instead of testing with every upstream PR, it will only test PRs that are dependent on one another. PRs are dependent on one another if they share at least one [impacted target](../merge/graph/merge-graph/impacted-targets.md).

When a PR is submitted to the merge graph, the graph will examine the provided list of impacted targets that result from code changes in a PR. The testing branch created only consists of other PRs that **transitively** share an edge with the PR. For example, if:

* PR 1 impacts `[src/protos/]`
* PR 2 impacts `[src/user_service/, src/protos/]`
* PR 3 impacts `[docs/]`,

a graph may look like:

![](<../.gitbook/assets/Screen Shot 2023-08-22 at 1.52.51 PM.png>)

but the queue will look like:

\


<figure><img src="../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

\


\
