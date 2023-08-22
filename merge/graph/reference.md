# Reference

## Submitting and Cancelling Pull Requests

We offer a few mechanisms for submitting a PR for to the MergeGraph:
- Posting a GitHub comment `/trunk merge` on a pull request.
- Ticking the checkbox in the Trunk comment on a pull request.
- Clicking the "Retry" button on the WebApp.
- Using the `trunk` CLI:
```bash
trunk login
trunk merge <pr-number>
```


We offer similar commands for cancellation.
- Posting a GitHub comment `/trunk cancel` on a pull request.
- Cancellation from the WebApp: 
TODO: add an image.
- Using the `trunk` CLI:
```bash
trunk login
trunk merge cancel <pr-number>
```

## PR States

A PR's lifecycle in the MergeGraph goes through the following states:

| State           | Description | 
| --------------- | ----------- |
| Not Ready       | The PR was submitted to Trunk Merge, but the PR isn't eligible for merging yet. Impacted targets may not be uploaded, or readiness checks may not have passed.       |
| Pending         | The MergeGraph created a node for the PR. Testing will begin if the graph has capacity. |
| Testing         | The PR is testing. Required tests are defined in `trunk.yaml.` |
| Tests Passed    | The PR successfully passed tests. It may have to wait for upstream PRs to complete tests before merging. | 
| Pending Failure | The PR failed tests. The cause of failures is still indeterminate - it may be due to an upstream PR, or due to the current PR. It will wait until the root cause of tests has been determined. |
| Merged          | The PR successfully merged into the target branch. It will be removed from the graph. | 
| Failed          | The PR caused a testing failure. It will be removed from the graph. |
| Cancelled       | The PR was cancelled, e.g. `/trunk cancel`. It will be removed from the graph. |