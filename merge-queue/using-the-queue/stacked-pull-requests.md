---
description: >-
  Merge a chain of dependent pull requests through Trunk Merge Queue, either as
  a single combined unit with /trunk stack or one at a time with /trunk merge.
---

# Stacked pull requests

Trunk Merge Queue supports merging **stacked pull requests**: a chain of PRs where each one builds on the previous, with the bottom PR targeting your merge queue branch. Trunk gives you two ways to get a stack merged:

* [`/trunk stack`](#merge-the-stack-as-one-unit): combine the entire stack into a single PR that moves through the queue as one unit. Faster, and requires the [Trunk Sudo GitHub App](../../setup-and-administration/trunk-sudo-app.md).
* [`/trunk merge`](#enqueue-each-pr-individually) on each PR: enqueue each PR in the stack separately and let Trunk process them sequentially. Slower but gives you per-PR test isolation, and has no additional setup requirements.

## What is a stack

A stack is a chain of pull requests connected through their base branches. Each PR targets the branch of the PR below it, and the bottom PR targets your merge queue branch:

```
merge queue branch <-- PR #1 (base: merge queue branch)
                          <-- PR #2 (base: PR #1's branch)
                                <-- PR #3 (base: PR #2's branch)
```

Trunk discovers the stack automatically by walking base branches. No separate configuration is required to mark PRs as stacked.

## Choose your approach

|  | `/trunk stack` (combined) | `/trunk merge` (individual) |
| --- | --- | --- |
| **Enqueue method** | Single `/trunk stack` comment on any PR | `/trunk merge` on each PR separately |
| **Queue processing** | One stacked PR tests and merges as a unit | Each PR tests and merges sequentially |
| **Test runs** | One test run for the combined changes | One test run per PR |
| **Speed** | Faster: one pass through the queue | Slower: each PR waits for the previous one |
| **Isolation** | Less: all changes test together | More: each PR tests against the actual merge queue branch |
| **On merge** | Member PRs closed automatically | Each PR merges individually |
| **Requirements** | [Trunk Sudo GitHub App](../../setup-and-administration/trunk-sudo-app.md) installed and configured | No additional setup |

## Merge the stack as one unit

Comment `/trunk stack` on any PR in the stack and Trunk combines every PR in the chain into a single stacked PR that moves through the merge queue together. That stacked PR tests and merges like any other PR in the queue; batching, priority, and failure handling all behave normally. When the stacked PR merges, Trunk automatically closes every member PR, since their code is already in your target branch.

### Prerequisites

Trunk Sudo is required because the stacked PR Trunk creates is brand-new and auto-generated, so it doesn't inherit the approvals or required status checks that have already been satisfied on the member PRs. Trunk Sudo merges the stacked PR on the strength of those member PRs by bypassing its branch protection.

* [ ] [Trunk Sudo GitHub App](../../setup-and-administration/trunk-sudo-app.md) installed on your repository. If it isn't installed, `/trunk stack` will fail with an error linking you to the install page.
* [ ] Trunk Sudo configured to bypass branch protection on your target branch. Required status checks must live in a [GitHub ruleset](../../setup-and-administration/trunk-sudo-app.md#option-a-github-rulesets-recommended) (not classic branch protection) with Trunk Sudo listed as an exempt bypass actor.
* [ ] You have write access to the repository, or you're a member of your repository's Trunk organization.

### Stack requirements

For `/trunk stack` to succeed, the stack must satisfy:

* The chain terminates at your merge queue branch (e.g., `main`).
* The stack contains **2 to 10 PRs**.
* Every member PR is **open**: not closed, not a draft, not already merged.
* No member PR already belongs to another active stacked PR group.

If any requirement fails, Trunk rejects the command with a message listing the specific problems (e.g., `#42: is a draft PR`).

### Command syntax

Comment on any PR in the stack:

```
/trunk stack [--title "Custom title"] [-p <priority>] [--no-batch]
```

| Option | Short | Description |
| --- | --- | --- |
| `--title` | `-t` | Custom title for the stacked PR. Defaults to the title of the **topmost** PR in the stack (the one furthest from the merge queue branch). |
| `--priority` | `-p` | [Priority level](../optimizations/priority-merging.md) for the stacked PR in the merge queue. |
| `--no-batch` |  | Prevent the stacked PR from being [batched](../optimizations/batching.md) with other items in the queue. |

**Examples:**

```
/trunk stack
/trunk stack --title "Feature: user authentication"
/trunk stack -t "Refactor auth module" -p 1
/trunk stack --no-batch
```

### What happens when you run `/trunk stack`

1. **Permissions check**: Trunk verifies you have write access to the repository or are a Trunk organization member.
2. **Prerequisite check**: Trunk verifies the Trunk Sudo GitHub App is installed and branch protection is configured.
3. **Stack discovery**: Trunk walks the base branch chain from your PR down to the merge queue branch, collecting all PRs.
4. **Validation**: Trunk checks every member PR is open, not a draft, and not already in another stack. If anything fails, the command is rejected.
5. **Temporary branch**: Trunk creates a branch at the current HEAD of your merge queue branch, named `trunk-stack/<group-id>`.
6. **Sequential merge**: Trunk merges each member PR into the temporary branch starting from the PR closest to the merge queue branch. If any merge conflicts occur, the operation fails and you'll need to resolve conflicts before retrying.
7. **Stacked PR creation**: Trunk opens a new pull request from `trunk-stack/<group-id>` to your target branch.
8. **Enqueue**: The stacked PR is automatically added to the merge queue.
9. **Status comments**: Trunk comments on each member PR to note that a stacked PR has been created and is queued.

Trunk reacts to your `/trunk stack` comment with a 👍 on success, or a 👎 plus an explanation on failure.

### The stacked PR

The stacked PR is a real GitHub pull request containing the combined changes from every member PR.

* **Title**: If you passed `--title`, that title is used exactly. Otherwise it defaults to the title of the topmost PR in the stack.
* **Body**: Auto-generated. Includes the list of member PRs, the target branch, and an explanation of how the stacked PR works (merge behavior, automatic closure of member PRs, cancellation triggers).
* **Branch**: `trunk-stack/<group-id>`. Managed entirely by Trunk and cleaned up automatically when the stacked PR merges or is cancelled.

### Lifecycle

#### On successful merge

1. Each member PR is automatically closed by Trunk, since its code is already in the target branch via the stacked PR.
2. Trunk posts a comment on each member PR: "Stacked PR #N merged successfully. Closing this PR as its code has been merged into `<merge queue branch>`."
3. The `trunk-stack/<group-id>` branch is deleted.

#### On test failure

1. Trunk posts a comment on each member PR: "Stacked PR #N failed testing in the merge queue. Please investigate the failure and re-submit the stack."
2. The stacked PR is closed on GitHub.
3. The `trunk-stack/<group-id>` branch is deleted.

Fix the issue in the relevant member PR, then run `/trunk stack` again to create a fresh stacked PR.

#### On cancellation

The stacked PR is automatically cancelled if any of the following happens:

| Trigger | What it means |
| --- | --- |
| **Member PR pushed to** | A new commit is pushed to any member PR's branch. |
| **Member PR closed** | Any member PR is closed without merging. |
| **Member PR merged independently** | Any member PR is merged outside of the stacked PR workflow. |
| **Member PR base branch changed** | The base branch of any member PR is changed. |
| **Stacked PR closed** | The stacked PR itself is closed manually. |
| **Stacked PR pushed to** | The stacked PR's branch is pushed to directly. |
| **User cancelled** | Someone runs `/trunk cancel` on the stacked PR. |

When cancellation occurs, Trunk posts a comment on each member PR explaining the reason (e.g., "Stacked PR #N was cancelled: a member PR was pushed to.") and closes the stacked PR. To re-stack, run `/trunk stack` again on any member PR. This creates a fresh stacked PR with the latest state of all member PRs.

## Enqueue each PR individually

If you prefer per-PR test isolation, or you don't want to install Trunk Sudo, you can enqueue each PR in the stack separately with `/trunk merge`. Trunk processes the PRs sequentially, testing and merging each one against the actual state of your merge queue branch.

### Step 1: Enqueue every PR in the stack

Each PR in the stack must be enqueued separately. Use any of the standard submission methods on every PR:

* Comment `/trunk merge` on each PR.
* Check the box in the Trunk comment on each PR.
* Use the CLI: `trunk merge <pr-number>` for each PR.

Enqueuing each PR separately gives you control over which PRs in your stack should be merged versus which might need more work.

### Step 2: Automatic sequential processing

Once enqueued, Trunk handles the rest:

1. The **bottom PR** in the stack (base branch = your merge queue branch) enters the queue, runs tests, and merges.
2. When it merges, **GitHub automatically updates** the next PR's base branch from the previous feature branch to your merge queue branch.
3. The **next PR** now targets the merge queue branch, so it proceeds through the queue.
4. This continues until every PR in the stack is merged.

For example, a stack of 5 PRs with merge queue branch `main`:

* PR #1 (base: `main`) → tests → merges
* PR #2's base automatically changes to `main` → tests → merges
* PR #3's base automatically changes to `main` → tests → merges
* …and so on.

### Considerations

**Sequential testing.** PRs in the stack are tested and merged one at a time in order. The second PR won't begin testing until the first PR has fully merged. This ensures each PR is tested against the actual state of your merge queue branch and results are deterministic, at the cost of speed. A stack of 5 PRs takes substantially longer than 5 independent PRs, since they can't be tested in parallel.

**Enqueued PRs with non-merge-branch bases.** If you enqueue a PR whose base branch is not your merge queue branch and that base never updates, the PR stays in the queue without processing. This typically means the parent PR in the stack was never enqueued or merged. The PR will begin processing as soon as its base branch updates to the merge queue branch.

**No special configuration.** Individual enqueuing requires no additional setup beyond a functioning merge queue. Trunk detects the stack relationship automatically from each PR's base branch.
