# Usage

### Basic Usage

The main Trunk Check commands when running `trunk` from the command line are:

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

<table><thead><tr><th width="238">options</th><th></th></tr></thead><tbody><tr><td><code>--all</code></td><td>Run on all the files in the repository. Useful if trying to assess a new linter in the system, or to find and fix pre-existing issues</td></tr><tr><td><code>--fix</code></td><td>Auto-apply all suggested fixes</td></tr><tr><td><code>--no-fix</code></td><td>Surface, but do not prompt for autofixes</td></tr><tr><td><code>--filter</code></td><td>List of comma-separated linters to run. Specify <code>--filter=-linter</code> to disable a linter.</td></tr><tr><td><code>--sample=N</code></td><td>Run check on a <a href="./#sample">sampling</a> of all files in the repo</td></tr><tr><td><code>--ci</code></td><td>Run in <a href="../check-cloud-ci-integration/continuous-integration/">Continuous Integration mode</a></td></tr><tr><td><code>--no-progress</code></td><td>Do not show progress while running</td></tr><tr><td><code>--ci-progress</code></td><td>Only show progress every 30s while running (useful for CI jobs). Implied by <code>--ci</code>.</td></tr><tr><td><code>--jobs</code></td><td>number of concurrent jobs (does not affect background linting)</td></tr><tr><td><code>--help</code></td><td>Output help information</td></tr></tbody></table>

### Recipes

| Check                                        | Command                                    |
| -------------------------------------------- | ------------------------------------------ |
| all files                                    | trunk check --all --no-fix                 |
| a specific file                              | trunk check some/file.py                   |
| all applicable files with flake8             | trunk check --all --no-fix --filter=flake8 |
| the behavior of all linters                  | trunk check --sample 5                     |
| the behavior of a specific linter            | trunk check --sample 5 --filter=flake8     |
| the formatting of the whole repo             | trunk fmt --all                            |
| the formatting of a specific file            | trunk fmt some/file.py                     |
| the formatting of all python code with black | trunk fmt --all --filter=black             |

### Options

#### --filter

`--filter` argument allows you to restrict `trunk check` to a subset of the linters enabled in your repository.

For example, to run `eslint` and `isort` on the entire repo:

```bash
trunk check --all --filter=eslint,isort
```

Alternatively, to run every linter _except_ `clang-tidy` and `shellcheck`:

```bash
trunk check --all --filter=-clang-tidy,-shellcheck
```

#### --sample

`--sample=N` will attempt to run every enabled linter against the requested number of files. The goal of the `sample` flag is to test the setup of the linters in your repository as well as any specific configuration they might honor.

The sample command will attempt to run each linter N times, but may run fewer if not enough applicable files exist in your set of files to lint. `--sample=N` can be combined with any other set of options for `trunk check`.

For example, to run `prettier` against 10 different prettier supported files:

```bash
trunk check --sample=10 --filter=prettier
```

Alternatively, to run every linter at most 5 times against its supported files:

```bash
trunk check --sample=5
```

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

### Discover new tools and available upgrades

```sh
trunk upgrade
```

`trunk upgrade` will upgrade the Trunk CLI, along with all plugins and linters in your trunk.yaml. We highly recommend running on the latest validated versions of tools as updates will frequently include important security fixes and additional valuable checks. Trunk only auto-suggests linter upgrades to versions that we have tested and support, so you may see a slight lag time when a new linter version is released.

Upgrade will also recommend new tools that have become applicable since the last time your repository was scanned. This can be a result of using new technologies in your repository or trunk itself adding support for more tools. If you don't like a particular recommendation you can run `trunk check disable <linter>` to teach trunk not to recommend it.

#### Pinned System Versions

When you enable a packaged or downloaded linter in your `trunk.yaml` and don't specify a version, Trunk will attempt to use the version of that tool installed on your system. Trunk will not automatically suggest upgrades for this tool. If you wish to upgrade to the latest version, you will first have to specify a base version in your `trunk.yaml`. See [Configuration](../configuration/) for more information about `trunk.yaml`.

### Advanced Trunk Check Features

| Options & Flags      | Explanation                                                                                                                                                              |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `--root`             | Explicitly set the root of the repository to run against                                                                                                                 |
| `--upstream`         | Specify the upstream branch used to calculate changed files as well as new vs existing issues.                                                                           |
| `--trigger`          | Supports running trunk check from inside a git hook. Options are manual (default), git-push, git-commit. Controls whether the check returns early and its interactivity. |
| `--output=format`    | Output results in specified format: `text` (default) or `json`                                                                                                           |
| `--output-file=FILE` | Write json results to specified file                                                                                                                                     |

