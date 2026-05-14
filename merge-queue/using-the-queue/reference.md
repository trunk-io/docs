---
description: >-
  Covers the journey of a PR from submission through various states to
  completion
---

# Submit and cancel pull requests

## Submitting and cancelling pull requests

We offer a few mechanisms for submitting a PR to the Merge Graph:

* Posting a GitHub comment `/trunk merge` on a pull request.
* Ticking the checkbox in the Trunk comment on a pull request.
* Clicking the "Retry" button on the WebApp.
* Using the `trunk` CLI:

```
trunk login
trunk merge <pr-number>
```

* Applying the configured enqueueing label to a pull request (when label commands are enabled — see [Label Commands](#label-commands) below).

Admins can also use [`/trunk merge --force`](force-merge.md) to push a PR through the queue when branch protection isn't satisfied.

We offer similar commands for cancellation.

* Posting a GitHub comment `/trunk cancel` on a pull request.
* Cancellation from the WebApp:

<figure><img src="../../.gitbook/assets/image (35).png" alt=""><figcaption></figcaption></figure>

* Using the `trunk` CLI:

```
trunk login
trunk merge cancel <pr-number>
```

* Removing the configured enqueueing label from a pull request (when label commands are enabled).

## Custom merge commit titles

You can specify a custom merge commit title for any PR by adding a `merge-commit-title:` directive on its own line anywhere in the PR body:

```
merge-commit-title: Your Custom Commit Title Here
```

When Trunk merges the PR, it uses this title instead of the default GitHub-generated title. When the directive is not present, the default behavior is preserved.

The directive name is case-sensitive. It must be lowercase `merge-commit-title:`. Variations such as `Merge-Commit-Title:` are not recognized.

This is useful for teams that follow conventional commit formats, include ticket numbers in merge commits, or want a cleaner git history.

### Example

```markdown
## Description
This PR adds user authentication.

merge-commit-title: feat(auth): add OAuth2 login flow [PROJ-123]
```

{% hint style="info" %}
The `merge-commit-title:` directive only customizes the merge commit **title**. The commit body follows the usual behavior for your configured [merge method](../administration/advanced-settings.md#merge-method).

The directive applies to the **Squash** and **Merge Commit** merge methods. It has no effect when using **Rebase**, since rebase replays the original commits onto the target branch and does not produce a separate merge commit.
{% endhint %}

## Label Commands

Label Commands let you enqueue and cancel PRs in the Merge Queue by applying or removing a GitHub label, without leaving a comment or using the CLI.

### Enabling Label Commands

Label Commands are configured per merge queue instance in **Merge Queue Settings** > **Label Commands**. Only organization admins can change this setting.

When Label Commands are enabled, you can configure the enqueueing label name. The default label is `trunk-merge-queue-submit`.

### How it works

| Action | Effect |
| ------ | ------ |
| Apply the enqueueing label to a PR | Submits the PR to the Merge Queue |
| Remove the enqueueing label from a PR | Cancels the PR from the queue |

The label must already exist in your GitHub repository. Trunk does not create the label automatically.

{% hint style="info" %}
Label Commands work alongside comment commands and the Trunk web app. You can use any combination of submission methods; they all target the same queue.
{% endhint %}

## Pull request processing

Once a PR is submitted to the merge queue it goes through several states. First, it starts as _Queued_ until all of the required conditions to submit it are met. Once ready, the PR moves to the _Pending_ state, waiting for a Merge Queue to pick it up, and then enters the _Testing_ state. Once the tests pass the PR may still need to wait for upstream PRs. Once any upstream PRs are complete the PR will be merged and then removed from the Merge Queue. If a PR fails or is canceled then it will go to the failed or canceled state.

## Pull request states

A PR's lifecycle in the Merge Queue goes through the following states:

| State           | Description                                                                                                                                                                                                                                                                                                                                                                                                  |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Queued          | The PR was submitted to Trunk Merge Queue, but the PR isn't eligible for merging yet. Impacted targets may not be uploaded, or readiness checks may not have passed.                                                                                                                                                                                                                                         |
| Pending         | The MergeGraph created a node for the PR. Testing will begin if the graph has capacity.                                                                                                                                                                                                                                                                                                                      |
| Testing         | The PR is testing. Required status checks that Trunk Merge Queue must gate on before merging PRs can be specified with in `.trunk/trunk.yaml` or through GitHub branch protection rules as the "Status checks that are required" before merging on your merge branch                                                                                                                                         |
| Tests Passed    | The PR successfully passed tests. It may have to wait for upstream PRs to complete tests before merging.                                                                                                                                                                                                                                                                                                     |
| Pending Failure | The PR failed tests. The cause of failures is still indeterminate - it may be due to an upstream PR, or due to the current PR. It will wait until the root cause of tests has been determined, and restart testing on your PR if due to an upstream PR. If you want to manually restart a failed PR, see [manually restarting PRs](handle-failed-pull-requests.md#manually-restarting-failed-pull-requests). |
| Merged          | The PR successfully merged into the target branch. It will be removed from the queue.                                                                                                                                                                                                                                                                                                                        |
| Failed          | The PR caused a testing failure. It will be removed from the queue.                                                                                                                                                                                                                                                                                                                                          |
| Cancelled       | The PR was cancelled, e.g. `/trunk cancel`. It will be removed from the queue.                                                                                                                                                                                                                                                                                                                               |
