# Why Metalinters?

### Why metalinters?

Real-world code bases are complicated. Every project has many different types of files. There are your main programming language files, Markdown docs, infrastructure as code (IaC), dependency files, YAML config files, images, and so much more. All of these files need to be linted, formatted, optimized, and scanned.

A metalinter helps you lint **every file** in a modern code base by installing, managing, running, and reporting from individual static analysis tools with a **single tool**.

### Use cases

There are many reasons for you to want to use a metalinter like Trunk Code Quality.

#### You don't want to think about linting

Trunk Code Quality is easy to adopt. [Running `trunk init`](setup-and-installation/initialize-trunk.md) will [recommend linters and formatters](linters/supported/) for your project with reasonable default configuration. Hold off on fixing existing issues using [hold-the-line](how-does-it-work.md#hold-the-line) and only get warnings for new issues introduced in each commit or PR.

Use Trunk Code Quality [GitHub Integrations](setup-and-installation/github-integration.md) to set up nightly runs and linter checks on PRs.

#### Run and manage a long list of linters

Trunk will install, manage, and run tools like linters and formatters for you. Trunk uses [hermetic installs](how-does-it-work.md#hermetic-tools-and-runtime-management) to manage both the static analysis [tools](cli/getting-started/tools.md) themselves and the [runtimes they depend](cli/getting-started/configuration/runtimes.md) on. No more conflicts because a linter requires `python 3.11` while your projects require `python 3.7`.

#### Incrementally adopt new linters

[Adopting new linters is a pain](https://trunk.io/blog/reasons-developers-hate-linters) because of the large amount of upfront configuration and fixes needed. Enabling a new linter or formatter in an old repo will yield thousands of issues, most of which might not have auto fixes.

Trunk supports [hold-the-line](how-does-it-work.md#hold-the-line) to lint only new issues introduced with a commit or PR, to let developers adopt new linters fast, focus on preventing new issues first, and[ report on existing issues nightly](setup-and-installation/github-integration.md) to fix later. Waiting will only accumulate debt; stop debt accumulation immediately and fix as you code.

#### Linters take too long to run

Do you have a giant code base? Maybe even a giant monorepo with many languages to lint? Most linters are not Git-aware, which makes them slow to run on large repos. Trunk Code Quality [can lint what's changed](how-does-it-work.md#hold-the-line), so you won't be stuck linting 20 million lines of code when you've changed just 1 word.

#### Installing many linters individually on everyone's machine

Many linters don't install neatly through a package manager, and for those that do, they depend on your system's runtime environment. Dodge repetitive setup by using a single tool to lint **every language in your organization** using any of the [100+ supported linters](linters/supported/).

#### Consistent linter configs and versions

Trunk Code Quality uses an extensible [plugin system](cli/getting-started/configuration/plugins/), so you can define linters to [auto-enable](cli/getting-started/configuration/lint/auto-enable.md) and [share linter configurations](linters/shared-configs.md) to standardize across code bases.

### Features

Trunk Code Quality helps address these issues by:

#### Hold-the-line

Linters are slow to run for large codebases with numerous issues and many linters. Trunk Code Quality solves this problem by _**only scanning new code**_ by default, allowing you to handle the backlog when you are ready while preventing new issues. This is the #1 reason people use Trunk Code Quality.

#### **Inconsistent tooling for different file types**

Trunk Code Quality provides a single way to check _everything_ in your codebase, including config and script files, as well as the main language(s) for your codebase. If you are already using ESLint for a JavaScript repo, you probably also have some bash scripts, CI yaml, Kube config, and other files for your workflow.

These all have linters you could be running, but they don't all install through npm. Trunk Code Quality simplifies this process by detecting and configuring the right tools for the files in your repo.

#### **Slow static analysis affecting development speed**

Trunk Code Quality speeds up static analysis by using a background daemon to check code as you modify files in your repo, run linters in batches, and cache the results. Since Code Quality is git-aware, it knows what you've changed, and by adding batched execution and caching, you end up with a much faster and smoother way to run these tools.

#### **Time-consuming** pull request **iteration and triage**

Trunk Code Quality speeds up PR iteration by showing the _same_ results locally and [on CI](setup-and-installation/prevent-new-issues/), improving PR triage. It can optionally also function as a [githooks manager](cli/getting-started/actions/git-hooks.md) to reject `git push`es unless they're passing `trunk check`.

### Components

Trunk Code Quality has many components that fit into different stages of your development workflow.

* **During local development:** Get realtime annotations using the [Trunk CLI](setup-and-installation/initialize-trunk.md), [VSCode Extension](ide-integration/vscode.md), or [Neovim plugin](ide-integration/neovim.md).
* **In cloud development environments:** Trunk can be used in [GitHub Codespaces](ide-integration/github-codespaces.md).
* **Before committing and pushing,** Trunk can automatically run linters and formatters using Git hooks.
* **On PRs and in CI:** Using our GitHub integration, setting up your own GitHub workflows, or in your own CI environments.
