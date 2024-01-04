# Custom Linters

Trunk Check's linter integrations are fully configurable. This means that you can easily tune existing linters or leverage our caching and [hold-the-line](../../under-the-hood.md#hold-the-line) solution with your own custom linters. Let's walk through the steps of setting up your own linter. For a full walkthrough, see our [blog](https://trunk.io/blog/integrating-your-own-custom-tools-with-trunk-check).

### Execution Model

Running `trunk check` tells `trunk` to do the following:

* compute the set of modified files (by comparing the current working tree and `upstream-ref`,\
  usually your `main` or `master` branch)
* compute the set of lint actions to run based on the modified files
  * each enabled linter is invoked once per [applicable modified file](./#applicable-filetypes); for\
    example, if `pylint` and `flake8` are enabled, they will both be run on every modified `python` file but not on any modified `markdown` files
  * every lint action also will have a corresponding _upstream_ lint action (i.e. the linter will\
    also be run on the upstream version of the file, so that we can determine which issues already\
    exist in your repository)
* [download](./#making-installs-hermetic) and install any newly enabled linters/formatters
* execute uncached lint actions
* parse linter [outputs](./#output-types) into configurable output types
* determine which lint issues are new, existing, or fixed

### [Output Types](output-types.md)

Trunk currently supports the following types of additional/proprietary linters:

<table data-header-hidden><thead><tr><th width="173.33333333333331"></th><th width="131" align="center"></th><th></th></tr></thead><tbody><tr><td>Linter Type</td><td align="center">Autofix<br>support</td><td>Description</td></tr><tr><td><a href="output-types.md#sarif"><code>sarif</code></a></td><td align="center">✓</td><td>Produces diagnostics as <a href="https://docs.oasis-open.org/sarif/sarif/v2.0/sarif-v2.0.html">Static Analysis Results Interchange Format</a> JSON.</td></tr><tr><td><a href="output-types.md#lsp-json"><code>lsp_json</code></a></td><td align="center"></td><td>Produces diagnostics as <a href="https://microsoft.github.io/language-server-protocol/">Language Server Protocol</a> JSON.</td></tr><tr><td><a href="output-types.md#pass-fail-linters"><code>pass_fail</code></a></td><td align="center"></td><td>Writes a single file-level diagnostic to <code>stdout</code>.</td></tr><tr><td><a href="output-types.md#regex"><code>regex</code></a></td><td align="center"></td><td>Produces diagnostics using a custom regex format.</td></tr><tr><td><a href="output-types.md#arcanist"><code>arcanist</code></a></td><td align="center">✓</td><td>Produces diagnostics as Arcanist JSON.</td></tr><tr><td><a href="output-types.md#formatters"><code>rewrite</code></a></td><td align="center">✓</td><td>Writes the formatted version of a file to <code>stdout</code>.</td></tr></tbody></table>

If your linter produces a different output type, you can also write a [parser](custom-parsers.md) to transform the linter's output into something Trunk can understand.

To set up a custom linter, add it to `trunk.yaml` under `lint.definitions` and enable it:

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

The `@SYSTEM` is a special identifier that indicates that we will forward the `PATH` environment variable to the custom linter when we invoke it.

Every custom linter must specify a name, the types of files it will run on, at least one command, and `success_codes` or `error_codes`.

> Info: Entries in `enabled` must specify both a linter name and a version. If you commit your linter into your repository, you should simply use `@SYSTEM`, which will run the linter with your shell's\
> `PATH`. If you have a versioned release pipeline for your linter, though, you'll want to define your\
> custom linter using a [`download`](./#downloads) and specify the download version to use.

### Configuration Options

When defining a custom linter, Trunk not only needs to know the output of the linter command but also details such as how to invoke it, how to specify the file to check, and more; the next few sections explain what options you use to configure these and how:

For even more details, you can refer to [the JSON schema for `trunk.yaml`](https://static.trunk.io/pub/trunk-yaml-schema.json).

#### Applicable filetypes

To determine which linters to run on which files (i.e. compute the set of lint actions), Trunk requires that every linter define the set of filetypes it applies to in `files`.

We have a number of pre-defined filetypes (e.g. `c++-header`, `gemspec`, `rust`; see our [plugins repo](https://github.com/trunk-io/plugins/blob/main/linters/plugin.yaml) for an up-to-date list), but you can also define your own filetypes. Here's how we define the `python` filetype:

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

This tells Trunk that files matching either of the following criteria should be considered `python` files:

* the extension is any of `.py`, `.py2`, or `.py3` (e.g. `lib.py`)
* the shebang is any of `python` or `python3` (e.g. `#!/usr/bin/env python3`)

#### Command

Once Trunk has figured out which linters it will run on which files, Trunk expands the template provided in the `run` field to determine the arguments it will invoke the linter with. Here's what that looks like for `detekt`, one of our Kotlin linters:

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

This command template contains all the information Trunk needs to execute `detekt` in a way where Trunk will be able to understand `detekt`'s output.

Note that some of the fields in this command template contain `${}` tokens: these tokens are why `command` is a template and are replaced at execution time with the value of that variable within the context of the lint action being executed.

| Variable          | Description                                                                   |
| ----------------- | ----------------------------------------------------------------------------- |
| `${workspace}`    | Path to the root of the repository                                            |
| `${target}`       | Path to the file to check, relative to `${workspace}`                         |
| `${linter}`       | Path to the directory the linter was downloaded to                            |
| `${runtime}`      | Path to the directory the runtime (e.g. `node`) was downloaded to             |
| `${upstream-ref}` | Upstream git commit that is being used to calculate new/existing/fixed issues |
| `${plugin}`       | Path to the root of the plugin's repository                                   |

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

#### Output

The output format that Trunk expects from a linter is determined by its [`output`](./#output) type.

**`stdout`, `stderr` or `tmp_file`**

`trunk` generally expects a linter to output its findings to `stdout`, but does support other output mechanisms:

| `read_output_from` | Description                                                                       |
| ------------------ | --------------------------------------------------------------------------------- |
| `stdout`           | Standard output.                                                                  |
| `stderr`           | Standard error.                                                                   |
| `tmp_file`         | If `${tmpfile}` was specified in `command`, the path of the created `${tmpfile}`. |

#### **Exit codes**

Linters often use different exit codes to categorize the outcome. For instance, [`markdownlint`](https://github.com/igorshubovych/markdownlint-cli#exit-codes) uses `0` to indicate that no issues were found, `1` to indicate that the tool ran successfully but issues were found, and `2`, `3`, and `4` for tool execution failures.

Trunk supports specifying either `success_codes` or `error_codes` for a linter:

* if `success_codes` are specified, Trunk expects a successful linter invocation (which may or may not find issues) to return one of the specified `success_codes`;
* if `error_codes` are specified, Trunk expects a successful linter invocation to return any exit\
  code which is _not_ one of the specified `error_codes`.

`markdownlint`, for example, has `success_codes: [0, 1]` in its configuration.

#### **Working directory**

`run_from` determines what directory a linter command is run from.

<table data-header-hidden><thead><tr><th width="415"></th><th></th></tr></thead><tbody><tr><td><code>run_from</code></td><td>Description</td></tr><tr><td><code>&#x3C;path></code> (<code>.</code> by default)</td><td>Explicit path to run from</td></tr><tr><td><code>${parent}</code></td><td>Parent of the target file; e.g. would be <code>foo/bar</code> for <code>foo/bar/hello.txt</code></td></tr><tr><td><code>${root_or_parent_with(&#x3C;file>)}</code></td><td>Nearest parent directory containing the specified file</td></tr><tr><td><code>${root_or_parent_with_dir(&#x3C;dir>)}</code></td><td>Nearest parent directory containing the specified directory</td></tr><tr><td><code>${root_or_parent_with_regex(&#x3C;regex>)}</code></td><td>Nearest parent directory containing a file or directory matching specified regex</td></tr><tr><td><code>${root_or_parent_with_direct_config}</code></td><td>Nearest parent directory containing a file from <code>direct_configs</code></td></tr><tr><td><code>${root_or_parent_with_any_config}</code></td><td>Nearest parent directory containing a file from <code>affects_cache</code> or <code>direct_configs</code></td></tr><tr><td><code>${target_directory}</code></td><td>Run the linter from the same directory as the target file, and change the target to be <code>.</code></td></tr><tr><td><code>${compile_command}</code></td><td>Run from the directory where <code>compile_commands.json</code> is located</td></tr></tbody></table>

#### **Limiting concurrency**

If you would like to limit the number of times trunk will invoke a linter concurrently, then you can use the `maximum_concurrency` option. For example, setting `maximum_concurrency: 1` will limit Trunk from running more than one instance of the linter simultaneously.

#### **Environment variables**

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

We use the same template syntax for `environment` as we do for [`command`](./#command).

### Hermetic Installs

You can use the `tools` section to specify trunk-configured binaries that the linter uses to run. The `tools` key should specify a list of tool names. We have two kinds of tool dependencies - they are described in turn below. See the [Tools Configuration](../../tools/configuration.md) page for more details on how to set up your tools.

Using tools is the preferred way of defining and versioning a linter, as it also allows repo users to conveniently run the linter binary outside of the `trunk check` context.

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

**(NOTE: This method of specifying linters is still supported, but using `tools` like specified** [**above**](./#tools) **is recommended going forward. Tools support referencing downloads from the top-level `downloads` section)**

If your custom linter has a separate release process (i.e. is not committed in your repo), then you can tell Trunk how to download it like so:

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
      ...
    - name: ipsum-linter
      files: [rust]
      download: ipsum-linter
      ...
  enabled:
    - lorem-linter@4.0.2
    - ipsum-linter@0.1.6
```

This tells Trunk that, for `lorem-linter`:

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
