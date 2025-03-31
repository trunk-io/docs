---
description: >-
  Learn more about which permissions the Trunk GitHub app requests and why Trunk
  needs them.
---

# GitHub App Permissions

The Trunk GitHub App enables functionality for all of Trunk's tools. Not every permission is required for every feature of Trunk, and if you have only enabled one of our tools, we will only access the permissions pertaining to that tool. For complete documentation of the individual permissions the Trunk GitHub App requires, see the [GitHub developer docs](https://docs.github.com/en/rest/authentication/permissions-required-for-github-apps). Below, find an explanation of every permission the Trunk GitHub App requires and what Trunk uses it for.

## **Repository permissions**

Repository permissions permit access to repositories and related resources.

### Actions (Read and write)

This permission allows access to the results of workflow and job runs.

Trunk uses this permission to read the results of workflow and job runs, and to dispatch or cancel workflow runs triggered by Trunk Merge.

### Administration (Read-only)

This permission includes read-only access to repository settings, teams, and collaborators.

Trunk uses this permission to access a repository’s branch protection rules. Trunk cannot edit any administration settings on your GitHub organization or repository.

### Checks (Read and write)

This permission includes access to checks on code (such as GitHub actions and other integrations like BuildKite, CircleCI).

Trunk uses this permission to examine the status of your commits, branches, and pull requests. Trunk uses this information to determine when pull requests are ready to merge. Trunk also uses this permission to post the results of code analysis.

### Commit statuses (Read-only)

This permission includes access to statuses on code. Some CI providers use this integration with GitHub to post the results of a job run.

Trunk uses this permission to examine the status of your commits, branches, and pull requests. Trunk uses this information to determine when pull requests are ready to merge.

### Contents (Read and write)

This permission includes access to repository contents, commits, branches, downloads, releases, and merges.&#x20;

Trunk uses this permission to read the `trunk.yaml` configuration file if you’ve added it to your repository. Trunk also uses write permissions to create, update, and delete the branches created and managed by Merge.

### Issues (Read and write)

This permission includes access to issues and related comments, assignees, labels, and milestones.

Trunk uses this permission to read and write comments on pull requests.

### Metadata (Read-only)

This permission includes access to search repositories, list collaborators, and access repository metadata.

This permission is required by all GitHub applications that access repository information.

### Pull requests (Read and write)

This permission includes access to pull requests and merges.

Trunk uses this permission to view and merge pull requests managed by Merge.

### Workflows (Read and write)

This permission includes access to update GitHub Action workflow files.

Trunk uses this permission to facilitate onboarding to running Trunk Check on CI, for users who use Github Actions.

## **Organization permissions**

Organization permissions permit access to organization-related resources.

### **Events (Read-only)**

This permission includes access to view events triggered by an activity in an organization.

Trunk uses this permission to get organization events to keep app install information up to date.

### **Members (Read-only)**

This permission includes access to organization members and teams.

Trunk uses this permission to subscribe to organization rename events to keep app install information current.
