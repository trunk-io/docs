# Linter Definition

The definition of a particular linter is put under `lint.definitions`.  The following
properties define the settings of a *particular linter*, not for all linters. For
global linter settings, see [Lint Config](lint-config.md)



## `affects_cache`

`affects_cache`: The list of files that affect the cache results of this linter. [See Caching](files.md#caching)

## `allow_empty_files`

`allow_empty_files`: *optional boolean*. Indicates to skip linting empty files for this linter.

## `batch`

`batch`: *optional boolean*. Combine multiple files into the same execution.

## `commands`

`commands`: The list of commands exposed by this linter. [See Linter Command Definition](commands/command-definition.md)

## `deprecated`

`deprecated`: *string*. Indicates the linter is deprecated and should not be used.

## `direct_configs`

`direct_configs`: *string list*. Indicates config files used to auto
enable the linter. [See auto enabling](common.md#auto-enabling).

## `disabled`

`disabled`: *optional boolean*: Whether linter is actively disabled (and will not be recommended)
and will not run (overrides enabled).

## `download`

`download`: *string*. The download url. You must provide either runtime + packages or download, not both. Using runtimes is preferred. [See Runtimes](../../advanced-setup/runtimes.md)

## `enabled`

`enabled`: *optional boolean*. Whether this linter is enabled.

## `environment`

`environment`: a list of runtime variables used when running the linter. See [Command Environment Variables](commands/commands.md#environment-variables).

## `extra_packages`

`extra_packages`: list of strings, Extra packages to install, versions are optional
See [Linter Dependencies](dependencies.md)

## `formatter`

`formatter`: *boolean*. Indicates whether this is a formatter and should be included in `trunk fmt`

## `good_without_config`

`good_without_config`: *optional boolean*. Indicates whether this linter is recommended without
the user tuning its configuration. Prefer [`suggest_if`](#suggest_if).

## `hold_the_line`

`hold_the_line`: *optional boolean*. Whether hold-the-line will be done for this linter or not.

## `include_lfs`

`include_lfs`: *boolean*. Allow this linter to operate on files tracked
using [git LFS](https://git-lfs.com/).

## `include_scanner_type`

`include_scanner_type`: which include scanner to use, if any.

## `issue_url_format`

`issue_url_format`: *string*, a format string that accepts issue codes for links to issues docs.

## `known_good_version`

`known_good_version`: *string*. A version to be used when Trunk cannot query the latest
version. Currently, Trunk can query the latest version for all package managers
and downloads hosted on GitHub.

## `known_bad_versions`

`known_bad_versions`: *string list*. Versions of a linter that are known to be broken
and should not be run with Trunk. We will fall back to a `known_good_version`
if init or upgrade chooses something in this set.

## `main_tool`

`main_tool`, *string*. If your linter depends on more than a single tool, and
none of the tools has the same name as the linter, then you will
need to specify which is the main tool here. It will be used
to version the tool from the linter's enabled version.

## `name`

`name` Is the name of the linter. This property will be used to refer to the linter in other
parts of the config, for example, in the list of enabled linters.

## `package`

`package`: string, What primary package to install, if using a package manager runtime. The
enabled version of the runtime for this linter will apply to this package.
See [Linter Dependencies](dependencies.md)

## `path_format`

`path_format`, Whether to use the platform-specific paths or generic "/". Default native.

## `plugin_url`

`plugin_url`: *string*, a plugin url for reporting issues.

## `prepare_command`

`prepare_command`. A command that is run once per session before linting any number
of files using this linter. ex. `[tflint, --init]`

## `query_compile_commands`

`query_compile_commands`, *optional boolean*.

## `read_output_from`

`read_output_from`,  Tell the parser where to expect output from for reading (stdout, stderr,
tmp file). [See Output Sources](commands/output-types.md#output-sources).

## `runtime`

`runtime`: RuntimeType, Which package manager runtime, if any, to require to be setup for 
this linter. Ex: `node`, `ruby`, `python`. See [Linter Dependencies](dependencies.md).

## `run_from_root_target`

`run_from_root_target`: *string*. Walk up to find this file to detect the run from directory.
Prefer `run_from` at the command level.

## `run_timeout`

`run_timeout`: *duration string*. Describes how long a linter can run before timing out.
[See timeouts](../README.md#timeout)

## `run_when`

`run_when`, *optional string*. Indicates when this linter should be run.
Possible values are: `cli`, `monitor`, `ci`, `lsp`. 
See also [command run_when](commands/definition.md#run_when).

## `suggest_if`

How to determine if this linter should be auto-enabled/recommended. Possible
values are `never`, `config_present`, and `files_present`.
[See auto-enabling](enabling.md#auto-enabling) for more details.

## `supported_platforms`

Platform constraint. If incompatible, renders a notice. 
See also [command `platforms`](commands/definition.md#platforms)

## `target`

`target`: *optional string*. What target does this linter run on. Defaults to `${file}`.

Examples:

**nancy** uses `.` as the target.
[full source](https://github.com/trunk-io/plugins/blob/main/linters/nancy/plugin.yaml)

```yaml
# nancy uses .
definitions:
  - name: nancy
    files: [go-lockfile]
    download: nancy
    runtime: go
    commands:
      - output: sarif
        run: sh ${plugin}/linters/nancy/run.sh
        success_codes: [0, 1, 2]
        target: .
        read_output_from: stdout
        is_security: true
```

**tflint** uses `${parent}` as the target.
[full source](https://github.com/trunk-io/plugins/blob/main/linters/tflint/plugin.yaml)

```yaml
lint:
  definitions:
    - name: tflint
      files: [terraform]
      commands:
        - name: lint
          output: sarif
          prepare_run: tflint --init
          run: tflint --format=sarif --force
          success_codes: [0, 1, 2]
          read_output_from: stdout
          # tflint can only run on the current directory unless --recursive is passed
          target: ${parent}
          run_from: ${target_directory}
          version: ">=0.47.0"
```

**Clippy** uses `${parent_with(Cargo.toml)}` as the target.
[full source](https://github.com/trunk-io/plugins/blob/main/linters/clippy/plugin.yaml)

```yaml
version: 0.1
lint:
  definitions:
    # clippy has 3 lint severities: deny, warn, and allow. Unfortunately deny causes rustc to
    # fail eagerly due to its implementation (https://github.com/rust-lang/rust/pull/87337),
    # We use --cap-lints to downgrade "deny" severity lints to warn. So rustc will find all
    # issues instead of hard stopping. There are currently only 70 of them, so we could hardcode
    # the list to fix their severity levels correctly.
    - name: clippy
      files: [rust]
      download: rust
      commands:
        - name: lint
          # Custom parser type defined in the trunk cli to handle clippy's JSON output.
          output: clippy
          target: ${parent_with(Cargo.toml)}
          run: cargo clippy --message-format json --locked -- --cap-lints=warn --no-deps
          success_codes: [0, 101, 383]
          run_from: ${target_directory}
          disable_upstream: true
```

## `tools`

`tools`, *string list*. The list of tools used by this linter. See [Dependencies](dependencies.md)

## `version_command`

`version_command`:  Version check commands.




