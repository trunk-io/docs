---
description: Interacting with your merge queue from the command line
---

# Command Line

The Trunk CLI allows you to insert and remove PRs into the Merge Queue. You can also pause and resume the queue from the CLI.

Before you can use the CLI, install it following the [CLI Installation docs](../../references/cli/install.md).

<table><thead><tr><th width="271">trunk merge &#x3C;command></th><th>Description</th></tr></thead><tbody><tr><td><code>status</code></td><td>display snapshot of activity in the merge queue including recently merged, currently testing, and enqueued pull requests</td></tr><tr><td><code>status &#x3C;pr-number></code></td><td>display merge queue history for the pull request</td></tr><tr><td><code>&#x3C;pr-number></code></td><td>insert the specified pull request into the merge queue</td></tr><tr><td><code>cancel &#x3C;pr-number></code> </td><td>remove a pull request from the merge queue</td></tr><tr><td><code>pause</code></td><td>[admin only] pause the merge queue processing</td></tr><tr><td><code>resume</code></td><td>[admin only] resume merge queue processing</td></tr></tbody></table>

