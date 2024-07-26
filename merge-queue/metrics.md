# Metrics

Your merge experience directly impacts the velocity and productivity of your development team. Merge Queue Metrics provides observability for the **health** of your Trunk Merge Queue, so you can discover issues early and make informed optimizations.

<figure><img src="../.gitbook/assets/Trunk Merge Queue Metrics.png" alt=""><figcaption><p>The Health tab showing metrics in the Trunk Web App.</p></figcaption></figure>

### Access Metrics

You can access the metrics in your Trunk Merge Queue by navigating to the Trunk Web App > **Merge Queue** > **Health**.&#x20;

{% hint style="info" %}
#### Enabling CI Time and CI Jobs Triggered

[Pushing data to CI Analytics](https://docs.trunk.io/ci-analytics/setup) is required to enable CI Time and CI Jobs Triggered charts if you're **not using GitHub Actions**.
{% endhint %}

### Time Buckets

The date ranges selector at the top left of the dashboard allows you to filter the data displayed by date and time. You can display time buckets by the day or hour in the day/hour dropdown.

The metrics displayed only include data that have **completed within the time rage**, jobs started but not completed during the selected time **will not be displayed**.&#x20;

{% hint style="info" %}
When working across multiple time zones, enable **Time in UTC** to ensure everyone sees the same data.&#x20;
{% endhint %}

### Conclusion Count

Conclusion count displays the number of pull requests that exited the merge queue during each time bucket. This includes passes, failures, and cancellations. Passes and failures signal a PR that was tested in the queue to completion, while canceled signals that the request to merge terminated before testing finished or before testing began.

Conclusion counts are an important signal to potential bottlenecks or underlying issues with your merging process, as a failure or cancellation in the merge queue can force other PRs to r**estart their testing**. A spike in the number of failures or passes can indicate a potential problem to investigate.

Conclusions are tagged with a reason to give further insights into how merges pass or fail in the queue. You can show or hide conclusions of a particular reason by using the **+ Add** button.

<table><thead><tr><th width="167">Category</th><th width="248">Reason</th><th>Description</th></tr></thead><tbody><tr><td>✅ Pass</td><td>Merged by Trunk</td><td>Passed all tests in Merge Queue and merged by Trunk</td></tr><tr><td>✅ Pass</td><td>Merged manually</td><td>User manually merged the PR in Git</td></tr><tr><td>❌ Failure</td><td>Test run timeout</td><td>User-defined timeout for tests exceeded</td></tr><tr><td>❌ Failure</td><td>Failed Tests</td><td>Required test failed while testing the PR in the merge queue</td></tr><tr><td>❌ Failure</td><td>Merge conflict</td><td>A (git) merge conflict encountered</td></tr><tr><td>❌ Failure</td><td>Config parsing failure</td><td>Malformed <code>trunk.yaml</code> that couldn't be parsed</td></tr><tr><td>❌ Failure</td><td>Config bad version</td><td>Invalid version field in <code>trunk.yaml</code></td></tr><tr><td>❌ Failure</td><td>Config bad required statuses</td><td>Failed to parse required statuses in <code>trunk.yaml</code></td></tr><tr><td>❌ Failure</td><td>No required statuses</td><td>No source for required tests was found in <code>trunk.yaml</code> or branch protection settings</td></tr><tr><td>❌ Failure</td><td>GitHub API Failed</td><td>GitHub returned an error to us that could not be resolved while processing the PR</td></tr><tr><td>❌ Failure</td><td>PR updated at merge time</td><td>PR updated as Trunk was attempting to merge it</td></tr><tr><td>🚫 Cancel</td><td>Canceled by user</td><td>PR explicitly canceled by user</td></tr><tr><td>🚫 Cancel</td><td>PR closed</td><td>PR closed (not merged)</td></tr><tr><td>🚫 Cancel</td><td>PR pushed to</td><td>New commits pushed to the PR branch while in the merge queue</td></tr><tr><td>🚫 Cancel</td><td>PR draft</td><td>PR was converted to a draft, which cannot be merged</td></tr><tr><td>🚫 Cancel</td><td>PR base branch changed</td><td>Base branch of PR in the merge queue changed</td></tr><tr><td>🚫 Cancel</td><td>Admin requested</td><td>Trunk employee canceled PR during a support session (extreme cases)</td></tr></tbody></table>

### Time in Queue

Time in queue shows how long each PR spends in the Merge Queue from the moment the PR enters the queue to the moment when it exits the queue, either from merging, failing, or being canceled.&#x20;

Understanding the amount of time a pull request is spending in the queue is important for ensuring your merge process continues to ship code quickly. A spike in the time to merge indicates a slowdown somewhere that's impacting all developers. For example, it's taking longer to run tests on PRs, PRs are waiting too long to start testing, or constant failures in the queue are causing PRs to take longer to merge

The time in queue can be displayed as different statistical measures. You can show or hide them by using the **+ Add** button.

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

CI Time measures the time it takes to test each pull request in the merge queue. Specifically, how long CI jobs have to run to test PRs. This measures **only CI steps relevant to the merge queue**, other CI steps like build or deploy or any workflows outside of the merge queue will not be measured.

{% hint style="info" %}
[Pushing data to CI Analytics](https://docs.trunk.io/ci-analytics/setup) is required to enable CI Time and CI Jobs Triggered charts if you're **not using GitHub Actions**.
{% endhint %}

Monitoring the amount of time it takes for CI workflows to test PRs is important for making sure PRs can move through the queue quickly. The more time it takes to test PRs, the more time a PR will be in the queue. Large spikes signal that work should be devoted to reducing the length of bottlenecking CI jobs, or more CI resources are needed.

\
CI Time to Test PRs can be shown as different statistical measures by pressing the **+ Add** button

| Measure                    | Explanation                                                                                                                                                                                                                                                                     |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Sum                        | The total time it has taken to run all CI jobs for all PRs in the queue                                                                                                                                                                                                         |
| Average Per Test Run       | The average amount of total CI time it takes to test a PR or batch of PRs in the queue.                                                                                                                                                                                         |
| Average Per Individual PR  | <p>The average amount of total CI time it takes to test an individual PR. This specifically accounts for <strong>batching</strong>.</p><p></p><p>For example, if a batch of 5 PRs takes 50 minutes of CI time to test, this would be 50 / 5 = 10 minutes on average per PR.</p> |
| Average Per Individual Job | The average amount of time it takes for an individual job to complete when testing a PR. There are usually multiple jobs launched when testing a PR.                                                                                                                            |

### **CI Jobs Triggered To Test PRs**

The count of Individual CI jobs that are triggered to test PRs in the merge queue. There could be multiple jobs triggered per PR - this metric captures all of them.

Each job will require a CI runner. A spike or large number of requested jobs can result in PRs waiting longer to begin testing.&#x20;

{% hint style="info" %}
[Pushing data to CI Analytics](https://docs.trunk.io/ci-analytics/setup) is required to enable CI Time and CI Jobs Triggered charts if you're **not using GitHub Actions**.
{% endhint %}
