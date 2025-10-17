---
description: >-
  Merge queue that guarantees branch stability and accelerates development at
  enterprise scale
---

# Introduction

**Trunk Merge Queue** is a hosted service that manages and controls how pull requests are merged into your `main` branch. It ensures incompatible changes never break the branch while maximizing merge throughput—essential for high-velocity teams working in monorepos.

{% embed url="https://youtu.be/qFCXVkx3pbo" %}

### The Problem: Traditional Merge Workflows Break at Scale

Traditional workflows fail at high velocity because of the fundamental race condition between testing and merging:

* **"Merge when green" breaks `main`:** PRs pass CI on their own branches and merge—but those test results are stale the moment another PR lands. At high velocity, this guarantees eventual `main` breakage.
* **"Require up-to-date branch" has a race condition:** Even GitHub's safeguard (rebase before merge + retest) fails at scale. While a PR's CI runs after rebasing, other PRs can merge, making the rebase stale by merge time.

**The result:** At high velocity, `main` breaks regularly. Deployments halt while teams investigate which recent commits caused the failure—pulling senior engineers away from feature work to review logs and coordinate reverts.

The only way to guarantee branch stability is predictive testing: validating that PRs will pass when combined with the future state of `main`.

### How Trunk Merge Queue Solves This

**Predictive testing eliminates the race condition**

Trunk Merge Queue tests each PR against the predicted future state of `main`—the state after all PRs ahead of it in the queue have merged. This eliminates the race condition: by the time a PR merges, it has already been validated against the exact state it will merge into.

When PR A and PR B both enter the queue, Trunk tests B against `main` + A, guaranteeing that the merged result will be stable. No stale test results, no post-merge failures, no broken `main`.

**But predictive testing at scale requires optimization**

Testing every PR serially against the predicted state guarantees correctness but creates new bottlenecks: queue wait times and CI costs scale linearly with PR volume. Trunk solves this with enterprise-grade optimizations:

* **Intelligent Batching** runs one CI test for multiple PRs together instead of testing each separately, reducing costs up to 90% with automated bisection when batches fail
* **Dynamic Parallel Queues** analyze which code each PR touches and create independent test lanes for non-overlapping changes—eliminating queue bottlenecks from unrelated PRs in large monorepos
* **Anti-Flake Protection** uses results from later PRs in the queue to validate earlier ones—if a PR fails but subsequent PRs that include its code pass, the failure was likely transient and all PRs merge together

The result: guaranteed branch stability with throughput that scales to thousands of PRs per day.

{% hint style="info" %}
### **Requirements**

Trunk Merge Queue is CI-agnostic and works with your existing pipeline infrastructure (Jenkins, CircleCI, GitHub Actions, Buildkite, etc.). GitHub repository hosting is required.
{% endhint %}

### **Next steps**

<table data-card-size="large" data-view="cards"><thead><tr><th></th><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td></td><td>Book a demo</td><td></td><td><a href="https://calendly.com/trunk/demo">https://calendly.com/trunk/demo</a></td></tr><tr><td></td><td>Get started on your own</td><td></td><td><a href="set-up-trunk-merge/">set-up-trunk-merge</a></td></tr></tbody></table>
