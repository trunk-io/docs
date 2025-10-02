---
description: Troubleshooting and FAQ
---

# FAQ

## My PR is testing in my Merge Queue, but it doesn't look like my required status checks are being triggered.

Most likely, you did not set up the required status checks to trigger for `trunk-merge/` branches. It is also possible that your CI provider just randomly never started testing on the Trunk Merge Queue branch, even after setting the required status checks to trigger. To assist with this, you can [configure a testing timeout](../set-up-trunk-merge/advanced-settings.md#timeout-for-tests-to-complete).

## My PR appears to be ready but isn't entering the Merge Queue.

First, check the Trunk web app to see what Trunk is waiting on before putting your PR into the merge queue.&#x20;

Next, if something on that page doesn't look right, for example, it says that GitHub is still checking the mergeability of the PR, comment `/trunk merge` again in the PR.

## My PR is constantly failing when it starts testing because of "GitHub errors".

Most likely, you have a branch protection rule that affects merge branches. For example, the wild card rule `*/*` applies to `trunk-merge/...`. The Trunk GitHub app does not have admin privileges, so it fails to do some actions on protected branches. To resolve this, you must remove this rule or reach out to Trunk on our community Slack if that is not possible.

## My PR is constantly failing when attempting to merge it

The two most likely problems are that you are restricting **who can merge** or that you have **disabled squash merges** into your repo. Trunk Merge Queue needs to use squash merges. To fix this, turn on `'allow squash merges'` for this repo in your GitHub setup.

## Why do Dependabot and Renovate PRs keep getting kicked from the Merge Queue?

By default, both [dependabot](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/managing-pull-requests-for-dependency-updates#changing-the-rebase-strategy-for-dependabot-pull-requests) and [renovate](https://docs.renovatebot.com/updating-rebasing/#updating-and-rebasing-branches) both will rebase their PRs whenever other PRs merge into their base branch. If that rebase happens when those PRs are in the queue, they will get kicked since they were updated. There are two ways to mitigate this:

1. Both dependabot and renovate can be configured to not automatically rebase, while renovate can specifically be configured to only rebase if there's a merge conflict ([dependabot](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/configuration-options-for-the-dependabot.yml-file#rebase-strategy), [renovate](https://docs.renovatebot.com/configuration-options/#rebasewhen))
2. Their PRs can be manually merged, and anything currently in the merge queue will restart with those merged changes

## I have an emergency PR that needs to merge right now. How can I do that?

**Recommended approach:** Use [PR Prioritization](../pr-prioritization.md) to fast-track your PR through the queue while still validating it:

```
/trunk merge --priority=urgent
```

The `urgent` priority is the only level that will interrupt currently testing PRs. Your PR will immediately begin testing, and other PRs will restart after yours completes.

**Emergency bypass:** If you need to completely bypass the merge queue, you can merge the PR directly through GitHub as you normally would. The merge queue will restart everything currently testing to account for the new head of the merge branch. However, this means your emergency PR won't be validated by the merge queue's predictive testing.
