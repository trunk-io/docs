# Commands

A command is the fundamental unit of linters. It defines specifically _what binary and arguments_ are used to run the linter. A linter can have multiple commands in case it has multiple behaviors (ex: lint and format), but it must have at least one.

## run

The `run` property is the command to actually run a linter. This command can use [variables](./#template-variables) provided by the runtime such as `${plugin}` and `${target}`.

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

We use the same template syntax for `environment` as we do for [`command`](./#commands).

## Output Types and Parsing

The output of a command should be in one of the supported output types like [SARIF](output-types.md#sarif) or something that can be parsed with a [regex](output-types.md#regex). See [Output Types](output-types.md) for more details. If the standard output types do not meet your needs, you can also create a [custom parser](custom-parsers.md).

## Other properties

Other less commonly used properties of commands can be found in the [Command Field Reference](definition.md).
