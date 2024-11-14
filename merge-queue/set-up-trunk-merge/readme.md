---
description: How to set up Trunk Merge Queue for your project
---

# Setup

Minimal set up is required to get started with Trunk Merge Queue, as it syncs with GitHub in order to run the same tests you're already running on PRs and require the same Status Checks to pass before merging.

### Connect your Trunk Organization to GitHub

Sign up at [app.trunk.io](https://app.trunk.io/signup?intent=merge\&tr\_s=mergesetup\&tr\_l=1), create a Trunk organization, and connect it to your GitHub repositories. If your repository is already connected to your Trunk organization, you can skip this step.

Select the repository you would like to use and click **Get Started.**

<figure><img src="../../.gitbook/assets/image (23).png" alt=""><figcaption></figcaption></figure>

### Set Up Trunk Merge Queue

Go to the Merge tab. You will see the "Set Up Trunk Merge Queue" page. From there, you can specify:

1. The name of the branch that Trunk Merge Queue should help manage merging PRs into.
2. The [number](advanced-settings.md#concurrency) of Pull Requests that Merge can test at the same time.
3. The [mode](../parallel-queues/) that Trunk Merge Queue Queues will start in.

<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1).png" alt="" width="414"><figcaption></figcaption></figure>

### Testing PRs In the Queue

Trunk will automatically create Draft PRs when PRs begin testing in the queue. The draft PR will contain the tip of the branch you're merging into, the change in the PR, and changes in any PRs in front of this one in the queue

By using draft PRs, Trunk will leverage your existing status checks that gate your PRs already with tests and linters. When the new draft PRs are created, Trunk will wait for your existing status checks to run, and merge PRs when they pass.

{% hint style="info" %}
If you do not want every check that runs when a PR is opened to also run when Trunk Merge Queue tests PRs, you can disable draft PR creation and run tests on branches instead. See [#draft-prs](advanced-settings.md#draft-prs "mention").
{% endhint %}

Trunk Merge Queue syncs with GitHub's branch protection rules, and will require the same status checks that need to pass in order to merge a PR to also pass when testing the PR in the queue.

### Submit Pull Requests

Try making a simple change on a branch and submit it as PR in GitHub.

Now trigger Trunk Merge Queue to process this PR using either a comment on the PR in GitHub or using the Trunk CLI.

{% tabs %}
{% tab title="GitHub Pull Request View" %}
Comment `/trunk merge` on a pull request

<figure><img src="../../.gitbook/assets/image (26).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Trunk CLI" %}
```bash
# Authenticate with trunk service
$ trunk login
# Queue pull request for merge
$ trunk merge {pr-number}
```
{% endtab %}
{% endtabs %}

If you have any problems with merge queueing PRs, take a look at the [branch protection](advanced-settings.md#branch-protection) docs.

### Pull Request Processing

Once a PR is submitted to the Merge queue, it will start as _Not Ready_ until all of the required conditions to submit it are met. Once ready, the Merge Queue will pick it up and run the tests. Once the tests pass, the PR may still need to wait for upstream PRs in the queue to finish their testing. Once the remaining upstream PRs are complete, the PR will be merged and then removed from the Merge Queue. If a PR fails or is canceled then it will go to the failed or canceled state. Read more about [PR States](../reference.md#pr-states).

## Success!

Now Trunk Merge Queue is setup with your repo. Whenever a PR is pushed to your merge branch it will be safely tested and automatically merged when all tests pass, regardless of the order they were pushed in.

### Next Steps

Now that you have the Merge Queue setup and running you can explore the knobs you can enable that will give you the most performant Merge solution. Explore the features powering Trunk Merge Queue here:

<table data-view="cards"><thead><tr><th align="center"></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td align="center">Batching</td><td><a href="../batching.md">batching.md</a></td></tr><tr><td align="center">Dynamic Parallel Queues</td><td><a href="../parallel-queues/">parallel-queues</a></td></tr><tr><td align="center">Optimistic Merging</td><td><a href="../optimistic-merging.md">optimistic-merging.md</a></td></tr><tr><td align="center">Pending Failure Depth</td><td><a href="../pending-failure-depth.md">pending-failure-depth.md</a></td></tr><tr><td align="center">Prioritization</td><td><a href="../pr-prioritization.md">pr-prioritization.md</a></td></tr><tr><td align="center">Flaky Test Protection</td><td><a href="../anti-flake-protection.md">anti-flake-protection.md</a></td></tr></tbody></table>
