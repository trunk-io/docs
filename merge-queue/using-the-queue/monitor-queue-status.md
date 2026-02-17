# Monitor queue status

### Access the Merge Queue dashboard

The Trunk Merge Queue dashboard gives you real-time visibility into your queue's activity.

**Access the dashboard:**

1. **Navigate to Trunk:** [https://app.trunk.io](https://app.trunk.io/)
2. **Select your organization** (if you're in multiple)
3. **Click** the **Merge Queue** tab in the upper left
4. Select your repository

**Quick access from GitHub:**

* Trunk bot comments include dashboard links
* Click any link in bot comments to go directly to that PR's status

### Queue overview

The main dashboard shows a high-level view of your merge queue activity.

<figure><img src="../../.gitbook/assets/merge-queue-screen.png" alt=""><figcaption><p>Clicking on a queue item navigates you to the details page.</p></figcaption></figure>

### Queue view

View status of the queue and recent activity in the **Queue** tab

#### **Active queue status:**

* **Currently testing**: Which PR is running tests right now
* **Queued PRs**: How many PRs are waiting
* **Merged**: List of previously merged PRs

#### **Activity feed:**

* PRs merged in the last 24 hours
* Success rate (percentage of PRs that passed tests)
* Average merge time
* Failed PRs requiring attention

### Graph view

The graph view provides a visual representation of all current PRs being tested by Trunk Merge Queue and their relationships. Each node represents a pull request or a batch of pull requests, and each edge indicates testing dependencies. All edges point towards the target branch; as items merge, the affected queues restructure. If running in `Single` mode, this will be a single line showing the testing and merging process.

#### Reading the graph

The graph organizes PRs into distinct sections based on their current status:

* **Merged section (green)**: PRs displayed at the top of the graph in the green section have successfully merged into the target branch.
* **Testing and queued sections**: PRs currently being tested or waiting in the queue appear in the main body of the graph.

**Batching information**: When [batching](../optimizations/batching.md) is enabled, each node in the graph displays batch details so you can see which PRs are grouped together for testing.

**Bisection tab**: When a batch fails and [bisection](../optimizations/batching.md#bisection-testing-concurrency) is in progress, a side tab appears showing the bisection process and its current status.

#### Interacting with the graph

* **Hover** over any node to highlight its path to the root of the graph, making it easy to trace a PR's position and dependencies in the queue.
* **Click** on a node to navigate to the details page for that PR. For batched items, clicking a batch node takes you to the actual PR opened for that batch.

#### Graph legend

The graph includes a legend that explains the meaning of each node color and icon, so you can quickly understand the state of every item in the queue at a glance.

#### Legacy graph view

If you need to access the previous graph layout, a link to the legacy graph view is available at the top of the graph page.

### Health view

Select a period of time to inspect using the **Period** dropdown (default 7 days) and a **Granularity** (defaults  to daily) of queue metrics

#### Conclusion counts

A Bar chart of PRs and their statuses. More Green = More Merges!

#### Time in queue

View statical trends of PR time in queue, default p50 view is useful for an "Average time in queue" evaluation.



## Pull request details

The PR details show information about a PR, including a link to the PR in GitHub, the history of the PR within Trunk Merge Queue, and what must be done before a PR can be admitted to the queue for PRs that have not entered the queue yet.

When a PR has not been admitted to the queue yet, Trunk Merge Queue waits for:

1. Impacted targets to be uploaded for the PRs current SHA (`Parallel` mode only)
2. The PR to be mergeable according to GitHub. If the PR is not mergeable yet, this most likely means that the PR is not meeting all branch protection rules you have set (for example, not all required status checks have passed yet) or has a merge conflict with the target branch
3. The target branch of the pull request to match the branch that merge queue merges into

<figure><img src="../../.gitbook/assets/merge-details (1).png" alt=""><figcaption><p>PR readiness details for a PR that has been submitted but has not yet entered the merge queue.</p></figcaption></figure>

In the screenshot above, the PR has been submitted to Merge but has not yet been added to the queue. It will be added once all of the branch protection rules pass and there are no merge conflics with the target branch.
