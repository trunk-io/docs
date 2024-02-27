---
description: Linter Integration overview
---

# Linter Integration

Trunk Check's linter integrations are fully configurable. This means that you can easily tune 
existing linters or leverage our caching and [hold-the-line](../../reference/under-the-hood.
md#hold-the-line) solution with your own custom linters. Every part of a linter config is set 
through YAML properties that can be adjusted or overridden.

See also:
* [Creating a custom linter from scratch](https://trunk.io/blog/integrating-your-own-custom-tools-with-trunk-check).
* [Complete Linter Configuration Reference](./reference.md)

## Execution Model

Running `trunk check` tells `trunk` to do the following:

* Compute the set of modified files (by comparing the current working tree and `upstream-ref`,  usually your `main` or `master` branch).
* Compute the set of lint actions to run based on the modified files.
  * Each enabled linter is invoked once per [applicable modified file](./#applicable-filetypes); for example, if `pylint` and `flake8` are enabled, they will both be run on every modified `python` file but not on any modified `markdown` files.
  * Every lint action also will have a corresponding _upstream_ lint action (i.e. the linter will also be run on the upstream version of the file, so that we can determine which issues already exist in your repository).
* [Download](./#making-installs-hermetic) and install any newly enabled linters/formatters.
* Execute uncached lint actions.
* Parse linter [outputs](./#output-types) into configurable output types.
* Determine which lint issues are new, existing, or fixed.


## Applicable filetypes

To determine which linters to run on which files (i.e. compute the set of lint actions), Trunk 
requires that every linter define the set of filetypes it applies to in `files` section.

We have a number of pre-defined filetypes (e.g. `c++-header`, `gemspec`, `rust`; see our 
[plugins repo](https://github.com/trunk-io/plugins/blob/main/linters/plugin.yaml) for an 
up-to-date list), but you can also define your own filetypes. Here's how we define the `python` 
filetype:


```yaml
lint:
  files:
    - name: python
      extensions:
        - py
        - py2
        - py3
      shebangs:
        - python
        - python3
```

This tells Trunk that files matching either of the following criteria should be considered 
`python` files:

* the extension is any of `.py`, `.py2`, or `.py3` (e.g. `lib.py`)
* the shebang is any of `python` or `python3` (e.g. `#!/usr/bin/env python3`)

## Input Sources

The `target` field specifies what paths this linter will run on given an input file. It may be a 
literal such a `.` which will run the linter on the whole repository. It also supports various 
substitutions:

| Variable                         | Description                                                                                                                                       |
|----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| `${file}`                        | The input file.                                                                                                                                   |
| `${parent}`                      | The folder containing the file.                                                                                                                   |
| `${parent_with(<name>)}`         | Walks up toward the repository root looking for the first folder containing `<name>`. If `<name>` is not found, do not run any linter.            |
| `${root_or_parent_with(<name>)}` | Walks up toward the repository root looking for the first folder containing `<name>`. If `<name>` is not found, evaluate to the repository root.  |


If `target` is not specified it will default to `${file}`.

This target may be referenced in the `run` field as `${target}`.

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

## Commands

Once Trunk has figured out which linters it will run on which files, Trunk expands the template 
provided in the `run` field to determine the arguments it will invoke the linter with. Here's 
what that looks like for `detekt`, one of our Kotlin linters:

```yaml
lint:
  definitions:
    - name: detekt
      # ...
      commands:
        - output: sarif
          run:
            detekt-cli --build-upon-default-config --config .detekt.yaml --input ${target} --report
            sarif:${tmpfile}
```

This command template contains all the information Trunk needs to execute `detekt` in a way
where Trunk will be able to understand `detekt`'s output. For more details see the [commands](commands.md) page.

## Environment variables

Trunk by default runs linters _without_ environment variables from the parent shell; however, 
most linters need at least some such variables to be set, so Trunk allows specifying them using 
`environment`; for example, the `environment` for `ktlint` looks like this:

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

Most `environment` entries are maps with `name` and `value` keys; these become `name=value` 
environment variables. For `PATH`, we allow specifying `list`, in which case we concatenate the 
entries with `:`.

We use the same template syntax for `environment` as we do for [`command`](./commands.md).

## Outputs

### Output Sources

The source of the output will be one of `stdout`, `stderr` or `tmp_file`. `trunk` generally 
expects a linter to output its findings to `stdout`, but does support other output mechanisms. 
See [Output Sources](output-types.md#output-sources)

### Output Types

The output format that Trunk expects from a linter is determined by its [`output`](output-types.md)
type. Trunk currently supports the following output types:

| Output Type                            | Autofix support | Description                                                                                                                              |
|----------------------------------------|-----------------|------------------------------------------------------------------------------------------------------------------------------------------|
| [Sarif](output-types.md#sarif)         | ✓               | Produces diagnostics as [Static Analysis Results Interchange Format](https://docs.oasis-open.org/sarif/sarif/v2.0/sarif-v2.0.html) JSON. |
| [lsp_json](output-types.md#lsp_json)   |                 | Produces diagnostics as [Language Server Protocol](https://microsoft.github.io/language-server-protocol/) JSON.                          |
| [pass_fail](output-types.md#pass_fail) |                 | Writes a single file-level diagnostic to <code>stdout</code>                                                                             |
| [regex](output-types.md#regex)         |                 | Produces diagnostics using a custom regex format.                                                                                        |
| [arcanist](output-types.md#arcanist    | ✓               | Produces diagnostics as Arcanist JSON                                                                                                    |
| [rewrite](output-types.md#formatters)  | ✓               | Writes the formatted version of a file to <code>stdout</code>.                                                                           |


If your linter produces a different output type, you can also write a [parser](custom-parsers.md)
to transform the linter's output into something Trunk can understand.

To set up a new linter,, add it to `trunk.yaml` under `lint.definitions` and enable it:

```yaml
lint:
  definitions:
    - name: foo
      files: [ALL]
      commands:
        - name: lint
          output: sarif
          success_codes: [0, 1]
          run: ${workspace}/bin/foo --file ${target}
          read_output_from: stdout
  enabled:
    # ...
    - foo@SYSTEM
```

The `@SYSTEM` is a special identifier that indicates that we will forward the `PATH` environment 
variable to the custom linter when we invoke it.

Every custom linter must specify a name, the types of files it will run on, at least one command,
and `success_codes` or `error_codes`.

> Info: Entries in `enabled` must specify both a linter name and a version. If you commit your 
> linter into your repository, you should simply use `@SYSTEM`, which will run the linter with 
> your shell's > `PATH`. If you have a versioned release pipeline for your linter, though, 
> you'll want to define your > custom linter using a [`download`](./#downloads) and specify the 
> download version to use.

## Exit codes

Linters often use different exit codes to categorize the outcome. For instance, [`markdownlint`](https://github.com/igorshubovych/markdownlint-cli#exit-codes) uses `0` to indicate that no issues were found, `1` to indicate that the tool ran successfully but issues were found, and `2`, `3`, and `4` for tool execution failures.

Trunk supports specifying either `success_codes` or `error_codes` for a linter:

* if `success_codes` are specified, Trunk expects a successful linter invocation (which may or may not find issues) to return one of the specified `success_codes`;
* if `error_codes` are specified, Trunk expects a successful linter invocation to return any exit\
  code which is _not_ one of the specified `error_codes`.

`markdownlint`, for example, has `success_codes: [0, 1]` in its configuration.

## Working directory

`run_from` determines what directory a linter command is run from.

| `run_from`                                    | Description                                                                                |
|-----------------------------------------------|--------------------------------------------------------------------------------------------|
| &lt;path&gt; (`.` by default)                 | Explicit path to run from.                                                                 |
| `${parent}`                                   | Parent of the target file; e.g. would be `foo/bar` for `foo/bar/hello.txt`                 |
| `${root_or_parent_with(&gt;file&lt;)}`        | Nearest parent directory containing the specified file                                     |
| `${root_or_parent_with_dir(&lt;dir&gt;)}`     | Nearest parent directory containing the specified directory                                |
| `${root_or_parent_with_regex(&lt;regex&gt;)}` | Nearest parent directory containing a file or directory matching specified regex           |
| `${root_or_parent_with_direct_config}`        | Nearest parent directory containing a file from `direct_configs`                           |
| `${root_or_parent_with_any_config}`           | Nearest parent directory containing a file from `affects_cache` or `direct_configs.        |
| `${target_directory}`                         | Run the linter from the same directory as the target file, and change the target to be `.` |
| `${compile_command}`                          | Run from the directory where `compile_commands.json` is located. |

## Limiting concurrency

If you would like to limit the number of times trunk will invoke a linter concurrently, then you can use the `maximum_concurrency` option. For example, setting `maximum_concurrency: 1` will limit Trunk from running more than one instance of the linter simultaneously.

## When to Run

Lint sessions are always associated with exactly one of the following session types:

* `ci`: triggered by a `CI` run, i.e. `trunk check --ci` or when running inside the GitHub action,
* `cli`: triggered by a human or script running `trunk check`,
* `lsp`: triggered by VSCode, or
* `monitor`: triggered by background linting.

You can use `run_when` to specify which session types you want to run a linter in; for example, to always disable a linter during CI:

```yaml
lint:
  definitions:
    - name: fizz-buzz
      run_when: [cli, lsp, monitor]
```

## Downloading Binaries and Dependencies

All linters are composed of external binaries or scripts that need to be downloaded from their source, along 
with any additional libraries, runtimes, or tools.  How a tool and it's dependencies are 
downloaded is a complex topic. See [Downloads and Dependencies](./dependencies.md) for the full 
details.
