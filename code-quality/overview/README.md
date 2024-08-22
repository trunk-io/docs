# Overview

### Why metalinters?

Real-world code bases are complicated. Every project has many different types of files. There are your main programming language files, Markdown docs, infrastructure as code (IaC), dependency files, YAML config files, images, and so much more. All of these files need to be linted, formatted, optimized, and scanned.

A metalinter helps you lint **every file** in a modern code base by installing, managing, running, and reporting from individual static analysis tools with a **single tool**.

### Use Cases

There are many reasons for you to want to use a metalinter like Trunk Code Quality.

#### You don't want to think about linting

Trunk Code Quality is easy to adopt. [Running `trunk init`](../setup-and-installation/initialize-trunk.md) will [recommend linters and formatters](../linters/supported/) for your project with reasonable default configuration. Hold off on fixing existing issues using [hold-the-line](how-does-it-work.md#hold-the-line) and only get warnings for new issues introduced in each commit or PR.

Trunk Code Quality [GitHub Integration](broken-reference)s to set up nightly runs and linter checks on PRs.&#x20;

#### Run and manage a long list of linters

Trunk will install, manage, and run tools like linters and formatters for you. Trunk uses [hermetic installs](how-does-it-work.md#hermetic-tools-and-runtime-management) to manage both the static analysis [tools](../../cli/getting-started/tools.md) themselves and the [runtimes they depend](../../cli/configuration/runtimes.md) on. No more conflicts because a linter requires `python 3.11` while your projects require `python 3.7`.

#### Incrementally adopt new linters

[Adopting new linters is a pain](https://trunk.io/blog/reasons-developers-hate-linters) because of the large amount of upfront configuration and fixes needed. Enabling a new linter or formatter in an old repo will yield thousands of issues, most of which might not have auto fixes.

Trunk supports [hold-the-line](how-does-it-work.md#hold-the-line) to lint only new issues introduced with a commit or PR, to let developers adopt new linters fast, focus on preventing new issues first, and[ report on existing issues nightly](broken-reference) to fix later. Waiting will only accumulate debt, stop debt accumulation immediately and fix as you code.

#### Linters take too long to run

Do you have a giant code base? Maybe even a giant monorepo with many languages to lint? Most linters are not Git-aware, which makes them slow to run on large repos. Trunk Code Quality [can lint what's changed](how-does-it-work.md#hold-the-line), so you won't be stuck linting 20 million lines of code when you've changed just 1 word.

#### Installing many linters individually on everyone's machine

Many linters don't install neatly through a package manager, and for those that do, they depend on your system's runtime environment. Dodge repetitive setup by using a single tool to lint **every language in your organization** using any of the [100+ supported linters](../linters/supported/).

#### Consistent linter configs and versions

Trunk Code Quality uses an extensible [plugin system](../../cli/configuration/plugins/), so you can define linters to [auto-enable](../../cli/configuration/lint/auto-enable.md) and [share linter configurations](../../cli/configuration/plugins/external-repositories.md) to standardize across code bases.&#x20;

#### Lack of consistent output and reporting

Every linter outputs differently. If you've got a backlog of issues like ESLint errors, OSV Scanner dependency vulnerabilities, poorly optimized images, and vulnerabilities in your Docker Config, you'd want to see them in an [organized report](broken-reference), sorted by severity or by file, with[ consistent format](../../cli/configuration/lint/output-parsing.md). Trunk Code Quality can do this.

### Features

Trunk Code Quality helps address these issues by:

#### Hold-the-line

Linters are slow to run for large codebases with numerous issues and many linters. Trunk Code Quality solves this problem by _**only scanning new code**_ by default, allowing you to handle the backlog when you are ready while preventing new issues. This is the #1 reason people use Trunk Code Quality.

#### **Inconsistent tooling for different file types**

Trunk Code Quality provides a single way to check _everything_ in your codebase, including config and script files, as well as the main language(s) for your codebase. If you are already using ESLint for a JavaScript repo, you probably also have some bash scripts, CI yaml, Kube config, and other files for your workflow.&#x20;

These all have great tools you could be running, but they don't all install through npm. Trunk Code Quality simplifies this process by detecting and configuring the right tools for the files in your repo.

#### **Slow static analysis affecting development speed**

Trunk Code Quality speeds up static analysis by using a background daemon to check code as you modify files in your repo, run linters in batches, and cache the results. Since Code Quality is git-aware, it knows what you've changed, and by adding batched execution and caching, you end up with a much faster and smoother way to run these tools.

#### **Time-consuming PR iteration and triage**

Trunk Code Quality speeds up PR iteration by showing the _same_ results locally and [on CI](https://docs.trunk.io/code-quality/ci), improving PR triage. It can optionally also function as a [githooks manager](https://docs.trunk.io/code-quality/advanced-setup/actions/git-hooks) to reject `git push`es unless they're passing `trunk check`

#### **Lack of team visibility into the repo's health**

Trunk Code Quality improves team communication by providing a [web app](https://app.trunk.io/login?intent=check) for repo stats and [slack notifications](https://docs.trunk.io/administration/integration-for-slack), ensuring everyone on the team is aware of the current health of your repo.

### Components

Trunk Code Quality has many components that fit into different stages of your development workflow.

* **During local development:** Get realtime annotations using the [Trunk CLI](../setup-and-installation/initialize-trunk.md), [VSCode Extension](../ide-integration/vscode.md), or [Neovim plugin](../ide-integration/neovim.md).
* **In cloud development environments:** Trunk can be used in [GitHub Codespaces](../../cli/configuration/github-codespaces.md).
* **Before committing and pushing,** Trunk can automatically run linters and formatters using Git hooks.
* **On PRs and in CI:** Using our GitHub integration, setting up your own GitHub workflows, or in your own CI environments.
* **Reporting and analytics**: Using the Trunk Web App.
