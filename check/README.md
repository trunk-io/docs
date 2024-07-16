---
description: 'Meta-linter for over 100 code checking tools: CLI, IDE, and on the web.'
---

# Check

## What is Trunk Check?

**Trunk Check** runs 100+ idiomatic code-checking tools for every language and technology, locally ([CLI](advanced-setup/cli/), [VS Code Extension](ide-integration/vs-code.md)), on CI ([CI](check-cloud-ci-integration/), [GitHub Bot](check-cloud-ci-integration/get-started/)), and in our [web app](https://app.trunk.io/login?intent=check). If you're already running a few of these tools (ESLint, Prettier, etc), Trunk Check lets you run them faster, upgrade them easier, integrate them with CI and PRs, and version them better.

{% hint style="info" %}
[Get started in 60 seconds](usage.md) locally with no login or account.
{% endhint %}

## Check handles:

* Auto-formatting your code, config files, IaC, and more
* Enforcing code style standards
* Linting
* Static Analysis
* Optimizing images
* Flagging leaked secrets
* Flagging open-source dependencies with vulnerabilities

## What problems does Trunk Check solve?

* **Handling large codebases with numerous issues.** Trunk Check solves this problem by _only scanning new code_ by default ([Hold The Line](configuration/hold-the-line.md)), allowing you to handle the backlog when you are ready. This is the #1 reason people use Trunk Check.
* **Inconsistent tooling for different file types.** Trunk Check provides a single way to check _everything_ in your codebase, including config and script files, as well as the main language for your codebase. If you are already using ESLint for a JavaScript repo, you probably also have some bash scripts, CI yaml, Kube config, and other files for your workflow. These all have great tools you could be running, but they don't all install through npm. Trunk Check simplifies this process by detecting and configuring the right tools for the files in your repo.
* **Slow static analysis affecting development speed.** Trunk Check speeds up static analysis by using a background daemon to check code as you modify files in your repo, run linters in batches, and cache the results. Since Check is git-aware, it knows what you've changed, and by adding batched execution and caching, you end up with a much faster and smoother way to run these tools.
* **Time-consuming PR iteration and triage.**  Trunk Check speeds up PR iteration by showing the _same_ results locally and [on CI](check-cloud-ci-integration/), speeding up PR iterations and PR triage. It can optionally also function as a [githooks manager](advanced-setup/actions/git-hooks.md) to reject `git push`es unless they're passing `trunk check`
* **Lack of team visibility into the repo's health.** Trunk Check improves team communication by providing a [web app](https://app.trunk.io/login?intent=check) for repo stats and [slack notifications](../administration/integration-for-slack.md), ensuring everyone on the team is aware of the current health of your repo.

Next Step: [ Get Started installing Trunk Check](usage.md).
