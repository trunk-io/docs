# Migrating From GitHub Merge Queue

For teams switching from [GitHub Merge Queues](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/merging-a-pull-request-with-a-merge-queue) to Trunk Merge Queue, the process is straight forward.&#x20;

At a high level the steps are:

1. Turn off GitHub Merge Queue
2. Turn on Trunk Merge Queue

Its really that straight forward.

{% hint style="success" %}
Not ready to jump in completely right away, thats ok, checkout the [#pre-migration](migrating-from-github-merge-queue.md#pre-migration "mention") section below for an example migration game plan that keeps your teams working.
{% endhint %}

***

### Turn off GitHub Merge Queue

To start, you will need to disable the exising merge queue for the target repository.  This can be done by navigating to the repository and opening **Settings > Branches >** branch rule **>** toggle **off Require merge queue.** Be sure to click **Save changes** to confirm the settings.

{% hint style="info" %}
Note that only users with admin permissions can manage merge queues for pull requests targeting selected branches of a repository. More information on  [manage merge queues](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/managing-a-branch-protection-rule#creating-a-branch-protection-rule) can be found in the GitHub documentation.
{% endhint %}

***

### Enable Trunk Merge Queue

Follow the [Quickstart guide](set-up-trunk-merge/) to setup your repo with Trunk Merge Queue and configure the [settings](set-up-trunk-merge/advanced-settings.md) for your repository.



***

### Pre Migration

Before migrating fully, it may be useful to evaluate the workflows "quiety" and confirm settings before conveting your repository to an entirly new workflow.

Here are some useful steps to get you familiar with the Trunk Merge Queue workflow without disrupting engineers.

#### Enable trunk merge for testing but with the automatic comments disabled

While evaluating and testing Trunk Merge Queue for your team, we suggest disabling automatic comments on PRs.  This can be done by toggling off GitHub Comments in the Trunk web app.

This setting is found under **Merge Queue** tab **>** repository **> Settings >** toggle **off GitHub Comments.**

#### Make the Switch

Once you have [configured settings](set-up-trunk-merge/advanced-settings.md) and tested out the workflow quietly, turn off other merge tools (like [GitHub merge queue](migrating-from-github-merge-queue.md#turn-off-github-merge-queue)), re-enable GitHub comments in the Trunk web app under the **Merge Queue** tab **>** repository **> Settings >** toggle **on GitHub Comments**

{% hint style="info" %}
It is important that a repository is configured to use ONLY Trunk Merge Queue and no other merge queue tools for best results.
{% endhint %}

#### Share the News

Now that you have migrated to Trunk Merge Queue, be sure to share the workflow with your team, using [Broken link](broken-reference "mention") as a great place to start.

***

### Getting Help

If you or your team are running into issues be sure to join the [Trunk Slack community](https://slack.trunk.io/) for assistance.
