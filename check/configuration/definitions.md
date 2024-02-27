# Lint Config Definition


Lint configuration is done in the `lint` section of the trunk.yaml file.

there are three parts:

* LintConfig
* LinterDefinition
* LinterCommandDefinition.

the top part represents the configuration of linting over all. inside that
is the definition of individual linters. inside that is the definition of the particular
command used to invoke the actual binary executable of the underlying linter tool.

The final config used at runtime is created by importing yaml files from the plugins
repo for each linter, merging them into a tree structure, then overriding values
from your repo's trunk.yaml file to yield the final structure.

This overriding process follows the rules of YAML files **link to yaml docs**

**example of single linter definition**
**example of trunk.yaml importing linter def and overriding a value**



## files

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

`files`: Categories of files (languages, headers vs source, etc)

`runtimes`: Node, python, cargo, etc.

`linters`: maps a linter name to it's corresponding linter definition

`definitions`: maps a linter name to it's corresponding linter definitions.

`enabled`: list of enabled linters

`disabled`: list of disablrd linters

`ignore`: the ignore configuration

`threshold`: threshold configuration

`landing_mode`: landing mode configuration

`do_not_recommend_linters`: list of linters to not recommend (actively disabled in repo)

`compile_commands`: source of compile commands for clang-tidy

`bazel`: bazel configuration

`downloads`: runtime and linter downloads

`enviornments`: environment configuration

`triggers`: ??

`comment_formats`: definitions of comment formats.

`exported_configs`: configs to export from a plugin repo and symlink into a sourcing repo.

`shared_configs`: ???

`default_max_file_size`: default maximum filesize in bytes

`extra_compilation_flags`: ??

`compile_commands_roots`: where to search for compile_commands.json

`hold_the_line_mode`: which algorithm to use for hold the line



## Linter Definition
`name` is the name of the linter. This property will be used to refer to the linter in other parts of the config, for example, in the list of enabled linters.


`type` is the type of output the linter produces.

`command`, string, command to run: ex: `[$workspace/tools/linters/clang-format, --assume-filename=${path}]`

`success_codes` is the list of success codes that indicates linter generated data and should be processed. Some linters return 0 for nothing to lint and 1 when there are issues.

`error_codes` is the list of error codes this linter will return when it hit an internal failure and couldn't generate results.

`direct_configs`
__If you have one of these config files, you're definitely using this linter__


`affects_cache`: the list of files that affect the cache results of this linter

`good_without_config`: boolean, indicates whether this linter is recommended without the user tuning its configuration. Prefer `suggest_if`.


`files` is a list of file types listed in the `lint.files` section that this
linter applies to.

`files` File configs for this command. If absent, will use the whole linter's file_configs. Note: this defines the entire list of file configs for this command, rather than appending to those of the entire lint command.


`include_lfs`: boolean, exclude this filetype if it is tracked using LFS.

`std_in`: boolean, Should the command be fed the file on standard input?

`cache_results` : boolean, indicates whether or not to support caching for this linter.

`disable_upstream` :boolean, indicates whether or not we support comparing against the upstream version of this file.  **should we expose this?**

`symlinks`: a list of symlinks to be created when using sandboxing.


`environment`: a list of runtime variables used when running the linter

`is_recommended`: boolean, indicating whether init should try to enable this linter. Prefer `suggest_if`

`run_linter_from`: indicates whether to set current working directory to WORKSPACE root, or the target files folder when run. Prefer `run_from` at the command level.

`include_scanner_type`: which include scanner to use, if any.

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

`version` 

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

`suggest_if`, How to determine if this linter should be auto-enabled/recommended.

`supported_platforms`, Platform constraint. If incompatible, renders a notice.

`tools`, string list

`main_tool`, string, The linter's main tool. This should be the tool that provides the binary for the linter. It will generally be the same as the linter's name, but may differ if the linter is a wrapper. The main tool is used to determine the linter's version.

`path_format`, Whether to use the platform-specific paths or generic "/". Default native.



## Linter Command Definition

`name` : a unique name for this commmand (some tools expose multiple commands, format, lint, analyze, etc.). This will default to trunk verb if not specified.

`output`: which C++ linter class to use to parse this linter output

`prepare_run`: undocumented

`run`: undocumented

`files`:  File configs for this command. If absent, will use the whole linter's file_configs. Note: this defines the entire list of file configs for this command, rather than appending to those of the entire lint command.

`run_when`: Should this command be run only in CI? (or locally, vscode, monitor)

`sucess_codes:` List of success codes that indicates linter generated data and should be processed. Some linters return 0 for nothing to lint and 1 for example when there are issues.

`error_codes` List of error codes this linter will return when it hit an internal failure and couldn't generate results

`no_issues_codes`: List of codes that trunk will just assume there were no issues without parsing the output.

`read_output_from`: Tell parser where to expect output from for reading (stdout, stderr, tmp file)


`run_from`: Whether to set current working directory to WORKSPACE root, or the target files folder when run

`batch`: Combine multiple files into the same execution.

`in_place`: optional boolean, Applies to formatters - does the formatter rewrite the file as opposed to reading its contents from stdin and outputting formatted contents to stdout?

`sandbox_type`: How to create the sandbox if it needs to be created

`allow_empty_files`: Skip linting empty files for this linter

`std_in`: Should the command be fed the file on standard input?

`cache_results`: optional boolean, Whether or not support caching for this linter.

`disable_upstream`: optional boolean,  Whether or not we support comparing against the upstream version of this file

`enabled`: optional boolean, Whether the command is enabled to run when the linter is run. Allows some commands of a linter to be run by default without others

`formatter`: Whether this is a formatter and should be included in `trunk fmt`

`parser`: the definition of a parser that will  transform the output of the linter into SARIF

`parse_regex`: A regular expression used to support regex parsing

`maximum_file_size`: the Maximum file size in Bytes

`idempotent`: optional boolean, Whether or not a linter is idempotent w.r.t. config + source code inputs e.g. semgrep fetches rules from the internet, so it's not idempotent.  If set, it causes `cache_ttl` to default to `24h`

`cache_ttl`: string, How long cached results are kept before they expire. Uses absl::FormatDuration format.

`version`: optional string, Version constraint.

`target`, optional string, What target does this run on.

`is_security`, boolean, Whether findings from this command should be considered "security" or not

`platforms`:  Platform constraint.

`fix_prompt`, optional string, e.g. Incorrect formatting || Unoptimized image

`fix_verb`: optional string, e.g. optimize || autoformat || compress

`max_concurrency`: int, The maximum concurrency this linter will run in a given thread pool.

