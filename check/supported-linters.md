# Supported Linters

> 📘 Our linter integrations are open-source!
>
> You can find them at [`trunk-io/plugins`](https://github.com/trunk-io/plugins).

Enable the following tools via:

```
trunk check enable {linter}
```

| Technology      | Linters                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| All             | [codespell](https://github.com/codespell-project/codespell#readme), [cspell](https://github.com/streetsidesoftware/cspell#readme), [gitleaks](https://github.com/zricethezav/gitleaks#readme), [git-diff-check](https://git-scm.com/docs/git-diff), [pre-commit-hooks](https://pre-commit.com/hooks.html)                                                                                                                                                                                                                                                                                            |
| Ansible         | [ansible-lint](https://github.com/ansible/ansible-lint#readme)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Apex            | [pmd](https://pmd.github.io/)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Bash            | [shellcheck](https://github.com/koalaman/shellcheck#readme), [shfmt](https://github.com/mvdan/sh#readme)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Bazel, Starlark | [buildifier](https://github.com/bazelbuild/buildtools/blob/master/buildifier/README.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| C, C++          | [clang-format](https://clang.llvm.org/docs/ClangFormat.html), [clang-tidy](https://clang.llvm.org/extra/clang-tidy/), [include-what-you-use](https://github.com/include-what-you-use/include-what-you-use#readme), [pragma-once](https://github.com/trunk-io/plugins/blob/main/linters/pragma-once/README.md)                                                                                                                                                                                                                                                                                        |
| C#              | \[dotnet-format]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| CircleCI Config | [circleci](https://github.com/CircleCI-Public/circleci-cli#readme)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Cloudformation  | [cfnlint](https://github.com/aws-cloudformation/cfn-lint#readme), [checkov](https://github.com/bridgecrewio/checkov#readme)                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| CSS, SCSS       | [stylelint](https://github.com/stylelint/stylelint#readme), [prettier](https://github.com/prettier/prettier#readme)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Cue             | [cue-fmt](https://cuelang.org/)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Docker          | [hadolint](https://github.com/hadolint/hadolint#readme), [checkov](https://github.com/bridgecrewio/checkov#readme)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Dotenv          | [dotenv-linter](https://github.com/dotenv-linter/dotenv-linter#readme)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| GitHub          | [actionlint](https://github.com/rhysd/actionlint#readme)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Go              | [gofmt](https://pkg.go.dev/cmd/gofmt), [gofumpt](https://pkg.go.dev/mvdan.cc/gofumpt), [goimports](https://pkg.go.dev/golang.org/x/tools/cmd/goimports), [gokart](https://github.com/praetorian-inc/gokart), [golangci-lint](https://github.com/golangci/golangci-lint#readme), [golines](https://pkg.go.dev/github.com/segmentio/golines), [semgrep](https://github.com/returntocorp/semgrep#readme)                                                                                                                                                                                                |
| GraphQL         | [graphql-schema-linter](https://github.com/cjoudrey/graphql-schema-linter#readme), [prettier](https://github.com/prettier/prettier#readme)                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| HAML            | [haml-lint](https://github.com/sds/haml-lint#readme)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| HTML Templates  | [djlint](https://github.com/Riverside-Healthcare/djlint#readme)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Java            | [google-java-format](https://github.com/google/google-java-format#readme), [pmd](https://pmd.github.io/), [semgrep](https://github.com/returntocorp/semgrep#readme)                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Javascript      | [deno](https://deno.land/manual), [eslint](https://github.com/eslint/eslint#readme), [prettier](https://github.com/prettier/prettier#readme), [rome](https://github.com/rome/tools#readme), [semgrep](https://github.com/returntocorp/semgrep#readme)                                                                                                                                                                                                                                                                                                                                                |
| JSON            | [deno](https://deno.land/manual), [eslint](https://github.com/eslint/eslint#readme), [prettier](https://github.com/prettier/prettier#readme), [semgrep](https://github.com/returntocorp/semgrep#readme)                                                                                                                                                                                                                                                                                                                                                                                              |
| Kotlin          | [detekt](https://github.com/detekt/detekt#readme)[1](https://github.com/trunk-io/plugins/edit/main/README.md#note-detekt), [ktlint](https://github.com/pinterest/ktlint#readme)                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Kubernetes      | [kube-linter](https://github.com/stackrox/kube-linter#readme)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Lua             | [stylua](https://github.com/JohnnyMorganz/StyLua/tree/main)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Markdown        | [deno](https://deno.land/manual), [markdownlint](https://github.com/DavidAnson/markdownlint#readme), [remark-lint](https://github.com/remarkjs/remark-lint#readme), [markdown-link-check](https://github.com/tcort/markdown-link-check#readme), [prettier](https://github.com/prettier/prettier#readme)                                                                                                                                                                                                                                                                                              |
| Nix             | [nixpkgs-fmt](https://github.com/nix-community/nixpkgs-fmt)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| package.json    | [sort-package-json](https://github.com/keithamus/sort-package-json#readme)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Perl            | [perlcritic](https://metacpan.org/pod/Perl::Critic), [perltidy](https://metacpan.org/dist/Perl-Tidy/view/bin/perltidy)                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| PNG             | [oxipng](https://github.com/shssoichiro/oxipng#readme)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Prisma          | [prisma](https://github.com/prisma/prisma#readme)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Protobuf        | [buf](https://github.com/bufbuild/buf#readme) (breaking, lint, and format), [clang-format](https://clang.llvm.org/docs/ClangFormat.html), [clang-tidy](https://clang.llvm.org/extra/clang-tidy/)                                                                                                                                                                                                                                                                                                                                                                                                     |
| Python          | [autopep8](https://github.com/hhatto/autopep8#readme), [bandit](https://github.com/PyCQA/bandit#readme), [black](https://github.com/psf/black#readme), [flake8](https://github.com/PyCQA/flake8#readme), [isort](https://github.com/PyCQA/isort#readme), [mypy](https://github.com/python/mypy#readme), [pylint](https://github.com/PyCQA/pylint#readme), [pyright](https://github.com/microsoft/pyright), [semgrep](https://github.com/returntocorp/semgrep#readme), [yapf](https://github.com/google/yapf#readme), [ruff](https://github.com/charliermarsh/ruff), [sourcery](https://sourcery.ai/) |
| Renovate        | [renovate](https://github.com/renovatebot/renovate#readme)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Ruby            | [brakeman](https://github.com/presidentbeef/brakeman#readme), [rubocop](https://github.com/rubocop/rubocop#readme), [rufo](https://github.com/ruby-formatter/rufo#readme), [semgrep](https://github.com/returntocorp/semgrep#readme), [standardrb](https://github.com/testdouble/standard#readme)                                                                                                                                                                                                                                                                                                    |
| Rust            | [clippy](https://github.com/rust-lang/rust-clippy#readme), [rustfmt](https://github.com/rust-lang/rustfmt#readme)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Scala           | [scalafmt](https://github.com/scalameta/scalafmt#readme)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Security        | [checkov](https://github.com/bridgecrewio/checkov#readme), [dustilock](https://github.com/Checkmarx/dustilock), [nancy](https://github.com/sonatype-nexus-community/nancy#readme), [osv-scanner](https://github.com/google/osv-scanner), [tfsec](https://github.com/aquasecurity/tfsec), [trivy](https://github.com/aquasecurity/trivy#readme), [trufflehog](https://github.com/trufflesecurity/trufflehog/), [terrascan](https://github.com/tenable/terrascan#readme)                                                                                                                               |
| SQL             | [sqlfluff](https://github.com/sqlfluff/sqlfluff#readme), [sqlfmt](https://github.com/tconbeer/sqlfmt#readme), [sql-formatter](https://github.com/sql-formatter-org/sql-formatter#readme)                                                                                                                                                                                                                                                                                                                                                                                                             |
| SVG             | [svgo](https://github.com/svg/svgo#readme)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Swift           | [stringslint](https://github.com/dral3x/StringsLint#readme), [swiftlint](https://github.com/realm/SwiftLint#readme), [swiftformat](https://github.com/nicklockwood/SwiftFormat#readme)                                                                                                                                                                                                                                                                                                                                                                                                               |
| Terraform       | [terraform](https://developer.hashicorp.com/terraform/cli/code) (validate and fmt), [checkov](https://github.com/bridgecrewio/checkov#readme), [tflint](https://github.com/terraform-linters/tflint#readme)[2](https://github.com/trunk-io/plugins/edit/main/README.md#note-tflint), [tfsec](https://github.com/aquasecurity/tfsec), [terrascan](https://github.com/tenable/terrascan#readme)                                                                                                                                                                                                        |
| Terragrunt      | [terragrunt](https://terragrunt.gruntwork.io/docs/getting-started/quick-start/)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Textproto       | [txtpbfmt](https://github.com/protocolbuffers/txtpbfmt/)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| TOML            | [taplo](https://github.com/tamasfe/taplo#readme)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Typescript      | [deno](https://deno.land/manual), [eslint](https://github.com/eslint/eslint#readme), [prettier](https://github.com/prettier/prettier#readme), [rome](https://github.com/rome/tools#readme), [semgrep](https://github.com/returntocorp/semgrep#readme)                                                                                                                                                                                                                                                                                                                                                |
| YAML            | [prettier](https://github.com/prettier/prettier#readme), [semgrep](https://github.com/returntocorp/semgrep#readme), [yamllint](https://github.com/adrienverge/yamllint#readme)                                                                                                                                                                                                                                                                                                                                                                                                                       |

1. Support for Detekt is under active development; see our [docs](https://docs.trunk.io/docs/check-supported-linters#detekt) for more details.
2. [Module inspection](https://github.com/terraform-linters/tflint/blob/master/docs/user-guide/module-inspection.md), [deep checking](https://github.com/terraform-linters/tflint-ruleset-aws/blob/master/docs/deep\_checking.md), and setting variables are not currently supported.

### Linter-specific Configuration

Most linters provide some mechanism to tweak their configuration, e.g. `.eslintrc` or `Cargo.toml`. `trunk` is aware of all the ways individual tools are configured and supports them. This means that all the linters you've already configured will continue to work exactly the same, just now supercharged by `trunk`.

Check out our open source [`plugins`](https://github.com/trunk-io/plugins/blob/main/linters/isort/.isort.cfg) repo for our always up to date collection of sane linter configurations.

### Ansible-lint

Ansible-lint must be configured with a trigger. See the [trigger rules](configuration.md#trigger-rules) documentation for more information.

In case your ansible setup is not contained within a single folder you would list all files and directories belonging to your ansible setup.

### Clang-format

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

We only support using `clang-tidy` from Bazel and CMake projects.

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

You can generate a local compilation database by running `trunk generate-compile-commands`.

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

#### Using `compile_commands.json` generated by CMake

Trunk supports using the `compile_commands.json` file generated by CMake. If you run `cmake` from a directory called `build` in the root of your project then trunk will find the compile commands automatically. If you run it in some other directory then you will have to symlink the `compile_commands.json` in that directory to the root of your repo for trunk to find them. Note that trunk does not currently support CMake out of tree builds.

#### Another tool claims I have clang-tidy issues, but not trunk. What gives?

Trunk runs clang-tidy with a compile commands database so that we can guarantee clang-tidy produces the correct diagnostics about your code. Other tools, such as `clangd`, may use best-effort heuristics to guess a compile command for a given clang-tidy input file (for example, see [this discussion](https://github.com/clangd/clangd/issues/519)) and consequently produce incorrect clang-tidy findings because they guessed the compile command wrong.

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

Most eslint users use a number of plugins, custom parsers, etc. Trunk has the ability to turn sandboxing and caching on or off for each linter, and we've turned it off for eslint so it can use your repo's installed packages for eslint plugins and other required eslint packages. Trunk does control the eslint version itself, but otherwise eslint looks for all plugins, configs, etc based on the path of source file its linting. **This all means you do need to have `npm/yarn install`d in your repo as a prerequisite before running eslint via trunk**.

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

Trunk uses hermetic runtime versions, which you can override if needed. If you're using a newer version of Python that our default (3.10.3 at the time of writing) you can override it in `trunk.yaml` via:

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

By default trunk uses prettier to autoformat many languages/config formats, including markdown. To line wrap within markdown, you need to set the following in your [prettier config](https://prettier.io/docs/en/configuration.html) (`.prettierrc.yaml`, etc):

```yaml
proseWrap: always
```

You may also want to configure `printWidth:` to your liking.

### Gitleaks

Gitleaks v7 only works with Go 1.16, not Go 1.18 while Gitleaks v8 works with 1.18. We recommend using v8, but if you specifically need to use v7 you can override the go runtime version like so:

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
