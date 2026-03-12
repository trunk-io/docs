# Direct merge to main

### Overview

Direct Merge to Main is an optimization that allows PRs to merge immediately without waiting in the queue when retesting would provide no value.

The merge queue's purpose is to test your PR against the latest version of main and all PRs ahead of it in the queue. However, if your PR is already based on the tip of main AND the queue is empty, running tests again provides no additional confidence—you've already tested against the exact state your PR will merge into.

With Direct Merge to Main enabled, Trunk recognizes this situation and merges your PR immediately, skipping the redundant test run and eliminating unnecessary wait time.

#### How It Works

**Without Direct Merge to Main:**

1. PR enters the queue based on tip of main
2. Queue creates a test branch
3. Tests run (even though they just passed on the same code)
4. After tests pass, PR merges
5. Total time: Test duration + queue overhead

**With Direct Merge to Main:**

1. PR enters the queue based on tip of main
2. Queue recognizes: PR is up-to-date AND queue is empty
3. PR merges immediately
4. Total time: \~seconds

#### When Direct Merge Happens

Direct Merge to Main only activates when **ALL** of these conditions are met:

✅ **PR is based on the tip of main** - The PR's base commit matches the current HEAD of your main branch

✅ **Queue is empty** - No other PRs are currently in the queue waiting to test or merge

✅ **PR's tests have passed** - The PR's CI checks passed on GitHub (before entering the queue)

✅ **Direct Merge is enabled** - The setting is turned on in your merge queue configuration

If any of these conditions are not met, the PR enters the queue normally and tests predictively as usual.

<details>

<summary><strong>Example Scenarios</strong></summary>

**Scenario 1: Perfect candidate for Direct Merge**

* Developer updates their PR to tip of main using "Update branch" on GitHub
* All CI checks pass on the PR
* Developer submits to merge queue
* Queue is currently empty
* **Result:** PR merges immediately (seconds instead of minutes)

**Scenario 2: PR not up-to-date**

* PR was created yesterday and main has advanced
* Developer submits to merge queue
* Queue is empty
* **Result:** PR enters queue normally, tests against current main

**Scenario 3: Queue has other PRs**

* PR is based on tip of main
* Another PR is already in the queue
* **Result:** PR enters queue normally behind existing PR, tests predictively

**Scenario 4: Tests haven't passed yet**

* PR is based on tip of main
* Queue is empty
* But CI checks are still running or failed
* **Result:** PR cannot enter queue until checks pass

</details>

### When to Enable

**Enable Direct Merge to Main if:**

* You enforce "branch must be up-to-date with main" GitHub protection
* Developers frequently update PRs to latest main before merging
* Your test suite takes 5+ minutes to run
* You have good test coverage and trust your main branch tests

**Don't enable if:**

* You rarely keep PRs up-to-date with main (feature won't trigger often)
* You want every PR to test in the queue regardless (for additional validation)
* Your tests are very fast (< 1 minute) and the optimization is negligible

### Configuration

#### Enable Direct Merge to Main

1. Navigate to **Settings** > **Repositories** > your repository > **Merge Queue**
2. Locate the **Direct Merge to Main** toggle
3. Enable the setting
4. Changes take effect immediately

<figure><img src="../../.gitbook/assets/1768426934-direct-merge-mode-toggle.avif" alt=""><figcaption></figcaption></figure>

#### Verify It's Working

When a PR is directly merged, you'll see different timeline messages and notifications:

**In Trunk Dashboard:**

> "Merged to main without going through the queue, as it was up-to-date with main and the queue was empty"

**In GitHub comments:**

> "This PR was merged directly to main because it was already up-to-date and the queue was empty."

**In** [**Slack notifications**](../integration-for-slack.md) **(if configured):**

> "✅ PR #123 merged directly (was up-to-date, queue empty)"

These messages confirm that the optimization triggered and your PR skipped the queue.

### How This Works with Other Features

Direct Merge to Main complements other optimizations:

[**Predictive Testing**](predictive-testing.md)

* When direct merge doesn't trigger, predictive testing takes over
* PRs not at tip of main test against predicted future state
* Both features work together seamlessly

[**Optimistic Merging**](optimistic-merging.md)

* Optimistic merging handles PRs deeper in queue
* Direct merge handles the special case at the front
* Both reduce unnecessary waiting

[**Batching**](batching.md)

* If queue has batching enabled and isn't empty, direct merge won't trigger
* Batching takes priority when multiple PRs are present
* Direct merge is for the empty queue case

[**Parallel Queues**](parallel-queues/)

* Works in both Single and Parallel mode
* In parallel mode, checks if PR's specific lane is empty
* Provides benefit across all queue configurations

### Troubleshooting

<details>

<summary><strong>Why didn't my PR merge directly?</strong></summary>

Check these conditions:

1. Was your PR based on the tip of main? (Check GitHub branch status)
2. Was the queue completely empty when you submitted? (Check queue dashboard)
3. Had your PR's tests passed? (Check GitHub status checks)
4. Is Direct Merge to Main enabled? (Check Merge Queue settings)

If all conditions were met but direct merge didn't happen, contact support with the PR number.

</details>

<details>

<summary><strong>Does this bypass security checks?</strong></summary>

No. Direct merge only skips the queue testing step. Your PR must still:

* Pass all required status checks on GitHub
* Meet all branch protection requirements
* Have the necessary approvals
* Be based on the latest main branch

</details>

<details>

<summary><strong>Will this slow down other PRs?</strong></summary>

No. Direct merge only happens when the queue is empty, so there are no other PRs to slow down. When other PRs are present, direct merge doesn't trigger and the queue operates normally.

</details>

<details>

<summary><strong>What if tests are flaky?</strong></summary>

Direct merge relies on the tests that ran on your PR branch (before entering the queue). If those tests are flaky and gave a false positive, the issue existed before direct merge. Focus on fixing flaky tests rather than disabling the optimization.

</details>

