# Code Quality

### trunk check

`trunk check`: Universal code checker.

#### **Usage** **example**

```
trunk check [options]
```

#### Filtering Options

* `-a, --all`: Check all files instead of only changed files
* `--sample`: Run each linter on N files
* `--filter`: Comma-separated list of linters and/or issue codes to include or exclude
* `--exclude`: Shorthand for an inverse --filter
* `--scope`: Scope of checks to run {all | security}
* `--ignore`: Glob pattern to exclude files from linting
* `--force`: Run on all files, even if ignored
* `--include-existing-autofixes`: Include existing issues that can be autofixed

#### **CI** Options

* `--replace`: Overwrite previously uploaded check run if one exists
* `--series`: Series name for this upload (usually the branch)
* `--upload`: Upload lint results to the trunk web app
* `--ci`: Run in non-interactive mode designed for CI environments
* `-j`, `--jobs`: Number of concurrent jobs

#### Git Hooks Options

* `--index`: Run linter on git-indexed files
* `--index-file`: Run linter on git-indexed files based on specified index
* `--commit-ref`: Commit ref to lint (instead of current working tree)
* `--commit-ref-from-pre-push`: Commit ref to lint from the stdin of a pre-push git hook (instead of the current working tree)

#### Output Options

* `--show-existing`: Show existing issues otherwise hidden by
* `--print-failures`: Print any failures that occur
* `--diff`: Diff printing mode {none | compact | full}
* `-v, --verbose`: Show verbose output for debugging purposes
* `--debug`: Show debug output

#### Behavior Options

* `-y, --fix`: Automatically apply all fixes without prompting
* `-n, --no-fix`: Don't automatically apply fixes
* `--cache`: Disable to skip cache for all check actions
* `--ignore-git-state`: Run linters even if a merge, rebase, or revert is in progress
* `--upstream`: Upstream branch used to compute changed files

### Trunk Check Enable Linter

`trunk check enable`: Enable linters for trunk check.

#### **Usage** **example**

```
trunk check enable [options]
```

### Trunk Check Disable Linter

`trunk check disable`: Disable linters for trunk check.

#### **Usage** **example**

```
trunk check disable [options]
```

### Trunk Check List Linters

`trunk check list`: List linters for trunk check.

#### **Usage** **example**

```
trunk check list [options]
```

### Trunk Check Run Format

`trunk fmt`: List linters for trunk check.

#### **Usage** **example**

```
trunk fmt [options]
```

#### **Options**

#### Filtering Options

* `-a, --all`: Check all files instead of only changed files
* `--filter`: Comma-separated list of linters and/or issue codes to include or exclude
* `--exclude`: Shorthand for an inverse --filter
* `--scope`: Scope of checks to run {all | security}
* `--ignore`: Glob pattern to exclude files from linting
* `--force`: Run on all files, even if ignored
* `--show-existing`: Show existing issues otherwise hidden by [hold-the-line](../../../code-quality/overview/how-does-it-work.md#hold-the-line)
* `--ignore-git-state`: Run linters even if a merge, rebase, or revert is in progress

#### Git Hooks Options

* `--index`: Run linter on git-indexed files
* `--index-file`: Run linter on git-indexed files based on specified index
* `--commit-ref`: Commit ref to lint (instead of current working tree)
* `--commit-ref-from-pre-push`: Commit ref to lint from the stdin of a pre-push git hook (instead of the current working tree)

#### Output Options

* `--show-existing`: Show existing issues otherwise hidden by
* `--print-failures`: Print any failures that occur
* `--diff`: Diff printing mode {none | compact | full}
* `-v, --verbose`: Show verbose output for debugging purposes
* `--debug`: Show debug output

#### Behavior Options

* `-y, --fix`: Automatically apply all fixes without prompting
* `-n, --no-fix`: Don't automatically apply fixes
* `--cache`: Disable to skip cache for all check actions
* `--ignore-git-state`: Run linters even if a merge, rebase, or revert is in progress
* `--upstream`: Upstream branch used to compute changed files
* `-j`, `--jobs`: Number of concurrent jobs

## Advanced Trunk Check Features

| Options & Flags      | Explanation                                                                                                                                                              |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `--root`             | Explicitly set the root of the repository to run against                                                                                                                 |
| `--upstream`         | Specify the upstream branch used to calculate new vs existing issued.                                                                                                    |
| `--trigger`          | Supports running trunk check from inside a git hook. Options are manual (default), git-push, git-commit. Controls whether the check returns early and its interactivity. |
| `--output=format`    | Output results in specified format: `text` (default) or `json`                                                                                                           |
| `--output-file=FILE` | Write json results to specified file                                                                                                                                     |

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
