# Lint Config Definitions


Lint configuration is done in the `lint` section of the trunk.yaml file. There are three parts:

* Lint Config
* Linter Definition
* Linter Command Definition.

The top part represents the configuration of overall linting. Inside that
is the definition of individual linters. And inside *that* is the definition of the particular
command used to invoke the actual binary executable of the underlying tool.

The final config used at runtime is created by importing `.yaml` files from the plugins
repo for each linter, merging them into a tree structure, then overriding values
from your repo's `trunk.yaml` file to yield the final configuration.

## Defining File Types

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


## Lint Config

The `lint` section represents the configuration of all linters. This is where you can:

* define the linters (`linters`),
* list linters to enable and disable (`enabled` and `disabled`)
* define file categories (`files`)
* list required `runtimes`, `downloads`, `environments` ,
* and additional cross-linter settings


`files`: Definitions of filetypes. See [defining file types](./reference.md#defining-file-types)

`runtimes`: Node, python, cargo, etc. Used to define or override a runtime environment for package management. 

[//]: # (`linters`: maps a linter name to it's corresponding linter definition)

`definitions`: Where you define or override linter settings. See [Linter Definition Config](#lint-config-definitions)

`enabled`: list of enabled linters

`disabled`: list of disabled linters

`ignore`: files to be [ignored by linters](../ignoring-issues.md#ignoring-multiple-files)

`threshold`: where you specify the blocking behavior of linters. The [threshold](../readme.md#blocking-thresholds) for whether an error from a linter should block commits or not.

[//]: # (`landing_mode`: landing mode configuration)

[//]: # (`do_not_recommend_linters`: list of linters to not recommend &#40;actively disabled in repo&#41;)

`compile_commands`: compile commands for clang-tidy. Must be one of `compile_commands_json` or `bazel`

`bazel`: bazel configuration
    * `paths` locations to look for Bazel binary. [Example](../configuring-existing-linters/README.md#using-bazel)

`downloads`: Locations to download binary artifacts from. Using [tool definitions](../../advanced-setup/tools/README.md) instead is preferred.

[//]: # (`environments`: environment configuration)

[//]: # (`triggers`: ??)

`comment_formats`: definitions of comment formats. Reused in linter definitions.

`exported_configs`: Linter configs to export when another project is [importing this plugin](../sharing-linters.md) 

[//]: # (`shared_configs`: ???)

`default_max_file_size`: Default maximum filesize in bytes. Trunk Check will not run linters on any files larger than this. Default value is 4 megabytes.

`extra_compilation_flags`: When running clang-tidy, this list will be appended to the compile command.

`compile_commands_roots`: Directories to search for `compile_commands.json`.

[//]: # (`hold_the_line_mode`: which algorithm to use for hold the line)


## Linter Definition

The linter definition is under `lint.definitions`.  The following
properties define the settings of a *particular linter*, not for all linters. For
global linter settings, see [Lint Config](reference.md#lint-config)


`name` Is the name of the linter. This property will be used to refer to the linter in other parts of the config, for example, in the list of enabled linters.

[//]: # (`type` is the type of output the linter produces. **link to output types**)

[//]: # (`command`, string, command to run: ex: `[$workspace/tools/linters/clang-format, --assume-filename=${path}]`)

[//]: # (`success_codes` is the list of success codes that indicates linter generated data and should be processed. Some linters return 0 for nothing to lint and 1 when there are issues.)

[//]: # (`error_codes` is the list of error codes this linter will return when it hit an internal failure and couldn't generate results.)

### `direct_configs`

__If you have one of these config files, you're definitely using this linter__

`affects_cache`: the list of files that affect the cache results of this linter.

`good_without_config`: optional boolean. Indicates whether this linter is recommended without the user tuning its configuration. Prefer `suggest_if`.

### files
`files` is a list of file types listed in the `lint.files` section that this linter applies to. 

### `files`
`files` File configs for this command. If absent, will use the whole linter's `file_configs`. Note: this defines the entire list of file configs for this command, rather than appending to those of the entire lint command.

### `include_lfs`

`include_lfs`: boolean, exclude this filetype if it is tracked using LFS.

[//]: # (`std_in`: boolean, Should the command be fed the file on standard input?)

[//]: # (`cache_results` : boolean, indicates whether or not to support caching for this linter.)

[//]: # (`disable_upstream` :boolean, indicates whether or not we support comparing against the upstream version of this file.  **should we expose this?**)

`symlinks`: a list of symlinks to be created when using sandboxing.

`environment`: a list of runtime variables used when running the linter

`is_recommended`: boolean, indicating whether init should try to enable this linter. Prefer [`suggest_if`](#suggest_if)

`run_linter_from`: indicates whether to set current working directory to WORKSPACE root, or the target files folder when run. Prefer `run_from` at the command level.

`include_scanner_type`: which include scanner to use, if any.

### `formatter`
`formatter`: boolean. Indicates whether this is a formatter and should be included in `trunk fmt`

`allow_empty_files`: boolean. Indicates to skip linting empty files for this linter.

`runtime`: RuntimeType, Which runtime, if any, to require to be setup for this linter.

`package`: string, What primary package to install, if using a package manager runtime

`extra_packages`: list of strings, Extra packages to install, versions are optional

`download`: string, download url. You must provide either runtime + packages or download, not both. Using runtimes is preferred.

`issue_url_format`: string, a format string that accepts issue codes for links to issues docs.

`run_from_root_target`: string, Walk up to find this file to detect the run from directory. Prefer `run_from` at the command level.

`hold_the_line`, optional boolean, whether hold-the-line will be done for this linter or not.

`read_output_from`,  Tell the parser where to expect output from for reading (stdout, stderr, tmp file)

`prepare_command`, ex. `[tflint, --init]`

[//]: # (`version`, **???** )

`known_good_version`, The version init inits with. If not present it will query the version from its runtime or use the default version from the download.

`version_command`,  Version check commands

`enabled`, optional boolean, Whether this linter is enabled

`batch`, optional boolean, Combine multiple files into the same execution.

`run_when`, Should this linter be run only in CI? (or locally, vscode, monitor)

`in_place`, optional boolean, Applies to formatters - does the formatter rewrite the file as opposed to reading its contents from stdin and outputting formatted contents to stdout?

`run_timeout`, duration string, describes how long a linter can run before timing out.

`disabled`, optional boolean, Whether linter is actively disabled (will not be recommended) and will not run (overrides enabled).

`commands`, commands exposed by this linter

`deprecated`, string, Deprecated information (set when linter is deprecated)

`known_bad_versions`, string list, Versions of a linter that are known to be broken or not work with trunk. We will fallback to a known_good_version if init or upgrade chooses something in this set.

`plugin_url`, string, a plugin url for reporting issues.

`query_compile_commands`, optional boolean

`idempotent`, optional boolean, Indicates whether or not a linter is idempotent w.r.t. config + source code inputs.  e.g. semgrep fetches rules from the internet, so it's not idempotent . If set, causes cache_ttl to default to 24h

`cache_ttl`, duration string, How long cached results are kept before they expire

`target`: optional string, what target does this run on


### `suggest_if`

How to determine if this linter should be auto-enabled/recommended. Possible 
values are `never`, `config_present`, and `files_present`.

* `config_present` will auto-enable a linter if Trunk sees any [`direct_config`](#direct_configs) for it .
* `files_present` will auto-enable a linter if Trunk sees any file type that it operates on.
* `never` will never auto-enable this linter.

Trunk curates the values of `suggest_if` for all linters in the plugins repo.

### `supported_platforms`

Platform constraint. If incompatible, renders a notice.

`tools`, string list

`main_tool`, string, The linter's main tool. This should be the tool that provides the binary for the linter. It will generally be the same as the linter's name, but may differ if the linter is a wrapper. The main tool is used to determine the linter's version.

`path_format`, Whether to use the platform-specific paths or generic "/". Default native.



## Linter Command Definition

The linter command definitions are defined in `lint.linter.commands`. A single linter can have 
multiple commands if it is used in different ways.


[//]: # (**action: if here and in linter def, remove from linter def**)

`name` : a unique name for this command (some tools expose multiple commands, format, lint, analyze, etc.).

### `output`

`output`: which type of output this linter produces. [See Output Types](output-types.md).

`prepare_run`: an extra command to run before running a linter.

`run`: The command to run a linter. **link to examples in main docs**

`files`:  File types that this linter operates on. **link to example**

`run_when`: Should this command be run only in CI? One of cli,lsp,monitor,ci

`sucess_codes:` List of exit codes that indicates linter ran successfully. **unrelated to whether or not there were issues reported by the linter**

`error_codes` List of exit codes this linter will return when it hit an internal failure and couldn't generate results.  **you need either success codes or error codes but not both**

`no_issues_codes`: List of exit codes that Trunk will just assume there were no issues without parsing the output.

`read_output_from`: Tell parser where to expect output from for reading **check values** (stdout, stderr, tmp_file) **link to output docs**

`run_from`: What current working directory to run the linter from. **link to section with more examples**.

`batch`: optional boolean, Combine multiple files into the same execution.

`in_place`: optional boolean, Applies to formatters - does the formatter rewrite the file as opposed to reading its contents from stdin and outputting formatted contents to stdout?

`sandbox_type`: How to create the sandbox if it needs to be created

`allow_empty_files`: optional boolean. Skip linting empty files for this linter. Will assume there are no linters if the file is empty.

`std_in`: optional boolean, Should the command be fed the file on standard input?

`cache_results`: optional boolean, Whether or not support caching for this linter. **explain how trunk does caching in another page**

`disable_upstream`: optional boolean,  Whether or not we support comparing against the upstream version of this file.  **link to a deeper explanation for when you set this to false**

`enabled`: optional boolean, Whether the command is enabled to run when the linter is run. Allows some commands of a linter to be run by default without others.

`formatter`: optional boolean, Whether this is a formatter and should be included in `trunk fmt`

`parser`: the definition of a parser that will transform the output of the linter into SARIF. Not needed if linter is already output SARIF.

`parse_regex`: A regular expression used to support regex parsing. **link to explanation of regex parsing**

`maximum_file_size`: the maximum file size in bytes. max size for input files to the linter.

`idempotent`: optional boolean, Whether or not a linter is idempotent w.r.t. config + source code inputs e.g. semgrep fetches rules from the internet, so it's not idempotent.  If set, it causes `cache_ttl` to default to `24h`. This affects how long linter outputs are cached.  

`cache_ttl`: string, How long cached results are kept before they expire. **link to deeper explanation** Only applies to if `idempotent: false` 

`version`: optional string, Version constraint.  **link to deeper explanation of version constraints with example**

`target`, optional string, What target does this run on. By default the target is the modified source code file. Some linters op on whole repo or dir. **link to deeper docs**.

`is_security`, boolean, Whether findings from this command should be considered "security" or not. Allows this linter to be run with `--scope==security`. **link to command line options**

`platforms`:  Platform constraint. mac vs win etc. **link to deeper explanation**

`fix_prompt`, optional string, e.g. Incorrect formatting || Unoptimized image. This string is used when prompting the user to use the linter interactively.

`fix_verb`: optional string, e.g. `optimize`, `autoformat`, or `compress`. This string is used when prompting the user to use the linter interactively.

`max_concurrency`: int, The maximum number of processes that Trunk Check will run concurrently for this linter. 


[//]: # (## JSON `trunk.yaml` Schema)

[//]: # (For even more details, you can refer to [the JSON schema for `trunk.yaml`]&#40;https://static.trunk.io/pub/trunk-yaml-schema.json&#41;)


