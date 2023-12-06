# Merge

**Trunk Merge** is a sophisticated merge queue. It's a GitHub bot and a web app that devs use to merge pull requests. If you have a big team, use trunk-based-development, or if you have a monorepo, you should use a merge queue. See below for why.

Trunk Merge can use any CI provider as long as you use GitHub for your repo hosting.

## About merge queues

Merge queues automate PR merges into your repo's main branch, ensuring incompatible changes never break the branch. They are a best practice for trunk-based development in repos with 10-1000 active engineers.

#### The problem they solve

Merge queues make sure your `main` branch is never broken ('broken', meaning: a service is not functioning correctly, your app segfaults, there are compilation errors, a unit test is failing, or anything else is going wrong).\
There are two common ways `main` branches "break":

1. A PR was branched off of on an old commit of `main`, and when merged into `main` it no longer functions with the latest state of the repo.
2. Two (or more) PRs recently merged and worked independently, but combining their changes breaks something.

Either way, the more pull request velocity you have in a repo, the more often issues arise. These issues are called [logical merge conflict](https://trunk.io/blog/what-is-a-logical-merge-conflict)s. A merge queue handles this problem by testing PRs queued to be merged _in combination, based on the latest `main`,_ and only if the extra combination testing passes do they merge.

### Single mode vs. Parallel mode

Trunk Merge has two modes, single and parallel. Single mode is a great way to start, and parallel mode is a great way to scale a repo to 10s or 100s of active developers.

#### Single Mode

In Single mode, Trunk Merge acts like a queue: first in, first out. All PRs are tested and merged in the order they arrived. It will still test many combinations of enqueued PRs at once against each other (and exactly how many is a configuration option), but fundamentally, regardless of whether two PRs are completely unrelated, it will test them against each other. This is a simple and effective way to start using Trunk Merge.

#### Parallel mode

In Parallel mode, Trunk knows which PRs are related and which are unrelated and can function effectively as having many merge queues in the same repo, queueing only related PRs on top of one another. Trunk knows the relationship between PRs by you sending it to us, we call this [impacted-targets.md](impacted-targets.md "mention") and it can be information pulled from build systems like Bazel, Nx, or Turborepo, or it can be defined by a set of glob file matching patterns.

## Build system integration

Trunk Merge in [#parallel-mode](./#parallel-mode "mention") uses information from build systems to optimize merging code. This can be set for _**any**_** build system**, but we currently have first-class support for...

### Bazel Integration

Trunk Merge has [first-class support](https://github.com/trunk-io/merge-action) for Bazel with GitHub Actions. Trunk Merge will automatically form a graph of PRs in parallel mode that mirrors the Bazel dependency graph relationship between the code changed in each PR. Testing enqueued PRs via Trunk Merge tests against _only_ other enqueued PRs with overlapping bazel dependencies. Read more about how to hook this up in the[ Impacted Targets docs](impacted-targets.md).
