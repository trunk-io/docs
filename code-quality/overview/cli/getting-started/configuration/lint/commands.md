# Commands

A command is the fundamental unit of linters. It defines specifically _what binary and arguments_ are used to run the linter. A linter can have multiple commands in case it has multiple behaviors (ex: lint and format), but it must have at least one.

## How Code Qualit Runs Linters

The `run` property is the command to actually run a linter. This command can use [variables](commands.md#template-variables) provided by the runtime such as `${plugin}` and `${target}`.

For example: this is the `run` field for **black**, one of our Python linters. The `run` field is set to `black -q ${target}`.

```yaml
version: 0.1
tools:
  definitions:
    - name: black
      runtime: python
      package: black[python2,jupyter]
      shims: [black]
      known_good_version: 22.3.0
lint:
  definitions:
    - name: black
      files: [python, jupyter, python-interface]
      commands:
        - name: format
          output: rewrite
          run: black -q ${target}
          success_codes: [0]
          batch: true
          in_place: true
          allow_empty_files: false
          cache_results: true
          formatter: true
      tools: [black]
      suggest_if: files_present
      affects_cache: [pyproject.toml]
      known_good_version: 22.3.0
      version_command:
        parse_regex: black, version (.*)
        run: black --version
```

This command template contains all the information Trunk needs to execute `black` in a way where Trunk will be able to understand `blacks`'s output.

## Input Target

The `target` field specifies what paths this linter will run on given an input file. It may be a string literal such as `.`, which will run the linter on the whole repository. It also supports various substitutions:

| Variable                         | Description                                                                                                                                      |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `${file}`                        | The input file.                                                                                                                                  |
| `${parent}`                      | The folder containing the file.                                                                                                                  |
| `${parent_with(<name>)}`         | Walks up toward the repository root looking for the first folder containing `<name>`. If `<name>` is not found, do not run any linter.           |
| `${root_or_parent_with(<name>)}` | Walks up toward the repository root looking for the first folder containing `<name>`. If `<name>` is not found, evaluate to the repository root. |

If `target` is not specified it will default to `${file}`.

This target may be referenced in the `run` field as `${target}`, as in the example above for **black**, or this simple example.

```yaml
lint:
  definitions:
    - name: noop
      files: [ALL]
      commands:
        - name: format
          output: rewrite
          formatter: true
          run: cat ${target}
```

or via `stdin`, by specifying `stdin: true`:

```yaml
lint:
  definitions:
    - name: noop
      files: [ALL]
      commands:
        - name: format
          output: rewrite
          formatter: true
          run: cat -
          stdin: true
```

> Note: Linters that take their input via `stdin` may still want to know the file's path so that they can, say, generate diagnostics with the file's path. In these cases you can still use `${target}` in `run`.

## Exit codes

Linters often use different exit codes to categorize the outcome. For instance, [`markdownlint`](https://github.com/igorshubovych/markdownlint-cli#exit-codes) uses `0` to indicate that no issues were found, `1` to indicate that the tool ran successfully but issues were found, and `2`, `3`, and `4` for tool execution failures.

Trunk supports specifying either `success_codes` or `error_codes` for a linter:

* if `success_codes` are specified, Trunk expects a successful linter invocation (which may or may not find issues) to return one of the specified `success_codes`;
* if `error_codes` are specified, Trunk expects a successful linter invocation to return any exit\
  code which is _not_ one of the specified `error_codes`.

`markdownlint`, for example, has `success_codes: [0, 1]` in its configuration.

**Note:** A linter command should set either success codes or error codes, but not both\*\*.\*\*

## Working directory

`run_from` determines what directory a linter command is run from.

<table><thead><tr><th width="415">run_from</th><th>Description</th></tr></thead><tbody><tr><td><code>&#x3C;path></code> (<code>.</code> by default)</td><td>Explicit path to run from</td></tr><tr><td><code>${parent}</code></td><td>Parent of the target file; e.g. would be <code>foo/bar</code> for <code>foo/bar/hello.txt</code></td></tr><tr><td><code>${root_or_parent_with(&#x3C;file>)}</code></td><td>Nearest parent directory containing the specified file</td></tr><tr><td><code>${root_or_parent_with_dir(&#x3C;dir>)}</code></td><td>Nearest parent directory containing the specified directory</td></tr><tr><td><code>${root_or_parent_with_regex(&#x3C;regex>)}</code></td><td>Nearest parent directory containing a file or directory matching specified regex</td></tr><tr><td><code>${root_or_parent_with_direct_config}</code></td><td>Nearest parent directory containing a file from <code>direct_configs</code></td></tr><tr><td><code>${root_or_parent_with_any_config}</code></td><td>Nearest parent directory containing a file from <code>affects_cache</code> or <code>direct_configs</code></td></tr><tr><td><code>${target_directory}</code></td><td>Run the linter from the same directory as the target file, and change the target to be <code>.</code></td></tr><tr><td><code>${compile_command}</code></td><td>Run from the directory where <code>compile_commands.json</code> is located</td></tr></tbody></table>

## Template Variables

Note that some of the fields in this command template contain `${}` tokens: these tokens are why `command` is a template and are replaced at execution time with the value of that variable within the context of the lint action being executed.

| Variable          | Description                                                                   |
| ----------------- | ----------------------------------------------------------------------------- |
| `${workspace}`    | Path to the root of the repository                                            |
| `${target}`       | Path to the file to check, relative to `${workspace}`                         |
| `${linter}`       | Path to the directory the linter was downloaded to                            |
| `${runtime}`      | Path to the directory the runtime (e.g. `node`) was downloaded to             |
| `${upstream-ref}` | Upstream git commit that is being used to calculate new/existing/fixed issues |
| `${plugin}`       | Path to the root of the plugin's repository                                   |

## Limiting concurrency

If you would like to limit the number of times trunk will invoke a linter concurrently, then you can use the `maximum_concurrency` option. For example, setting `maximum_concurrency: 1` will limit Trunk from running more than one instance of the linter simultaneously.

## Environment variables

Trunk by default runs linters _without_ environment variables from the parent shell; however, most linters need at least some such variables to be set, so Trunk allows specifying them using `environment`; for example, the `environment` for `ktlint` looks like this:

```yaml
lint:
  definitions:
    name: ktlint
    # ...
    environment:
      - name: PATH
        list: ["${linter}"]
      - name: LANG
        value: en_US.UTF-8
```

Most `environment` entries are maps with `name` and `value` keys; these become `name=value` environment variables. For `PATH`, we allow specifying `list`, in which case we concatenate the entries with `:`.

We use the same template syntax for `environment` as we do for [`command`](commands.md#commands).

## Output Types and Parsing

The output of a command should be in one of the supported output types like [SARIF](output.md#sarif) or something that can be parsed with a [regex](output.md#regex). See [See Output Types](commands.md#output-types-and-parsing) for more details. If the standard output types do not meet your needs, you can also create a [custom parser](output-parsing.md).

## Full Reference

The linter command definitions are defined in `lint.definitions.commands`. A single linter can have multiple commands if it is used in different ways.

_Note:_. If you define the executable to run here (the command definition), then you should _not_ define it also in the linter definition. Defining it here as a command is preferred.

## `allow_empty_files`

`allow_empty_files`: _optional boolean_. Skip linting empty files for this linter. Trunk will assume there are no linters if the file is empty.

## `batch`

`batch`: _optional boolean_. Combine multiple files into the same execution. If true, the `${target}` template substitution in the `run` field may expand into multiple files.

## `cache_ttl`

`cache_ttl`, _duration string_. If this linter is not [idempotent](commands.md#idempotent), this is how long cached results are kept before they expire. Defaults to 24hrs. See [Output Caching](../../caching.md) for more details.

## `cache_results`

`cache_results`: _optional boolean_. Indicates if this linter wants to cache results. See [Caching](files-and-caching.md) for more details.

## `disable_upstream`

`disable_upstream`: _optional boolean_, Whether this linter supports comparing against the upstream version of this file.

## `error_codes`

`error_codes`: List of exit codes this linter will return when it hit an internal failure and couldn't generate results. **A linter should set either success codes or error codes, but not both.** See also [`success_codes`](commands.md#success_codes).

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

`idempotent`: _optional boolean_. Indicates whether a linter is idempotent with config and source code inputs. For example, `semgrep` fetches rules from the Internet, so it is not idempotent . If set, will only cache results a duration of `cache_ttl`. See [Output Caching](files-and-caching.md) for more details.

## `is_security`

`is_security`: _optional boolean_. Whether findings from this command should be considered "security" or not. Allows this linter to be run with `--scope==security`. [See Command Line Options](../../../../../../merge-queue/managing-merge-queue/reference.md)

## `maximum_file_size`

`maximum_file_size`: _optional number_. The maximum file size in bytes for input files to the linter. If not specified, the [lint.default\_max\_file\_size](./#default_max_file_size) will be used.

## `max_concurrency`

`max_concurrency`: _optional integer_, The maximum number of processes that Trunk Code Quality will run concurrently for this linter. [See Limiting Concurrency](commands.md#limiting-concurrency)

## `name`

`name`: _string_. A unique name for this command (some tools expose multiple commands, format, lint, analyze, etc.).

## `no_issues_codes`

`no_issues_codes`: List of exit codes that Trunk will use to assume there were no issues without parsing the output.

## `output`

`output`: _string_. which type of output this linter produces. [See Output Types](commands.md#output-types-and-parsing).

## `parser`

`parser`: The definition of a parser that will transform the output of the linter into SARIF. Not needed if linter is already output SARIF. [See Output Types](commands.md#output-types-and-parsing)

## `parse_regex`

`parse_regex`: _string_. A regular expression used to support regex parsing. [See Regex output type](output.md#regex)

## `platforms`

`platforms`: A list of platforms this linter supports. (ex: `windows`, `macos`, `linux`). Linters using managed runtimes (node, python, etc.) can generally run cross-platform and do not need the `platforms` property set. For tools which _are_ platform specific or which have different configuration for each platform, this property can be used to distinguish between them. When multiple command definitions have the same name, Trunk Check will pick the first one that matches the `platforms` setting.

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

`read_output_from`: Tell parser where to expect output from for reading. Should be one of `stdout`, `stderr`, and `tmp_file`. [See Output Sources](output.md#output-sources)

## `run`

`run`: The command to run a linter. This command can use variables provided at runtime such as `$plugin}` and `$target}`. [Full list of variables](commands.md#template-variables). See [Run](commands.md#how-code-qualit-runs-linters) for more details.

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

`run_from`: What current working directory to run the linter from. See [Working Directory](commands.md#working-directory) for more details.

## `run_when`

`run_when`: When this command should be run. One of `cli`, `lsp`, `monitor`, or `ci`.

## `std_in`

`std_in`: _optional boolean_. Should the command be fed the file on standard input?

## `success_codes`

`success_codes:` List of exit codes that indicates linter ran successfully. **This is unrelated to whether or not there were issues reported by the linter**.

**Note:** a linter should set either success codes or error codes, but not both. See also [`error_codes`](commands.md#error_codes).

## `target`

`target`, _optional string_, What target does this run on. By default, the target is the modified source code file, `${file}`. Some linters operate on a whole repo or directory. See [Input Target](commands.md#input-target) for more details.

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

`version`: _optional string_, Version constraint. When a linter has multiple commands with the same name, Trunk Code Quality will select the first command that matches the version constraint. This is useful for when multiple incompatible versions of a tool need to be supported.

Example: the `ruff` linter changed a command line argument from `--format` to `--output-format` in version `v0.1.0`. To handle both versions, the linter defines two commands with different version attributes. The first is for version `>=0.1.0`. If the first is not matched (because the install version of run is less that 0.1.0) then Trunk Code Quality will move on to the next command until it finds a match. [Full source](https://github.com/trunk-io/plugins/blob/main/linters/ruff/plugin.yaml).

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
