---
description: >-
  Yes, Trunk Merge Queue fully supports stacked pull requests. You can use
  stacked PR workflows with your preferred tooling (GitHub CLI, web interface,
  or third-party apps).
---

# Stacked pull requests

### How it works

Trunk Merge Queue determines PR dependencies by examining each pull request's **base branch** (the branch it will merge into, shown under the PR title on GitHub).

* If a PR's base branch is your main branch (e.g., `main`), it's ready to process immediately
* If a PR's base branch is another feature branch (indicating it's part of a stack), Merge Queue will wait until that base branch changes to your main branch before processing

### Merging stacked PRs

#### Step 1: Enqueue all PRs in your stack

Each PR in the stack must be enqueued separately. You can:

* Comment `/trunk merge` on each PR
* Check the box in the Trunk comment on each PR
* Use the CLI: `trunk merge <pr-number>` for each PR

**Why enqueue separately?** Each PR is an independent merge operation in the queue. This gives you control over which PRs in your stack should be merged versus which might need more work.

#### Step 2: Automatic sequential processing

Once enqueued, Trunk handles the rest automatically:

1. The **first PR** in the stack (base branch = `main`) enters the queue, runs tests, and merges
2. When it merges, **GitHub automatically updates** the next PR's base branch from the previous feature branch to `main`
3. The **second PR** now has `main` as its base, so it proceeds through the queue
4. This continues until all PRs in the stack are merged

**Example:** For a stack of 5 PRs:

* PR #1 (base: `main`) → tests → merges
* PR #2's base automatically changes from PR #1's branch to `main` → tests → merges
* PR #3's base automatically changes from PR #2's branch to `main` → tests → merges
* And so on...

***

### Important considerations

#### Sequential testing

PRs in a stack are tested and merged **one at a time** in order. The second PR won't begin testing until the first PR has fully merged. This ensures:

* Each PR is tested against the actual state of your main branch
* No conflicts arise from dependencies
* Test results are deterministic and reliable

**Tradeoff:** This sequential approach means that a stack of 5 PRs will take longer to merge than 5 independent PRs, since they cannot be tested in parallel. However, it provides the safest merge path for dependent changes.

#### Enqueued PRs with non-main base branches

If you enqueue a PR whose base branch is not your main branch and that base never changes to main, the PR will remain in the queue without processing. This typically happens if:

* The parent PR in the stack was not enqueued or merged
* You're testing queue behavior with a non-standard workflow

The PR will begin processing as soon as its base branch updates to your main branch.

### Configuration

No special configuration is required. Trunk Merge Queue automatically detects stacked relationships based on the base branch field in GitHub.
