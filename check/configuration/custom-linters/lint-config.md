## Lint Config

The `lint` section represents the configuration of all linters. This is where you can:

* define the linters (`linters`),
* list linters to enable and disable (`enabled` and `disabled`)
* define file categories (`files`)
* list required `runtimes`, `downloads`, `environments` ,
* and additional cross-linter settings

### `files`

`files`: Definitions of filetypes

Every linter must define the set of filetypes it applies to in the `lint.files` section.

New filetypes are defined with the name and extensions properties.
They may also include the comments properties to describe what style of
comments are used in these files.

This is how the C++ source filetype is defined.

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

### `runtimes`

`runtimes`: Node, python, cargo, etc. Used to define or override a runtime environment for package management. [See Runtimes](../../advanced-setup/runtimes.md)

[//]: # (`linters`: maps a linter name to it's corresponding linter definition)

### `definitions`

`definitions`: Where you define or override linter settings. See [Linter Definition Config](#lint-config-definitions)

### `enabled`

`enabled`: The list of linters to enable. Linter names can be in the form of `<name>` or `<name>@<version>`.
Examples:

```yaml
lint:
  enabled:
    markdownlint
    markdown-link-checker@1.3.0
```

### `disabled`

`disabled`: The list of linters to disable. Adding a linter here will prevent trunk from suggesting
it as a new linter each time you upgrade. Linter names can be in the form of `<name>` or `<name>@<version>`,
the same format as [enabled](#enabled)

### `ignore`

`ignore`: files to be [ignored by linters](../ignoring-issues.md#ignoring-multiple-files)

### `threshold`

`threshold`: where you specify the blocking behavior of linters. The [threshold](../#blocking-thresholds) for whether an error from a linter should block commits or not.


### `compile_commands`

`compile_commands`: compile commands for clang-tidy. Must be one of `compile_commands_json` or `bazel`

### `bazel`

`bazel`: bazel configuration

* `paths` locations to look for Bazel binary. [Example](../configuring-existing-linters/README.md#using-bazel)

### `downloads`

`downloads`: Locations to download binary artifacts from. Using [tool definitions](../../advanced-setup/tools/README.md) instead is preferred.

### `comment_formats`

`comment_formats`: Definitions of comment formats. Reused in linter definitions. Trunk Check
already defines many common comment format such as `hash` (`# comment`), `slashes-block`
(`/* comment */`), and `slashes-inline` (`// comment`).
For the full list [see the linters plugin.yaml](https://github.com/trunk-io/plugins/blob/main/linters/plugin.yaml).

To create a new comment format provide the name and delimiters, like this:

```yaml
lint:
  comment_formats:
    - name: dashes-block
      leading_delimiter: --[[
      trailing_delimiter: --]
```


### `exported_configs`

`exported_configs`: Linter configs to export when another project is [importing this plugin](../sharing-linters.md)

[//]: # (`shared_configs`: ???)

### `default_max_file_size`

`default_max_file_size`: Default maximum filesize in bytes. Trunk Check will not run linters on any files larger than this. Default value is 4 megabytes.

### `extra_compilation_flags`

`extra_compilation_flags`: When running clang-tidy, this list will be appended to the compile command.

### `compile_commands_roots`

`compile_commands_roots`: Directories to search for `compile_commands.json`. The
default is `build/`.


