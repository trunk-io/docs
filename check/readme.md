# Check Overview

## What is Check?

Trunk Check runs [80+ code-checking tools](https://github.com/trunk-io/plugins) on your repositories, locally and in CI, which allow you to automatically...

* Keep bugs and security vulnerabilities out of your code base
* Enforce code formatting and style
* Optimize images
* Flag secrets
* and much more

Check is typically used as both a local tool ([CLI](cli/readme.md), [VS Code Extension](https://marketplace.visualstudio.com/items?itemName=trunk.io)), and a [CI tool](continuous-integration.md) / [GitHub bot](get-started/github-integration.md).

## Standout Features

- does everything from formatting, to linting, to security checking, to optimizing images
- config-as-code (`.trunk/trunk.yaml``)
- caching
- pre-existing issue detection
- a daemon & language server
- [githooks management](actions/git-hooks.md)
- cli available ([docs](cli/readme.md))
- a [web app](https://app.trunk.io/) for repo stats and slack notifications


## I run a large eng org, why should I use Check?

When you modify a file, Trunk Check has a feature called Hold The Line which only flags the *new* issues. It does this by being git-aware, and in fact only functions in git repos.

This feature is critical for eng orgs because it allows you to start leveling up your codebase without making devs fix every preexisting issue in every file that touch, which would dramatically slow down development and cause a lot of frustration.

## Supported Linters, Formatters, and Security Tools

We integrate new linters every release. Stop by on [Slack] and let us know what you'd like next! All
tool integrations are open source [here](https://github.com/trunk-io/plugins)

Enable the following tools via:

```bash
trunk check enable {linter}
```

| Technology      | Linters                                                                                                   |
| --------------- | --------------------------------------------------------------------------------------------------------- |
| All             | [codespell], [cspell], [gitleaks], [git-diff-check]                                                       |
| Ansible         | [ansible-lint]                                                                                            |
| Bash            | [shellcheck], [shfmt]                                                                                     |
| Bazel, Starlark | [buildifier]                                                                                              |
| C, C++          | [clang-format], [clang-tidy], [include-what-you-use], [pragma-once]                                       |
| CircleCI Config | [circleci]                                                                                                |
| Cloudformation  | [cfnlint], [checkov]                                                                                      |
| CSS, SCSS       | [stylelint]                                                                                               |
| Cue             | [cue-fmt]                                                                                                 |
| Docker          | [hadolint], [checkov]                                                                                     |
| Dotenv          | [dotenv-linter]                                                                                           |
| GitHub          | [actionlint]                                                                                              |
| Go              | [gofmt], [gofumpt], [goimports], [gokart], [golangci-lint], [golines], [semgrep]                          |
| HAML            | [haml-lint]                                                                                               |
| HTML Templates  | [djlint]                                                                                                  |
| Java            | [google-java-format], [semgrep]                                                                           |
| Javascript      | [eslint], [prettier], [rome], [semgrep]                                                                   |
| JSON            | [eslint], [prettier], [semgrep]                                                                           |
| Kotlin          | [detekt]<sup><a href="#note-detekt">1</a></sup>, [ktlint]                                                 |
| Kubernetes      | [kube-linter]                                                                                             |
| Lua             | [stylua]                                                                                                  |
| Markdown        | [markdownlint], [remark-lint]                                                                             |
| Nix             | [nixpkgs-fmt]                                                                                             |
| package.json    | [sort-package-json]                                                                                       |
| PNG             | [oxipng]                                                                                                  |
| Protobuf        | [buf] (breaking, lint, and format), [clang-format], [clang-tidy]                                          |
| Python          | [autopep8], [bandit], [black], [flake8], [isort], [mypy], [pylint], [semgrep], [yapf], [ruff], [sourcery] |
| Renovate        | [renovate]                                                                                                |
| Ruby            | [brakeman], [rubocop], [rufo], [semgrep], [standardrb]                                                    |
| Rust            | [clippy], [rustfmt]                                                                                       |
| Scala           | [scalafmt]                                                                                                |
| Security        | [nancy], [trivy], [tfsec], [osv-scanner], [trufflehog]                                                    |
| SQL             | [sqlfluff], [sqlfmt], [sql-formatter]                                                                     |
| SVG             | [svgo]                                                                                                    |
| Swift           | [stringslint], [swiftlint], [swiftformat]                                                                 |
| Terraform       | [terraform] (validate and fmt), [checkov], [tflint]<sup><a href="#note-tflint">2</a></sup>, [tfsec]       |
| TOML            | [taplo]                                                                                                   |
| Typescript      | [eslint], [prettier], [rome], [semgrep]                                                                   |
| YAML            | [prettier], [semgrep], [yamllint]                                                                         |

[actionlint]: https://github.com/rhysd/actionlint#readme
[ansible-lint]: https://github.com/ansible/ansible-lint#readme
[autopep8]: https://github.com/hhatto/autopep8#readme
[bandit]: https://github.com/PyCQA/bandit#readme
[black]: https://github.com/psf/black#readme
[brakeman]: https://github.com/presidentbeef/brakeman#readme
[buf]: https://github.com/bufbuild/buf#readme
[buildifier]: https://github.com/bazelbuild/buildtools/blob/master/buildifier/README.md
[checkov]: https://github.com/bridgecrewio/checkov#readme
[cfnlint]: https://github.com/aws-cloudformation/cfn-lint#readme
[circleci]: https://github.com/CircleCI-Public/circleci-cli#readme
[clang-format]: https://clang.llvm.org/docs/ClangFormat.html
[clang-tidy]: https://clang.llvm.org/extra/clang-tidy/
[clippy]: https://github.com/rust-lang/rust-clippy#readme
[codespell]: https://github.com/codespell-project/codespell#readme
[cspell]: https://github.com/streetsidesoftware/cspell#readme
[cue-fmt]: https://cuelang.org/
[detekt]: https://github.com/detekt/detekt#readme
[djlint]: https://github.com/Riverside-Healthcare/djlint#readme
[dotenv-linter]: https://github.com/dotenv-linter/dotenv-linter#readme
[eslint]: https://github.com/eslint/eslint#readme
[flake8]: https://github.com/PyCQA/flake8#readme
[git-diff-check]: https://git-scm.com/docs/git-diff
[gitleaks]: https://github.com/zricethezav/gitleaks#readme
[gofmt]: https://pkg.go.dev/cmd/gofmt
[gofumpt]: https://pkg.go.dev/mvdan.cc/gofumpt
[goimports]: https://pkg.go.dev/golang.org/x/tools/cmd/goimports
[gokart]: https://github.com/praetorian-inc/gokart
[golangci-lint]: https://github.com/golangci/golangci-lint#readme
[golines]: https://pkg.go.dev/github.com/segmentio/golines
[google-java-format]: https://github.com/google/google-java-format#readme
[hadolint]: https://github.com/hadolint/hadolint#readme
[haml-lint]: https://github.com/sds/haml-lint#readme
[include-what-you-use]: https://github.com/include-what-you-use/include-what-you-use#readme
[isort]: https://github.com/PyCQA/isort#readme
[ktlint]: https://github.com/pinterest/ktlint#readme
[kube-linter]: https://github.com/stackrox/kube-linter#readme
[markdownlint]: https://github.com/DavidAnson/markdownlint#readme
[mypy]: https://github.com/python/mypy#readme
[nancy]: https://github.com/sonatype-nexus-community/nancy#readme
[nixpkgs-fmt]: https://github.com/nix-community/nixpkgs-fmt
[oxipng]: https://github.com/shssoichiro/oxipng#readme
[osv-scanner]: https://github.com/google/osv-scanner
[pragma-once]: linters/pragma-once/readme.md
[prettier]: https://github.com/prettier/prettier#readme
[pylint]: https://github.com/PyCQA/pylint#readme
[remark-lint]: https://github.com/remarkjs/remark-lint#readme
[renovate]: https://github.com/renovatebot/renovate#readme
[rome]: https://github.com/rome/tools#readme
[rubocop]: https://github.com/rubocop/rubocop#readme
[ruff]: https://github.com/charliermarsh/ruff
[rufo]: https://github.com/ruby-formatter/rufo#readme
[rustfmt]: https://github.com/rust-lang/rustfmt#readme
[scalafmt]: https://github.com/scalameta/scalafmt#readme
[semgrep]: https://github.com/returntocorp/semgrep#readme
[shellcheck]: https://github.com/koalaman/shellcheck#readme
[shfmt]: https://github.com/mvdan/sh#readme
[sort-package-json]: https://github.com/keithamus/sort-package-json#readme
[sql-formatter]: https://github.com/sql-formatter-org/sql-formatter#readme
[sqlfluff]: https://github.com/sqlfluff/sqlfluff#readme
[sqlfmt]: https://github.com/tconbeer/sqlfmt#readme
[standardrb]: https://github.com/testdouble/standard#readme
[stringslint]: https://github.com/dral3x/StringsLint#readme
[stylelint]: https://github.com/stylelint/stylelint#readme
[stylua]: https://github.com/JohnnyMorganz/StyLua/tree/main
[sourcery]: https://sourcery.ai/
[svgo]: https://github.com/svg/svgo#readme
[swiftformat]: https://github.com/nicklockwood/SwiftFormat#readme
[swiftlint]: https://github.com/realm/SwiftLint#readme
[taplo]: https://github.com/tamasfe/taplo#readme
[terraform]: https://developer.hashicorp.com/terraform/cli/code
[tflint]: https://github.com/terraform-linters/tflint#readme
[tfsec]: https://github.com/aquasecurity/tfsec
[trivy]: https://github.com/aquasecurity/trivy#readme
[trufflehog]: https://github.com/trufflesecurity/trufflehog/
[yamllint]: https://github.com/adrienverge/yamllint#readme
[yapf]: https://github.com/google/yapf#readme

<sup><ol>

<li><a aria-hidden="true" tabindex="-1" class="customAnchor" id="note-detekt"></a>
Support for Detekt is under active development; see our <a href="https://docs.trunk.io/docs/check-supported-linters#detekt">docs</a> for more
details.
</li>

<li><a aria-hidden="true" tabindex="-1" class="customAnchor" id="note-tflint"></a>
<a href="https://github.com/terraform-linters/tflint/blob/master/docs/user-guide/module-inspection.md">Module inspection</a>, <a href="https://github.com/terraform-linters/tflint-ruleset-aws/blob/master/docs/deep_checking.md">deep checking</a>, and setting variables are not currently supported.
</li>

</ol></sup>

## How it works

Trunk downloads everything it needs to run on demand and caches it in `~/.cache/trunk`. We run
linters in parallel, in the background, and function as a
[language server](https://microsoft.github.io/language-server-protocol) to show results inline in
VSCode via the [Trunk VSCode Extension][vscode].

## Install the CLI

The `trunk` command line tool runs locally on your developer machine, right where your code is. Later you can automatically scan your repo using Trunk Check Cloud.

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

This will scan your repository and create a `.trunk/trunk.yaml` which enables all the linters, formatters, and security analyzers that [Trunk Check](./) recommends. For more details, see [here](cli/init-in-a-git-repo.md).

{% hint style="info" %}
Security-conscious users may want to also record the signature of the CLI, which the [Trunk Launcher](reference/components.md#trunk-launcher) will use to verify the CLI's provenance:

```
trunk init --lock
```
{% endhint %}

## Install the VSCode Extension

If you run VSCode you can also install the [trunk VSCode extension](vscode:extension/Trunk.io). Read more about it [here](https://marketplace.visualstudio.com/items?itemName=Trunk.io).

## Run `trunk check`

`trunk` is git-aware, so without further arguments it will run on the files you've changed in your repo:

```bash
trunk check
```

Note: if you have no modified any files, `trunk check` will not check anything. See the [CLI usage docs](cli/usage.md) for more info on basic `trunk` usage.
