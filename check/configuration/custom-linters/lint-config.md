---
description: Lint Config YAML property reference guide
---

# Lint Config Fields

### Lint Config

The `lint` section of `.trunk/trunk.yaml` represents the configuration of all linters. This is where you can:

* Define the linters (`lint.definitions`),
* List linters to enable and disable (`lint.enabled` and `lint.disabled`)
* Define file categories (`lint.files`)
* List required `runtimes` and `downloads`.
* And additional cross-linter settings.

### `bazel`

`bazel`: bazel configuration

* `paths` locations to look for Bazel binary. [Example](../configuring-existing-linters/#using-bazel)

### `comment_formats`

`comment_formats`: Definitions of comment formats. Reused in linter definitions. Trunk Check already defines many common comment format such as `hash` (`# comment`), `slashes-block` (`/* comment */`), and `slashes-inline` (`// comment`). For the full list [see the linters plugin.yaml](https://github.com/trunk-io/plugins/blob/main/linters/plugin.yaml).

To create a new comment format provide the name and delimiters like this:

```yaml
lint:
  comment_formats:
    - name: dashes-block
      leading_delimiter: --[[
      trailing_delimiter: --]
```

### `compile_commands`

`compile_commands`: compile commands for clang-tidy. Must be one of `json` or `bazel`.

### `compile_commands_roots`

`compile_commands_roots`: Directories to search for `compile_commands.json`. The default is `build/`.

### `default_max_file_size`

`default_max_file_size`: Default maximum filesize in bytes. Trunk Check will not run linters on any files larger than this. Default value is 4 megabytes.

### `definitions`

`definitions`: Where you define or override linter settings. See [Linter Definition Config](linter-definition.md).

### `disabled`

`disabled`: The list of linters to disable. Adding a linter here will prevent trunk from suggesting it as a new linter each time you upgrade. Linter names can be in the form of `<name>` or `<name>@<version>`, the same format as the [enabled](lint-config.md#enabled) property.

### `downloads`

`downloads`: Locations to download binary artifacts from. Using [tool definitions](../../advanced-setup/tools/) instead is preferred.

### `enabled`

`enabled`: The list of linters to enable. Linter names can be in the form of `<name>` or `<name>@<version>`. Examples:

```yaml
lint:
  enabled:
    markdownlint
    markdown-link-checker@1.3.0
```

### `exported_configs`

`exported_configs`: Linter configs to export when another project is [importing this plugin](../sharing-linters.md)

### `extra_compilation_flags`

`extra_compilation_flags`: When running clang-tidy, this list will be appended to the compile command.

### `files`

`files`: Definitions of filetypes

Every linter must define the set of filetypes it applies to in the `lint.files` section.

New filetypes are defined with the name and extensions properties. They may also include the comments properties to describe what style of comments are used in these files.&#x20;

This is how the C++ source filetype is defined. See also [Files and Caching](files.md#applicable-filetypes).

```yaml
lint:
  files:
    - name: c++-source
      extensions:
        - C
        - cc
        - cpp
        - cxx
      comments:
        - slashes-block
        - slashes-inline
```

### `ignore`

`ignore`: files to be [ignored by linters](../ignoring-issues.md#ignoring-multiple-files).

### `reuse_upstream`

`reuse_upstream`:  If enabled, Trunk will cache upstream sandboxes instead of creating a new one each time. Options are `true`, or `false`.

### `runtimes`

`runtimes`: Node, python, cargo, etc. Used to define or override a runtime environment for package management. [See Runtimes](../../advanced-setup/runtimes.md).

### `threshold`

`threshold`: where you specify the blocking behavior of linters. The [threshold](../README.md#blocking-thresholds) for whether an error from a linter should block commits or not.

### `upstream_mode`

`upstream_mode`: How to generate the upstream sandbox used for generating lint results for revisions not currently checked out. Options are`symlink` (default), `hardlink`, or `copy`. If using `copy`, it can be slow without also enabling `reuse_upstream: true`.
