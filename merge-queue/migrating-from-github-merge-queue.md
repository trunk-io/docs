---
description: >-
  Move a repository from GitHub Merge Queue to Trunk Merge Queue with a brief
  dual-mode validation followed by a full switch.
---

# Migrate from GitHub Merge Queue

For teams switching from [GitHub Merge Queues](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/merging-a-pull-request-with-a-merge-queue) to Trunk Merge Queue, the recommended path is a short dual-mode validation followed by a full switch to Trunk.

{% hint style="success" %}
Looking for a more detailed comparison between Trunk and GitHub's Merge Queues? [Learn more](https://trunk.io/trunk-vs-github-merge-queue)
{% endhint %}

{% hint style="warning" %}
Running both queues for an extended period is not recommended. Use dual mode only to verify Trunk's settings against a few real PRs, then disable GitHub Merge Queue and run on Trunk only. See [Why complete the migration](#why-complete-the-migration) for the reasoning.
{% endhint %}

***

### Migration steps

The recommended sequence for admins moving a repository from GitHub Merge Queue to Trunk Merge Queue.

#### 1. Enable Trunk Merge Queue alongside GitHub

Follow [Getting Started](getting-started/) to install Trunk and configure your repository. Leave GitHub Merge Queue enabled for now.

Before opting your team in, turn off Trunk's automatic PR comments so developers aren't confused by comments from a queue they don't yet know about.

This setting is under **Merge Queue** tab **>** repository **> Settings >** toggle **off GitHub Comments.**

#### 2. Verify settings in dual mode

With both queues enabled, run a few real PRs through Trunk to confirm:

* Branch protection rules trigger the required checks you expect.
* Test orchestration policies match your repo's CI.
* [Advanced settings](administration/advanced-settings.md) such as timeouts, batching, and optimistic merging behave correctly for your repo.

Dual mode exists for this validation step only. The goal is to confirm Trunk's configuration before committing to the switch, not to run both queues indefinitely. See [What happens during dual mode](#what-happens-during-dual-mode) for behavior details.

#### 3. Turn off GitHub Merge Queue

Once you've validated Trunk's configuration, disable GitHub Merge Queue. In the GitHub repository, navigate to **Settings > Branches >** branch rule **>** toggle **off Require merge queue.** Click **Save changes** to confirm.

{% hint style="info" %}
Only users with GitHub admin permissions can manage merge queues for pull requests targeting selected branches of a repository. See GitHub's [managing merge queues](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/managing-a-branch-protection-rule#creating-a-branch-protection-rule) documentation for details.
{% endhint %}

#### 4. Re-enable Trunk's GitHub comments and announce

Turn Trunk's automatic PR comments back on under the **Merge Queue** tab **>** repository **> Settings >** toggle **on GitHub Comments.**

Share the change with your team. See [Dev-facing announcement copy](#dev-facing-announcement-copy) for a template you can paste into Slack or email, and [Using the Queue](using-the-queue/) for the full developer workflow.

***

### What happens during dual mode

While both queues are enabled, Trunk Merge Queue detects when a PR is merged outside of its queue (for example, by GitHub's merge queue or a direct push to the target branch):

* **If the PR is also in Trunk's queue**: Trunk automatically marks it as merged on its side.
* **If the PR is not in Trunk's queue**: Trunk restarts any PRs currently in its queue so they can test on top of the new commit.

This ensures that Trunk always tests against the latest state of your target branch and never merges a PR that would conflict with a commit that landed externally.

#### Why complete the migration

The handling above is correct, but every restart cancels in-flight test runs and re-tests against the new target branch head. With both queues active and busy, in-flight PRs from both sides will preempt each other, and your team will see slower merge times overall. That is why dual mode is a verification step, not a long-term mode.

{% hint style="info" %}
A repository should be configured to use ONLY Trunk Merge Queue. Running both queues long-term degrades the merge experience for the whole team.
{% endhint %}

***

### Dev-facing announcement copy

Once you've cut over, share the change with your team. Below is a template admins can adapt for Slack or email.

> **Heads up: we're moving to Trunk Merge Queue.**
>
> Starting \[date], pull requests on `[repo]` will merge through Trunk Merge Queue instead of GitHub's. The day-to-day flow is the same: open a PR, get required checks green, then post `/trunk merge` on the PR instead of clicking GitHub's "Merge when ready" button.
>
> Trunk will leave a comment on each PR with its queue position and status. The full developer workflow is documented at \[link to Trunk's Using the Queue page].
>
> Questions? Reply in this thread or DM \[admin contact].

***

### Getting help

If you or your team are running into issues, join the [Trunk Slack community](https://slack.trunk.io/) for assistance.
