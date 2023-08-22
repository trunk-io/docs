---
description: >-
  The web app offers detailed information about pull requests, the state of the
  merge graph, and more.
---

# Using the WebApp

The web app can be found at [app.trunk.io](https://app.trunk.io).&#x20;

## Graph Overview

The queue tab provides an overview of the work done by the Merge Graph. Merged, testing, and pending PRs should all appear here. Clicking on a row will show the history of that item: click "view more history" to get a better understanding of the item.

<figure><img src="../.gitbook/assets/image (3).png" alt=""><figcaption><p>The "view more history" link navigates you to the details page. </p></figcaption></figure>

## PR Details

A PR details page will display a complete history of a PR - state transitions, associated test runs, etc. We also offer the uploaded impacted targets for a particular PR, and a resubmit button.

<figure><img src="../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

## Graph Visualization

The current Merge Graph. Each node in the graph is a pull request, and each edge indicates that the pull request is testing with the item above. All edges point towards the target branch; as items merge, the graph restructures.

<figure><img src="../.gitbook/assets/image (3) (1).png" alt=""><figcaption></figcaption></figure>

## Failures

A tabulated view of all the items that have failed in the MergeGraph, e.g. due to testing.

<figure><img src="../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>
