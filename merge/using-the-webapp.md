---
description: >-
  The web app offers detailed information about pull requests, the state of the
  merge queue, and more.
---

# Using the Trunk Merge UI

The web app can be found at [app.trunk.io](https://app.trunk.io).&#x20;

## Queue Overview

The queue tab provides an overview of the work done by Merge. Merged, testing, and pending PRs should all appear here. Clicking on a row will show the history of that item: click "view more history" to get a better understanding of the item.

<figure><img src="../.gitbook/assets/image (3) (1) (1).png" alt=""><figcaption><p>The "view more history" link navigates you to the details page. </p></figcaption></figure>

### Pull Request Details

The PR details shows information about a PR, including a link to the PR in GitHub, the history of the PR within Trunk Merge, and what must be done before a PR can be admitted to the queue for PRs that have not entered the queue yet.

When a PR has not been admitted to the queue yet, Trunk Merge waits for:

1. Impacted targets to be uploaded for the PRs current SHA (`Parallel` mode only)
2. The PR to be mergeable according to GitHub. If the PR is not mergeable yet, this most likely means that the PR is not meeting all branch protection rules you have set (for example, not all required status checks have passed yet) or has a merge conflict with the target branch
3. The target branch of the pull request to match the branch that merge queue merges into

<figure><img src="../.gitbook/assets/image (2).png" alt="" width="510"><figcaption><p>PR readiness details for a PR that has been submitted but has not yet entered the merge queue. In this example, the queue is waiting for impacted targets to be uploaded for the PR and is also waiting for the PR to be mergeable according to GitHub.</p></figcaption></figure>

In the screenshot above the PR's base branch matches the Merge branch, but the impacted targets are not yet uploaded, but it is not mergable on GitHub yet.

The PR Details panel has a dropdown menu (labeled "**..."**) with actions. From this menu you can:

1. Remove a PR from the queue. If the PR is "Not Ready", then it will cancel it, preventing it from going into the queue until it is re-queued. If the PR is currently in the queue, it will be removed from the queue, which will restart all PRs that depended on it
2. Re-queue a PR if it is currently not in the queue
3. Download any impacted targets that have been [uploaded](impacted-targets.md#generating-impacted-targets) for the PR (uploading impacted targets is only required for [Parallel](configuration.md#parallel-mode) mode, but this option will still show regardless of mode if impacted targets have been uploaded for the PR)

<figure><img src="../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

The "Remove from queue" action will remove the PR from the merge queue. If the PR is "Not Ready", then it will cancel it, preventing it from going into the queue until it is re-queued. If the PR is currently in the queue, it will be removed from the queue, which will restart all PRs that depended on it:

1. ## PR Details

A PR details page will display a complete history of a PR - state transitions, associated test runs, a visual of what's currently in the Merge Queue, etc. The same dropdown menu described above (labeled "...") is on this page as well.

<figure><img src="../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

## Failures

A tabulated view of all the items that have failed in the Merge Queue, e.g. due to testing.

<figure><img src="../.gitbook/assets/image (5) (1).png" alt=""><figcaption></figcaption></figure>

## Queue Visualization

The view of all current PRs being tested by Trunk Merge and their respective queues. Each node shown is a pull request, and each edge indicates that the pull request is testing with the item above and depends on it. All edges point towards the target branch; as items merge, the affected queues restructure. If running in `Single` mode, the this will be a single line showing the testing and merging process.

<figure><img src="../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>

You can click on any shown PR to navigate to the details page for that PR.
