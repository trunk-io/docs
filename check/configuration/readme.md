---
description: Overview of Trunk Check's supported linters and configuration
---

# Linters

Trunk Check supports over [100 different linters](supported-linters.md) and formatters out of the box. The configurations for `trunk check` and `trunk fmt` are governed by the `lint` section of the [`trunk.yaml`](../reference/trunk-yaml/#cli)file stored in the `.trunk` directory of your git repo. Here's an example of what a fully-featured `lint` section looks like:

```yaml
lint:
  # list of linters to run using trunk
  enabled:
    - ansible-lint@5.3.2
    - bandit@1.7.0
    - black@21.6b0
    - buf-lint@1.0.0-rc3
    - buildifier@5.1.0
    - cfnlint@0.51.0
    - eslint@7.30.0
    - gitleaks@7.6.1
    - gofmt@1.16.7
    - golangci-lint@1.41.1
    - hadolint@2.6.0
    - isort@5.8.0
    - markdownlint@0.28.1
    - mypy@0.910
    - prettier@2.3.2
    - pylint@2.8.1
    - rustfmt@1.55.0
    - semgrep@0.104.0
    - shellcheck@0.7.2
    - shfmt@3.3.1
  disabled:
    - rufo
    - tflint
  ignore:
    - linters: [ALL]
      paths:
        # Generated files
        - a/proto/code_pb*
        # Test data
        - b/test_data/**
    - linters: [eslint]
      paths:
        - c/run.ts
  threshold:
    - linters: [clang-tidy]
      level: high
  triggers:
    - linters:
        - ansible-lint
      paths:
        - ansible # A directory
      targets:
        - ansible # A directory
```

### Test your config changes

Normally when you run `trunk check` or `trunk fmt` it runs only on files you've changed. We've made it easy to test how a linter will behave in your repo. As you're tuning your linter configuration simply run check with the `--sample` flag. When sampling, Trunk will find applicable files for the linters you've enabled and show you how the linter will behave against a sampling of inputs.

<table><thead><tr><th width="260">Sample</th><th>Command</th></tr></thead><tbody><tr><td>all linters on 5 files</td><td><code>trunk check --sample 5</code></td></tr><tr><td>a specific linter with 7 files</td><td><code>trunk check --sample=7 --filter=clippy</code></td></tr><tr><td>all linters on a specific file</td><td><code>trunk check foo.file</code></td></tr></tbody></table>

In sampling mode, Trunk may run multiple linters on a single file, and may not run each linter on the full number of requested samples (if not enough applicable files can be found).

### Tuning your linters

Most linters offer some form of configuration. **Trunk uses the native configuration setup of all the tools it runs**. No need to learn a new config language or hunt for specific ways to tune a linter inside trunk. Whether it's `clang-tidy`, `eslint`, or any other linter, all the documentation you'll find online about it is still applicable. We're proud to stand on the shoulders of giants and believe that the open source communities building these tools know best how they should work. Our goal is simply to make it as easy as possible for you to adopt these tools.

To configure **what** a linter does, you will continue to use the linter's own config files. Check out our [configs](https://github.com/trunk-io/configs) repository for always-up-to-date linter configs and some tips on how to structure your linters and repo. Check out our [docs](configuring-existing-linters/) on linter-specific tips. To configure **how** Trunk runs a linter, read on.

#### Moving linter configs

If you'd like, Trunk also supports migrating any linter configurations from the root of your repository into a `.trunk/configs` folder. These config files will be symlinked in during any `trunk check` run. Note that if you're using an IDE Extension like clangd with an LSP that relies on those configs being in the root, you will need to create an additional symlink from the hidden config to the workspace root.

If you find that you want to tweak how Trunk runs a given linter, you may want to consult the documentation on [overriding defaults](../reference/trunk-yaml/#overriding-defaults) and [the various linter settings](custom-linters/); for example, hold-the-line is enabled by default for most linters, but can be disabled like so:

```yaml
lint:
  definitions:
    - name: pylint
      hold_the_line: false
      disable_upstream: true
```

Disabling [hold-the-line](../reference/under-the-hood.md#hold-the-line) for a linter will require that all issues found by said linter be fixed before changes to that file can be landed.

Disabling the upstream for a linter will elide the execution of the linter on the upstream.

### Enable Linters

Trunk only runs linters listed in the `enabled` section; linters which are defined in `lint.definitions` but are not listed in `enabled` are not run.

When enabling a linter, you must specify a version for the linter:

```yaml
lint:
  enabled:
    # enabling a version with a linter
    - gitleaks@7.6.1
    - gofmt@1.16.7
    - golangci-lint@1.41.1
    - hadolint@2.6.0
```

Custom linters are slightly different; see [those docs](custom-linters/) to learn more.

{% hint style="info" %}
You can also ask Trunk to detect new linters and upgrade existing linters to their latest respective versions by running [`trunk upgrade check`](../advanced-setup/cli/upgrade.md).
{% endhint %}

### Disable Linters

Trunk will continuously monitor your repository and make recommendations of additional new tools to run on your codebase. You can tell trunk not to recommend a specific linter by adding it to the disabled list.

```yaml
lint:
  disabled:
    # disabled a linter tells trunk not to recommend it during upgrade scans
    - rufo
    - tflint
```

### Installing additional packages

We support installing additional packages along with your linter. For example, Pylint supports adding plugins which are installable as pip packages. For example, if you want to run the plugin `pylint-django` as part of your setup, you need to tell Trunk to install the package:

```yaml
lint:
  enabled:
    - pylint@2.11.0:
        packages:
          - pylint-django@2.4.4
        ...
```

#### Runtime versioning

By default Trunk will install hermetic versions of runtimes required by the linters you have chosen. If you need to peg to a specific runtime version or you want to use the version installed on your system, consult the [runtimes documentation](../reference/trunk-yaml/#runtimes).

### Ignoring Issues and Files

By default Check will ignore issues in files which are listed in the `.gitignore` file.&#x20;

If you want to ignore groups of files, such as generated code, you can do that with the [`lint.ignore`](./#ignoring-files) section of your `.trunk/trunk.yaml` file. ex:

```yaml
lint:
  ignore:
    - linters: [ALL]
      paths:
        # Ignore generated files
        - src/generated/**
```

You can also ignore particular issues _within a file_ using special comments like this:

```cpp
struct FooBar {
  // trunk-ignore(clang-tidy/modernize-use-nullptr): load-bearing NULL, see ISSUE-832
  void *ptr = NULL;
};
```

This tells Trunk that the `clang-tidy` linter found a `modernize-use-nullptr` issue on the highlighted line and that Trunk should suppress this linter issue.

For full details please see the [Ignoring Issues and Files](ignoring-issues.md) page.

### Blocking Thresholds

All [issue severities](../#issue-severity) are considered blocking by default. In cases where you might want to slowly try out a new linter, we provide a mechanism to set specific thresholds for each linter.

```yaml
lint:
  threshold:
    - linters: [clang-tidy]
      level: high
```

Every entry in `threshold` defines a set of linters and the severity threshold that is considered blocking. In this example, we're saying that only `high` lint issues should be considered blocking for `clang-tidy`.

<table><thead><tr><th width="97">Key</th><th>Value</th></tr></thead><tbody><tr><td>linters</td><td>List of linters (e.g. <code>[black, eslint]</code>) or the special <code>[ALL]</code> tag</td></tr><tr><td>level</td><td>Threshold at which issues are considered blocking. One of : <code>low</code>, <code>medium</code>, <code>high</code>, or <code>none</code> (this last option will result in issues never blocking)</td></tr></tbody></table>

### Trigger rules

Some linters do not operate on individual files. Instead you must lint your entire repo at once. The way this is handled in trunk is to set up a trigger rule. Most linters will not require the use of a trigger rule.

Trigger rules work on 3 principles:

1. Input(s) that trigger the linters. These can be files, directories, or extended globs.
2. Linter(s) to run when a triggered file is modified.
3. Targets(s) to pass to the linters (can be files or directories).

An example for ansible-lint:

```yaml
lint:
  enabled:
    - ansible-lint@5.3.2

  triggers:
    - linters:
        - ansible-lint
      paths:
        - ansible # A directory
      targets:
        - ansible # A directory
```

Triggered linters will also be run when executing trunk check with `--all` so long as a file exists that matches one of the listed paths.

You may use `.` as a target to run on the entire repo instead of an isolated directory.

### File Size

By default, Trunk only lints files up to 4 MiB in size. To override this globally, specify a `default_max_file_size` in `lint`:

```yaml
lint:
  default_max_file_size: 1048576 # Bytes
```

To override this for a specific linter, specify a `max_file_size` in its definition:

```yaml
lint:
  definitions:
    - name: prettier
      max_file_size: 2097152 # Bytes
```



### Timeout

Each linter has a default timeout of 10 minutes. If its execution takes longer than this amount of time, Trunk Check will terminate the process and return an error to the user.

To override the timeout for a specific linter, specify a `run_timeout` in its definition:

```
lint:
    definitions:
    - name: clang-tidy
      run_timeout: 5m
```

The `run_timeout` value can be specified in seconds (`s`), minutes (`m`), or hours (`h`).



##
