# Configure Linters

Trunk Code Quality's linter integrations are fully configurable. This means that you can easily tune existing linters or leverage our caching and [hold-the-line](../overview/how-does-it-work.md#hold-the-line) solution with your own custom linters.

Here's an overview of the ways you can configure linters.

### Config Hierarchy

Linters can be configured at different places:

1. The source plugin repo usually `https://github.com/trunk-io/plugins`.
2. The repo-wide Trunk config file overrides the definitions in the plugin repos, `.trunk/trunk.yaml`
3. Local, per-user configuration in `.trunk/user.yaml` which is used for local overrides of `.trunk/trunk.yaml` and doesn't
4. Per linter configuration in linter config files such as `eslint.config.js` or `.prettierrc`.

### Plugin system <a href="#lint-config-definitions" id="lint-config-definitions"></a>

Trunk defines linter configuration in a plugin system. By default, it'll point to the [Trunk plugin repo on GitHub](https://github.com/trunk-io/plugins). You can check if other custom plugin sources are specified in your `trunk.yaml` file for [shared-configs.md](shared-configs.md "mention").

```yaml
version: 0.1
cli:
  version: 1.22.2
# Trunk provides extensibility via plugins. (https://docs.trunk.io/cli/configuration/plugins)
plugins:
  sources:
    - id: trunk
      ref: v1.6.1
      uri: https://github.com/trunk-io/plugins
```

### Linter Definitions <a href="#lint-config-definitions" id="lint-config-definitions"></a>

Each linter implemented in the Plugin Repo has its own linter definition. Let's take clang-tidy as an example, which ships with the following default configuration:

```yaml
definitions:
  ...
  - name: clang-tidy
    files: [c/c++-source]
    type: llvm
    commands:
      - output: llvm
        run: clang-tidy --export-fixes=- ${target}
        success_codes: [0]
    download: clang-tidy
    direct_configs: [.clang-tidy]
    disable_upstream: true
    include_scanner_type: compile_command
    environment:
      - name: PATH
        list: ["${linter}/bin"]
  ...
```

#### Linter Definition Reference

