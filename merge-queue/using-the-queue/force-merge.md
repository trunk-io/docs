---
description: >-
  Admins can push a pull request through Merge Queue even when GitHub branch
  protection rules aren't satisfied. The PR is still tested; only the final
  merge bypasses protection.
---

# Force merge

### What it is

Force merge lets a GitHub repository admin push a pull request through the Trunk Merge Queue even when branch protection requirements are not satisfied. The PR is still tested by the queue exactly like any other PR — only the final protection gate is bypassed at merge time, using the [Trunk Sudo GitHub App](../../setup-and-administration/trunk-sudo-app.md).

{% hint style="warning" %}
**Force merge is admin-only and can only be triggered by a GitHub comment.** Trunk verifies admin identity via GitHub comment authorship, which is why other submission paths (CLI, checkbox, web app) don't support `--force`. If a non-admin posts `/trunk merge --force`, Trunk will reply on the PR with a rejection comment explaining that the command requires admin access.
{% endhint %}

### Why use it

* **Unblock misconfigured protection.** Ship a PR when a required status check is broken or misconfigured, without disabling the rule for everyone else.
* **Merge emergency fixes safely.** You still get queue validation — predictive testing, batching, failure detection — instead of merging directly to `main` and hoping for the best.
* **Avoid direct-to-`main` bypass.** Force merge is strictly safer than pushing to the protected branch manually, because the PR is fully tested before it lands.

### Prerequisites

Before you can use force merge, make sure you have:

* [ ] [Trunk Sudo GitHub App](../../setup-and-administration/trunk-sudo-app.md) installed and configured for this repository
* [ ] GitHub admin access on the repository

### How to use it

#### Via GitHub comment

On any pull request, post:

```
/trunk merge --force
```

There is no CLI, checkbox, or web app equivalent. This is intentional: Trunk verifies admin identity through GitHub comment authorship, so the command is only accepted through the PR comment flow.

### What happens step by step

1. **Admission.** The PR enters the queue despite branch protection not being satisfied. Normally Trunk Merge Queue waits until GitHub marks a PR as ready to merge; `--force` skips that wait.
2. **Testing.** The PR is tested normally. Batching, ordering, priority, and failure handling all behave exactly as they would for any other PR — nothing about the testing pipeline changes.
3. **Merge.** If tests pass, Trunk Sudo merges the PR, bypassing branch protection. Without Trunk Sudo installed and configured, this step will fail.
4. **Failure.** If tests fail, the PR is handled like any normal queue failure. See [Handle failed pull requests](handle-failed-pull-requests.md).

### Combining with other flags

Force merge can be combined with other `/trunk merge` flags. The most common combination is with [priority](../optimizations/priority-merging.md) when both urgency and protection bypass are needed — for example:

```
/trunk merge --force --priority=urgent
```

### Tradeoffs and considerations

#### What you gain

* **Queue validation is preserved** — tests still run before merge.
* **No direct-to-`main` push** — the PR goes through the same merge flow as every other PR.
* **Unblock stuck PRs** without weakening your default branch protection for everyone.

#### What you give up

* **Bypasses the human review gate** if required reviews aren't satisfied.
* **Bypasses required status checks** that would otherwise block the merge.
* Because force merge bypasses protections that every other PR must satisfy, overuse erodes the value of those protections.

#### When NOT to use force merge

* **Normal feature work.** If a PR is going to merge eventually, let it wait for reviews and checks.
* **"The required check is slow."** Fix the check or the CI configuration — force merge is not a substitute for unbreaking your pipeline.
* **Non-admin urgency.** If you aren't an admin, don't ask an admin to force merge your PR — escalate via the usual incident or on-call process.

### Common misconceptions

* **Misconception:** "Force merge skips testing."
  * **Reality:** Tests still run normally. The PR goes through the full merge queue testing pipeline — only the branch protection gate is bypassed at merge time.
* **Misconception:** "I can force merge through the CLI."
  * **Reality:** Force merge is comment-only and admin-only. The CLI, web app checkbox, and "Retry" button don't accept `--force`.
* **Misconception:** "Force merge is the same as emergency pull requests."
  * **Reality:** [Emergency pull requests](emergency-pull-requests.md) bypass the queue entirely and push directly to your merge branch. Force merge still goes through the queue and still tests the PR — it only bypasses branch protection at merge time.

### Visibility in the queue dashboard

Force-merged pull requests appear with a **Forced** badge in the merge queue PR list. This lets you identify which PRs bypassed branch protection at a glance without opening each PR individually.

### Next steps

* [Trunk Sudo GitHub App](../../setup-and-administration/trunk-sudo-app.md) — install and configure the app that powers force merge.
* [Emergency pull requests](emergency-pull-requests.md) — when the queue itself needs to be bypassed, not just branch protection.
* [Priority merging](../optimizations/priority-merging.md) — fast-track a PR without bypassing any rules.
