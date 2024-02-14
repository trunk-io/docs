---
description: Trunk Check detailed command line options
---

# CLI options

## Options

<table><thead><tr><th width="238">options</th><th></th></tr></thead><tbody><tr><td><code>--all</code></td><td>Run on all the files in the repository. Useful if trying to assess a new linter in the system, or to find and fix pre-existing issues</td></tr><tr><td><code>--fix</code></td><td>Auto-apply all suggested fixes</td></tr><tr><td><code>--no-fix</code></td><td>Surface, but do not prompt for autofixes</td></tr><tr><td><code>--filter</code></td><td>List of comma-separated linters to run. Specify <code>--filter=-linter</code> to disable a linter.</td></tr><tr><td><code>--sample=N</code></td><td>Run check on a <a href="cli-options.md#sample">sampling</a> of all files in the repo</td></tr><tr><td><code>--ci</code></td><td>Run in <a href="../../check-cloud-ci-integration/continuous-integration/">Continuous Integration mode</a></td></tr><tr><td><code>--no-progress</code></td><td>Do not show progress while running</td></tr><tr><td><code>--ci-progress</code></td><td>Only show progress every 30s while running (useful for CI jobs). Implied by <code>--ci</code>.</td></tr><tr><td><code>--jobs</code></td><td>number of concurrent jobs (does not affect background linting)</td></tr><tr><td><code>--help</code></td><td>Output help information</td></tr></tbody></table>

## Advanced Trunk Check Features

| Options & Flags      | Explanation                                                                                                                                                              |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `--root`             | Explicitly set the root of the repository to run against                                                                                                                 |
| `--upstream`         | Specify the upstream branch used to calculate new vs existing issued.                                                                                                    |
| `--trigger`          | Supports running trunk check from inside a git hook. Options are manual (default), git-push, git-commit. Controls whether the check returns early and its interactivity. |
| `--output=format`    | Output results in specified format: `text` (default) or `json`                                                                                                           |
| `--output-file=FILE` | Write json results to specified file                                                                                                                                     |

## Details

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
