# Linter Command Definition

The linter command definitions are defined in `lint.definitions.commands`. A single linter can have 
multiple commands if it is used in different ways.  

*Note:*. If you define the executable to run here (the command definition), then you should *not*
define it also in the linter definition. Defining it here as a command is preferred.


## `allow_empty_files`

`allow_empty_files`: *optional boolean*. Skip linting empty files for this linter. Trunk will
assume there are no linters if the file is empty.

## `batch`

`batch`: *optional boolean*. Combine multiple files into the same execution.
If true, the `${target}` template substitution in the `run`
field may expand into multiple files.

## `cache_ttl`

`cache_ttl`, *duration string*. If this linter is not [idempotent](#idempotent), this is how long cached results are kept before they expire. Defaults to 24hrs. See [Output Caching](../files.md#idempotency) for more details.

## `cache_results`

`cache_results`: *optional boolean*. Indicates if this linter wants to cache results. See [Caching](../files.md#caching) for more details.

## `disable_upstream`

`disable_upstream`: *optional boolean*,  Whether this linter supports comparing against the
upstream version of this file.

[//]: # (TODO: **link to a deeper explanation for when you set this to false**)

## `error_codes`

`error_codes`: List of exit codes this linter will return when it hit an internal failure and
couldn't generate results.  **A linter should set either success codes or error codes, but not both.**

## `enabled`

`enabled`: *optional boolean*. Whether the command is enabled to run when the linter is run.
Allows some commands of a linter to be run by default without others.

## `files`

`files` is a list of file types listed in the `lint.files` section that this linter applies to.

Example: **prettier** [full source](https://github.com/trunk-io/plugins/blob/main/linters/prettier/plugin.yaml)

```yaml
lint:
  definitions:
    - name: prettier
      files:
        - typescript
        - yaml
        - css
        - sass
        - html
        - markdown
        - json
        - javascript
        - graphql
        - prettier_supported_configs
```

## `fix_prompt`

`fix_prompt`, *optional string*, e.g. 'Incorrect formatting' or 'Unoptimized image'. This string is
used when prompting the user to use the linter interactively.

## `fix_verb`

`fix_verb`: *optional string8. This string is used when prompting the user to use the linter
interactively. Example: `optimize`, `autoformat`, or `compress`.

## `formatter`

`formatter`: *optional boolean*. Whether this command is a formatter and should be included in
`trunk fmt`.

## `in_place`

`in_place`: *optional boolean*. Indicates that this formatter will
rewrite the file in place **Only applies to formatters**.

## `idempotent`

`idempotent`: *optional boolean*. Indicates whether a linter is idempotent with config and source code inputs. For example, semgrep fetches rules from the internet, so it is not idempotent . If set, will only cache results a duration of `cache_ttl`. See [Output Caching](../files.md#idempotency) for more details.

## `is_security`

`is_security`: *optional boolean*. Whether findings from this command should be considered "security" or
not. Allows this linter to be run with `--scope==security`. [See Command Line Options](../../../advanced-setup/cli/cli-options.md)

## `maximum_file_size`

`maximum_file_size`: *optional number*. The maximum file size in bytes for input files to the linter.

## `max_concurrency`

`max_concurrency`: *optional integer*, The maximum number of processes that Trunk Check will run
concurrently for this linter. [See Limiting Concurrency](README.md#limiting-concurrency)

## `name`

`name`: *string*. A unique name for this command (some tools expose multiple commands, format, lint, analyze, etc.).

## `no_issues_codes`

`no_issues_codes`: List of exit codes that Trunk will use to assume there were no issues without
parsing the output.

## `output`

`output`: *string*. which type of output this linter produces. [See Output Types](output-types.md).

## `parser`

`parser`: The definition of a parser that will transform the output of the linter into SARIF.
Not needed if linter is already output SARIF. [See Output Types](output-types.md)

## `parse_regex`

`parse_regex`: *string*. A regular expression used to support regex parsing.[See Regex output type](output-types.md#regex)

## `platforms`

`platforms`:  A list of platforms this linter supports. (ex: `windows`, `macos`, `linux`). 
Linters using managed runtimes (node, python, etc.) can generally run cross-platform
and do not need the `platforms` property set. For tools which *are* platform specific or which
have different configuration for each platform, this property can be used to distinguish between
them. 

For example, the `detekt` plugin has different exit codes for Windows than for 
MacOS and Linux, and has two command definitions with different `success_codes` fields.
[Full Source](https://github.com/trunk-io/plugins/blob/main/linters/detekt/plugin.yaml)

```yaml
lint:
  definitions:
    - name: detekt
      files: [kotlin]
      download: detekt
      commands:
        - name: lint
          platforms: [windows]
          output: sarif
          run:
            detekt-cli --build-upon-default-config --config .detekt.yaml --input ${target,} --report
            sarif:${tmpfile}
          success_codes: [0, 1, 2]
          read_output_from: tmp_file
          batch: true
          cache_results: true
        - name: lint
          output: sarif
          run:
            detekt-cli --build-upon-default-config --config .detekt.yaml --input ${target,} --report
            sarif:${tmpfile}
          success_codes: [0, 2]
          read_output_from: tmp_file
          batch: true
          cache_results: true
```

## `prepare_run`

`prepare_run`: an extra command to run before running a linter.

## `read_output_from`

`read_output_from`: Tell parser where to expect output from for reading. Should
be one of `stdout`, `stderr`, and `tmp_file`.
[See Output Sources](output-types.md#output-sources)

## `run`

`run`: The command to run a linter. This command can use variables provided at
runtime such as `$plugin}` and `$target}`. [Full list of variables](README.md#template-variables).
See [Run](README.md#run) for more details.

Examples:

Dart format command:
[full source](https://github.com/trunk-io/plugins/blob/main/linters/dart/plugin.yaml)

```yaml
lint:
  files:
    - name: dart
      extensions: [dart]
  definitions:
    - name: dart
      main_tool: dart
      commands:
        - name: format
          output: rewrite
          run: dart format ${target}
```

## `run_from`

`run_from`: What current working directory to run the linter from. See [Working Directory](README.md#working-directory) for more details.

## `run_when`

`run_when`: When this command should be run. One of `cli`, `lsp`, `monitor`, or `ci`.

## `std_in`

`std_in`: *optional boolean*. Should the command be fed the file on standard input?

## `success_codes`

`success_codes:` List of exit codes that indicates linter ran successfully. **This is unrelated to
whether or not there were issues reported by the linter**

## `target`

`target`, *optional string*, What target does this run on. By default, the target is the modified
source code file. Some linters operate on a whole repo or directory.  See [Input Target](README.md#input-target) for more details

## `version`

`version`: *optional string*, Version constraint.  

[//]: # (TODO: link to deeper explanation of version constraints with example)

