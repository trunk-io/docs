# Debugging

## Why Aren't Issues Showing up Anymore?

If you aren’t seeing any issues the likely cause is that your local repo is clean. By default Trunk Code Quality only processes new changes to your codebase (read about [hold-the-line](overview/how-does-it-work.md#hold-the-line)).

You can use `trunk check` to scan for older, pre-existing lint issues.

For example, to look at a sampling of each linter's issues for 5 random files:

```sh
trunk check --samples=5 
```

You can also scan all files using `--all`:

```sh
trunk check --all
```

[Read our docs for more information on CLI options](setup-and-installation/deal-with-existing-issues.md#fixing-existing-issues).

## My Linters Are Failing or Not Running as Expected

When your linters aren’t working the way you expect, first check their configuration. Trunk’s [list of supported linters](linters/supported/) provides some specific tips for certain linters. You can see the full default configuration of every linter in [Trunk’s public plugin repo](https://github.com/trunk-io/plugins/tree/main).

You can also try running `trunk check --verbose` to see what’s going on under the hood. If that still doesn’t work then please reach out to us on [our community Slack](https://trunkcommunity.slack.com/ssb/redirect) with the output of `trunk check --verbose`.

## Why Does Trunk Take up So Much Disk Space?

Trunk Code Quality uses hermetically versioned tools, which means it downloads a separate copy of the tools and runtime for each tool version. Over time, as tools are upgraded, this can leave a lot of unnecessary files in the cache directory. Trunk is working on a way to automatically remove unneeded files from the cache. In the meantime, you can safely clear your cache with

```
trunk cache clean --all
```

then run `trunk install` again in your repos.

## How do I Make a Linter Work with a Different File Type?

Every linter defines a set of file types that it wants to work with in a section of the YAML called `files`. To change this you need to override the files section of that linter’s definition. [More linter application file types](../cli/configuration/lint/files-and-caching.md#applicable-filetypes).

Suppose you are using the **foo-linter** which normally runs on `foo` files. The config might look like this:

```yaml
lint:
  files:
    - name: foo
      extensions: [foo]
  definitions:
    - name: foo-linter
      files: [foo]
      commands:
        - name: lint
          output: pass_fail
          run: echo “foo”
          success_codes: [0, 1]
```

To add support for `bar` files add this to your `trunk.yaml` file. The first part defines the `bar` file type, and the second says that `foo-linter` uses both `foo` and `bar` files.

```yaml
lint:
  files:
    - name: bar
      extensions: [bar]
...
      
  definitions:
    - name: foo-linter
        files:
          - foo
          - bar
```

## How can I Disable Trunk on a Commit for just Me, but Keep it on for the Rest of my Team?

If you prefer to never run Trunk on commit and push you can disable it just for you. Edit or create the `.trunk/user.yaml` file and change the `actions.disabled` section to look like this:

```yaml
version: 0.1
actions:
  disabled:
    - trunk-check-pre-push
    - trunk-fmt-pre-commit
  
```

This will disable the checks for just the current user. The `.trunk/user.yaml` file is specifically gitignored but will be loaded locally if present.

## What Should I do if a Linter Process Seems to Take Longer than Expected During a Trunk Check?

There are two main strategies to address this issue: **configuring timeouts** and **ignoring certain files**.

**Timeout Configuration**

Each linter integrated with Trunk Code Quality has a default timeout of 10 minutes to prevent processes from running indefinitely. If a linter exceeds this time frame, Trunk Code Quality will automatically terminate the process and notify you of the timeout.

To adjust the timeout duration for a specific linter, you can modify its `run_timeout` setting in your configuration. For example:

```
lint:
    definitions:
    - name: clang-tidy
      run_timeout: 5m
```

Timeouts can be specified using `s` for seconds, `m` for minutes, or `h` for hours, allowing you to tailor the behavior to your project's needs. More on [linter timeouts](linters/configure-linters.md#timeout).

**Ignoring Files**

Certain files, particularly those that are auto-generated, may not require linting and can significantly extend the duration of checks. To exclude these from being checked, use the `ignore` key in your configuration:

```
lint:
  ignore:
    - linters: [ALL]
      paths:
        # Ignore generated files
        - src/generated/**
        # Except for files ending in .foo
        - !src/generated/**/*.foo # Test data
        - test/test_data
```

This approach lets you specify which linters to ignore for particular paths, optimizing the check process and focusing on relevant files. [More details on ignoring files](linters/).

## `trunk init` says "Trunk can only init if it's run at the root of a git repo"

Trunk requires that you run `trunk init` from the root of a git repository. Trunk is git-aware, and relies on git to understand which files are modified, gitignored, and more.

If you see this message, it means that you are not in the root directory of a git repository. If you are in a git worktree, Trunk _does_ support worktrees. Your worktree may be in a broken state, try running `git worktree repair` and then `trunk init` again.
