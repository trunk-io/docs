# Merge

**Trunk Merge** is a particularly sophisticated merge queue. It's a GitHub bot and a web app that devs use to merge pull requests. If you have a big team, use trunk-based-development, or if you have a monorepo, you should use a merge queue. See below for why.

## What is a Merge Queue

Merge queues are a best practice for trunk-based development in repos with 10-1000 active engineers.

#### The problem they solve

Merge queues make sure your `main` branch is never broken ('broken', meaning: a service is not functioning correctly, your app segfaults, there are compilation errors, a unit test is failing, or anything else is going wrong).

\
There are two common ways `main` branches "break":

1. A PR was branched off of on an old commit of `main`, and when merged into `main` it no longer functions with the latest state of the repo.
2. Two (or more) PRs that were recently merged worked independently, but the combination of their changes breaks something.

Either way, the more pull request velocity you have in a repo, the more often issues arise. These issues are called [logical merge conflict](https://trunk.io/blog/what-is-a-logical-merge-conflict)s. A merge queue handles this problem by testing PRs queued to be merged _in combination, based on the latest `main`,_ and only if the extra combination testing passes do they merge.

#### History

For the last 5-10yrs merge queues have been extremely popular in silicon valley big tech companies who trend towards trunk-based development and either large repos or monorepos. But, until recently, if you wanted one, you had to build your own. Now there's Trunk Merge.

### Single mode vs. Parallel mode

Trunk Merge has two modes, **Single** mode and **Parallel** mode. Single mode is a great way to start, and parallel mode is a great way to scale a repo to 10s or 100s of active developers.

#### Single Mode

In Single mode, Trunk Merge acts like a queue: first in, first out. All PRs are tested and merged in the order they arrived. It will still test many combinations of enqueued PRs at once against each other (and exactly how many is a configuration option), but fundamentally regardless of whether two PRs are completely unrelated or not, it will test them against eachother. This is a simple and effective way to start using Trunk Merge.

#### Parallel mode

In Parallel mode, Trunk knows which PRs are related and which are unrelated, and is able to function effectively as having many merge queues in the same repo, queueing only related PRs on top of one another. Trunk knows the relationship between PRs by you sending it to us, we call this [impacted-targets.md](impacted-targets.md "mention") and it can be information pulled from build systems like Bazel, Nx, or Turborepo, or it can be defined by a set of glob file matching patterns.

## Build system integration

Trunk Merge in [#parallel-mode](./#parallel-mode "mention") uses information from build systems to optimize merging code. This can be set for _any_ build system, but we currently have first-class support for...

### Bazel Integration

Trunk Merge has [first-class support](https://github.com/trunk-io/merge-action) for Bazel with GitHub Actions. Trunk Merge will automatically form a graph of PRs in parallel mode that mirrors the Bazel dependency graph relationship between the code changed in each PR. Testing enqueued PRs via Trunk Merge tests against _only_ other enqueued PRs with overlapping bazel dependencies. Read more about how to hook this up in the[ Impacted Targets docs](impacted-targets.md).

## How Trunk Merge Works

Trunk Merge creates temporary test branches with the combination of enqueued PRs to run an additional test CI run (which you specify), and only if that test run passes does it merge pull requests into your main branch.&#x20;

A typical developer workflow _without using **Trunk Merge**_  might look like this:

1. Create a feature branch from the main branch
2. Author a Change
3. Open a Pull Request
4. Tests are Run on CI
5. Code Review
6. When tests & code review pass, the author merges their PR

In a repository with many contributors, **the state of the main branch will have advanced significantly after step 1**. Because of this, the results of the tests run in step 4 are out of date. Merge solves this by adding another test pass to ensure no broken code lands on your main branch. A developer workflow with Merge integrated might look like this:

1. Create a feature branch from the main branch
2. Author a Change
3. Open a Pull Request
4. Tests are Run on CI
5. Code Review
6. When tests & code review pass, the Author submits the PR to Trunk Merge
7. Tests are run on a branch consisting of head of main + the pull request changes
8. If the tests pass, the pull request is merged automatically
