---
description: >-
  The web app offers detailed information about pull requests, the state of the
  merge graph, and more.
---

# Using the WebApp

The web app can be found at [app.trunk.io](https://app.trunk.io).&#x20;

## Graph Overview

The queue tab provides an overview of the work done by the Merge Graph. Merged, testing, and pending PRs should all appear here. Clicking on a row will show the history of that item: click "view more history" to get a better understanding of the item.

<figure><img src="../.gitbook/assets/image (3) (1).png" alt=""><figcaption><p>The "view more history" link navigates you to the details page. </p></figcaption></figure>

In addition to showing information about the work done by Merge Graph, this page also contains other helpful features.

### Showing PR Readiness

The details sidebar for PRs that have been queued but have not yet entered the graph will show what specifically the merge graph is waiting on before allowing it to begin testing. Specifically, the merge graph waits for:

1. Impacted targets to be uploaded for the PRs current SHA
2. The PR to be mergeable according to GitHub. If the PR is not mergeable yet, this most likely means that the PR is not meeting any branch protection rules you have set (for example, not all required status checks have passed yet) or has a merge conflict with the target branch
3. The target branch of the pull request to match the branch that merge graph merges into

<figure><img src="../.gitbook/assets/image (18).png" alt=""><figcaption><p>PR readiness details for a PR that has been queued but has not yet entered the graph. In this example, the merge graph is waiting for impacted targets to be uploaded for the PR and is also waiting for the PR to be mergeable according to GitHub.</p></figcaption></figure>

### Interacting With PRs

For items in the queue tab that have not been merged, the details sidebar that appears when clicking on a row will contain a meatball menu in the right hand corner.

<figure><img src="../.gitbook/assets/image (17).png" alt=""><figcaption><p>Menu with additional actions that can be done on a PR</p></figcaption></figure>

From the menu, you can do the following:

1. "Remove from graph" - this will remove the PR from the merge graph. If the PR is "Not Ready", then it will cancel it, preventing it from going into the graph until it is requeued. If the PR is currently in the graph, it will be removed from the graph, which will restart all PRs that depended on it.

## PR Details

A PR details page will display a complete history of a PR - state transitions, associated test runs, etc. We also offer the uploaded impacted targets for a particular PR, and a resubmit button.

<figure><img src="../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

## Graph Visualization

The current Merge Graph. Each node in the graph is a pull request, and each edge indicates that the pull request is testing with the item above. All edges point towards the target branch; as items merge, the graph restructures.

<figure><img src="../.gitbook/assets/image (3) (1) (1).png" alt=""><figcaption></figcaption></figure>

## Failures

A tabulated view of all the items that have failed in the MergeGraph, e.g. due to testing.

<figure><img src="../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>
