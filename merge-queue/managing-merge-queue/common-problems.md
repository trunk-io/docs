---
description: Troubleshooting and FAQ
---

# Merge Queue FAQ

### Can I add a pull request to the merge queue before all its required status checks have passed?

Yes. A pull request can be submitted to the queue at any time, even if it's not yet ready to merge. The pull request will enter the queue in a "Queued" state and wait for all branch protection rules (like passing status checks and required reviews) to be met. Once the PR is ready, Trunk Merge Queue will automatically move it into the testing phase.

### Do settings like "Optimistic Merging" or "Batching" cause multiple pull requests to be merged into a single commit?

No. Pull requests are always merged individually, and each PR will result in a separate commit in your `main` branch's history, regardless of your configuration.

Features like Optimistic Merging and Batching are validation and testing strategies, not merging strategies.

* [Optimistic Merging](../concepts/optimistic-merging.md) uses the successful test of a pull request later in the queue to validate all the PRs ahead of it in the queue, allowing the entire sequence to be merged without waiting for the earlier PRs to finish testing.
* [Batching](../concepts/batching.md) allows the queue to _test_ multiple PRs in a single CI job to save time and resources. After the test passes, the PRs in the batch are still merged one by one.

### How am I notified if my pull request fails in the merge queue?

When a pull request is removed from the queue due to a failure, the Trunk bot updates its comment on the original PR. This update includes direct links to the specific workflows that failed, allowing you to quickly investigate and resolve the issue. Example below.

<div align="left" data-full-width="false" data-with-frame="true"><figure><img src="../../.gitbook/assets/Screenshot 2025-10-09 at 3.28.03 PM.png" alt="Example of a Trunk bot PR comment, detailing a failed status check that caused the PR to be removed from the merge queue."><figcaption></figcaption></figure></div>

### Can I create multiple merge queues for a single repository? For example, can I have a separate 'test' queue for validating CI changes?

Currently, Trunk Merge Queue supports one merge queue per repository. If this is critical for your use case, [talk to us](../../support.md) and we'll consider adding support for your use case.

For validating significant changes to your CI process or queue configuration without impacting your primary workflow, the recommended approach is to use a fork of your repository. You can set up and test a separate merge queue on the fork to ensure your changes work as expected before applying them to your primary repository.

### My pull request is testing in my Merge Queue, but it doesn't look like my required status checks are being triggered.

Most likely, you did not set up the required status checks to trigger for `trunk-merge/` branches. It is also possible that your CI provider just randomly never started testing on the Trunk Merge Queue branch, even after setting the required status checks to trigger. To assist with this, you can [configure a testing timeout](advanced-settings.md#timeout-for-tests-to-complete).

### My pull request appears to be ready but isn't entering the Merge Queue.

First, check the Trunk web app to see what Trunk is waiting on before putting your PR into the merge queue.&#x20;

Next, if something on that page doesn't look right, for example, it says that GitHub is still checking the mergeability of the PR, comment `/trunk merge` again in the PR.

### My pull request is constantly failing when it starts testing because of "GitHub errors".

Most likely, you have a branch protection rule that affects merge branches. For example, the wild card rule `*/*` applies to `trunk-merge/...`. The Trunk GitHub app does not have admin privileges, so it fails to do some actions on protected branches. To resolve this, you must remove this rule or reach out to Trunk on our community Slack if that is not possible.

### My pull request is constantly failing when attempting to merge it

The two most likely problems are that you are restricting **who can merge** or that you have **disabled squash merges** into your repo. Trunk Merge Queue needs to use squash merges. To fix this, turn on `'allow squash merges'` for this repo in your GitHub setup.

### Why do Dependabot and Renovate pull requests keep getting kicked from the Merge Queue?

By default, both [dependabot](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/managing-pull-requests-for-dependency-updates#changing-the-rebase-strategy-for-dependabot-pull-requests) and [renovate](https://docs.renovatebot.com/updating-rebasing/#updating-and-rebasing-branches) both will rebase their PRs whenever other PRs merge into their base branch. If that rebase happens when those PRs are in the queue, they will get kicked since they were updated. There are two ways to mitigate this:

1. Both dependabot and renovate can be configured to not automatically rebase, while renovate can specifically be configured to only rebase if there's a merge conflict ([dependabot](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/configuration-options-for-the-dependabot.yml-file#rebase-strategy), [renovate](https://docs.renovatebot.com/configuration-options/#rebasewhen))
2. Their PRs can be manually merged, and anything currently in the merge queue will restart with those merged changes

### I have an emergency pull request that needs to merge right now. How can I do that?

**Recommended approach:** Use [PR Prioritization](../concepts-and-optimizations/pr-prioritization.md) to fast-track your PR through the queue while still validating it:

```
/trunk merge --priority=urgent
```

The `urgent` priority is the only level that will interrupt currently testing PRs. Your PR will immediately begin testing, and other PRs will restart after yours completes.

**Emergency bypass:** If you need to completely bypass the merge queue, you can merge the PR directly through GitHub as you normally would. The merge queue will restart everything currently testing to account for the new head of the merge branch. However, this means your emergency PR won't be validated by the merge queue's predictive testing.
