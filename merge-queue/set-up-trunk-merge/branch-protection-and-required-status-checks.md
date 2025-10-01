---
description: >-
  Configure GitHub branch protection rules and define which CI status checks
  must pass before Trunk Merge Queue can merge pull requests into your protected
  branch.
---

# Branch Protection & Required Status Checks

## Branch Protection & Required Status Checks

Trunk Merge Queue respects GitHub's branch protection rules and works with both Classic branch protection rules and Rulesets. Since Merge Queue ultimately merges PRs through GitHub, any protection rules on your target branch (like required code reviews or status checks) will still apply before PRs can enter the queue.

### Using Rulesets vs. Classic Rules

You can use GitHub's newer Rulesets feature alongside Classic branch protection rules—both systems work together through GitHub's rule layering. However, there's one important requirement:

{% hint style="danger" %}
**Configure push permission restrictions using Classic branch protection rules only.**
{% endhint %}

Trunk Merge Queue cannot programmatically detect push restrictions configured in Rulesets due to GitHub API limitations. To ensure Merge Queue can properly respect push permissions:

1. Go to **Settings** > **Branches** in your repository
2. Edit or create a Classic branch protection rule for your target branch
3. Under "Rules applied to everyone including administrators," select:
   * **Restrict who can push to matching branches**
   * **Restrict pushes that create matching branches**
4. **Add the `trunk-io` bot** to the list of allowed actors (required for Trunk Merge Queue to merge PRs)
5. (Optional) Add Organization admins and repository admins who need the ability to perform emergency merges outside the queue

**For urgent PRs:** Regular users should use [PR Prioritization](../pr-prioritization.md) with `--priority=urgent` or `--priority=high` to fast-track PRs through the queue while still maintaining validation. Direct push access is only needed for rare situations where the queue itself must be bypassed entirely.

All other branch protection settings (required reviews, status checks, signed commits, etc.) can be configured using either Classic rules or Rulesets.

#### Critical: Exclude Trunk Branches from Protection

Trunk Merge Queue creates temporary branches (`trunk-temp/*` and `trunk-merge/*`) to test PRs before merging them. Trunk needs unrestricted access to create, push to, and delete these branches. If they're protected by branch rules, Merge Queue cannot function.

**Ensure your branch protection rules do NOT apply to:**

* `trunk-temp/*`
* `trunk-merge/*`

If these branches are protected (for example, by a wildcard rule like `*/*`), Merge Queue will encounter GitHub permission errors and cannot function properly.

**To verify this:**

1. Go to **Settings** > **Branches** in your repository
2. Review all Classic branch protection rules
3. Check that no rules use wildcard patterns that would match `trunk-temp/*` or `trunk-merge/*`&#x20;
4. If you have rules using wildcards like `*/*`, `**/*`, or similar patterns, you'll need to either:
   * Remove those wildcard rules and create more specific rules, or
   * Ensure those rules have the `trunk-io` bot in the bypass list

{% hint style="info" %}
If there are any questions or help is needed, reach out on our questions or help is needed, reach out on our [community Slack](https://slack.trunk.io/)!
{% endhint %}

## Draft PRs

By default, Trunk Merge Queue creates **draft pull requests** when testing PRs in the queue. This allows Trunk to leverage your existing PR-triggered CI workflows—the same status checks that run when you open a regular PR will automatically run when Trunk tests changes in the queue.

#### When to Disable Draft PR Creation

In some cases, you may not want every check triggered by PR creation to run during queue testing. For example:

* You deploy preview environments for every PR that reviewers interact with
* You run expensive integration tests or security scans only for review purposes
* You have PR-triggered workflows that are unnecessary for merge validation

If you need different CI behavior for queue testing versus PR review, you can disable draft PR creation by navigating to **Settings > Repositories >** select your repository **> Merge >** toggle off **Trunk Draft PR Creation.**

#### What Happens When Draft PRs are Disabled

When draft PR creation is disabled, Trunk Merge Queue creates `trunk-merge/*` branches instead of draft PRs to test changes. You'll need to:

1. Configure push-triggered workflows in your CI provider to run on `trunk-merge/*` branches
2. Define which status checks Trunk should wait for before merging (see Define Required Status Checks below)

This gives you complete control over which CI jobs run during merge queue testing versus during PR review.

#### Configure a Push Triggered Workflow For Required Status Checks

{% hint style="warning" %}
**This section only applies if you've disabled Draft PR creation.** If Draft PRs are enabled (the default), Trunk automatically triggers your existing PR-based CI workflows and you can skip this section.
{% endhint %}

When Draft PR creation is disabled, Trunk Merge Queue creates branches with the prefix `trunk-merge/` to test PRs. You need to configure your CI provider to run status checks whenever branches matching this pattern are pushed.

**For GitHub Actions**

Set up a `push`-triggered workflow filtered to `trunk-merge/**` branches:

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

## Define Required Status Checks For Testing

Trunk needs to know which _status checks_ must pass while testing pull requests in the queue before it can merge a PR into your branch. Merge can pick up this list of required statuses in one of two ways:

{% tabs %}
{% tab title="Automatic (default)" %}
In automatic mode, the status checks specified in your branch's [GitHub branch protection](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches#require-status-checks-before-merging) rule will be used.

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
Use custom when the status checks you want to enforce before merging do not match 1:1 with your GitHub branch protection rules. The names of the required\_statuses must match as specified on your [GitHub status checks](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/collaborating-on-repositories-with-code-quality-features/about-status-checks) or [jobs](https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions#jobs)\
\
Custom `required_statuses` defined in the `.trunk/trunk.yaml` file take precedence over the GitHub required status checks from branch protection.
{% endtab %}
{% endtabs %}

## Restricting Push permissions

Trunk needs access to push to protected branches, and works best alone. Add protections to restrict who can push to matching branches. In most cases, permissions should be restricted to Organization admins, repository admins and the `trunk-io` bot.

To update this configuration selecting your repository, navigate to **Settings** **> Branches >** your branch rule **> Edit >** toggle **Restrict who can push to matching branches and toggle  Restrict pushes that create matching branches**

Remove any existing configurations or special permissions for roles or groups and add an exception for the `trunk-io` bot only. Be sure to click **Save changes** to confirm the settings.

<figure><img src="../../.gitbook/assets/docs-mq-restrict-push.png" alt=""><figcaption></figcaption></figure>
