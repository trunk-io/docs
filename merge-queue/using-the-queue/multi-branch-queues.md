---
description: >-
  Run independent merge queues on different branches in the same repository.
---

# Multi-branch merge queues

Trunk Merge Queue supports running multiple independent queues in a single repository, each targeting a different branch. This is useful for teams that maintain multiple long-lived branches, such as `main` and `release/*` branches, or `develop` and `staging`.

## How it works

Each merge queue is associated with a specific target branch in your repository. When you create a queue, you select a repository and a target branch. You can create additional queues for the same repository by selecting different target branches.

PRs are automatically routed to the correct queue based on their target branch in GitHub. A PR targeting `main` enters the `main` queue, and a PR targeting `release/v2` enters the `release/v2` queue. Each queue:

- Operates independently with its own position ordering
- Has its own configuration (concurrency, batching, parallel mode, merge method, etc.)
- Can be paused, drained, or running independently of other queues
- Creates its own `trunk-merge/*` test branches
- Reports status independently in the Trunk dashboard

## Setting up multiple queues

### Prerequisites

Before creating an additional queue, make sure:

- The Trunk GitHub App is already installed on the repository
- The target branch exists in your repository
- You have admin access to your Trunk organization

### Create an additional queue

1. Navigate to the **Merge Queue** tab in [app.trunk.io](https://app.trunk.io).
2. Click the **Create New Queue** button.
3. Select your repository from the dropdown.
4. Enter the target branch for the new queue (e.g., `release/v2`).
5. Click **Create Queue**.

### Configure branch protection for each target branch

Each target branch needs its own branch protection configuration. Follow the [Configure branch protection](../getting-started/configure-branch-protection.md) guide for each branch you are protecting with a merge queue. Specifically:

- Add the `trunk-io` bot to the push restriction list for each target branch
- Ensure `trunk-temp/*` and `trunk-merge/*` branches are excluded from any wildcard branch protection rules

### Configure CI for each queue

Your CI workflows need to run on `trunk-merge/*` branches (or draft PRs, if using the default mode) regardless of which queue triggered them. If you use push-triggered mode, confirm your CI triggers cover branches created by all queues.

## Common use cases

### Release branches

Maintain a queue on `main` for ongoing development and separate queues on `release/*` branches for cherry-picked hotfixes. Each queue validates changes independently, preventing broken releases.

### Environment branches

Teams that deploy from specific branches (e.g., `staging`, `production`) can protect each environment branch with its own queue, ensuring changes are validated before reaching each environment.

### Monorepo with multiple deploy targets

In a monorepo where different branches correspond to different deployment targets, each branch can have its own queue with tailored concurrency and batching settings.

## Managing multiple queues

### Dashboard

Each queue appears separately in the Merge Queue tab of the Trunk dashboard. Select the repository, then choose the target branch to view and manage a specific queue.

### CLI

The Trunk CLI automatically detects the correct queue based on the PR's target branch. Commands like `trunk merge <pr-number>` route to the appropriate queue without any additional flags.

### API

When using the [Merge Queue API](../reference/merge.md), specify the `targetBranch` field in your requests to interact with a specific queue. For example, the `createQueue` endpoint requires both `repo` and `targetBranch`.

## Limitations

- Each target branch can have at most one queue. You cannot create two queues for the same branch.
- Queue settings are independent. There is no way to share or inherit configuration between queues in the same repository.
- Each queue consumes its own concurrency slots. If you have two queues each set to a concurrency of 5, up to 10 PRs may be testing simultaneously across both queues.
