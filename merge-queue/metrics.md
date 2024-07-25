# Metrics

Your merge experience directly impacts the velocity and productivity of your development team. Merge Queue Metrics provides observability for the health of your Trunk Merge Queue, so you can discover issues early and make informed optimizations.

<figure><img src="../.gitbook/assets/Trunk Merge Queue Metrics.png" alt=""><figcaption><p>The Health tab showing metrics in the Trunk Web App.</p></figcaption></figure>

### Access Metrics

You can access the metrics in your Trunk Merge Queue by navigating to the Trunk Web App > **Merge Queue** > **Health**.&#x20;

{% hint style="info" %}
#### Enabling CI Time and CI Jobs Triggered

CI Analytics is required to enabling CI Time and CI Jobs Triggered charts if you're **not using GitHub Actions**.
{% endhint %}

### Time Buckets

The date ranges selector at the top left of the dashboard allows you to filter the data displayed by date and time. You can display time buckets by the day or hour in the day/hour dropdown.

The metrics displayed only include data that has **completed within the time rage**, jobs started but not completed during the selected time will now be displayed.s&#x20;

{% hint style="info" %}
When working across multiple time zones, enable **Time in UTC** to ensure everyone sees the same data.&#x20;
{% endhint %}

### Conclusion Counts

Conclusion count displays the jobs terminated during each time bucket. This includes passes, failures, and cancellations. Passes and failures signal a PR that was tested in the queue to completion, while canceled signals that the request to merge terminated before testing finished or before testing began.

Conclusions are tagged with a reason to give further insights into how merges pass or fail in the queue. You can show or hide conclusions of a particular reason by using the **+ Add** button.

<table><thead><tr><th width="167">Category</th><th width="248">Reason</th><th>Description</th></tr></thead><tbody><tr><td>✅ Pass</td><td>Merged by Trunk</td><td>Passed all tests in Merge Queue and merged by Trunk</td></tr><tr><td>✅ Pass</td><td>Merged manually</td><td>User manually merged the PR in Git</td></tr><tr><td>❌ Failure</td><td>Test run timeout</td><td>User-defined timeout for tests exceeded</td></tr><tr><td>❌ Failure</td><td>Required status failed</td><td>Required status check for merge failed</td></tr><tr><td>❌ Failure</td><td>Merge conflict</td><td>A (git) merge conflict encountered</td></tr><tr><td>❌ Failure</td><td>Config parsing failure</td><td>Malformed <code>trunk.yaml</code> that couldn't be parsed</td></tr><tr><td>❌ Failure</td><td>Config bad version</td><td>Invalid version field in <code>trunk.yaml</code></td></tr><tr><td>❌ Failure</td><td>Config bad required statuses</td><td>Failed to parse required statuses in <code>trunk.yaml</code></td></tr><tr><td>❌ Failure</td><td>No required statuses</td><td>No source for required tests was found in <code>trunk.yaml</code> or branch protection settings</td></tr><tr><td>❌ Failure</td><td>GitHub API Failed</td><td>GitHub failed to perform the requested action</td></tr><tr><td>❌ Failure</td><td>PR updated at merge time</td><td>PR updated just before Trunk's merge attempt</td></tr><tr><td>🚫 Cancel</td><td>By user</td><td>PR explicitly canceled by user</td></tr><tr><td>🚫 Cancel</td><td>PR closed</td><td>PR closed (not merged)</td></tr><tr><td>🚫 Cancel</td><td>PR pushed to</td><td>New commits pushed to the PR branch in queue</td></tr><tr><td>🚫 Cancel</td><td>PR base branch changed</td><td>Base branch of PR in queue changed</td></tr><tr><td>🚫 Cancel</td><td>Admin requested</td><td>Trunk employee canceled PR (extreme cases)</td></tr></tbody></table>

### Time in Queue

Time in queue shows how long each PR spends in the Merge Queue from the moment the merge is requested to the moment when it's merged into the target branch.

The time in queue can be displayed as different statistical measures. You can show or hide conclusions of a particular reason by using the **+ Add** button.

| Measure | Explanation                                         |
| ------- | --------------------------------------------------- |
| Average | Average of all time in queue during the time bucket |
| Minimum | The shortest time in queue in the time bucket.      |
| Maximum | The longest time in queue in the time bucket.       |
| Sum     | The total of all time in queue added together.      |
| P50     | The value below 50% of the time in queue falls.     |
| P95     | The value below 95% of the time in queue falls.     |
| P99     | The value below 99% of the time in queue falls.     |

### CI Time to Test PRs

CI Time measures the time it takes to test each merge request in CI. This measures **only CI steps relevant to the merge queue**, other CI steps like build or deploy will not be measured.\
\
Sum measures the total CI time consumed by merge-related CI jobs. Average measures the average of the individual CI jobs run during merge, not as an average of total CI time used to merge individual PRs. You can toggle sum and average display through the **+ Add** button.

If **batching** is enabled, CI time to test PRs is shown as `time_to_test_batch/batch_size` which means if a batch of 5 PRs take 15 minutes to test together, then CI time for each PR is displayed as 3 minutes.

{% hint style="info" %}
CI Analytics is required for this feature to work if you're not running CI through GitHub Actions.
{% endhint %}

### **CI Jobs Triggered To Test PRs**

Individual CI jobs that are triggered to test PRs in the merge queue. There could be multiple jobs triggered per PR. If batching is enabled, there could be a single CI job triggered for multiple PRs.&#x20;

{% hint style="info" %}
CI Analytics is required for this feature to work if you're not running CI through GitHub Actions.
{% endhint %}
