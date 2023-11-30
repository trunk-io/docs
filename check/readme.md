# Check

## What is Check?

Trunk Check runs [100+ code-checking tools](https://github.com/trunk-io/plugins) on your repositories, locally and in CI, which allow you to automatically...

* Keep bugs and security vulnerabilities out of your codebase
* Enforce code formatting and style
* Optimize images
* Flag secrets
* and much more

Check is typically used as a local tool ([CLI](cli/), [VS Code Extension](https://marketplace.visualstudio.com/items?itemName=trunk.io)) and a [CI tool](check-cloud-ci-integration/continuous-integration/) / [GitHub bot](check-cloud-ci-integration/get-started/github-integration.md).

## Standout Features

* does everything from formatting, to linting, to security checking, to optimizing images
* config-as-code (`.trunk/trunk.yaml`)
* caching
* pre-existing issue detection
* a daemon & language server
* [githooks management](actions/git-hooks.md)
* cli available ([docs](cli/))
* a [web app](https://app.trunk.io/) for repo stats and slack notifications

## I run a large eng org. Why should I use Check?

When you modify a file, Trunk Check has a feature called Hold The Line which only flags the _new_ issues. It does this by being git-aware and by using some sophisticated heuristics (to handle the case where you change one line of code and new issues pop up somewhere else because of it).

This feature is critical for eng orgs because it allows you to start leveling up your codebase without making devs fix every preexisting issue in every file they touch, which would dramatically slow down development and cause a lot of frustration. Without this feature, it's impractical to turn on new rules in existing code-checking tools, but it's also impractical to add new tools to your code-checking arsenal. With it, adding a new tool is as easy as `trunk check enable {linter}`, and you can start being better going forward and tackle your tech debt incrementally, on your own terms.

## Supported Linters, Formatters, and Security Tools

We integrate new linters every release. Stop by on [Slack](https://slack.trunk.io) and let us know what you'd like next! All tool integrations are open-source [here](https://github.com/trunk-io/plugins)

Enable the following tools:

```bash
trunk check enable {linter}
```

| Technology      | Linters                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| All             | [codespell](https://github.com/codespell-project/codespell#readme), [cspell](https://github.com/streetsidesoftware/cspell#readme), [gitleaks](https://github.com/zricethezav/gitleaks#readme), [git-diff-check](https://git-scm.com/docs/git-diff)                                                                                                                                                                                                                                                                                                  |
| Ansible         | [ansible-lint](https://github.com/ansible/ansible-lint#readme)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Bash            | [shellcheck](https://github.com/koalaman/shellcheck#readme), [shfmt](https://github.com/mvdan/sh#readme)                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Bazel, Starlark | [buildifier](https://github.com/bazelbuild/buildtools/blob/master/buildifier/README.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| C, C++          | [clang-format](https://clang.llvm.org/docs/ClangFormat.html), [clang-tidy](https://clang.llvm.org/extra/clang-tidy/), [include-what-you-use](https://github.com/include-what-you-use/include-what-you-use#readme), [pragma-once](linters/pragma-once/)                                                                                                                                                                                                                                                                                              |
| CircleCI Config | [circleci](https://github.com/CircleCI-Public/circleci-cli#readme)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Cloudformation  | [cfnlint](https://github.com/aws-cloudformation/cfn-lint#readme), [checkov](https://github.com/bridgecrewio/checkov#readme)                                                                                                                                                                                                                                                                                                                                                                                                                         |
| CSS, SCSS       | [stylelint](https://github.com/stylelint/stylelint#readme)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Cue             | [cue-fmt](https://cuelang.org/)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Docker          | [hadolint](https://github.com/hadolint/hadolint#readme), [checkov](https://github.com/bridgecrewio/checkov#readme)                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Dotenv          | [dotenv-linter](https://github.com/dotenv-linter/dotenv-linter#readme)                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| GitHub          | [actionlint](https://github.com/rhysd/actionlint#readme)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Go              | [gofmt](https://pkg.go.dev/cmd/gofmt), [gofumpt](https://pkg.go.dev/mvdan.cc/gofumpt), [goimports](https://pkg.go.dev/golang.org/x/tools/cmd/goimports), [gokart](https://github.com/praetorian-inc/gokart), [golangci-lint](https://github.com/golangci/golangci-lint#readme), [golines](https://pkg.go.dev/github.com/segmentio/golines), [semgrep](https://github.com/returntocorp/semgrep#readme)                                                                                                                                               |
| HAML            | [haml-lint](https://github.com/sds/haml-lint#readme)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| HTML Templates  | [djlint](https://github.com/Riverside-Healthcare/djlint#readme)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Java            | [google-java-format](https://github.com/google/google-java-format#readme), [semgrep](https://github.com/returntocorp/semgrep#readme)                                                                                                                                                                                                                                                                                                                                                                                                                |
| Javascript      | [eslint](https://github.com/eslint/eslint#readme), [prettier](https://github.com/prettier/prettier#readme), [rome](https://github.com/rome/tools#readme), [semgrep](https://github.com/returntocorp/semgrep#readme)                                                                                                                                                                                                                                                                                                                                 |
| JSON            | [eslint](https://github.com/eslint/eslint#readme), [prettier](https://github.com/prettier/prettier#readme), [semgrep](https://github.com/returntocorp/semgrep#readme)                                                                                                                                                                                                                                                                                                                                                                               |
| Kotlin          | [detekt](https://github.com/detekt/detekt#readme)[1](./#note-detekt), [ktlint](https://github.com/pinterest/ktlint#readme)                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Kubernetes      | [kube-linter](https://github.com/stackrox/kube-linter#readme)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Lua             | [stylua](https://github.com/JohnnyMorganz/StyLua/tree/main)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Markdown        | [markdownlint](https://github.com/DavidAnson/markdownlint#readme), [remark-lint](https://github.com/remarkjs/remark-lint#readme)                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Nix             | [nixpkgs-fmt](https://github.com/nix-community/nixpkgs-fmt)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| package.json    | [sort-package-json](https://github.com/keithamus/sort-package-json#readme)                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| PNG             | [oxipng](https://github.com/shssoichiro/oxipng#readme)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Protobuf        | [buf](https://github.com/bufbuild/buf#readme) (breaking, lint, and format), [clang-format](https://clang.llvm.org/docs/ClangFormat.html), [clang-tidy](https://clang.llvm.org/extra/clang-tidy/)                                                                                                                                                                                                                                                                                                                                                    |
| Python          | [autopep8](https://github.com/hhatto/autopep8#readme), [bandit](https://github.com/PyCQA/bandit#readme), [black](https://github.com/psf/black#readme), [flake8](https://github.com/PyCQA/flake8#readme), [isort](https://github.com/PyCQA/isort#readme), [mypy](https://github.com/python/mypy#readme), [pylint](https://github.com/PyCQA/pylint#readme), [semgrep](https://github.com/returntocorp/semgrep#readme), [yapf](https://github.com/google/yapf#readme), [ruff](https://github.com/charliermarsh/ruff), [sourcery](https://sourcery.ai/) |
| Renovate        | [renovate](https://github.com/renovatebot/renovate#readme)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Ruby            | [brakeman](https://github.com/presidentbeef/brakeman#readme), [rubocop](https://github.com/rubocop/rubocop#readme), [rufo](https://github.com/ruby-formatter/rufo#readme), [semgrep](https://github.com/returntocorp/semgrep#readme), [standardrb](https://github.com/testdouble/standard#readme)                                                                                                                                                                                                                                                   |
| Rust            | [clippy](https://github.com/rust-lang/rust-clippy#readme), [rustfmt](https://github.com/rust-lang/rustfmt#readme)                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Scala           | [scalafmt](https://github.com/scalameta/scalafmt#readme)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Security        | [nancy](https://github.com/sonatype-nexus-community/nancy#readme), [trivy](https://github.com/aquasecurity/trivy#readme), [tfsec](https://github.com/aquasecurity/tfsec), [osv-scanner](https://github.com/google/osv-scanner), [trufflehog](https://github.com/trufflesecurity/trufflehog/)                                                                                                                                                                                                                                                        |
| SQL             | [sqlfluff](https://github.com/sqlfluff/sqlfluff#readme), [sqlfmt](https://github.com/tconbeer/sqlfmt#readme), [sql-formatter](https://github.com/sql-formatter-org/sql-formatter#readme)                                                                                                                                                                                                                                                                                                                                                            |
| SVG             | [svgo](https://github.com/svg/svgo#readme)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Swift           | [stringslint](https://github.com/dral3x/StringsLint#readme), [swiftlint](https://github.com/realm/SwiftLint#readme), [swiftformat](https://github.com/nicklockwood/SwiftFormat#readme)                                                                                                                                                                                                                                                                                                                                                              |
| Terraform       | [terraform](https://developer.hashicorp.com/terraform/cli/code) (validate and fmt), [checkov](https://github.com/bridgecrewio/checkov#readme), [tflint](https://github.com/terraform-linters/tflint#readme)[2](./#note-tflint), [tfsec](https://github.com/aquasecurity/tfsec)                                                                                                                                                                                                                                                                      |
| TOML            | [taplo](https://github.com/tamasfe/taplo#readme)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Typescript      | [eslint](https://github.com/eslint/eslint#readme), [prettier](https://github.com/prettier/prettier#readme), [rome](https://github.com/rome/tools#readme), [semgrep](https://github.com/returntocorp/semgrep#readme)                                                                                                                                                                                                                                                                                                                                 |
| YAML            | [prettier](https://github.com/prettier/prettier#readme), [semgrep](https://github.com/returntocorp/semgrep#readme), [yamllint](https://github.com/adrienverge/yamllint#readme)                                                                                                                                                                                                                                                                                                                                                                      |

1. Support for Detekt is under active development; see our [docs](https://docs.trunk.io/docs/check-supported-linters#detekt) for more details.
2. [Module inspection](https://github.com/terraform-linters/tflint/blob/master/docs/user-guide/module-inspection.md), [deep checking](https://github.com/terraform-linters/tflint-ruleset-aws/blob/master/docs/deep\_checking.md), and setting variables are not currently supported.

## How it works

Trunk downloads everything it needs to run on demand and caches it in `~/.cache/trunk`. We run linters in parallel, in the background, and function as a [language server](https://microsoft.github.io/language-server-protocol) to show results inline in VSCode via the \[Trunk VSCode Extension]\[vscode].

## Install the CLI

The `trunk` command line tool runs locally on your developer machine, right where your code is. Later, you can automatically scan your repo using Trunk Check Cloud.

Check will automatically keep tools up to date, suggest standard tools for your project type (eg: `clang-format` for C++, `eslint` for JS/TS), and pin versions in `trunk.yaml` to ensure Trunk Check is reproducible.

{% tabs %}
{% tab title="bash" %}
```bash
curl https://get.trunk.io -fsSL | bash
```
{% endtab %}

{% tab title="bash (no prompts)" %}
```bash
curl https://get.trunk.io -fsSL | bash -s -- -y
```
{% endtab %}

{% tab title="brew" %}
```bash
brew install trunk-io
```
{% endtab %}

{% tab title="npm" %}
```bash
npm install -D @trunkio/launcher
```
{% endtab %}

{% tab title="pnpm" %}
```bash
pnpm add -D @trunkio/launcher
```
{% endtab %}

{% tab title="yarn" %}
```bash
yarn add -D @trunkio/launcher
```
{% endtab %}
{% endtabs %}

## Initialize `trunk`

From the root of a git repo, run:

```bash
trunk init
```

This will scan your repository and create a `.trunk/trunk.yaml` that enables all the linters, formatters, and security analyzers that [Trunk Check](./) recommends. For more details, see [here](cli/init-in-a-git-repo.md).

## Install the VSCode Extension

If you run VSCode you can also install the [trunk VSCode extension](vscode:extension/Trunk.io). Read more about it [here](https://marketplace.visualstudio.com/items?itemName=Trunk.io).

## Run `trunk check`

`trunk` is git-aware, so without further arguments, it will run on the files you've changed in your repo:

```bash
trunk check
```

Note: if you have not modified any files, `trunk check` will not check anything. See the [CLI usage docs](usage/usage.md) for more info on basic `trunk` usage.
