---
description: >-
  Explanation of settings for states, timeouts, concurrency, and branch
  protection.
---

# Settings

We offer some knobs and dials when configuring Merge. All of the following settings are specific to individual Merge Queues, and can be applied can be applied at [app.trunk.io](https://app.trunk.io/login?intent=merge) in the `Settings > Repositories > Repo-Name` page.

## Merge Queue States

You can change the state of your Merge Queue, which will affect behavior around PRs entering the queue and merging. PRs will always continue testing no matter what state the Merge Queue is in. Below are the possible different states:

<table><thead><tr><th width="149">State</th><th>Will PRs Enter the Queue?</th><th>Will PRs Merge After Testing?</th></tr></thead><tbody><tr><td><code>Running</code></td><td>Yes <span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td><td>Yes <span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td></tr><tr><td><code>Paused</code></td><td>No <span data-gb-custom-inline data-tag="emoji" data-code="274c">❌</span></td><td>No <span data-gb-custom-inline data-tag="emoji" data-code="274c">❌</span></td></tr><tr><td><code>Draining</code></td><td>No <span data-gb-custom-inline data-tag="emoji" data-code="274c">❌</span></td><td>Yes <span data-gb-custom-inline data-tag="emoji" data-code="2705">✅</span></td></tr></tbody></table>

There is an additional state, `Switching Modes`, that functions exactly like `Draining`. The Merge Queue enters this state when you switch the mode of the queue while PRs are still testing.

## Timeout for Tests to Complete

Configure how long a PR's test can run before auto-cancelling while testing in the Merge Queue. If a long-running test is detected, Merge will automatically cancel the test.

{% hint style="info" %}
If you're unsure about what timeout to set, you can use our [CI Analytics](https://trunk.io/products/ci-analytics) to analyze the runtime of your CI.
{% endhint %}

For example, assuming a timeout of 4 hours:

* At 3:00, Bob submits PR 456 to the Merge Queue.
* At 3:05, PR 456 starts testing using Bob's CI system.
* At 7:05, Trunk cancels PR 456, since PR 456 is still testing.

## Concurrency

Configure how many PRs may test in parallel. A larger number may increase throughput, since more PRs are tested in parallel, but at the expense of CI, since more jobs are running in parallel. When the queue is at capacity, PRs will still be submitted to it, but they will not begin testing until a PR leaves the queue.

{% hint style="info" %}
If your testing workload contains some flaky tests, a deeper queue (i.e. a higher concurrency) may struggle. Running Merge in Parallel mode can help with this, as it will reduce the average depth of your merge queue, since all PRs won't be queued directly behind each other.
{% endhint %}

For example, assuming a concurrency of 3:

* At 12:00, Alice submits PR 1000 to the Merge Queue, and it starts testing.
* At 12:05, Bob submits PR 888 to the Merge Queue, and it starts testing.
* At 12:10, Charlie submits PR 777 to the Merge Queue, and it starts testing.
* At 12:15, Alice submits PR 1001 to the Merge Queue. Tests do not start, because the Merge Queue is at its concurrency limit.

## Branch Protection

Trunk Merge Queue, since it will eventually merge your PR on GitHub, is still **bound by any protection rules set in GitHub** that affect the branch Trunk Merge Queue will merge into or that affect your Trunk Merge Queue branch. For example, if a PR requires at least one review to merge, then Trunk Merge Queue would display `'not mergable GitHub yet'` until that PR has a review.

If you have trouble with merge queueing PRs, check if there is any kind of additional branch protection set up on your repo. Existing branch protection rules must be changed in order to **not** protect branches in the form of `trunk-temp/*` and `trunk-merge/*` . If either of those branches are considered protected in any way according to GitHub (e.g., if there is a `*/*` branch protection rule), then Merge will not be able to run tests properly due to GitHub permission errors.

If there are any questions or help is needed, reach out on our questions or help is needed, reach out on our [community slack](https://slack.trunk.io/)!

### Draft PRs

In some cases, you might not want every check that gets triggered when a PR gets created to run when testing PRs in the merge queue (say for example, you deploy your frontend on every PR so that reviewers can interact with it). In that case, if you prefer to use Trunk Merge Queue without Draft PRs, you can disable it by navigating to **Settings > Repositories >** select your repository **> Merge >** toggle **Trunk Draft PR Creation.**\
\
When draft PR creation is disabled, you will need to configure push-triggered workflows to run on branches to test each merge request. You can also configure custom gating for your PRs if you want to gate on a different set of checks for Trunk Merge Queue.

#### Configure a Push Triggered Workflow For Required Status Checks

When creating Draft PRs is disabled, Trunk Merge Queue creates branches with the prefix `trunk-merge/` in order to test PRs. To ensure the required statuses Merge should gate on get triggered when it tests PRs, your CI provider must be configured to run the status checks you care about whenever a branch with that prefix is pushed to.

{% hint style="info" %}
If you already have tests that trigger on new PRs, you can use the [Draft PR Creation](https://docs.trunk.io/merge/set-up-trunk-merge/advanced-settings#draft-pr-creation) feature to let Trunk Merge Queue create draft PRs instead of setting up a push triggered workflow.
{% endhint %}

For GitHub Actions, that'll mean setting up a `push`-triggered workflow, filtered to `trunk-merge/**` branches, like so:

```yaml
name: Run Required Checks
run-name: PR Checks for ${{ github.ref_name }}

# Trigger jobs whenever Trunk Merge Queue tests a PR using a `trunk-merge/` branch
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

#### Define Required Status Checks For Testing

Trunk needs to know which _status checks_ must pass while testing pull requests in the queue before it can merge a PR into your branch. Merge can pick up this list of required statuses in one of two ways:

{% tabs %}
{% tab title="Automatic (default)" %}
In automatic mode, the status checks specified in your branch's [GitHub branch protection](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches#require-status-checks-before-merging) rule will be used.&#x20;

Trunk Merge Queue does not work with GitHub's new Rulesets. Make sure to click the **Add classic branch protection rule** link when configuring new rules.

<figure><img src="../../.gitbook/assets/cubesGreen (3).png" alt=""><figcaption></figcaption></figure>

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
Use custom when the status checks you want to enforce before merging do not match 1:1 with your GitHub branch protection rules. The names of the required\_statuses must match as specified on your[GitHub status checks](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/collaborating-on-repositories-with-code-quality-features/about-status-checks) or [jobs](https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions#jobs)\
\
Custom `required_statuses` defined in the `.trunk/trunk.yaml` file take precedence over the GitHub required status checks from branch protection.
{% endtab %}
{% endtabs %}
