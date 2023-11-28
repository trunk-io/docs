# Custom Linters

The beautiful thing about `trunk` is that you can leverage our caching and hold-the-line solution with your own custom linters; you just need to tell us how to interpret the results from your linter.

Trunk currently supports the following types of additional/proprietary linters:

<table data-header-hidden><thead><tr><th width="173.33333333333331"></th><th width="131" align="center"></th><th></th></tr></thead><tbody><tr><td>Linter Type</td><td align="center">Autofix<br>support</td><td>Description</td></tr><tr><td><a href="custom-linters.md#sarif"><code>sarif</code></a></td><td align="center">✓</td><td>Produces diagnostics as <a href="https://docs.oasis-open.org/sarif/sarif/v2.0/sarif-v2.0.html">Static Analysis Results Interchange Format</a> JSON.</td></tr><tr><td><a href="custom-linters.md#lsp-json"><code>lsp_json</code></a></td><td align="center"></td><td>Produces diagnostics as <a href="https://microsoft.github.io/language-server-protocol/">Language Server Protocol</a> JSON.</td></tr><tr><td><a href="custom-linters.md#pass-fail-linters"><code>pass_fail</code></a></td><td align="center"></td><td>Writes a single file-level diagnostic to <code>stdout</code>.</td></tr><tr><td><a href="custom-linters.md#regex"><code>regex</code></a></td><td align="center"></td><td>Produces diagnostics using a custom regex format.</td></tr><tr><td><a href="custom-linters.md#arcanist"><code>arcanist</code></a></td><td align="center">✓</td><td>Produces diagnostics as Arcanist JSON.</td></tr><tr><td><a href="custom-linters.md#formatters"><code>rewrite</code></a></td><td align="center">✓</td><td>Writes the formatted version of a file to <code>stdout</code>.</td></tr></tbody></table>

If your linter produces a different output type, you can also write a [parser](custom-parsers.md) to transform the linter's output into something trunk can understand.

To set up a custom linter, add it to `trunk.yaml` under `lint > definitions` and enable it:

```yaml
lint:
  definitions:
    - name: foo
      files: [ALL]
      commands:
        - output: sarif
          success_codes: [0, 1]
          run: ${workspace}/bin/foo --file ${target}
          read_output_from: stdout
  enabled:
    # ...
    - foo@SYSTEM
```

The `@SYSTEM` is a special identifier that indicates that we will forward the `PATH` environment variable to the custom linter when we invoke it.

Every custom linter must specify a name, the types of files it will run on, at least one command, and `success_codes` or `error_codes`.

