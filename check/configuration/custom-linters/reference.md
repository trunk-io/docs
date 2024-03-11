# Lint Config Definitions


Lint configuration is done in the `lint` section of the trunk.yaml file. There are three parts:

* [Lint Config](./reference.md#lint-config)
* [Linter Definition](./reference.md#linter-definition)
* [Linter Command Definition](./reference.md#linter-command-definition).

The top part represents the configuration of overall linting. Inside that
is the definition of individual linters. And inside *that* is the definition of the particular
command used to invoke the actual binary executable of the underlying tool.

The final config used at runtime is created by importing `.yaml` files from the plugins
repo for each linter, merging them into a tree structure, then overriding values
from your repo's `trunk.yaml` file to yield the final configuration.

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

[//]: # (`landing_mode`: landing mode configuration)

[//]: # (`do_not_recommend_linters`: list of linters to not recommend &#40;actively disabled in repo&#41;)

### `compile_commands`

`compile_commands`: compile commands for clang-tidy. Must be one of `compile_commands_json` or `bazel`

### `bazel`

`bazel`: bazel configuration

* `paths` locations to look for Bazel binary. [Example](../configuring-existing-linters/README.md#using-bazel)

### `downloads`

`downloads`: Locations to download binary artifacts from. Using [tool definitions](../../advanced-setup/tools/README.md) instead is preferred.

[//]: # (`environments`: environment configuration)

[//]: # (`triggers`: ??)

### `comment_formats`

`comment_formats`: definitions of comment formats. Reused in linter definitions.

### `exported_configs`

`exported_configs`: Linter configs to export when another project is [importing this plugin](../sharing-linters.md) 

[//]: # (`shared_configs`: ???)

### `default_max_file_size`

`default_max_file_size`: Default maximum filesize in bytes. Trunk Check will not run linters on any files larger than this. Default value is 4 megabytes.

### `extra_compilation_flags`

`extra_compilation_flags`: When running clang-tidy, this list will be appended to the compile command.

### `compile_commands_roots`

`compile_commands_roots`: Directories to search for `compile_commands.json`.

[//]: # (`hold_the_line_mode`: which algorithm to use for hold the line)


## Linter Definition

The definition of a particular linter is put under `lint.definitions`.  The following
properties define the settings of a *particular linter*, not for all linters. For
global linter settings, see [Lint Config](reference.md#lint-config)


### `name`

`name` Is the name of the linter. This property will be used to refer to the linter in other 
parts of the config, for example, in the list of enabled linters.

[//]: # (`type` is the type of output the linter produces. **link to output types**)

[//]: # (`command`, string, command to run: ex: `[$workspace/tools/linters/clang-format, --assume-filename=${path}]`)

[//]: # (`success_codes` is the list of success codes that indicates linter generated data and should be processed. Some linters return 0 for nothing to lint and 1 when there are issues.)

[//]: # (`error_codes` is the list of error codes this linter will return when it hit an internal failure and couldn't generate results.)

### `direct_configs`

__If you have one of these config files, you're definitely using this linter__

### `affects_cache`

`affects_cache`: the list of files that affect the cache results of this linter.

### `good_without_config`

`good_without_config`: *optional boolean*. Indicates whether this linter is recommended without 
the user tuning its configuration. Prefer `suggest_if`.

### `files`

`files` is a list of file types listed in the `lint.files` section that this linter applies to. 


### `include_lfs`

`include_lfs`: boolean, exclude this filetype if it is tracked using LFS.

[//]: # (`std_in`: boolean, Should the command be fed the file on standard input?)

[//]: # (`cache_results` : boolean, indicates whether or not to support caching for this linter.)

[//]: # (`disable_upstream` :boolean, indicates whether or not we support comparing against the upstream version of this file.  **should we expose this?**)

### `symlinks`

`symlinks`: a list of symlinks to be created when using sandboxing.

### `environment`

`environment`: a list of runtime variables used when running the linter.

### `is_recommended`

`is_recommended`: *boolean*. Indicating whether `trunk init` should try to enable this linter. 
Prefer [`suggest_if`](#suggest_if)

### `run_linter_from`

`run_linter_from`: indicates whether to set current working directory to WORKSPACE root, or the 
target files folder when run. Prefer `run_from` at the command level.

`include_scanner_type`: which include scanner to use, if any.

### `formatter`

`formatter`: boolean. Indicates whether this is a formatter and should be included in `trunk fmt`

### `allow_empty_files`

`allow_empty_files`: boolean. Indicates to skip linting empty files for this linter.

### `runtime`

`runtime`: RuntimeType, Which runtime, if any, to require to be setup for this linter.

### `package`

`package`: string, What primary package to install, if using a package manager runtime

### `extra_packages`

`extra_packages`: list of strings, Extra packages to install, versions are optional

### `download`

`download`: *string*. The download url. You must provide either runtime + packages or download, not both. Using runtimes is preferred. [See Runtimes](../../advanced-setup/runtimes.md)

`issue_url_format`: string, a format string that accepts issue codes for links to issues docs.

### `run_from_root_target`

`run_from_root_target`: *string*. Walk up to find this file to detect the run from directory. 
Prefer `run_from` at the command level.

### `hold_the_line`

`hold_the_line`: *optional boolean*. Whether hold-the-line will be done for this linter or not.

### `read_output_from`

`read_output_from`,  Tell the parser where to expect output from for reading (stdout, stderr, 
tmp file). [See Output Sources](output-types.md#output-sources)

### `prepare_command`

`prepare_command`, ex. `[tflint, --init]`

[//]: # (`version`, **???** )

### `known_good_version`

`known_good_version`: The version `trunk init` inits with. If not present Trunk will query the 
version from its runtime or use the default version from the download.

### `version_command`

`version_command`:  Version check commands

### `enabled`

`enabled`: *optional boolean*. Whether this linter is enabled.

### `batch`

`batch`: *optional boolean*. Combine multiple files into the same execution.

### `run_when`

`run_when`, Should this linter be run only in CI? (or locally, vscode, monitor)

### `in_place`

`in_place`: *optional boolean*. Applies to formatters - does the formatter rewrite the file as 
opposed to reading its contents from STDIN and outputting formatted contents to STDOUT?

### `run_timeout`

`run_timeout`: *duration string*. Describes how long a linter can run before timing out. 
[See timeouts](../readme.md#timeout)

### `disabled`

`disabled`: *optional boolean*: Whether linter is actively disabled (and will not be recommended)
and will not run (overrides enabled).

### `commands`
`commands`: Commands exposed by this linter. [See Linter Command Definition](#linter-command-definition)

### `deprecated`

`deprecated`: *string*. Deprecated information (set when linter is deprecated)

### `known_bad_versions`

`known_bad_versions`: *string list*. Versions of a linter that are known to be broken 
and should not be run with Trunk. We will fall back to a `known_good_version` 
if init or upgrade chooses something in this set.

### `plugin_url`

`plugin_url`: *string*, a plugin url for reporting issues.

### `query_compile_commands`

`query_compile_commands`, *optional boolean*

### `idempotent`

`idempotent`: *optional boolean*. Indicates whether a linter is idempotent w.r.t. config + 
source code inputs.  e.g. semgrep fetches rules from the internet, so it's not idempotent . If 
set, causes cache_ttl to default to 24h

### `cache_ttl`

`cache_ttl`, duration string, How long cached results are kept before they expire

### `target`

`target`: optional string, what target does this run on

### `suggest_if`

How to determine if this linter should be auto-enabled/recommended. Possible 
values are `never`, `config_present`, and `files_present`.

* `config_present` will auto-enable a linter if Trunk sees any [`direct_config`](#direct_configs) for it .
* `files_present` will auto-enable a linter if Trunk sees any file type that it operates on.
* `never` will never auto-enable this linter.

Trunk curates the values of `suggest_if` for all linters in the [plugins](https://github.com/trunk-io/plugins) repo.

### `supported_platforms`

Platform constraint. If incompatible, renders a notice.

### `tools`

`tools`, string list

### `main_tool`

`main_tool`, *string*. The linter's main tool. This should be the tool that provides the binary 
for the linter. It will generally be the same as the linter's name, but may differ if the linter 
is a wrapper. The main tool is used to determine the linter's version.

### `path_format`

`path_format`, Whether to use the platform-specific paths or generic "/". Default native.



## Linter Command Definition

The linter command definitions are defined in `lint.linter.commands`. A single linter can have 
multiple commands if it is used in different ways.  

*Note:*. If you define the executable to run here (the command definition), then you should *not*
define it also in the linter definition. Defining it here as a command is preferred.

### `name`

`name`: *string*. A unique name for this command (some tools expose multiple commands, format, 
lint, analyze, etc.).

### `output`

`output`: which type of output this linter produces. [See Output Types](output-types.md).

### `prepare_run`

`prepare_run`: an extra command to run before running a linter.

### `run`

`run`: The command to run a linter. 

[//]: # (TODO: link to examples in main docs)

### `files`

`files` File configs for this command. If absent, will use the whole linter's `file_configs`. Note: this defines the entire list of file configs for this command, rather than appending to those of the entire lint command.

[//]: # (TODO: link to example)

### `run_when`

`run_when`: Should this command be run only in CI? One of `cli`, `lsp`, `monitor`, or `ci`.

### `success_codes`

`sucess_codes:` List of exit codes that indicates linter ran successfully. **Unrelated to 
whether or not there were issues reported by the linter**

### `error_codes`

`error_codes`: List of exit codes this linter will return when it hit an internal failure and 
couldn't generate results.  **A linter should set either success codes or error codes, but not both.**

### `no_issues_codes`

`no_issues_codes`: List of exit codes that Trunk will use to assume there were no issues without 
parsing the output.

### `read_output_from`

`read_output_from`: Tell parser where to expect output from for reading.
[See Output Sources](output-types.md#output-sources)

[//]: # (TODO: **check values** &#40;stdout, stderr, tmp_file&#41; )

[//]: # (TODO: **link to output docs**)

### `run_from`

`run_from`: What current working directory to run the linter from. 

[//]: # (TODO: **link to section with more  examples**.)

### `batch`

`batch`: *optional boolean*. Combine multiple files into the same execution.

### `in_place`

`in_place`: *optional boolean*. Applies to formatters - does the formatter rewrite the file as 
opposed to reading its contents from STDIN and outputting formatted contents to STDOUT?

### `sandbox_type`

`sandbox_type`: How to create the sandbox if it needs to be created.

### `allow_empty_files`

`allow_empty_files`: *optional boolean*. Skip linting empty files for this linter. Trunk will 
assume there are no linters if the file is empty.

### `std_in`

`std_in`: *optional boolean*. Should the command be fed the file on standard input?

### `cache_results`

`cache_results`: *optional boolean*. Indicates if this linter wants to cache results. 

[//]: # (TODO: **explain how trunk does caching in another page**)

### `disable_upstream`

`disable_upstream`: *optional boolean*,  Whether this linter supports comparing against the 
upstream version of this file.  

[//]: # (TODO: **link to a deeper explanation for when you set this to false**)

### `enabled`

`enabled`: *optional boolean*. Whether the command is enabled to run when the linter is run. 
Allows some commands of a linter to be run by default without others.

### `formatter`

`formatter`: *optional boolean*. Whether this command is a formatter and should be included in 
`trunk fmt`.

### `parser`

`parser`: The definition of a parser that will transform the output of the linter into SARIF. 
Not needed if linter is already output SARIF. [See Output Types](./output-types.md)

### `parse_regex`

`parse_regex`: *string*. A regular expression used to support regex parsing.
[See Regex output type](./output-types.md#regex)

### `maximum_file_size`

`maximum_file_size`: *number*. The maximum file size in bytes for input files to the linter.

### `idempotent`

`idempotent`: *optional boolean*. Indicates whether a linter is idempotent with config 
and source code inputs. For example, `semgrep` fetches rules from the internet, so it is not 
idempotent.  If set, it causes `cache_ttl` to default to `24h`. This affects how long linter 
outputs are cached.

### `cache_ttl`

`cache_ttl`: *string*. How long cached results are kept before they expire.  Only applies if `idempotent: false`

[//]: # (TODO: link to deeper explanation** )

### `version`

`version`: *optional string*, Version constraint.  

[//]: # (TODO: link to deeper explanation of version constraints with example)

### `target`

`target`, *optional string*, What target does this run on. By default, the target is the modified 
source code file. Some linters operate on a whole repo or directory. 

[//]: # (TODO: link to deeper docs.)

### `is_security`

`is_security`: *boolean*. Whether findings from this command should be considered "security" or 
not. Allows this linter to be run with `--scope==security`. [See Command Line Options](../../advanced-setup/cli/cli-options.md)

### `platforms`

`platforms`:  Platform constraint. mac vs win etc. 

[//]: # (TODO: link to deeper explanation)

### `fix_prompt`

`fix_prompt`, optional string, e.g. 'Incorrect formatting' or 'Unoptimized image'. This string is 
used when prompting the user to use the linter interactively.


### `fix_verb`

`fix_verb`: optional string. This string is used when prompting the user to use the linter 
interactively. Example: `optimize`, `autoformat`, or `compress`.

### `max_concurrency`

`max_concurrency`: integer, The maximum number of processes that Trunk Check will run 
concurrently for this linter. [See Limiting Concurrency](./readme.md#limiting-concurrency)


[//]: # (## JSON `trunk.yaml` Schema)

[//]: # (For even more details, you can refer to [the JSON schema for `trunk.yaml`]&#40;https://static.trunk.io/pub/trunk-yaml-schema.json&#41;)


