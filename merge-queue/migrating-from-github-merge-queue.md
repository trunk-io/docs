---
description: >-
  Move a repository from GitHub Merge Queue to Trunk Merge Queue with a clean
  same-day switch. Optional cautious route for teams that want to validate
  first.
---

# Migrate from GitHub Merge Queue

For teams switching from [GitHub Merge Queues](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/merging-a-pull-request-with-a-merge-queue) to Trunk Merge Queue, the recommended path is a clean same-day switch: set up Trunk, disable GitHub Merge Queue, and announce to your team.

{% hint style="success" %}
Looking for a more detailed comparison between Trunk and GitHub's Merge Queues? [Learn more](https://trunk.io/trunk-vs-github-merge-queue)
{% endhint %}

{% hint style="warning" %}
Don't run both queues for an extended period. Long-term dual mode means in-flight PRs from both sides preempt each other and your team will see slower merge times overall. Pick one queue.
{% endhint %}

***

### Migration steps

The recommended sequence for admins moving a repository from GitHub Merge Queue to Trunk Merge Queue.

#### 1. Set up Trunk Merge Queue

Follow [Getting Started](getting-started/) to install Trunk and configure your repository. Configure branch protection rules to include Trunk's status checks, and review [Advanced settings](administration/advanced-settings.md) such as timeouts, batching, and optimistic merging for your repo.

Keep Trunk's automatic PR comments off for now so developers aren't surprised by comments from a queue they don't yet know about. This setting is under **Merge Queue** tab **>** repository **> Settings >** toggle **off GitHub Comments.**

#### 2. Disable GitHub Merge Queue

In the GitHub repository, navigate to **Settings > Branches >** branch rule **>** toggle **off Require merge queue.** Click **Save changes** to confirm.

{% hint style="info" %}
Only users with GitHub admin permissions can manage merge queues for pull requests targeting selected branches of a repository. See GitHub's [managing merge queues](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/managing-a-branch-protection-rule#creating-a-branch-protection-rule) documentation for details.
{% endhint %}

#### 3. Turn on Trunk's PR comments

Turn Trunk's automatic PR comments back on under **Merge Queue** tab **>** repository **> Settings >** toggle **on GitHub Comments.** This is when Trunk becomes visible to your team on every PR.

#### 4. Announce to your team

Share the change with your team. See [Dev-facing announcement copy](#dev-facing-announcement-copy) for a template you can paste into Slack or email, and [Using the Queue](using-the-queue/) for the full developer workflow.

***

### Cautious route: validate first

If you want to confirm Trunk's configuration on a few real PRs before disabling GitHub Merge Queue, run a short validation window before doing step 2 above.

1. Complete step 1 (set up Trunk Merge Queue, GitHub Comments toggled off).
2. As an admin, post `/trunk merge` on a handful of representative PRs to confirm Trunk processes them as expected. Watch for required checks running, optimistic merging behavior, timeouts, and any anti-flake protections behaving as you'd expect.
3. Once confident, continue with steps 2 through 4 above.

During this window, most PRs continue merging through GitHub's queue as normal. Only PRs where the admin explicitly posts `/trunk merge` enter Trunk's queue.

{% hint style="info" %}
**Safety net.** If a PR ends up enqueued in both queues at once, or if a commit lands on your target branch from outside Trunk while Trunk has in-flight PRs, Trunk handles it correctly:

* A queued PR merged externally is marked as merged on Trunk's side.
* An external commit on the target branch restarts any of Trunk's in-flight PRs so they re-test on the new target branch head.

These are safeguards against accidental collisions during validation, not features that support long-term coexistence.
{% endhint %}

***

### Dev-facing announcement copy

Once you've switched, share the change with your team. Below is a template admins can adapt for Slack or email.

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
