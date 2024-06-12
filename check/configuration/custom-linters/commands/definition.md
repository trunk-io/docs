---
description: Guide to every field in the command section of trunk.yaml
---

# Field Reference

The linter command definitions are defined in `lint.definitions.commands`. A single linter can have multiple commands if it is used in different ways.

_Note:_. If you define the executable to run here (the command definition), then you should _not_ define it also in the linter definition. Defining it here as a command is preferred.

## `allow_empty_files`

`allow_empty_files`: _optional boolean_. Skip linting empty files for this linter. Trunk will assume there are no linters if the file is empty.

## `batch`

`batch`: _optional boolean_. Combine multiple files into the same execution. If true, the `${target}` template substitution in the `run` field may expand into multiple files.

## `cache_ttl`

`cache_ttl`, _duration string_. If this linter is not [idempotent](definition.md#idempotent), this is how long cached results are kept before they expire. Defaults to 24hrs. See [Output Caching](../files.md#idempotency) for more details.

## `cache_results`

`cache_results`: _optional boolean_. Indicates if this linter wants to cache results. See [Caching](../files.md#caching) for more details.

## `disable_upstream`

`disable_upstream`: _optional boolean_, Whether this linter supports comparing against the upstream version of this file.

## `error_codes`

`error_codes`: List of exit codes this linter will return when it hit an internal failure and couldn't generate results. **A linter should set either success codes or error codes, but not both.** See also [`success_codes`](definition.md#success\_codes).

## `enabled`

`enabled`: _optional boolean_. Whether the command is enabled to run when the linter is run. Allows some commands of a linter to be run by default without others.

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

`fix_prompt`, _optional string._ e.g. 'Incorrect formatting' or 'Unoptimized image'. This string is used when prompting the user to use the linter interactively.

## `fix_verb`

`fix_verb`: _optional string_. This string is used when prompting the user to use the linter interactively. Example: `optimize`, `autoformat`, or `compress`.

## `formatter`

`formatter`: _optional boolean_. Whether this command is a formatter and should be included in `trunk fmt`.

## `in_place`

`in_place`: _optional boolean_. Indicates that this formatter will rewrite the file in place. **Only applies to formatters**.

## `idempotent`

`idempotent`: _optional boolean_. Indicates whether a linter is idempotent with config and source code inputs. For example, `semgrep` fetches rules from the Internet, so it is not idempotent . If set, will only cache results a duration of `cache_ttl`. See [Output Caching](../files.md#idempotency) for more details.

## `is_security`

`is_security`: _optional boolean_. Whether findings from this command should be considered "security" or not. Allows this linter to be run with `--scope==security`. [See Command Line Options](../../../advanced-setup/cli/cli-options.md)

## `maximum_file_size`

`maximum_file_size`: _optional number_. The maximum file size in bytes for input files to the linter. If not specified, the [lint.default\_max\_file\_size](../lint-config.md#default\_max\_file\_size) will be used.

## `max_concurrency`

`max_concurrency`: _optional integer_, The maximum number of processes that Trunk Check will run concurrently for this linter. [See Limiting Concurrency](./#limiting-concurrency)

## `name`

`name`: _string_. A unique name for this command (some tools expose multiple commands, format, lint, analyze, etc.).

## `no_issues_codes`

`no_issues_codes`: List of exit codes that Trunk will use to assume there were no issues without parsing the output.

## `output`

`output`: _string_. which type of output this linter produces. [See Output Types](output-types.md).

## `parser`

`parser`: The definition of a parser that will transform the output of the linter into SARIF. Not needed if linter is already output SARIF. [See Output Types](output-types.md)

## `parse_regex`

`parse_regex`: _string_. A regular expression used to support regex parsing. [See Regex output type](output-types.md#regex)

## `platforms`

`platforms`: A list of platforms this linter supports. (ex: `windows`, `macos`, `linux`). Linters using managed runtimes (node, python, etc.) can generally run cross-platform and do not need the `platforms` property set. For tools which _are_ platform specific or which have different configuration for each platform, this property can be used to distinguish between them.  When multiple command definitions have the same name, Trunk Check will pick the first one that matches the `platforms` setting.

For example, the `detekt` plugin has different exit codes for Windows than MacOS or Linux, and has two command definitions with different `success_codes` fields. [Full Source](https://github.com/trunk-io/plugins/blob/main/linters/detekt/plugin.yaml).

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
            detekt-cli --build-upon-default-config --config 
                .detekt.yaml --input ${target,} --report
            sarif:${tmpfile}
          success_codes: [0, 1, 2]
          read_output_from: tmp_file
          batch: true
          cache_results: true
        - name: lint
          output: sarif
          run:
            detekt-cli --build-upon-default-config --config 
                .detekt.yaml --input ${target,} --report
            sarif:${tmpfile}
          success_codes: [0, 2]
          read_output_from: tmp_file
          batch: true
          cache_results: true
```

## `prepare_run`

`prepare_run`: An extra command to run before running a linter.

## `read_output_from`

`read_output_from`: Tell parser where to expect output from for reading. Should be one of `stdout`, `stderr`, and `tmp_file`. [See Output Sources](output-types.md#output-sources)

## `run`

`run`: The command to run a linter. This command can use variables provided at runtime such as `$plugin}` and `$target}`. [Full list of variables](./#template-variables). See [Run](./#run) for more details.

`dart` `format` command: [full source](https://github.com/trunk-io/plugins/blob/main/linters/dart/plugin.yaml)

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

`run_from`: What current working directory to run the linter from. See [Working Directory](./#working-directory) for more details.

## `run_when`

`run_when`: When this command should be run. One of `cli`, `lsp`, `monitor`, or `ci`.

## `std_in`

`std_in`: _optional boolean_. Should the command be fed the file on standard input?

## `success_codes`

`success_codes:` List of exit codes that indicates linter ran successfully. **This is unrelated to whether or not there were issues reported by the linter**.

**Note:** a linter should set either success codes or error codes, but not both. See also [`error_codes`](definition.md#error\_codes).

## `target`

`target`, _optional string_, What target does this run on. By default, the target is the modified source code file, `${file}`. Some linters operate on a whole repo or directory. See [Input Target](./#input-target) for more details.

Examples:

**nancy** uses `.` as the target. [full source](https://github.com/trunk-io/plugins/blob/main/linters/nancy/plugin.yaml)

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

**tflint** uses `${parent}` as the target. [full source](https://github.com/trunk-io/plugins/blob/main/linters/tflint/plugin.yaml)

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

**Clippy** uses `${parent_with(Cargo.toml)}` as the target. [full source](https://github.com/trunk-io/plugins/blob/main/linters/clippy/plugin.yaml)

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

## `version`

`version`: _optional string_, Version constraint. When a linter has multiple commands with the same name, Trunk Check will select the first command that matches the version constraint. This is useful for when multiple incompatible versions of a tool need to be supported.

Example: the `ruff` linter changed a command line argument from `--format` to `--output-format` in version `v0.1.0`. To handle both versions, the linter defines two commands with different version attributes.  The first is for version `>=0.1.0`. If the first is not matched (because the install version of run is less that 0.1.0) then Trunk Check will move on to the next command until it finds a match.

&#x20;[Full source](https://github.com/trunk-io/plugins/blob/main/linters/ruff/plugin.yaml).

In this&#x20;

```yaml
lint:
  definitions:
    - name: ruff
      files: [python]
      commands:
        - name: lint
          # As of ruff v0.1.0, --format is replaced with --output-format
          version: ">=0.1.0"
          run: ruff check --cache-dir ${cachedir} --output-format json ${target}
          output: sarif
          parser:
            runtime: python
            run: python3 ${cwd}/ruff_to_sarif.py 0
          batch: true
          success_codes: [0, 1]
        - name: lint
          run: ruff check --cache-dir ${cachedir} --format json ${target}
          output: sarif
          parser:
            runtime: python
            run: python3 ${cwd}/ruff_to_sarif.py 1
          batch: true
          success_codes: [0, 1]


```

