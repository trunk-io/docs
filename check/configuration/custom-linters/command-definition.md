
## Linter Command Definition

The linter command definitions are defined in `lint.definitions.commands`. A single linter can have 
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

`run`: The command to run a linter. This command can use variables provided at
runtime such as `$plugin}` and `$target}`. [Full list of variables](./commands.md#template-variables)

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

### `files`

`files` is a list of file types listed in the `lint.files` section that this linter applies to.

Example: **prettier**
[full source](https://github.com/trunk-io/plugins/blob/main/linters/prettier/plugin.yaml)

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


### `run_when`

`run_when`: When this command should be run. One of `cli`, `lsp`, `monitor`, or `ci`.

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

`read_output_from`: Tell parser where to expect output from for reading. Should
be one of `stdout`, `stderr`, and `tmp_file`. 
[See Output Sources](output-types.md#output-sources)

### `run_from`

`run_from`: What current working directory to run the linter from. 

[//]: # (TODO: **link to section with more  examples**.)

### `batch`

`batch`: *optional boolean*. Combine multiple files into the same execution.
If true, the `${target}` template substitution in the `run`
field may expand into multiple files.

### `in_place`

`in_place`: *optional boolean*. Indicates that this formatter will
rewrite the file in place **Only applies to formatters**.

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

`idempotent`: *optional boolean*. Indicates whether a linter is idempotent with config and source code inputs. For example, semgrep fetches rules from the internet, so it is not idempotent . If set, will only cache results a duration of `cache_ttl`.

### `cache_ttl`

`cache_ttl`, *duration string*. If this linter is not [idempotent](#idempotent), this is how long cached results are kept before they expire. Defaults to 24hrs.

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

