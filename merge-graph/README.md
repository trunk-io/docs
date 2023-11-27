# Merge

**Trunk Merge** is a merge queue that manages all of the important git merges in your repository, ensuring your main branch is always working.

## What is a Merge Queue

When multiple PRs are merged at the same time it is possible for each PR to be correct by itself, but the PRs conflict when all merged together. This is called a [logical merge conflict](https://trunk.io/blog/what-is-a-logical-merge-conflict).  A **merge queue** handles this problem by adding additional tests, including all of the pull requests you want to merge. Trunk Merge is a powerful merge queue that ensures your repository can adhere to the _“Not Rocket Science Rule Of Software Engineering”_: automatically maintain a repository of code that always passes all the tests on your main branch**.**

Trunk Merge has two modes, **Single** mode and **Parallel** mode. In Single mode Trunk Merge acts like a queue: first in first out. All PRs are tested and merged in the order they arrived. In Parallel mode, Trunk Merge can run PRs in parallel so if one PR fails the rest of the PRs can still be merged (subject to certain constraints). In this mode Trunk Merge acts more like a graph than a queue.

## How It Works

Trunk Merge adds an additional test pass before merging pull requests into your main branch. For example, a typical developer workflow for authoring a feature and merging the code to a repository might look like this:

1. Create a feature branch from the main branch
2. Author a Change
3. Open a Pull Request
4. Tests are Run
5. Code Review
6. When tests & code review pass, author merges request

In a repository with many contributors, **the state of the main branch will have advanced significantly after step 1**. Because of this, the results of the tests run in step 4 are out of date. Merge solves for this by adding another test pass to ensure no broken code lands on your main branch. A developer workflow with Merge integrated might look like this:

1. Create a feature branch from the main branch
2. Author a Change
3. Open a Pull Request
4. Tests are Run
5. Code Review
6. When tests & code review pass, Author submits pull request to Merge
7. Tests are run on a branch consisting of head of main + the pull request changes
8. If the tests pass, the pull request is merged automatically
