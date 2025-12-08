# Priority merging

### What it is

Priority merging allows you to fast-track critical pull requests to the front of the merge queue.&#x20;

By assigning a priority level to a PR, you can ensure urgent changes (like hotfixes, security patches, or critical bug fixes) merge ahead of regular feature work. PRs with higher priority are tested and merged before lower-priority PRs, regardless of when they were submitted.

### Why use it

* **Fast-track critical fixes** - Get security patches and hotfixes to production in minutes, not hours. Priority PRs bypass the normal queue order and merge immediately after testing.
* **Respond to incidents quickly** - When production is down, you can't wait for 20 feature PRs to merge first. Priority merging lets you deploy fixes urgently while maintaining merge queue safety.
* **Prevent emergency merges** - Instead of bypassing the queue entirely (risky!), use priority merging to maintain safety while getting urgent PRs through fast. All PRs still get tested, but yours goes first.
* **Balance urgency with safety** - Priority PRs still go through full testing and validation. You get speed without sacrificing the protection that merge queues provide.

### How to enable

Priority merging is **built in** - you don't need to enable a setting. You set priority on individual PRs when you need them to be fast-tracked.

#### Enable via GitHub comment

On any pull request, comment:

```
/trunk merge --priority=<level>
```

or

```
/trunk merge -p <level>
```



#### Enable via Command Line argument

From the command line enter the following command:

```shell
trunk merge <pr-number> --priority=<level>
```

or

```
trunk merge <pr-number> -p <level>
```

#### Valid priority levels

<table><thead><tr><th width="151">label</th><th width="109">number</th><th>note</th></tr></thead><tbody><tr><td>urgent</td><td>0</td><td>Production outages, security vulnerabilities.<br><br>urgent items will interrupt running jobs and begin testing immediately</td></tr><tr><td>high</td><td>10</td><td>Urgent bug fixes, important hotfixes</td></tr><tr><td>medium</td><td>100</td><td>Regular feature work (default)</td></tr><tr><td>low</td><td>200</td><td>Non-urgent refactors, documentation</td></tr><tr><td></td><td>255</td><td>lowest possible priority</td></tr></tbody></table>

### How priority affects PR order

PRs with a higher priority will always begin testing before any other PR that isn't currently being tested, ensuring that prioritized PRs move into the queue as soon as they can. A PR without a priority will use the default `medium` (100) priority. If there is already a PR in the queue with the same priority, then the new one will be behind it.

When prioritizing a PR, Merge will explicitly **not interrupt** any currently testing PR, as restarting testing on PRs is usually costly, even if you want another PR to be sooner. Because of this, if a PR is submitted with a priority and there is still room in the queue to begin testing PRs, it will begin testing as normal without interrupting other PRs.

**There is an exception to this rule.** Sometimes, when there is a PR urgent enough to get in that it is worth the cost of restarting a currently testing PR, you can move the new PR to the front using the `"urgent"` priority. This is the only time Merge will reschedule a PR that is already in testing.

{% hint style="warning" %}
Another exception: Admins can still merge PRs in absolutely necessary cases outside of the merge queue. Merge Queue handles thes gracefull and will react properly to restart the rest of the queue.
{% endhint %}

#### Example:

Say you have a queue that is configured to test two PRs at once. The queue currently looks like this:

<img src="../../.gitbook/assets/file.excalidraw (11).svg" alt="Queue with two testing PRs and one pending" class="gitbook-drawing">

If you submit a PR D with a `"high"` priority it will be put in front of C (since it is a higher priority than C and C is not testing). D will begin as soon as either A or B finishes, like this:

<img src="../../.gitbook/assets/file.excalidraw (12).svg" alt="Queue with two testing PRs and a new higher priority pending PR" class="gitbook-drawing">

Instead, if you submit PR D with an `"urgent"` priority, then D would be tested immediately, A would be restarted, and B would be bumped back to pending, like this:

<img src="../../.gitbook/assets/file.excalidraw (13).svg" alt="Queue with an urgent PR moved to the front and a normal PR restarting" class="gitbook-drawing">

### Tradeoffs and considerations

#### What you gain

* **Emergency response capability** - Critical fixes merge in minutes
* **Incident resolution speed** - Production issues resolved faster
* **Maintained safety** - Unlike bypassing the queue, priority PRs still get tested
* **Team confidence** - Developers know urgent fixes can get through quickly

#### What you give up or risk

* **Queue disruption for others** - Normal PRs wait longer when priority PRs jump ahead
* **Potential for abuse** - If everyone marks their PR as high priority, the system loses effectiveness
* **Fairness concerns** - Team members may feel frustrated if priorities are used unfairly

#### When NOT to use priority merging

Don't use high priority for:

* **Feature work marked "urgent" by product** - This should be normal priority
* **"I want my PR to merge faster"** - Wait your turn
* **End-of-sprint rushing** - Better sprint planning is the solution
* **Every PR from senior engineers** - Priority should be about the PR, not the author

**Use high priority ONLY for:**

* Production outages and incidents
* Security vulnerabilities
* Critical bug fixes blocking users
* Emergency hotfixes

#### Best practices

**Establish priority guidelines:** Document when priority should and shouldn't be used. Example:

* `high` = Production down, security issue, critical bug affecting users
* `medium` = Everything else

**Monitor priority usage:** Track how often priority is used. If >10% of PRs are high priority, you have a process problem, not a priority problem.

**Rotate on-call priority power:** Only the current on-call engineer can set high priority. This prevents abuse and ensures judgment calls are made by whoever is dealing with the incident.

#### Common misconceptions

* **Misconception:** "Priority PRs skip testing"&#x20;
  * **Reality:** No! Priority PRs go through full testing, they just test first. Safety is never compromised.
* **Misconception:** "I can mark my PR priority to avoid waiting"&#x20;
  * **Reality:** Priority should be reserved for genuine emergencies. Overuse makes the system meaningless for everyone.
* **Misconception:** "Priority PRs interrupt currently running tests"&#x20;
  * **Reality:** Priority PRs queue at the front but don't cancel in-progress tests. The system remains stable.

### Next Steps

**Set up priority guidelines:**

1. Document when to use high priority (share with your team)
2. Configure permissions (limit who can set priority)
3. Communicate guidelines in team onboarding docs

**Use priority responsibly:**

* Reserve for true emergencies only
* Monitor usage to prevent abuse
* Consider rotation-based permission (only on-call can set priority)

**For true emergencies:**

* If priority isn't fast enough → Emergency pull requests
* If you need to pause the queue → **Settings** > **Repositories** > your repository > **Merge Queue** > **Merge Queue State** and select **Paused** from the dropdown.

**Monitor impact:**

* [Metrics and monitoring](../administration/metrics.md) - Track priority PR usage and merge times
* Watch for priority overuse (should be <5% of PRs)

