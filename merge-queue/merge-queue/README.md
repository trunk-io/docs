---
description: >-
  Enterprise-scale merge queue to merge pull requests quickly while protecting
  your main branch.
---

# Overview

**Trunk Merge Queue** is a hosted merge queue service. It manages and controls the order in which enqueued pull requests are merged into the `main` branch of your repository. Trunk Merge Queue enables large teams working in a monorepo to reduce merge conflicts and maintain a green, healthy main branch.

{% embed url="https://youtu.be/qFCXVkx3pbo" %}

### **Why use a merge queue?**

Merge queues automate PR merges into your repo's `main` branch, ensuring incompatible changes never break the branch. They are a best practice for trunk-based development in repos with 10-1000+ active engineers.

### **Why do teams adopt a merge queue?**

As the number of concurrent, changes to a repository grows, the likelihood that your pull request has stale/invalid test results increases. The only way to guarantee that your `main` branch does not become "broken" is to make sure that all code changes are tested against the head of `main`.

As an example:

1. Jack opens pull request **A** which renames the function `foo()` to `bar()` and updates all the call sites to the new name.
2. Jill opens pull request **B** which adds a new file that uses the existing function `foo().`
3. Jack and Jill are not aware of each other's PRs, and the automated build and tests for each of these independent pull requests both pass.
4. Regardless of order, when pull requests **A** and **B** both merge, there is code in the system calling the function `foo()` that no longer exists.
5. The build is now broken.

A merge queue's purpose is to give you the guarantee of all code being tested against `main` without actually doing that work serially or in reaction to code merging onto main. The merge queue service predicts the future state of `main` and tests against that. ([see predictive testing](../concepts/predictive-testing.md)). Returning to our example - pull requests A and B would both be submitted to the merge queue, which would then perform the predictive testing to ensure that A and B, when combined, do not break the build.

### **What is unique about Trunk Merge Queue?**

<table data-view="cards"><thead><tr><th align="center"></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td align="center">Batching</td><td><a href="../concepts/batching.md">batching.md</a></td></tr><tr><td align="center">Dynamic Parallel Queues</td><td><a href="../concepts/parallel-queues/">parallel-queues</a></td></tr><tr><td align="center">Optimistic Merging</td><td><a href="../concepts/optimistic-merging.md">optimistic-merging.md</a></td></tr><tr><td align="center">Pending Failure Depth</td><td><a href="../concepts/pending-failure-depth.md">pending-failure-depth.md</a></td></tr><tr><td align="center">Prioritization</td><td><a href="../pr-prioritization.md">pr-prioritization.md</a></td></tr><tr><td align="center">Flaky Test Protection</td><td><a href="../concepts/anti-flake-protection.md">anti-flake-protection.md</a></td></tr></tbody></table>

### **Requirements**

Trunk Merge Queue works with any CI provider as long as you use GitHub for your repo hosting.

### **Next Steps**

<table data-view="cards"><thead><tr><th></th><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td></td><td>Talk to a developer</td><td></td><td><a href="https://calendly.com/trunk/demo">https://calendly.com/trunk/demo</a></td></tr><tr><td></td><td>Get started on your own</td><td></td><td><a href="../set-up-trunk-merge/">set-up-trunk-merge</a></td></tr></tbody></table>
