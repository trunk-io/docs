---
description: Parallel-powered Merge Queue to speed up developer workflows.
---

# Merge

**Trunk Merge** is a hosted merge queue service. It manages and controls the order in which enqueued pull requests are merged into the `main` branch of your repository. Trunk Merge enables large teams working in a monorepo to reduce merge conflicts and maintain a green, healthy main branch. \
\
Trunk Merge works with any CI provider as long as you use GitHub for your repo hosting.

### Why use a merge queue?

Merge queues automate PR merges into your repo's `main` branch, ensuring incompatible changes never break the branch. They are a best practice for trunk-based development in repos with 10-1000+ active engineers.\
\
**Why are Merge Queues recommended for large monorepos?**\
As the number of concurrent, unrelated changes to a repository grows, the likelihook of a [logical merge conflict](https://trunk.io/blog/what-is-a-logical-merge-conflict) increases. A logical merge conflict creates what is often referred to as a "broken main". \
\
There are two common ways a `main` branch can become broken:

1. A PR was branched off of on an old commit of `main`, passed tests when run against that old view of main, but when merged into `main` no longer functions as expected.
2. Two (or more) PRs made code changes that when tested independently function correctly, but not when combined onto main. e.g. - PR-1 adds a new test that calls function foo() while PR-2 renames the existing function foo() to bar(). In this case both PRs are correct in isolation but they are in conflict once merged onto main.

Either way, the more pull request velocity you have in a repo, the more often issues like these arise. A merge queue handles these problematic conflicts by testing PRs queued to be merged _in combination, based on the latest `main`,_ and only if the extra combination testing passes do they merge.

## Single mode vs. Parallel mode <a href="#single-mode-vs-parallel-mode" id="single-mode-vs-parallel-mode"></a>

Trunk Merge has two modes, single and parallel. Single mode is a great way to start, and parallel mode is a great way to scale a repo to 10s or 100s of active developers.

#### Single Mode

In Single mode, Trunk Merge acts like a typical queue: first in, first out. All PRs are tested and merged in the order they arrived. It will still test many combinations of enqueued PRs at once against each other (and exactly how many is a configuration option), but fundamentally, regardless of whether two PRs are completely unrelated, it will test them against each other. This is a simple and effective way to start using Trunk Merge.

#### Parallel mode

In Parallel mode, Trunk knows which PRs are related and which are unrelated and can function effectively as having many merge queues in the same repo, queueing only related PRs on top of one another. Trunk knows the relationship between PRs by you sending it to us; we call this [impacted-targets.md](set-up-trunk-merge/impacted-targets.md "mention") and it can be information pulled from build systems like Bazel, Nx, or Turborepo, or it can be defined by a set of glob file matching patterns.

For more information see [Queue Mode](set-up-trunk-merge/configuration.md).

## Build system integration

Trunk Merge in [#parallel-mode](./#parallel-mode "mention") uses information from build systems to optimize merging code. This can be set for _**any**_** build system**, but we currently have first-class support for...

### Bazel Integration

Trunk Merge has [first-class support](https://github.com/trunk-io/merge-action) for Bazel with GitHub Actions. Trunk Merge will automatically form a graph of PRs in parallel mode that mirrors the Bazel dependency graph relationship between the code changed in each PR. Testing enqueued PRs via Trunk Merge tests against _only_ other enqueued PRs with overlapping bazel dependencies. Read more about how to hook this up in the[ Impacted Targets docs](set-up-trunk-merge/impacted-targets.md).

## Getting Started

Setup Trunk Merge with your repo [now](set-up-trunk-merge/).
