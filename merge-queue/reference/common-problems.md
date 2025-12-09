---
description: Troubleshooting and FAQ
---

# FAQ

#### Entering the Queue <a href="#entering-the-queue" id="entering-the-queue"></a>

<details>

<summary>Can I add a pull request to the queue before all required checks pass?</summary>

Yes. A pull request can be submitted to the queue at any time, even if it's not yet ready to merge. The pull request will enter the queue in a "Queued" state and wait for all branch protection rules (like passing status checks and required reviews) to be met. Once the PR is ready, Trunk Merge Queue will automatically move it into the testing phase.

</details>

<details>

<summary>Why isn’t my pull request entering the queue?</summary>

First, check the Trunk web app to see what Trunk is waiting on before putting your PR into the merge queue.

Next, if something on that page doesn't look right, for example, it says that GitHub is still checking the mergeability of the PR, comment `/trunk merge` again in the PR.

</details>

<details>

<summary>Why aren't my required checks triggering, even though my pull request is being tested in queue?</summary>

Most likely, you did not set up the required status checks to trigger for `trunk-merge/` branches. It is also possible that your CI provider just randomly never started testing on the Trunk Merge Queue branch, even after setting the required status checks to trigger. To assist with this, you can [configure a testing timeout](../administration/advanced-settings.md#timeout-for-tests-to-complete).

</details>

#### Merge Behavior <a href="#merge-behavior" id="merge-behavior"></a>

<details>

<summary>Can I choose the merge strategy for my pull requests?</summary>

No, Trunk Merge Queue exclusively uses a **squash merge** for all pull requests. It is not currently possible to select a different merge strategy like rebase or a standard merge commit on a per-PR basis.

</details>

<details>

<summary>How is the squash-merge commit message determined?</summary>

The commit message for the squashed commit is automatically generated from the **pull request's title and description**, which is the default behavior provided by GitHub.

</details>

<details>

<summary>Do Optimistic Merging or Batching ever merge multiple pull requests into a single commit?</summary>

No. Pull requests are always merged individually, and each PR will result in a separate commit in your `main` branch's history, regardless of your configuration.

Features like Optimistic Merging and Batching are validation and testing strategies, not merging strategies.

* [Optimistic Merging](../optimizations/optimistic-merging.md) uses the successful test of a pull request later in the queue to validate all the PRs ahead of it in the queue, allowing the entire sequence to be merged without waiting for the earlier PRs to finish testing.
* [Batching](../optimizations/batching.md) allows the queue to _test_ multiple PRs in a single CI job to save time and resources. After the test passes, the PRs in the batch are still merged one by one.

</details>

#### Queue Configuration <a href="#queue-configuration" id="queue-configuration"></a>

<details>

<summary>Can I create multiple merge queues for a single repository?</summary>

Currently, Trunk Merge Queue supports one merge queue per repository. If this is critical for your use case, [talk to us](../../setup-and-administration/support.md) and we'll consider adding support for your use case.

For validating significant changes to your CI process or queue configuration without impacting your primary workflow, the recommended approach is to use a fork of your repository. You can set up and test a separate merge queue on the fork to ensure your changes work as expected before applying them to your primary repository.

</details>

<details>

<summary>What are <code>trunk-temp/*</code> branches, and should CI run on them?</summary>

No, you should configure your CI to completely ignore `trunk-temp/*` branches. Running workflows on them will only create unnecessary or canceled builds.

The `trunk-temp/*` branch is a temporary, intermediate branch that the merge queue uses to assemble the necessary commits for a test run. Once the build is prepared, this branch is immediately renamed to a `trunk-merge/*` branch.

</details>

#### Priority & Overrides <a href="#prioirty-and-overrides" id="prioirty-and-overrides"></a>

<details>

<summary>How can I merge a pull request immediately?</summary>

**Recommended approach:** Use [PR Prioritization](../optimizations/priority-merging.md) to fast-track your PR through the queue while still validating it:

```
/trunk merge --priority=urgent
```

The `urgent` priority is the only level that will interrupt currently testing PRs. Your PR will immediately begin testing, and other PRs will restart after yours completes.

</details>

<details>

<summary>How do I merge an emergency pull request right now?</summary>

**Recommended approach:** Use [PR Prioritization](../optimizations/priority-merging.md) to fast-track your PR through the queue while still validating it:

```
/trunk merge --priority=urgent
```

The `urgent` priority is the only level that will interrupt currently testing PRs. Your PR will immediately begin testing, and other PRs will restart after yours completes.

</details>

### Failures, Errors & Debugging <a href="#failures-errors-and-debugging" id="failures-errors-and-debugging"></a>

<details>

<summary>How am I notified if my pull request fails in the queue?</summary>

When a pull request is removed from the queue due to a failure, the Trunk bot updates its comment on the original PR. This update includes direct links to the specific workflows that failed, allowing you to quickly investigate and resolve the issue. Example below.

<div align="left" data-full-width="false" data-with-frame="true"><figure><img src="../../.gitbook/assets/Screenshot 2025-10-09 at 3.28.03 PM.png" alt="Example of a Trunk bot PR comment, detailing a failed status check that caused the PR to be removed from the merge queue."><figcaption></figcaption></figure></div>

</details>

<details>

<summary>Why does my pull request consistently fail during testing due to "GitHub errors"?</summary>

Most likely, you have a [branch protection rule](../getting-started/configure-branch-protection.md) that affects merge branches.&#x20;

For example, the wild card rule `*/*` applies to `trunk-merge/...`. The Trunk GitHub app does not have admin privileges, so it fails to do some actions on protected branches. To resolve this, you must remove this rule or reach out to Trunk on our community Slack if that is not possible.

</details>

<details>

<summary>Why does my pull request keep failing to merge in the queue?</summary>

The two most likely problems are that you are restricting **who can merge** or that you have **disabled squash merges** into your repo. Trunk Merge Queue needs to use squash merges. To fix this, turn on `'allow squash merges'` for this repo in your GitHub setup.

</details>

<details>

<summary>Why do Dependabot and Renovate pull requests keep getting kicked from the queue?</summary>

By default, both [dependabot](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/managing-pull-requests-for-dependency-updates#changing-the-rebase-strategy-for-dependabot-pull-requests) and [renovate](https://docs.renovatebot.com/updating-rebasing/#updating-and-rebasing-branches) both will rebase their PRs whenever other PRs merge into their base branch. If that rebase happens when those PRs are in the queue, they will get kicked since they were updated. There are two ways to mitigate this:

1. Both dependabot and renovate can be configured to not automatically rebase, while renovate can specifically be configured to only rebase if there's a merge conflict ([dependabot](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/configuration-options-for-the-dependabot.yml-file#rebase-strategy), [renovate](https://docs.renovatebot.com/configuration-options/#rebasewhen))
2. Their PRs can be manually merged, and anything currently in the merge queue will restart with those merged changes

</details>

