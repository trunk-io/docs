# Testing Pull Requests

## Submitting Pull Requests

Now you can submit a pull request, either using the Trunk CLI or in the GitHub Pull Request UI. Try making a simple change on a branch and submit it as PR in GitHub.

Now trigger Trunk Merge to process this PR using either a comment on the PR or the Trunk CLI.

{% tabs %}
{% tab title="GitHub Pull Request View" %}
Comment `/trunk merge` on a pull request

<figure><img src="../.gitbook/assets/image (7) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Trunk CLI" %}
```bash
# Authenticate with trunk service
$ trunk login
# Queue pull request for merge
$ trunk merge {pr-number}
```
{% endtab %}
{% endtabs %}

Please note that Trunk Merge, since it will eventually merge your PR on GitHub, is still **bound by any protection rules set in GitHub** that affect the branch Trunk Merge will merge into or that affect your Trunk Merge branch.&#x20;

For example, if a PR requires at least one review to merge, then Trunk Merge would display `'not mergable GitHub yet'` until that PR has a review.

If you have trouble with merge queueing PRs, check if there is any kind of additional branch protection set up on your repo. Existing branch protection rules must be changed in order to **not** protect branches in the form of `trunk-temp/*` and `trunk-merge/*` . If either of those branches are considered protected in any way according to GitHub (e.g., if there is a `*/*` branch protection rule), then Merge will not be able to run tests properly due to GitHub permission errors.

If there are any questions or help is needed, reach out on our [community slack](https://slack.trunk.io/)!

## Pull Request Processing

Once a PR is submitted to the merge queue it goes through several states. First it starts as _Not Ready_ until all of the required conditions to submit it are met. Once ready, the PR moves to the _Pending_ state, waiting for a Merge Queue to pick it up, and then enters the _Testing_ state.  Once the tests pass the PR may still need to wait for upstream PRs. Once any upstream PRs are complete the PR will be merged and then removed from the Merge Queue. If a PR fails or is canceled then it will go to the failed or canceled state.

### PR States

A PR's lifecycle in Merge Queue goes through the following states:

| State           | Description                                                                                                                                                                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Not Ready       | The PR was submitted to Trunk Merge, but the PR isn't eligible for merging yet. Impacted targets may not be uploaded, or readiness checks may not have passed.                                                                                          |
| Pending         | The Merge Queue created a node for the PR. Testing will begin if the queue has capacity.                                                                                                                                                                |
| Testing         | The PR is testing. Required tests are defined in `trunk/trunk.yaml.`                                                                                                                                                                                    |
| Tests Passed    | The PR successfully passed tests. It may have to wait for upstream PRs to complete tests before merging.                                                                                                                                                |
| Pending Failure | The PR failed tests. The cause of failures is still indeterminate - it may be due to an upstream PR, or due to the current PR. It will wait until the root cause of tests has been determined, and restart testing on your PR if due to an upstream PR. |
| Merged          | The PR successfully merged into the target branch. It will be removed from the Merge Queue.                                                                                                                                                             |
| Failed          | The PR caused a testing failure. It will be removed from the queue.                                                                                                                                                                                     |
| Cancelled       | The PR was cancelled, e.g. `/trunk cancel`. It will be removed from the queue.                                                                                                                                                                          |

## Canceling Pull Requests

You can cancel a PR in progress with either a `/trunk cancel` comment to the pull request, or using the Trunk Merge UI:

{% tabs %}
{% tab title="GitHub Pull Request View" %}
![](<../.gitbook/assets/Screenshot 2023-11-09 at 1.58.30 PM.png>)
{% endtab %}

{% tab title="Trunk Merge UI" %}
![](<../.gitbook/assets/Screenshot 2023-11-09 at 1.59.35 PM.png>)
{% endtab %}
{% endtabs %}
