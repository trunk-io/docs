---
description: >-
  Merge queue that guarantees branch stability and accelerates development at
  enterprise scale
---

# Overview

If you've hit the limits of GitHub's serial merge queue - main turning red, CI costs spiraling, chaos at scale - Trunk Merge Queue is the enterprise upgrade built for reliability at any scale. Handle your noisiest pipelines, cut CI costs up to 90%, and fire and forget.

***

### Benefits of using Trunk Merge Queue

Trunk Merge Queue solves three critical problems that break traditional workflows at scale.

#### #1: Stop main from turning red

**The problem:** Flaky tests fail unpredictably. Your team mutes tests, locks branches, and gets paged to investigate.

**How Trunk fixes it:** Failed PRs stay in queue while downstream PRs continue testing. If a later PR that includes the failed code passes, Trunk knows the failure was transient, both PRs merge together.

**Key capabilities:**

* Anti-flake protection with optimistic merging
* Pending failure depth prevents cascade failures
* Automatic quarantine of flaky tests

→ Learn about [anti-flake protection](optimizations/anti-flake-protection.md)

***

#### #2: Stop CI costs from spiraling

**The problem:** GitHub runs full CI for every PR. 50 PRs/day = 50 full runs. With growing teams, CI costs become seven figures.

**How Trunk fixes it:** Intelligent batching tests up to 100 PRs in a single CI run. When a batch fails, automatic bisection isolates the culprit without ejecting the entire batch or requiring manual debugging.

**Key capabilities:**

* Intelligent Batching
* Batch up to 100 PRs
* Auto-Bisection
* Configurable batch size & wait time

→ See how [batching](optimizations/batching.md) works

***

#### #3: Stop waiting in a serial queue

**The problem:** Single-track queue means your 2-line fix waits 45 minutes behind a slow feature PR testing an unrelated part of the codebase.

**How Trunk fixes it:** Parallel queues create independent test lanes for non-overlapping changes. Frontend merges in Lane A while backend runs in Lane B. Native Bazel/Nx integration analyzes impacted targets automatically.

**Key capabilities:**

* Parallel Queues
* Bazel/Nx integration
* Impacted targets analysis
* Priority merging

→ Explore [parallel queues](optimizations/parallel-queues/)

***

### Try Trunk Merge Queue

**Start with free trial:**

1. Install Trunk GitHub App (5 minutes)
2. Create your first queue (2 minutes)
3. Submit a test PR

**Total setup time: < 10 minutes**

→ [Get started](getting-started/)
