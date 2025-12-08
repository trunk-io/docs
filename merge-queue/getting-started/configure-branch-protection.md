# Configure branch protection

### Prerequisites

Before configuring branch protection:

* [ ] Trunk GitHub App installed and queue created (previous step)
* [ ] Repository has CI/CD configured (GitHub Actions, CircleCI, etc.)
* [ ] CI runs on pull requests and reports status checks to GitHub
* [ ] You have admin access to repository settings

### How Trunk Merge Queue works

Trunk Merge Queue respects GitHub's branch protection rules and works with both Classic branch protection rules and Rulesets. Since Merge Queue ultimately merges pull requests through GitHub, any protection rules on your target branch (like required code reviews or status checks) will still apply.

### Choose your testing approach

Trunk Merge Queue can test pull requests in two ways. Choose the approach that fits your CI setup:

#### Draft PR mode (Recommended - Default) <a href="#draft-pr-mode-recommended---default" id="draft-pr-mode-recommended---default"></a>

{% hint style="info" %}
**Best for:** Most teams who want the simplest setup with no additional configuration.
{% endhint %}

When a pull request enters the queue, Trunk creates a draft pull request to test the changes. This automatically triggers your existing pull request-based CI workflows, the same checks that run when you open a regular pull request.

**Advantages:**

* No additional CI configuration required
* Works immediately with your existing workflows
* Simple to set up and maintain

Things to look out for:

* This mode also creates a `trunk-merge/` branch
* Trunk automatically closes the draft PRs and merge the original PRs

**When to use a different approach:** If you have expensive preview deployments, review-only workflows, or security scans that you don't want running during merge queue testing, consider Push-triggered mode instead.

#### Push-Triggered mode (Advanced) <a href="#push-triggered-mode-advanced" id="push-triggered-mode-advanced"></a>

{% hint style="info" %}
**Best for:** Teams who need different CI behavior for merge queue testing versus pull request review.
{% endhint %}

When a pull request enters the queue, Trunk creates a `trunk-merge/*` branch and pushes to it. You configure specific CI jobs to run on these branches.

**Advantages:**

* Complete control over which jobs run during queue testing
* Avoid triggering expensive preview environments or review-only workflows
* Can optimize for faster merge queue throughput

**Requirements:**

* Configure push-triggered workflows in your CI provider for `trunk-merge/**` branches
* Define required status checks in your `.trunk/trunk.yaml` [configuration file](configure-ci-status-checks.md#if-using-draft-pr-mode-default)

**To enable:** Go to **Settings** > **Repositories** > repository > **Merge Queue** > toggle **off** **Trunk Draft PR Creation**.

### Configure Branch Protection Rules

#### Using Rulesets vs. Classic Rules <a href="#using-rulesets-vs-classic-rules" id="using-rulesets-vs-classic-rules"></a>

You can use GitHub's Rulesets feature alongside Classic branch protection rules—both systems work together. However, **push permission restrictions must be configured using Classic branch protection rules only** because GitHub's API does not expose push restriction settings from Rulesets.

All other branch protection settings (required reviews, status checks, signed commits, etc.) can be configured using either Classic rules or Rulesets.

#### Configure Push Restrictions (Required) <a href="#configure-push-restrictions-required" id="configure-push-restrictions-required"></a>

Trunk Merge Queue needs permission to push to your protected branch. Configure these settings using Classic branch protection rules:

<figure><img src="../../.gitbook/assets/merge-github-classic-branch-rules.png" alt=""><figcaption></figcaption></figure>

1. Go to **Settings > Branches** in your repository on GitHub.
2. Edit or create a Classic branch protection rule for your target branch (e.g., `main`)
3. Under "Rules applied to everyone including administrators," select:
   * **Restrict who can push to matching branches**
   * **Restrict pushes that create matching branches**
4. Add the `trunk-io` bot to the list of allowed actors
5. Optionally, add Organization admins and repository admins who need emergency merge access
6. Save your changes

{% hint style="warning" %}
**Important:** Regular users should use [pull request prioritization](https://file+.vscode-resource.vscode-cdn.net/merge-queue/pr-prioritization) with `--priority=urgent` or `--priority=high` to fast-track pull requests through the queue while maintaining validation. Direct push access is only needed for rare emergencies where the queue itself must be bypassed.
{% endhint %}

#### Exclude Trunk's temporary branches (Critical) <a href="#exclude-trunks-temporary-branches-critical" id="exclude-trunks-temporary-branches-critical"></a>

Trunk Merge Queue creates temporary branches to test pull requests before merging them:

* `trunk-temp/*` - Temporary testing branches
* `trunk-merge/*` - Merge testing branches

{% hint style="danger" %}
**Trunk needs unrestricted access** to create, push to, and delete these branches. If your branch protection rules apply to these branches, Merge Queue cannot function.
{% endhint %}

**To verify and fix:**

1. Go to **Settings > Branches** in your repository
2. Review all Classic branch protection rules
3. Check for wildcard patterns like `*/*`, `**/*`, or similar that would match `trunk-temp/*` or `trunk-merge/*`
4. If you find matching rules, either:
   * **Option A:** Remove the wildcard rules and create more specific rules for your actual branches
   * **Option B:** Add the `trunk-io` bot to the bypass list for those rules

**Example of a problematic rule:** A branch protection rule with pattern `*/*` would protect all branches including `trunk-temp/*` and `trunk-merge/*`.

**What happens if these branches are protected:** Merge Queue will encounter GitHub permission errors and display messages like "Permission denied on trunk-merge/\* branch."



### Next Steps

→ [**Configure CI status checks**](configure-ci-status-checks.md) **-** Configure CI status checks for your branch.

_Having trouble?_ See our [Troubleshooting guide](../reference/troubleshooting.md) for common installation issues.
