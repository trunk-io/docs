---
description: 'Meta-linter for over 100 code checking tools: CLI, IDE, and on the web.'
---

# Check

## What is Trunk Check?

**Trunk Check** runs 100+ idiomatic code-checking tools for every language and technology, locally ([CLI](advanced-setup/cli/), [VS Code Extension](ide-integration/vs-code.md)), on CI ([CI](check-cloud-ci-integration/), [GitHub Bot](check-cloud-ci-integration/get-started/)), and in our [web app](https://app.trunk.io). If you're already running a few of these tools (ESLint, Prettier, etc), Trunk Check lets you run them faster, upgrade them easier, integrate them with CI and PRs, and version them better.

{% hint style="info" %}
[Get started in 60 seconds](usage.md) locally with no login or account.
{% endhint %}

## Check handles:

* Auto-formatting your code, config files, IaC, and more
* Linting
* Static Analysis
* Optimizing images
* Flagging leaked secrets
* Flagging open-source dependencies with vulnerabilities

## What problems does Trunk Check solve?

* **Only scanning new code by default.** Trunk Check can handle a code base with lots of issues by only scanning new code by default ([Hold The Line](configuration/hold-the-line.md)), so you can handle the backlog when you are ready. (This is the #1 reason people use Trunk check).
* **Supporting config and script files** as well as the main language for your codebase. If you are already using eslint for a javascript repo, you probably also have some bash scripts, ci yaml, kube config, and other files for your workflow. These all have great tools you could be running but they don't all install through npm. Trunk Check gives you a single way to check everything in your codebase.
* **Speed up static analysis** by using a daemon to check code as you modify files in your repo, run linting in batches, and cache the results for many linters. Since Check it's git-aware, it knows what you've changed, and by adding batched execution and caching, you end up with a much faster and smoother way to run these tools.
* **Speed up PR integration** by showing the _same_ results locally and [on CI](check-cloud-ci-integration/), speeding up PR iterations and PR triage. It can optionally also function as a [githooks manager](advanced-setup/actions/git-hooks.md) to reject `git push`es unless they're passing `trunk check`.
* Team Communication. Using a [web app](https://app.trunk.io/) for repo stats and [slack notifications](../administration/integration-for-slack.md), everyone on the team knows the current health of your repo.

Next Step: [ Get Started installing Trunk Check](usage.md).
