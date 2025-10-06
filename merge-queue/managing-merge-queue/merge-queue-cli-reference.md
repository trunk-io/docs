# Merge Queue CLI Reference

The Trunk CLI allows you to insert and remove PRs into the Merge Queue. You can also pause and resume the queue from the CLI.

### Installation

{% tabs %}
{% tab title="macOS/Linux" %}
```bash
curl -LO https://trunk.io/releases/trunk
chmod +x trunk
```
{% endtab %}

{% tab title="Homebrew" %}
```bash
brew install trunk-io
```
{% endtab %}

{% tab title="Windows" %}
```bash
curl https://get.trunk.io -fsSL | bash
```
{% endtab %}
{% endtabs %}

### Prerequisites

Before using the CLI:

* **Authenticate:** Run `trunk login`
* **Git repository:** Execute commands from your repository root

### Usage

```bash
trunk merge [flags] <pr-number>
trunk merge [subcommand]
```

#### **Submit a PR to the Queue**

```bash
trunk merge <pr-number> [flags]
```

**Arguments**

`<pr-number>` - Pull request number to submit. Can be specified with or without `#` prefix (e.g., `1234` or `#1234`)

**Flags**

`-p, --priority <0-255>` - Priority determines the order PRs are tested and merged. When a PR is submitted with a priority, it will begin testing before any lower priority PR that isn't currently being tested. Levels:

* `0` (Urgent) **Interrupts currently testing PRs** to begin testing immediately. Use sparingly as restarting tests is costly. This is the only priority that interrupts running tests
* `10` (High) Tests before default priority PRs
* `100` (Default) Used when no priority is specified
* `200` (Low) Tests after default priority PRs
* `255` ( Lowest) Lowest possible priority

If multiple PRs have the same priority, they are processed in the order they were submitted. See [Priority Levels](../concepts-and-optimizations/pr-prioritization.md).

**Examples**

{% tabs %}
{% tab title="Default Priority" %}
```bash
trunk merge 1234
```
{% endtab %}

{% tab title="High Priority" %}
```bash
trunk merge 1234 -p 10
```
{% endtab %}

{% tab title="Low Priority" %}
```bash
trunk merge 1234 -p 200
```
{% endtab %}

{% tab title="Urgent" %}
{% hint style="warning" %}
Other PRs testing in the queue will be restarted behind PR 1234
{% endhint %}

```bash
trunk merge 1234 -p 0
```
{% endtab %}
{% endtabs %}

#### Check Queue Status

```bash
trunk merge status
```

Display a snapshot of merge queue activity for the current branch, including:

* Recently merged PRs
* Currently testing PRs
* PRs waiting in queue

```
Trunk Merge Status [main] [Running]

 ✔ Merged     #1835  fix: smoke test workflows
                     Updated 12 minutes ago

   Testing    #1840  Add new feature
                     Testing for 3 minutes

   Queued    #1842  Update documentation
                     Waiting in queue
```

#### **View PR Status and History**

```bash
trunk merge status <pr-number>
```

Display detailed merge history and timeline for a specific pull request, including:

* When it was submitted
* Status changes over time
* Test results
* Links to test runs

Example output:

```bash
trunk merge status 1835

#1835 fix: smoke test workflows (username)
Learn more at https://app.trunk.io/gh/org/repo/merge/main/1835

10-03 21:01:36    Not Ready      Pull request submitted to Merge. Waiting for branch protection rules.
10-03 21:04:34    Pending        Added to merge queue
10-03 21:04:38    Testing        Tests running
10-03 21:17:02    Tests Passed   All required tests passed
10-03 21:17:05    ✔ Merged       Pull request merged successfully
```

#### **Cancel a PR**

Remove a pull request from the merge queue. Use cases:

* Cancel before making additional changes to the PR
* Cancel to resubmit with different priority

```bash
trunk merge cancel <pr-number>
```

#### Pause Queue \[admin only]

Pause the merge queue, changing its state from `Running` to `Paused`.  The ordering of PRs in the queue is preserved while paused.

```bash
trunk merge pause
```

**When to use:**

* **CI failure recovery** - Stop merges and testing until infrastructure issues are resolved
* **Test infrastructure outages** - Pause until systems are back online
* **Emergency situations** - Prevent any merges during incident response
* **Scheduled maintenance** - Block merges during maintenance window

#### Resume Queue \[admin only]

Resume merge queue processing, changing its state from `Paused` back to `Running`. The queue will begin testing waiting PRs in priority order.

```bash
trunk merge resume
```



