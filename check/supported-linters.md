# Supported Linters

> 📘 Our linter integrations are open-source!
>
> You can find them at [`trunk-io/plugins`](https://github.com/trunk-io/plugins).

We currently support the following linters:

| Language                           | Linters                                                                                      |
| ---------------------------------- | -------------------------------------------------------------------------------------------- |
| All                                | `codespell`, `cspell`, `gitleaks`, `git-diff-check`                                          |
| Ansible                            | `ansible-lint`                                                                               |
| Bash                               | `shellcheck`, `shfmt`                                                                        |
| Bazel, Starlark                    | `buildifier`                                                                                 |
| C, C++, Protobuf                   | `clang-format`, `clang-tidy`, `include-what-you-use`                                         |
| Cloudformation                     | `cfnlint`                                                                                    |
| CSS, SCSS                          | `stylelint`                                                                                  |
| Cue                                | `cue-fmt`                                                                                    |
| Docker                             | `hadolint`                                                                                   |
| Dotenv                             | `dotenv-linter`                                                                              |
| GitHub                             | `actionlint`                                                                                 |
| Go                                 | `gofmt`, `gokart`, `golangci-lint`, `semgrep`, `goimports`                                   |
| HAML                               | `haml-lint`                                                                                  |
| Java                               | `semgrep`                                                                                    |
| JavaScript, TypeScript, YAML, JSON | `eslint`, `prettier`, `semgrep`                                                              |
| Kotlin                             | `detekt`, `detekt-explicit`, `detekt-gradle`, `ktlint`                                       |
| Markdown                           | `markdownlint`                                                                               |
| Protobuf                           | `buf-breaking`, `buf-lint`                                                                   |
| Python                             | `autopep8`, `bandit`, `black`, `flake8`, `isort`, `mypy`, `pylint`, `ruff`,`semgrep`, `yapf` |
| Ruby                               | `brakeman`, `rubocop`, `rufo`, `semgrep`, `standardrb`                                       |
| Rust                               | `clippy`, `rustfmt`                                                                          |
| Scala                              | `scalafmt`                                                                                   |
| SQL                                | `sql-formatter`, `sqlfluff`                                                                  |
| SVG                                | `svgo`                                                                                       |
| Terraform                          | `terraform` (`validate` and `fmt`), `tflint`[1](broken-reference/)                           |
| TOML                               | `taplo`                                                                                      |
| YAML                               | `prettier`, `semgrep`, `yamllint`                                                            |

1. [Module inspection](https://github.com/terraform-linters/tflint/blob/master/docs/user-guide/module-inspection.md), [deep Checking](https://github.com/terraform-linters/tflint-ruleset-aws/blob/master/docs/deep\_checking.md), and setting variables are not currently supported.

### Caching

Caching is currently enabled for about half the linters/formatters. Since Trunk needs to know all the inputs to a linter for a file/directory in order to cache the results, we don't yet cache every linter, but we are building out the functionality to do so. You can see which linters are currently configured to be cached by running `trunk print-config` and seeing which linter configurations have `cache_results: true` set. That's also how you can enable/disable caching for any custom linters you integrate.

### Linter-specific Configuration

Most linters provide some mechanism to tweak their configuration, e.g. `.eslintrc` or `Cargo.toml`. `trunk` is aware of all the ways individual tools are configured and supports them. This means that all the linters you've already configured will continue to work exactly the same, just now supercharged by `trunk`.

Check out our open source [`plugins`](https://github.com/trunk-io/plugins/blob/main/linters/isort/.isort.cfg) repo for our always up to date collection of sane linter configurations.

### Ansible-lint

Ansible-lint must be configured with a trigger. See the [trigger rules](configuration.md)#trigger-rules) documentation for more information.

In case your ansible setup is not contained within a single folder you would list all files and directories belonging to your ansible setup.

### Clang-format

We currently only support versions 12.0.0, 12.0.1, and 13.0.0 (`clang-format@13.0.0` in `trunk.yaml`)

By default trunk uses clang-format to additionally format `.proto` files. However, for this to work, you need to have enabled `clang-format` to do so in your `.clang-format` config file. You can do that by adding the following to the end of your `.clang-format`:

```yaml
---
Language: Proto
```

For example, you might have this for your entire `.clang-format` file:

```yaml
BasedOnStyle: Google
ColumnLimit: 100
---
Language: Cpp
DerivePointerAlignment: false
---
Language: Proto
```

### Clang-tidy

We currently only support versions 12.0.0, 12.0.1, and 13.0.0 (`clang-tidy@13.0.0` in `trunk.yaml`), and we only support using `clang-tidy` from Bazel and CMake projects.

In order to only see issues in your own code, not from library header files your code includes, add this to your `.clang-tidy` file:

```yaml
HeaderFilterRegex: \./.+
```

You may have to build your project first if you depend on any generated header files.

#### Linter Failures

If a file you're linting does not compile, clang-tidy may fail to process it. In `trunk`, this will show up as a "Linter Failure". The output you'll see will look like a compilation error. This can also happen if the pre-reqs to running clang-tidy haven't been met (see below).

#### Using Bazel

By default `trunk` will query bazel for compile commands used to run clang-tidy. This requires no configuration.

Trunk will build needed compilation pre-requisites before invoking clang-tidy on each file (e.g. generated protobuf headers).

**Finding the bazel binary**

Trunk will search for the bazel binary in two ways.

1. Paths relative to the workspace root.
2. Binaries in any of the directories in the PATH environment variable.

First trunk will search all workspace root relative paths and then all system directories. If you override anything in lint.bazel.paths then we only search the paths you specify. By default the configuration is as follows.

```yaml
lint:
  bazel:
    paths:
      workspace:
        - tools/bazel
        - bazelisk
      system:
        - bazel
        - bazelisk
```

#### Using compile\_commands.json generated by CMake

Trunk supports using the `compile_commands.json` file generated by CMake. If you run `cmake` from a directory called `build` in the root of your project then trunk will find the compile commands automatically. If you run it in some other directory then you will have to symlink the `compile_commands.json` in that directory to the root of your repo for trunk to find them. Note that trunk does not currently support CMake out of tree builds.

#### Another tool claims I have clang-tidy issues, but not trunk- what gives?

Trunk runs clang-tidy with a compile commands database so that we can guarantee clang-tidy produces the correct diagnostics about your code. Other tools, such as clangd, may use best-effort heuristics to guess a compile command for a given clang-tidy input file (for example, see [this discussion](https://github.com/clangd/clangd/issues/519)) and consequently produce incorrect clang-tidy findings because they guessed the compile command wrong.

### Clippy

Clippy is distributed with rust itself, so specify your rust version for your clippy version (for example `clippy@1.61.0`).

### Detekt

Detekt is usually invoked through gradle, which allows specifying additional configuration in `build.gradle`. We do not yet automatically parse your Gradle scripts to infer your `detekt` configuration; instead, what we do is this:

* `detekt` invokes [`detekt-cli`](https://detekt.github.io/detekt/cli.html) with the\
  `--build-upon-default-config` flag (this appears to be\
  [more common](https://cs.github.com/?q=%2FbuildUponDefaultConfig.\*%28true%29%2F+detekt) than the\
  alternative)
* `detekt-explicit` invokes [`detekt-cli`](https://detekt.github.io/detekt/cli.html) without the\
  `--build-upon-default-config` flag

You will also need to provide a valid detekt config as `.detekt.yaml` (an empty `.detekt.yaml` is valid, if you don't want to configure `detekt`); if you already have a detekt config, then you can symlink it like so:

```bash
ln -s path/to/existing/detekt-config.yml .detekt-config.yaml
```

To use `./gradlew detekt` to invoke Detekt, you can add `detekt-gradle@SYSTEM` to your `enabled` list. Note that since you're running Detekt via Gradle, you should also add the paths to your Detekt configurations to `direct_configs`, e.g.

```gradle
direct_configs: ["lib/detekt.yaml"]
```

### Eslint

Most eslint users use a number of plugins, custom parsers, etc. Trunk has the ability to turn sandboxing and caching on or off for each linter, and we've turned it off for eslint so it can use your repo's installed packages for eslint plugins and other required eslint packages. Trunk does control the eslint version itself, but otherwise eslint looks for all plugins, configs, etc based on the path of source file its linting. This all means you do need to have `npm/yarn install`d in your repo as a prerequisite before running eslint via trunk.

We recommend you disable all prettier rules in your eslint config and let trunk run prettier automatically on your files. It's much nicer to just autoformat a file than to see a lint error for every missing space.

You can easily do this by adding the `eslint-config-prettier` package and in your eslint config's `extends` section adding `prettier` as the last element. For example, your `extends` list might look like:

```yaml
extends:
  # Order matters, later configs purposefully override settings from earlier configs
  - eslint:recommended
  - airbnb
  - plugin:@typescript-eslint/recommended
  - plugin:import/recommended
  - plugin:import/typescript
  - plugin:node/recommended
  - plugin:mocha/recommended
  - plugin:react/recommended
  - prettier # this actually turns OFF all prettier rules running via eslint
```

### Python linters (flake8, pylint, black, etc)

Trunk uses hermetic runtime versions, which you can override if needed. If you're using a newer version of python that our default (3.10.3 at the time of writing) you can override it in `trunk.yaml` via:

```yaml
runtimes:
  enabled:
    - python@3.10.3
```

As always, you can view the defaults and configuration of everything trunk runs via `trunk print-config`.

### Flake8

Flake8 has a plugin architecture where if you install a plugin, it gets used. You can enable Flake8 plugins via:

```yaml
enabled:
  - flake8@3.9.2:
      packages:
        - flake8-bugbear@21.4.3
```

flake8-bugbear is probably the most popular flake8 plugin, we recommend it!

### Prettier

By default trunk uses prettier to autoformat many languages/config formats, including markdown. To line wrap within markdown, you need to set the following in your prettier config (`.prettierrc.yaml` or similar):

```yaml
proseWrap: always
```

You may also want to configure `printWidth:` to your liking.

### Gitleaks

Gitleaks v7 only works with go 1.16, not go 1.18 while Gitleaks v8 works with 1.18. We recommend using v8, but if you specifically need to use v7 you can override the go runtime version like so:

```yaml
runtimes:
  enabled:
    - go@1.16.7
```

Again, this is not recommended. Just use Gitleaks v8 or later with go 1.18 or later.

### Golangci-lint

Make sure your go version in `go.mod` matches Trunk's go runtime version. At the time you writing, Trunk's default go runtime version is 1.18.3. You can find out what it is via `trunk print-config`, and look for the `runtime` section, and you can override the default version in your `trunk.yaml` via:

```yaml
runtimes:
  enabled:
    - go@1.18.3
```

### Pylint

You may specify additional pylint plugins in your `.pylintrc`, using the line `load-plugins=...`

if you want to run the plugin `pylint-django` as part of your setup, you would add the line

`load-plugins=pylint_django` to your `.pylintrc`, but you **also** need to tell trunk to install the package:

```yaml
- pylint@2.11.0:
    packages:
      - pylint-django@2.4.4
      ...
```

### Markdownlint

Older versions of markdownlint had a bug where it printed plaintext output even when run with `--json`. We rely on JSON output so we can parse and ingest the results from markdownlint. The package we use for markdownlint is actually [markdownlint-cli](https://www.npmjs.com/package/markdownlint-cli); `>= 0.29.0` is verified to work.

### Rustfmt

We currently use the version of `rustfmt` packaged with rust, so for `rustfmt` version, specify your rust version (for example `rustfmt@1.61.0`).

If you have `edition` in your `cargo.toml`, `rustfmt` also needs the same information in `.rustfmt.toml` in your repo root. For example, your `.rustfmt.toml` might contain:

```toml
edition = "2021"
```

### Sqlfluff

`sqlfluff` is only configured as a linter because its formatting capabilities are very subpar compared to `sql-formatter`.

### Terraform

We currently support `terraform validate` and `terraform fmt`, but only `fmt` is enabled by default when you add `terraform` to your enabled list in `trunk.yaml`. To enable `validate`, add this to your `trunk.yaml`:

```yaml
lint:
  linters:
    - name: terraform
      commands:
        - name: validate
          enabled: true
  enabled:
    - ...
```

Note: you must run `terraform init` before running `trunk check` with `terraform validate` enabled (both locally, or on CI).