You can find the default definitions for linters in the [Plugin Repo](https://github.com/trunk-io/plugins/tree/main/linters) and find references for these fields on the [Linter Definitions](../../references/cli/configuration/lint/definitions.md) page.

### Overriding Default Linter Definitions

You may find while using Trunk that you want to modify one of these defaults: perhaps you want `clang-tidy` to not run on the upstream, or maybe you want the `node` runtime to include another environment variable. In these cases, you can specify the field in your `trunk.yaml` to override the default value.

If you wanted to flip the value of `disable_upstream` to `false`, you could, in your own `trunk.yaml`, specify:

<pre class="language-yaml"><code class="lang-yaml"><strong>definitions:
</strong>  ...
  - name: clang-tidy
    disable_upstream: false
  ...
</code></pre>

{% hint style="info" %}
Overriding definitions in your `trunk.yaml` file doesn't require you to specify the entire definition again. You only need to specify what's being overridden.
{% endhint %}

#### Configure Linter Commands

Some linters have multiple commands, such as [Ruff](supported/ruff.md), which can run in different ways. By default, Ruff is configured to only run as a linter:

```yaml
lint:
  enabled:
    - ruff@<version>:
        commands: [lint]
```

You can configure ruff to also run the format command by adding it to the commands tuple:

```yaml
lint:
  enabled:
    - ruff@<version>:
        commands: [lint, format]
```

#### Configure Linter Platforms

Similarly, some linters are configured to run differently on different platforms or at different versions. When overriding a command definition, overrides are applied on the tuple `[name, version, platforms]`.

For example, if you wanted to disable batching when running [ktlint](https://github.com/trunk-io/plugins/blob/main/linters/ktlint/plugin.yaml) on Windows, you could consider its default configuration:

```yaml
definitions:
  ...
  - name: ktlint
    ...
    commands:
      - name: format
        platforms: [windows]
        run: java -jar ${linter}/ktlint.exe -F "${target}"
        output: rewrite
        cache_results: true
        formatter: true
        in_place: true
        batch: true
        success_codes: [0, 1]
      - name: format
        run: ktlint -F "${target}"
        output: rewrite
        cache_results: true
        formatter: true
        in_place: true
        batch: true
        success_codes: [0, 1]
  ...
```

And override it as such:

```yaml
definitions:
  ...
  - name: ktlint
    ...
    commands:
      - name: format
        platforms: [windows]
        batch: false
  ...
```

When executing linters, Trunk will execute the first matching command based on its compatible platforms and linter version. Note when overriding that new commands that don't match an existing tuple are prepended to the resulting commands list.

Alternatively, consider the default `node` runtime:

```yaml
runtimes:
  definitions:
    - type: node
      download: node
      runtime_environment:
        - name: HOME
          value: ${home}
        - name: PATH
          list: ["${runtime}/bin"]
      linter_environment:
        - name: PATH
          list: ["${linter}/node_modules/.bin"]
      version: 16.14.2
      version_commands:
        - run: "node --version"
          parse_regex: ${semver}
```

If you want to add `${home}/my/special/node/path` to `PATH`, you could specify the following:

```yaml
runtimes:
  - type: node
    runtime_environment:
      - name: HOME
        value: ${home}
      - name: PATH
        list: ["${home}/my/special/node/path", "${runtime}/bin"]
```

### Blocking Thresholds

All issue severities low-high are considered blocking by default. In cases where you might want to slowly try out a new linter, we provide a mechanism to set specific thresholds for each linter.

```yaml
lint:
  threshold:
    - linters: [clang-tidy]
      level: high
```

Every entry in `threshold` defines a set of linters and the severity threshold that is considered blocking. In this example, we're saying that only `high` lint issues should be considered blocking for `clang-tidy`.

<table><thead><tr><th width="97">Key</th><th>Value</th></tr></thead><tbody><tr><td>linters</td><td>List of linters (e.g. <code>[black, eslint]</code>) or the special <code>[ALL]</code> tag</td></tr><tr><td>level</td><td>Default <code>low</code>. Threshold at which issues are considered blocking. One of: <code>note</code>, <code>low</code>, <code>medium</code>, <code>high</code>, or <code>none</code> (this last option will result in issues never blocking)</td></tr></tbody></table>

### Trigger rules

Some linters do not operate on individual files. Instead, you must lint your entire repo at once. The way this is handled in Trunk is to set up a trigger rule. Most linters will not require the use of a trigger rule.

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

Each linter has a default timeout of 10 minutes. If its execution takes longer than this amount of time, Trunk Code Quality will terminate the process and return an error to the user.

To override the timeout for a specific linter, specify a `run_timeout` in its definition:

```
lint:
    definitions:
    - name: clang-tidy
      run_timeout: 5m
```

The `run_timeout` value can be specified in seconds (`s`), minutes (`m`), or hours (`h`).

### Local Linter Overrides

Trunk can also be managed by the `.trunk/user.yaml` file in your repository. This file is optional, but it allows individual developers to customize how they want `trunk` to run on their machines.

Simply configure `.trunk/user.yaml` as you would for `.trunk/trunk.yaml`. Be mindful that `.trunk/user.yaml` takes precedence over `.trunk/trunk.yaml`, so substantial modifications could violate hermeticity.

### Per Linter Definitions

Trunk allows you to keep using your existing linter configs, and new linters recommended by Trunk will have their configs added in the `.trunk/configs` folder. These config files will be symlinked in during any `trunk check` run.

{% hint style="info" %}
If you're using an IDE Extension like clangd with an LSP that relies on those configs being in the root, you will need to create an additional symlink from the hidden config to the workspace root.
{% endhint %}

#### Moving Linters

You can move existing linter config files into the `.trunk/config` folder. You can check which files are automatically symlinked by looking for the `direct_configs` of [each plugin's definition](https://github.com/trunk-io/plugins/). If there are config files not listed, you can add them by overriding the definition like this:

```yaml
lint:
  definitions:
    - name: some_linter_name
      direct_configs:
        - .custom_config.file
```
