---
description: How to set up Trunk Merge for your project
---

# Setup

### Connect your Trunk Organization to GitHub

Sign up at [app.trunk.io](https://app.trunk.io/), create a Trunk organization, and connect it to your GitHub repositories. If your repository is already connected to your Trunk organization, you can skip this step.

Select the repository you would like to use and click **Get Started.**

<figure><img src="../../.gitbook/assets/image (23).png" alt=""><figcaption></figcaption></figure>

### Set Up Trunk Merge

Go to the Merge tab. You will see the "Set Up Trunk Merge" page. From there, you can specify:

1. The name of the branch that Trunk Merge should help manage merging PRs into.
2. The [number](advanced-settings.md#concurrency) of Pull Requests that Merge can test at the same time.
3. The [mode](../parallel-queues/) that Trunk Merge Queues will start in.

<figure><img src="../../.gitbook/assets/image (1) (1) (1).png" alt="" width="414"><figcaption></figcaption></figure>

### Define Required Status Checks For Testing

Trunk needs to know which _status checks_ must pass while testing pull requests in the queue before it can merge a PR into your branch. Merge can pick up this list of required statuses in one of two ways:

{% tabs %}
{% tab title="Automatic (default)" %}
In automatic mode, the status checks specified in your branch's [GitHub branch protection](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches#require-status-checks-before-merging) rule will be used.\
\
See GitHub's doc for more information on configuring [required status checks](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches#require-status-checks-before-merging).
{% endtab %}

{% tab title="Custom (trunk.yaml)" %}
```
version: 0.1 
```

```
cli:
  version: 1.16.0
merge: 
  required_statuses:
    - Trunk Check 
    - Unit tests & test coverage
    # Add more required statuses here
```

\
Use custom when the status checks you want to enforce before merging do not match 1:1 with your GitHub branch protection rules. The names of the required\_statuses must match as specified on your [ ](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/collaborating-on-repositories-with-code-quality-features/about-status-checks)[GitHub status checks](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/collaborating-on-repositories-with-code-quality-features/about-status-checks) or [jobs](https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions#jobs) \
\
Custom `required_statuses` defined in the `.trunk/trunk.yaml` file take precedence over the GitHub required status checks from branch protection.&#x20;
{% endtab %}
{% endtabs %}

### Configure a Push Triggered Workflow For Required Status Checks

Trunk Merge creates branches with the prefix `trunk-merge/` in order to test PRs. To ensure the required statuses Merge should gate on get triggered when it tests PRs, your CI provider must be configured to run the status checks you care about whenever a branch with that prefix is pushed to.

{% hint style="info" %}
If you already have tests that trigger on new PRs, you can use the [Draft PR Creation](https://docs.trunk.io/merge/set-up-trunk-merge/advanced-settings#draft-pr-creation) feature to let Trunk Merge create draft PRs instead of setting up a push triggered workflow.
{% endhint %}

For GitHub Actions, that'll mean setting up a `push`-triggered workflow, filtered to `trunk-merge/**` branches, like so:

```yaml
name: Run Required Checks
run-name: PR Checks for ${{ github.ref_name }}

# Trigger jobs whenever Trunk Merge tests a PR using a `trunk-merge/` branch
on:
  push:
    branches:
      - trunk-merge/**

jobs:
  trunk_check:
    runs-on: ubuntu-latest
    # "Trunk Check" is specified in merge.required_status above
    name: Trunk Check
    steps:
      - name: Checkout
        uses: actions/checkout@v3

  unit_tests:
    runs-on: ubuntu-latest
    # "Unit tests & test coverage" is specified in merge.required_status above
    name: Unit tests & test coverage
    steps:
      - name: Checkout
        uses: actions/checkout@v3

    # Add more steps here..    
```

Now you are ready to submit your first PR. Let's go!

### Submit Pull Requests

Try making a simple change on a branch and submit it as PR in GitHub.

Now trigger Trunk Merge to process this PR using either a comment on the PR  in GitHub or using the Trunk CLI.

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

Now Trunk Merge is setup with your repo. Whenever a PR is pushed to your merge branch it will be safely tested and automatically merged when all tests pass, regardless of the order they were pushed in.

### Next Steps

Now that you have the Merge Queue setup and running you can explore the knobs you can enable that will give you the most performant Merge solution. Explore the features powering Trunk Merge here:

<table data-view="cards"><thead><tr><th align="center"></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td align="center">Batching</td><td><a href="../batching.md">batching.md</a></td></tr><tr><td align="center">Dynamic Parallel Queues</td><td><a href="../parallel-queues/">parallel-queues</a></td></tr><tr><td align="center">Optimistic Merging</td><td><a href="../optimistic-merging.md">optimistic-merging.md</a></td></tr><tr><td align="center">Pending Failure Depth</td><td><a href="../pending-failure-depth.md">pending-failure-depth.md</a></td></tr><tr><td align="center">Prioritization</td><td><a href="../pr-prioritization.md">pr-prioritization.md</a></td></tr><tr><td align="center">Flaky Test Protection</td><td><a href="../anti-flake-protection.md">anti-flake-protection.md</a></td></tr></tbody></table>
