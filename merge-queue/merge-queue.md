---
description: >-
  Merge queue that guarantees branch stability and accelerates development at
  enterprise scale
---

# Overview

**Trunk Merge Queue** is a hosted service that manages and controls how pull requests are merged into your `main` branch. It ensures incompatible changes never break the branch while maximizing merge throughput—essential for high-velocity teams working in monorepos.

{% embed url="https://youtu.be/qFCXVkx3pbo" %}

### The Problem: Traditional Merge Workflows Break at Scale

Traditional workflows fail at high velocity because of the fundamental race condition between testing and merging:

* **"Merge when green" breaks `main`:** PRs pass CI on their own branches but never test integration. At high velocity, this guarantees eventual `main` breakage when independently-passing PRs conflict.
* **"Require up-to-date branch" prevents merges:** GitHub's safeguard (rebase + retest) creates a race condition. While a PR's CI runs after rebasing, other PRs merge, making it stale again. At high velocity, PRs get stuck in endless rebase-retest loops and can't land.

**The result: At high velocity, teams can't deploy reliably.** Either `main` breaks regularly—forcing engineers to investigate failures and coordinate reverts—or PRs get stuck in endless rebase-retest loops, starving the pipeline.

**The solution is predictive testing:** validating that PRs will pass when combined with the future state of `main`. This eliminates the race condition—ensuring both branch stability and that PRs can actually land.

### How Trunk Merge Queue Solves This

**Predictive testing eliminates the race condition**

Trunk Merge Queue [tests each PR against the predicted future state of `main`](concepts/predictive-testing.md)—the state after all PRs ahead of it in the queue have merged. This eliminates the race condition: by the time a PR merges, it has already been validated against the exact state it will merge into.

When PR A and PR B both enter the queue, Trunk tests B against `main` + A, guaranteeing that the merged result will be stable. No stale test results, no post-merge failures, no broken `main`.

**But predictive testing at scale requires optimization**

Testing every PR serially against the predicted state guarantees correctness but creates new bottlenecks: queue wait times and CI costs scale linearly with PR volume. Trunk solves this with enterprise-grade optimizations:

* [**Intelligent Batching**](concepts/batching.md) runs one CI test for multiple PRs together instead of testing each separately, reducing costs up to 90% with automated bisection when batches fail
* [**Dynamic Parallel Queues**](concepts-and-optimizations/parallel-queues/) analyze which code each PR touches and create independent test lanes for non-overlapping changes—eliminating queue bottlenecks from unrelated PRs in large monorepos
* [**Anti-Flake Protection**](concepts/anti-flake-protection.md) uses results from later PRs in the queue to validate earlier ones—if a PR fails but subsequent PRs that include its code pass, the failure was likely transient and all PRs merge together

The result: guaranteed branch stability with throughput that scales to thousands of PRs per day.

{% hint style="info" %}
**Integration Requirements**

Trunk Merge Queue is CI-agnostic and works with your existing pipeline infrastructure (Jenkins, CircleCI, GitHub Actions, Buildkite, etc.). Currently supports GitHub for repository hosting. Interested in GitLab support? [Contact us](https://emailto:support@trunk.io).
{% endhint %}

### **Next steps**

<table data-card-size="large" data-view="cards"><thead><tr><th></th><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td></td><td>Book a demo</td><td></td><td><a href="https://calendly.com/trunk/demo">https://calendly.com/trunk/demo</a></td></tr><tr><td></td><td>Get started on your own</td><td></td><td><a href="set-up-trunk-merge/">set-up-trunk-merge</a></td></tr></tbody></table>
