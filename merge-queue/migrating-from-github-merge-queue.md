# Migrating From GitHub Merge Queue

For teams switching from [GitHub Merge Queues](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/merging-a-pull-request-with-a-merge-queue) to Trunk Merge Queue, the process is straight forward.&#x20;

At a high level the steps are:

1. Turn off GitHub Merge Queue
2. Turn on Trunk Merge Queue

Its really that straight forward.

***

### Turn off GitHub Merge Queue

To start, you will need to disable the exising merge queue for the target repository.  This can be done by navigating to the repository and opening **Settings > Branches >** branch rule **>** toggle **off Require merge queue.** Be sure to click **Save changes** to confirm the settings.

{% hint style="info" %}
Note that only users with admin permissions can manage merge queues for pull requests targeting selected branches of a repository. More information on  [manage merge queues](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/managing-a-branch-protection-rule#creating-a-branch-protection-rule) can be found in the GitHub documentation.
{% endhint %}

***

### Enable Trunk Merge Queue

Follow the [Quickstart guide](set-up-trunk-merge/) to setup your repo with Trunk Merge Queue and configure the [settings](set-up-trunk-merge/advanced-settings.md) for your repository.

It is important that a repository is configured to use ONLY Trunk Merge Queue and no other merge queue tools. &#x20;

***

### Getting Help

If you or your team are running into issues be sure to join the [Trunk Slack community](https://slack.trunk.io/) for assistance.
