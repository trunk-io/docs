---
description: >-
  Covers the journey of a PR from submission through various states to
  completion
---

# Pull Request Lifecycle

## Submitting and Cancelling Pull Requests

We offer a few mechanisms for submitting a PR to the Merge Graph:

* Posting a GitHub comment `/trunk merge` on a pull request.
* Ticking the checkbox in the Trunk comment on a pull request.
* Clicking the "Retry" button on the WebApp.
* Using the `trunk` CLI:

```
trunk login
trunk merge <pr-number>
```

We offer similar commands for cancellation.

* Posting a GitHub comment `/trunk cancel` on a pull request.
* Cancellation from the WebApp:

<figure><img src="../../.gitbook/assets/image (16).png" alt=""><figcaption></figcaption></figure>

* Using the `trunk` CLI:

```
trunk login
trunk merge cancel <pr-number>
```

## Pull Request Processing

Once a PR is submitted to the merge queue it goes through several states. First, it starts as _Queued_ until all of the required conditions to submit it are met. Once ready, the PR moves to the _Pending_ state, waiting for a Merge Queue to pick it up, and then enters the _Testing_ state. Once the tests pass the PR may still need to wait for upstream PRs. Once any upstream PRs are complete the PR will be merged and then removed from the Merge Queue. If a PR fails or is canceled then it will go to the failed or canceled state.

## PR States

A PR's lifecycle in the Merge Queue goes through the following states:

| State           | Description                                                                                                                                                                                                                                                                                                                                                                    |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Queued          | The PR was submitted to Trunk Merge Queue, but the PR isn't eligible for merging yet. Impacted targets may not be uploaded, or readiness checks may not have passed.                                                                                                                                                                                                           |
| Pending         | The MergeGraph created a node for the PR. Testing will begin if the graph has capacity.                                                                                                                                                                                                                                                                                        |
| Testing         | The PR is testing. Required status checks that Trunk Merge Queue must gate on before merging PRs can be specified with in `.trunk/trunk.yaml` or through GitHub branch protection rules as the "Status checks that are required" before merging on your merge branch                                                                                                           |
| Tests Passed    | The PR successfully passed tests. It may have to wait for upstream PRs to complete tests before merging.                                                                                                                                                                                                                                                                       |
| Pending Failure | The PR failed tests. The cause of failures is still indeterminate - it may be due to an upstream PR, or due to the current PR. It will wait until the root cause of tests has been determined, and restart testing on your PR if due to an upstream PR. If you want to manually restart a failed PR, see [manually restarting PRs](using-the-webapp.md#restarting-failed-prs). |
| Merged          | The PR successfully merged into the target branch. It will be removed from the queue.                                                                                                                                                                                                                                                                                          |
| Failed          | The PR caused a testing failure. It will be removed from the queue.                                                                                                                                                                                                                                                                                                            |
| Cancelled       | The PR was cancelled, e.g. `/trunk cancel`. It will be removed from the queue.                                                                                                                                                                                                                                                                                                 |

## Stacked PR Support

Trunk Merge Queue supports workflows that use stacked pull requests with minimal configuration required.

Merge Queue operates by merging pull requests into the specific target branch `main`. If a pull request is enqueued with a different target branch (as is common in stacked PR workflows), Trunk will defer merging until the pull request’s target branch becomes `main`. This happens automatically in GitHub when the parent pull request in the stack is merged.

As a result, you can enqueue all PRs in a stack at once, and Merge Queue will handle them in the correct order. Each pull request will wait until its dependency PRs have merged before proceeding. This ensures that stacked pull requests are merged in order, even if they were enqueued out of order.