> Info: Entries in `enabled` must specify both a linter name and a version. If you commit your linter into\
> your repository, you should simply use `@SYSTEM`, which will run the linter with your shell's\
> `PATH`. If you have a versioned release pipeline for your linter, though, you'll want to define your\
> custom linter using a [`download`](custom-linters.md#downloads) and specify the download version to use.

### Execution Model

Running `trunk check` tells `trunk` to do the following:

* compute the set of modified files (by comparing the current working tree and `upstream-ref`,\
  usually your `main` or `master` branch)
* compute the set of lint actions to run based on the modified files
  * each enabled linter is invoked once per applicable modified file ([details](custom-linters.md)); for\
    example, if `pylint` and `flake8` are enabled, they will both be run on every modified `python`\
    file but not on any modified `markdown` files
  * every lint action also will have a corresponding _upstream_ lint action, i.e. the linter will\
    also be run on the upstream version of the file, so that we can determine which issues already\
    exist in your repository
* execute uncached lint actions
* determine which lint issues are new, existing, or fixed

### Linter Types

#### SARIF

`output: sarif` linters produce diagnostics in the [Static Analysis Results Interchange Format](https://docs.oasis-open.org/sarif/sarif/v2.0/sarif-v2.0.html):

```json
{
  "$schema": "https://raw.githubusercontent.com/oasis-tcs/sarif-spec/master/Schemata/sarif-schema-2.1.0.json",
  "version": "2.1.0",
  "runs": [
    {
      "results": [
        {
          "level": "warning",
          "locations": [
            {
              "physicalLocation": {
                "artifactLocation": {
                  "uri": "/dev/shm/sandbox/detekt_test_repo/example.kt"
                },
                "region": {
                  "startColumn": 12,
                  "startLine": 18
                }
              }
            }
          ],
          "message": {
            "text": "A class should always override hashCode when overriding equals and the other way around."
          },
          "ruleId": "detekt.potential-bugs.EqualsWithHashCodeExist"
        }
      ],
      "tool": {
        "driver": {
          "downloadUri": "https://github.com/detekt/detekt/releases/download/v1.19.0/detekt",
          "fullName": "detekt",
          "guid": "022ca8c2-f6a2-4c95-b107-bb72c43263f3",
          "informationUri": "https://detekt.github.io/detekt",
          "language": "en",
          "name": "detekt",
          "organization": "detekt",
          "semanticVersion": "1.19.0",
          "version": "1.19.0"
        }
      }
    }
  ]
}
```

#### LSP JSON

`output: lsp_json` linters output issues as [Language Server Protocol](https://microsoft.github.io/language-server-protocol/specification#diagnostic) JSON.

```json
[
  {
    "message": "Not formatted correctly. Missing owner",
    "code": "missing-owner",
    "severity": "Error",
    "range": {
      "start": {
        "line": 12,
        "character": 8
      },
      "end": {
        "line": 12,
        "character": 12
      }
    }
  },
  {
    "message": "TODO is assigned to someone not listed in this project",
    "code": "unknown-user",
    "severity": "Warning",
    "range": {
      "start": {
        "line": 37,
        "character": 0
      },
      "end": {
        "line": 37,
        "character": 14
      }
    }
  }
]
```

#### Pass/Fail Linters

`output: pass_fail` linters find either:

* no issues in a file, indicated by exiting with `exit_code=0`, or
* a single file-level issue in a file, whose message is the linter's `stdout`, indicated by exiting\
  with `exit_code=1`.

> Note: Exiting with `exit_code=1` but writing nothing to `stdout` is considered to be a linter tool failure.
>
> Note: `pass_fail` linters are required to have `success_codes: [0, 1]`

#### Regex

`output: regex` linters produce output that can be parsed with custom regular expressions and named capture groups. The regular expression is specified in the `parse_regex` field.

`regex` supports capturing strings from a linter output for the following named capture groups:

* `path`: file path (required)
* `line`: line number
* `col`: column number
* `severity`: one of `allow`, `deny`, `disabled`, `error`, `info`, `warning`
* `code`: linter diagnostic code
* `message`: description

For example, the output

```
.trunk/trunk.yaml:7:81: [error] line too long (82 > 80 characters) (line-length)
```

can be parsed with the regular expression

```
((?P<path>.*):(?P<line>\d+):(?P<col>\d+): \[(?P<severity>.*)\] (?P<message>.*) \((?P<code>.*)\))
```

and would result in a `trunk` diagnostic that looks like this:

```
7:81  high    line too long (82 > 80 characters)      regex-linter/line-length
```

In the event that multiple capture groups of the same name are specified, the nonempty capture will be preferred. If there are multiple non-empty captures, a linter error will be thrown. Adjust your regular expression accordingly to match the specifics of your output.

> Note: For additional information on building custom regular expressions, see [re2](https://github.com/google/re2/wiki/Syntax). More complicated regex may require additional escape characters in yaml configuration.

#### Arcanist

You can also output JSON using the Arcanist format.

```json
[
  {
    "Char": 1,
    "Code": "missing_copyright",
    "Description": "Message about things\nMaybe contain multiple lines and web\nlinks\nhttps://website.com/notice-about-stuff\n",
    "Line": 1,
    "Name": "Incorrect (or missing) copyright notice",
    "OriginalText": "",
    "Path": "somefile.py"
  }
]
```

#### Formatters

`output: rewrite` linters write the formatted version of a file to `stdout`; this becomes an autofix which `trunk` can prompt you to apply (which is what `trunk check` does by default) or automatically apply for you (if you `trunk check --fix` or `trunk fmt`).

For example, if you wanted a linter to normalize your line endings, you could do this:

```yaml
lint:
  definitions:
    - name: no-carriage-returns
      files: [ALL]
      commands:
        - output: rewrite
          formatter: true
          command: sed s/\r// ${target}
          success_codes: [0]
```

Setting `formatter: true` will cause `trunk fmt` to run this linter.

### Configuration Options

When defining a custom linter, `trunk` not only needs to know the output of the linter command but also details such as how to invoke it, how to specify the file to check, and more; the next few sections explain what options you use to configure these and how:

For even more details, you can refer to [the JSON schema for `trunk.yaml`](https://static.trunk.io/pub/trunk-yaml-schema.json).

#### Applicable filetypes

To determine which linters to run on which files (i.e. compute the set of lint actions), `trunk` requires that every linter define the set of filetypes it applies to in `files`.

We have a number of pre-defined filetypes (e.g. `c++-header`, `gemspec`, `rust`; see our [configuration schema](https://static.trunk.io/pub/trunk-yaml-schema.json) for an up-to-date list), but you can also define your own filetypes. Here's how we define the `python` filetype:

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

This tells `trunk` that files matching either of the following criteria should be considered `python` files:

* the extension is any of `.py`, `.py2`, or `.py3` (e.g. `lib.py`)
* the shebang is any of `python` or `python3` (e.g. `#!/usr/bin/env python3`)

#### Command

Once `trunk` has figured out which linters it will run on which files, `trunk` expands the template provided in the `run` field to determine the arguments it will invoke the linter with. Here's what that looks like for `detekt`, one of our Kotlin linters:

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

This command template contains all the information `trunk` needs to execute `detekt` in a way where `trunk` will be able to understand `detekt`'s output.

Note that some of the fields in this command template contain `${}` tokens: these tokens are why `command` is a template and are replaced at execution time with the value of that variable within the context of the lint action being executed.

| Variable          | Description                                                                   |
| ----------------- | ----------------------------------------------------------------------------- |
| `${workspace}`    | Path to the root of the repository                                            |
| `${target}`       | Path to the file to check, relative to `${workspace}`                         |
| `${linter}`       | Path to the directory the linter was downloaded to                            |
| `${runtime}`      | Path to the directory the runtime (e.g. `node`) was downloaded to             |
| `${upstream-ref}` | Upstream git commit that is being used to calculate new/existing/fixed issues |

#### Input

The `target` field specifies what paths this linter will run on given an input file. It may be a\
literal such a `.` which will run the linter on the whole repository. It also supports various\
substitutions:

| Variable                         | Description                                                                                                                                      |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `${file}`                        | The input file.                                                                                                                                  |
| `${parent}`                      | The folder containing the file.                                                                                                                  |
| `${parent_with(<name>)}`         | Walks up toward the repository root looking for the first folder containing `<name>`. If `<name>` is not found, do not run any linter.           |
| `${root_or_parent_with(<name>)}` | Walks up toward the repository root looking for the first folder containing `<name>`. If `<name>` is not found, evaluate to the repository root. |

If `target` is not specified it will default to `${file}`.

This target may be referenced in the `run` field as `${target}`.

```yaml
lint:
  definitions:
    - name: noop
      files: [ALL]
      commands:
        - output: rewrite
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
        - output: rewrite
          formatter: true
          run: cat -
          stdin: true
```

> Info: Linters that take their input via `stdin` may still want to know the file's path so that they can, say, generate >diagnostics with the file's path. In these cases you can still use `${target}` in `run`.

#### Output

The output format that `trunk` expects from a linter is determined by its [`type`](custom-linters.md#linter-types).

**`stdout`, `stderr` or `tmp_file`**

`trunk` generally expects a linter to output its findings to `stdout`, but does support other output mechanisms:

| `read_output_from` | Description                                                                       |
| ------------------ | --------------------------------------------------------------------------------- |
| `stdout`           | Standard output.                                                                  |
| `stderr`           | Standard error.                                                                   |
| `tmp_file`         | If `${tmpfile}` was specified in `command`, the path of the created `${tmpfile}`. |

#### **Exit codes**

Linters often use different exit codes to categorize the outcome. For instance, [`markdownlint`](https://github.com/igorshubovych/markdownlint-cli#exit-codes) uses `0` to indicate that no issues were found, `1` to indicate that the tool ran successfully but issues were found, and `2`, `3`, and `4` for tool execution failures.

`trunk` supports specifying either `success_codes` or `error_codes` for a linter:

* if `success_codes` are specified, `trunk` expects a successful linter invocation (which may or may\
  not find issues) to return one of the specified `success_codes`;
* if `error_codes` are specified, `trunk` expects a successful linter invocation to return any exit\
  code which is _not_ one of the specified `error_codes`.

`markdownlint`, for example, has `success_codes: [0, 1]` in its configuration.

#### **Working directory**

`run_from` determines what directory a linter command is run from.

<table data-header-hidden><thead><tr><th width="415"></th><th></th></tr></thead><tbody><tr><td><code>run_from</code></td><td>Description</td></tr><tr><td><code>&#x3C;path></code> (<code>.</code> by default)</td><td>Explicit path to run from</td></tr><tr><td><code>${parent}</code></td><td>Parent of the target file; e.g. would be <code>foo/bar</code> for <code>foo/bar/hello.txt</code></td></tr><tr><td><code>${root_or_parent_with(&#x3C;file>)}</code></td><td>Nearest parent directory containing the specified file</td></tr><tr><td><code>${root_or_parent_with_dir(&#x3C;dir>)}</code></td><td>Nearest parent directory containing the specified directory</td></tr><tr><td><code>${root_or_parent_with_regex(&#x3C;regex>)}</code></td><td>Nearest parent directory containing a file or directory matching specified regex</td></tr><tr><td><code>${target_directory}</code></td><td>Run the linter from the same directory as the target file, and change the target to be <code>.</code></td></tr><tr><td><code>${compile_command}</code></td><td>Run from the directory where <code>compile_commands.json</code> is located</td></tr></tbody></table>

#### **Limiting concurrency**

If you would like to limit the number of times trunk will invoke a linter concurrently, then you can use the `maximum_concurrency` option. For example, setting `maximum_concurrency: 1` will limit trunk from running more than one instance of the linter simultaneously.

#### **Environment variables**

`trunk` by default runs linters _without_ environment variables from the parent shell; however, most linters need at least some such variables to be set, so `trunk` allows specifying them using `environment`; for example, the `environment` for `ktlint` looks like this:

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

We use the same template syntax for `environment` as we do for [`command`](custom-linters.md#command).

### Tools

You can use the `tools` section to specify trunk-configured binaries that the linter uses to run. The `tools` key should specify a list of strings referring to tool names. We have two kinds of tool dependencies - they are described in turn below. See the [Tools Configuration](tools/configuration.md) page for more details on how to set up your tools.

This is the preferred way of defining and versioning a linter, as it also allows repo users to conveniently run the linter binary outside of the `trunk check` context.

#### Eponymous Tool Dependencies

Here is an example of where the tool matches the linter name:

```yaml
tools:
  definitions:
    - name: pylint
      runtime: python
      package: pylint
      shims: [pylint]
      known_good_version: 2.11.1
lint:
  definitions:
    - name: pylint
      files: [python]
      commands:
        - name: lint
          # Custom parser type defined in the trunk cli to handle pylint's JSON output.
          output: pylint
          run: pylint --exit-zero --output ${tmpfile} --output-format json ${target}
          success_codes: [0]
          read_output_from: tmp_file
          batch: true
          cache_results: true
      tools: [pylint]
      suggest_if: config_present
      direct_configs:
        - pylintrc
        - .pylintrc
      affects_cache:
        - pyproject.toml
        - setup.cfg
      issue_url_format: http://pylint-messages.wikidot.com/messages:{}
      known_good_version: 2.11.1
      version_command:
        parse_regex: pylint ${semver}
        run: pylint --version
```

In this case, the tool name (`pylint`) matches that of the linter, making it an _eponymous tool_. Eponymous tools need to be defined separately from the linter but implicitly enabled with the linter's version. You may explicitly enable the eponymous tool if you wish, but note that its version needs to be synced to that of the linter.

#### Additional Tool Dependencies

You can also have a scenario where a linter depends on a tool that is not identically named - an _additional tool dependency_. We give an example below:

```yaml
tools:
  definitions:
    - name: terragrunt
      known_good_version: 0.45.8
      download: terragrunt
      shims:
        - name: terragrunt
          target: terragrunt
lint:
  definitions:
    - name: terragrunt
      tools: [terragrunt, terraform]
      known_good_version: 0.45.8
      files: [hcl]
      suggest_if: never
      environment:
        - name: PATH
          list: ["${linter}"]
      commands:
        - name: format
          output: rewrite
          run: terragrunt hclfmt ${target}
          success_codes: [0]
          sandbox_type: copy_targets
          in_place: true
          formatter: true
          batch: true
      version_command:
        parse_regex: terragrunt v${semver}
        run: terragrunt -version
```

In this scenario, `terraform` is an additional tool dependency - `terragrunt` requires it to be in `$PATH`. If the tool is an additional dependency, it must be enabled explicitly and versioned independently of the linter - that is, it must be listed in the `tools.enabled` section.

#### Downloads

**(NOTE: This method of specifying linters is still supported, but using `tools` like specified** [**above**](custom-linters.md#tools) **is recommended going forward)**

If your custom linter has a separate release process (i.e. is not committed in your repo), then you can tell `trunk` how to download it like so:

```yaml
lint:
  downloads:
    - name: lorem-linter
      # the default version to download; overridden by the version in `enabled`
      version: 4.0.1
      executable: true
      downloads:
        - os: linux
          cpu: x86_64
          url: https://github.com/my-org/my-repo/releases/download/${version}/lorem-darwin-x86-64
        - os: macos
          cpu: x86_64
          url: https://github.com/my-org/my-repo/releases/download/${version}/lorem-linux-x86-64
    - name: ipsum-linter
      # the default version to download; overridden by the version in `enabled`
      version: 0.1.1
      downloads:
        - os: linux
          cpu: x86_64
          url: https://github.com/my-org/my-repo/releases/download/${version}/ipsum-darwin-x86-64.tar.gz
          strip_components: 2
        - os: macos
          cpu: x86_64
          url: https://github.com/my-org/my-repo/releases/download/${version}/ipsum-linux-x86-64.tar.gz
          strip_components: 2
  definitions:
    - name: lorem-linter
      files: [javascript, typescript]
      download: lorem-linter
    - name: ipsum-linter
      files: [rust]
      download: ipsum-linter
  enabled:
    - lorem-linter@4.0.2
    - ipsum-linter@0.1.6
```

This tells `trunk` that, for `lorem-linter`:

* you want to run version `4.0.2` on `javascript` and `typescript` files,
* it is available for macOS and Linux at the specified URLs (expanded by replacing `${version}` with\
  `4.0.2`), and
* the download consists of a single executable binary, since `executable: true` is set;

for `ipsum-linter`:

* you want to run version `0.1.6` on `rust` files,
* it is available for macOS and Linux at the specified URLs (expanded by replacing `${version}` with\
  `0.1.6`), and
* the download is a compressed archive, the linter binary is `strip_components: 2` directories deep\
  inside the uncompressed archive, and `trunk` should automatically extract and unpack the linter\
  from the archive.

#### Download via package manager

If your linter can be downloaded via `gem install`, `go get`, `npm install`, or `pip install`, you can specify a `runtime` and the `package` key:

```yaml
lint:
  definitions:
    - name: fizz-buzz
      files: [javascript]
      # npm install fizz-buzz
      runtime: node
      package: fizz-buzz
```

This will now create a hermetic directory in `~/.cache/trunk/linters/fizz-buzz` and `npm install fizz-buzz` there. You can refer to different versions of your package in `trunk.yaml` as normal, via `fizz-buzz@1.2.3`.

> Note: Such downloads will use the _hermetic_ version of the specified runtime that `trunk` installs, not the one >you've installed on your machine.

#### `run_when`

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
