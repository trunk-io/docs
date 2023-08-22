# Using the WebApp

Our [web app](app.trunk.io) offers detailed information about pull requests, the state of the merge graph, and more.

## Queue

The queue tab provides an overview of the work done by the MergeGraph. Merged, testing, and pending PRs should all appear here.
Clicking on a row will show the history of that item: click "view more history" to get a better understanding of the item.

### PR Details

A PR details page will display a complete history of a PR - state transitions, associated test runs, etc. We also offer the uploaded impacted targets for a particular PR, and a resubmit button.

{% hint style="info" %}
IMAGE of the PR DETAILS
{% endhint %}

## Graph

The current MergeGraph. Each node in the graph is a pull request, and each edge indicates that the pull request is testing with the item above. All edges point towards the target branch; as items merge, the graph restructures.

{% hint style="info" %}
IMAGE OF THE GRAPH
{% endhint %}

## Failures

A tabulated view of all the items that have failed in the MergeGraph, e.g. due to testing.

{% hint style="info" %}
IMAGE OF FAILURES
{% endhint %}