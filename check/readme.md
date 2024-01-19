# Check

## What is Trunk Check?

**Trunk Check** runs 100+ idiomatic code-checking tools for every language and technology, locally ([CLI](cli/), [VS Code Extension](https://marketplace.visualstudio.com/items?itemName=trunk.io)), on CI ([CI](check-cloud-ci-integration/), [GitHub Bot](check-cloud-ci-integration/get-started/)), and in our [web app](https://app.trunk.io). You're probably already running a few of these tools (ESLint, Prettier, etc), but Trunk Check adds valuable features to let you integrate with CI and PRs, run them faster, upgrade them easier, integrate them with CI and PRs, version them better, and much more.

Check handles:

* Autoformatting code, config files, IaC, and more
* Linting
* Static Analysis
* Optimizing images
* Flagging leaked secrets
* Flagging open-source dependencies with vulnerabilities

## Install the CLI

The `trunk` command line tool runs locally on your developer machine, right where your code is. Later, you can automatically scan your repo using [Trunk Check Cloud](check-cloud-ci-integration/).

Check will automatically keep tools up to date, suggest standard tools for your project type (eg: `clang-format` for C++, `eslint` for JS/TS), and pin versions in `trunk.yaml` to ensure Trunk Check is reproducible.

{% tabs %}
{% tab title="bash" %}
```bash
curl https://get.trunk.io -fsSL | bash
```
{% endtab %}

{% tab title="bash (no prompts)" %}
```bash
curl https://get.trunk.io -fsSL | bash -s -- -y
```
{% endtab %}

{% tab title="brew" %}
```bash
brew install trunk-io
```
{% endtab %}

{% tab title="npm" %}
```bash
npm install -D @trunkio/launcher
```
{% endtab %}

{% tab title="pnpm" %}
```bash
pnpm add -D @trunkio/launcher
```
{% endtab %}

{% tab title="yarn" %}
```bash
yarn add -D @trunkio/launcher
```
{% endtab %}
{% endtabs %}

## Initialize `trunk`

From the root of a git repo, run:

```bash
trunk init
```

This will scan your repository and create a `.trunk/trunk.yaml` that enables all the linters, formatters, and security analyzers that [Trunk Check](./) recommends. For more details, see [here](cli/init-in-a-git-repo.md).

## What problems does Trunk Check solve?

#### If I turn on a new rule or code-checking tool, how do I handle the zillion existing issues in my repo?

'[Hold the line](under-the-hood.md#hold-the-line)' is a Trunk Check feature that works for _all_ tools Trunk Check runs. It detects which issues are preexisting or not, in a sophisticated way (we correctly handle the cases in which you modify one line of code and it causes new issues downstream of that). By default, we only call _new_ issues "blocking issues" for the purposes of gating PRs and running `trunk check` locally.

This is the #1 feature driving why large companies purchase Trunk Check licenses. Without this, turning on a new linting rule may counter-intuitively _increase_ your tech debt. This typically happens because you force every modified file to be clean of errors in pull requests. In real life, this means devs optimize for touching as few files as possible to avoid cleaning up all the issues they didn't affect. Things like renaming a class or function across many files will never be done, because a simple find+replace turns into an effort of fixing a hundred lint issues just to merge it. Plus, fixing unrelated issues to your changes is just a poor separation of responsibilities for pull requests.

#### There are more tools I could run, but they're not in the package manager my repo uses

In the world of code checking, more is more! Let's say you have a mostly javascript/typescript repo, so your package manager ecosystem is npm. You have other technologies in the repo though, maybe some bash scripts, dockerfiles, kube config, ci yaml, and all of those technologies have great checking tools that you could be running, but some are golang, some are direct downloads, some are python, and they aren't available on npm. You don't want to bring a bunch of new package managers into your repo for these 1-off tools. That's where Trunk Check comes in. You version these tools in `.trunk/trunk.yaml`, and trunk can fetch them and run them from all the package managers or direct downloads you _don't_ use in your repo.

#### Static analysis is slow

Trunk Check has a daemon that checks code as you modify files in your repo, runs linting in batches, and caches off the results for many linters. Since it's git-aware, it knows what you've changed, and by adding batched execution and caching, you end up with a much faster and smoother way to run these tools.

#### PRs often fail our "Lint" CI job and need one or more extra iterations to fix it

PR iterations kill productivity. Every time a dev updates a PR, even trivially, they have to context switch, break out of flow, reviewers also context switch to look at it, and that's not to mention the CI time to run a new suite of jobs.

`trunk check` shows the _same_ results locally and [on CI](check-cloud-ci-integration/). It can optionally also function as a[git-hooks.md](actions/git-hooks.md "mention") manager to reject `git push`es unless they're passing `trunk check`.

## Standout Features

* does everything from formatting, to linting, to security checking, to optimizing images
* config-as-code (`.trunk/trunk.yaml`)
* caching
* pre-existing issue detection
* a daemon & language server
* [githooks management](actions/git-hooks.md)
* cli available ([docs](cli/))
* a [web app](https://app.trunk.io/) for repo stats and slack notifications

## I run a large eng org. Why should I use Check?

When you modify a file, Trunk Check has a feature called Hold The Line, which only flags the _new_ issues. It does this by being git-aware and using sophisticated heuristics (to handle the case where you change one line of code and new issues pop up somewhere else because of it).

This feature is critical for eng orgs because it allows you to start leveling up your codebase without making devs fix every preexisting issue in every file they touch, which would dramatically slow down development and cause a lot of frustration. Without this feature, it's impractical to turn on new rules in existing code-checking tools, but it's also impractical to add new tools to your code-checking arsenal. With it, adding a new tool is as easy as `trunk check enable <linter>`, and you can start being better going forward and tackle your tech debt incrementally, on your own terms.

## Supported Linters, Formatters, and Security Tools

We support over 100 different linters and formatters, and we're adding new integrations every release. Check out our full list of [Supported Linters](usage/supported-linters.md). Stop by on [Slack](https://slack.trunk.io) and let us know what you'd like next! All tool integrations are open-source [here](https://github.com/trunk-io/plugins).Enable the following tools:

```bash
trunk check enable <linter>
```

1. Support for Detekt is under active development; see our [docs](https://docs.trunk.io/docs/check-supported-linters#detekt) for more details.
2. [Module inspection](https://github.com/terraform-linters/tflint/blob/master/docs/user-guide/module-inspection.md), [deep checking](https://github.com/terraform-linters/tflint-ruleset-aws/blob/master/docs/deep\_checking.md), and setting variables are not currently supported.

## How it works

Trunk downloads everything it needs to run on demand and caches it in `~/.cache/trunk`. We run linters in parallel, in the background, and function as a [language server](https://microsoft.github.io/language-server-protocol) to show results inline in VSCode via the [Trunk VSCode Extension](./#install-the-vscode-extension).

## Install the VSCode Extension

If you run VSCode you can also install the [trunk VSCode extension](vscode:extension/Trunk.io). Read more about it [here](https://marketplace.visualstudio.com/items?itemName=Trunk.io).

## Run `trunk check`

`trunk` is git-aware, so without further arguments, it will run on the files you've changed in your repo:

```bash
trunk check
```

Note: if you have not modified any files, `trunk check` will not check anything. See the [CLI usage docs](usage/) for more info on basic `trunk` usage.
