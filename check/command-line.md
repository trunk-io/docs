# Command Line

The following commands are available when using `trunk` from the command line

```bash
$ trunk check       # runs the universal linter on all applicable files
$ trunk fmt         # runs all the enabled formatters and auto-applies changes
```

You can always find this list using `trunk check --help`.

### check

`trunk check` runs linters & formatters on your changed files, prompting you to apply fixes. Without additional args, `trunk check` will run all applicable linters on all files changed in the current branch.

### fmt

Run all applicable formatters as configured in `trunk.yaml`. `trunk fmt` is short-hand for running\
`trunk check` with a `--fix --filter` set to all formatters enabled in your repository.

| options              |                                                                                                                                       |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| `--all`              | Run on all the files in the repository. Useful if trying to assess a new linter in the system, or to find and fix pre-existing issues |
| `--fix`              | Auto-apply all suggested fixes                                                                                                        |
| `--no-fix`           | Surface, but do not prompt for autofixes                                                                                              |
| `--filter`           | List of comma-separated linters to run. Specify `--filter=-linter` to disable a linter.                                               |
| `--sample=N`         | Run check on a [sampling](../check/command-line.md#sample) of all files in the repo                                                   |
| `--ci`               | Run in Continuous Integration mode                                                                                                    |
| `--no-progress`      | Do not show progress while running                                                                                                    |
| `--ci-progress`      | Only show progress every 30s while running (useful for CI jobs). Implied by `--ci`.                                                   |
| `--output`           | Output results in specified format: text (default) or json                                                                            |
| `--output-file=FILE` | Write json results to specified file                                                                                                  |
| `--show-fixed`       | Include fixed issues in the output                                                                                                    |
| `--help`             | Output help information                                                                                                               |

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

### Discover new tools and available upgrades

`trunk upgrade` will upgrade the Trunk CLI, along with all plugins and linters in your trunk.yaml. We highly recommend running on the latest validated versions of tools as updates will frequently include important security fixes and additional valuable checks. Trunk only auto-suggests linter upgrades to versions that we support, so you may see a slight lag time when a new linter version is released.

Upgrade will also recommend new tools that have become applicable since the last time your repository was scanned. This can be a result of using new technologies in your repository or trunk itself increasing support for more tools. If you don't like a particular recommendation you can run `trunk check disable {tool-name}` to teach trunk not to recommend it.

#### Pinned System Versions

When you enable a packaged or downloaded linter in your `trunk.yaml` and don't specify a version, trunk will attempt to use the version of that tool installed on your system. Trunk will not automatically suggest upgrades for this tool. If you wish to upgrade to the latest version, you will first have to specify a base version in your `trunk.yaml`.

### Advanced Features

| Options & Flags | Explanation                                                                                                                                                              |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| --root          | Explicitly set the root of the repository to run against                                                                                                                 |
| --upstream      | Specify the upstream branch used to calculate new vs existing issued.                                                                                                    |
| --trigger       | Supports running trunk check from inside a git hook. Options are manual (default), git-push, git-commit. Controls whether the check returns early and its interactivity. |
