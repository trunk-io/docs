# Definitions

The definition of a particular linter is put under `lint.definitions`. The following properties define the settings of a _particular linter_, not for all linters. For global linter settings, see [Lint Config](./).

## `affects_cache`

`affects_cache`: The list of files that affect the cache results of this linter. [See Caching](../../caching.md).

## `allow_empty_files`

`allow_empty_files`: _optional boolean_. Indicates to skip linting empty files for this linter.

## `batch`

`batch`: _optional boolean_. Combine multiple files into the same execution.

## `commands`

`commands`: The list of commands exposed by this linter. See [Linter Command Definition](commands.md).

## `deprecated`

`deprecated`: _string_. Indicates the linter is deprecated and should not be used.

## `direct_configs`

`direct_configs`: _string list_. Indicates config files used to auto-enable the linter. See [Auto Enabling](auto-enable.md).

## `disabled`

`disabled`: _optional boolean_: Whether linter is actively disabled (and will not be recommended) and will not run (overrides enabled).

## `download`

`download`: _string_. The download URL. You must provide either runtime + packages or download, not both. Using runtimes is preferred. See [Runtimes](../runtimes.md).

## `enabled`

`enabled`: _optional boolean_. Whether this linter is enabled.

## `environment`

`environment`: a list of runtime variables used when running the linter. See [Command Environment Variables](commands.md#environment-variables).

## `extra_packages`

`extra_packages`: list of strings, Extra packages to install, versions are optional. See [Linter Dependencies](dependencies.md).

## `formatter`

`formatter`: _boolean_. Indicates whether this is a formatter and should be included in `trunk fmt`.

## `good_without_config`

`good_without_config`: _optional boolean_. Indicates whether this linter is recommended without the user tuning its configuration. Prefer [`suggest_if`](definitions.md#suggest_if).

## `hold_the_line`

`hold_the_line`: _optional boolean_. Whether [hold-the-line will](../../../code-quality/overview/how-does-it-work.md#hold-the-line) be done for this linter or not.

## `include_lfs`

`include_lfs`: _boolean_. Allow this linter to operate on files tracked using [git LFS](https://git-lfs.com/).

## `include_scanner_type`

`include_scanner_type`: which include scanner to use, if any.

## `issue_url_format`

`issue_url_format`: _string_, a format string that accepts issue codes for links to issues docs.

## `known_good_version`

`known_good_version`: _string_. A version to be used when Trunk cannot query the latest version. Currently, Trunk can query the latest version for all package managers and downloads hosted on GitHub.

## `known_bad_versions`

`known_bad_versions`: _string list_. Versions of a linter that are known to be broken and should not be run with Trunk. We will fall back to a `known_good_version` if init or upgrade chooses something in this set.

## `main_tool`

`main_tool`, _string_. If your linter depends on more than a single tool, and none of the tools has the same name as the linter, then you will need to specify which is the main tool here. It will be used to version the tool from the linter's enabled version.

## `name`

`name` _required string._ The name of the linter. This property will be used to refer to the linter in other parts of the config, for example, in the list of enabled linters.

## `package`

`package`: string, What primary package to install, if using a package manager runtime. The enabled version of the runtime for this linter will apply to this package. See [Linter Dependencies](dependencies.md).

## `path_format`

`path_format`, Whether to use the platform-specific paths or generic "/". Default native.

## `plugin_url`

`plugin_url`: _string_, a plugin url for reporting issues.

## `prepare_command`

`prepare_command`. A command that is run once per session before linting any number of files using this linter. ex. `[tflint, --init]`.

## `query_compile_commands`

`query_compile_commands`, _optional boolean_.

## `runtime`

`runtime`: RuntimeType, Which package manager runtime, if any, to require to be setup for this linter. Ex: `node`, `ruby`, `python`. See [Linter Dependencies](dependencies.md).

## `run_timeout`

`run_timeout`: _duration string_. Describes how long a linter can run before timing out. [See timeouts](../../../code-quality/linters/configure-linters.md#timeout).

## `suggest_if`

How to determine if this linter should be auto-enabled/recommended. Possible values are `never`, `config_present`, and `files_present`. [See auto-enabling](auto-enable.md) for more details.

## `supported_platforms`

Platform constraint. If incompatible, renders a notice. See also [Command `platforms`](commands.md#platforms).

## `tools`

`tools`, _string list_. The list of tools used by this linter. See [Linter Dependencies](dependencies.md).

## `version_command`

`version_command`: Version check commands.

## `verbatim_message`

`verbatim_message`: Do not try to truncate or reflow the output of this linter.
