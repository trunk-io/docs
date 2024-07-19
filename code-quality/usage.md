---
description: How to install the Trunk CLI to check your code in less than 60 seconds.
---

# Getting Started

The `trunk` command line tool runs locally on your developer machine, right where your code is. Later, you can automatically scan your repo using the [Trunk Code Quality webapp](ci/). Trunk Code Quality will automatically keep tools up to date, suggest standard tools for your project type (eg: `clang-format` for C++, `eslint` for JS/TS), and pin versions in `trunk.yaml` to ensure Trunk Code Quality is reproducible.

## Install the CLI

Run one of the following to install the `trunk` command line tool.

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

This will scan your repository and create a `.trunk/trunk.yaml` that enables all the linters, formatters, and security analyzers that are recommended for your project based on the source code types (\*`.c`, \*.`py`, \*.`js`, etc.) as well as existing tool configuration files (ex: `.eslintrc`, `.clang-format`, `.flake8`).  You can enable additional linters with the `trunk check enable <toolname>` command.  For more details, see [here](advanced-setup/cli/init-in-a-git-repo.md).

## Basic Usage

The main commands when running `trunk` from the command line are:

```bash
trunk check       # runs the universal linter on all applicable files
trunk fmt         # runs all the enabled formatters and auto-applies changes
```

You can always find this list using `trunk check --help`.

{% hint style="info" %}
Trunk is git-aware. When you run `trunk check` it will **only run on files you've modified according to git**. To run on a sampling in your repo, run: `trunk check --sample 5`
{% endhint %}

### check

`trunk check` runs linters & formatters on your changed files, prompting you to apply fixes. Without additional args, `trunk check` will run all applicable linters on all files changed in the current branch.

### fmt

Run all applicable formatters as configured in `trunk.yaml`. `trunk fmt` is short-hand for running\
`trunk check` with a `--fix --filter` set to all formatters enabled in your repository.

## Options

<table><thead><tr><th width="238">options</th><th></th></tr></thead><tbody><tr><td><code>--all</code></td><td>Run on all the files in the repository. Useful if trying to assess a new linter in the system, or to find and fix pre-existing issues</td></tr><tr><td><code>--fix</code></td><td>Auto-apply all suggested fixes</td></tr><tr><td><code>--no-fix</code></td><td>Surface, but do not prompt for autofixes</td></tr><tr><td><code>--filter</code></td><td>List of comma-separated linters to run. Specify <code>--filter=-linter</code> to disable a linter.</td></tr><tr><td><code>--sample=N</code></td><td>Run check on a <a href="usage.md#sample">sampling</a> of all files in the repo</td></tr><tr><td><code>--help</code></td><td>Output help information</td></tr></tbody></table>

### Recipes

| Check                                                        | Command                                      |
| ------------------------------------------------------------ | -------------------------------------------- |
| all files                                                    | `trunk check --all --no-fix`                 |
| a specific file                                              | `trunk check some/file.py`                   |
| all applicable files with flake8                             | `trunk check --all --no-fix --filter=flake8` |
| a selection of five files in the repo                        | `trunk check --sample 5`                     |
| a selection of five files in the repo with a specific linter | `trunk check --sample 5 --filter=flake8`     |
| format the whole repo                                        | `trunk fmt --all`                            |
| format a specific file                                       | `trunk fmt some/file.py`                     |
| format all python code with `black`                          | `trunk fmt --all --filter=black`             |

### Manage the linters

List all of the available linters

```sh
trunk check list
```

Enable a single linter

```sh
trunk check enable <linter name>
```

Disable a single linter

```sh
trunk check disable <linter name>
```

## CI Setup

Once you have Trunk Code Quality configured on your local machine, you can set up the Trunk Code Quality webapp to automatically run checks whenever your CI system builds and runs tests. See [Continuous Integration Setup](ci/) for more information.

## Hold the Line

By default Trunk Code Quality will _Hold The Line_, meaning it will only run against new changes in your codebase, not old ones. For more see [Hold the Line](configuration/hold-the-line.md).

## Ignoring Issues by Line

To tell Trunk Code Quality to ignore a line in your source code with a special comment like this:

```cpp
struct FooBar {
  // trunk-ignore(clang-tidy)
  void *ptr = NULL;
};
```

The comment should contain the name of the linter you want to ignore the following line, in this case `clang-tidy` For more complex ignore commands, see [Ignoring Issues](configuration/ignoring-issues.md).

## Ignoring Issues by File

Sometimes you may want to ignore entire files or groups of files, such as generated code. To ignore them, use the `ignore` key to your `.trunk/trunk.yaml` file:

```yaml
lint:
  ignore:
    - linters: [ALL]
      paths:
        # Ignore generated files
        - src/generated/**
```

See [Ignoring Multiple Files](configuration/ignoring-issues.md#ignoring-multiple-files) more information.

## Upgrading

`trunk upgrade` will upgrade the Trunk CLI, along with all plugins and linters in your `trunk.yaml`. We highly recommend running on the latest validated versions of tools as updates will frequently include important security fixes and additional valuable checks. Trunk only auto-suggests linter upgrades to versions that we have tested and support, so you may see a slight lag time when a new linter version is released.

```sh
trunk upgrade
```

`trunk upgrade` will also recommend new tools that have become applicable since the last time your repository was scanned. This can be a result of using new technologies in your repository or trunk itself adding support for more tools. If you don't like a particular recommendation you can run `trunk check disable <linter>` to teach trunk not to recommend it.

