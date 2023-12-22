# Check

## What is Trunk Check?

**Trunk Check** runs 100+ idiomatic code-checking tools for every language and technology, locally ([CLI](cli/), [VS Code Extension](https://marketplace.visualstudio.com/items?itemName=trunk.io)), on CI ([CI](check-cloud-ci-integration/), [GitHub Bot](check-cloud-ci-integration/get-started/)), and in our [web app](https://app.trunk.io). You're probably already running a few of these tools (eslint, prettier, etc), but Trunk Check adds valuable features to let you integrate with CI and PRs, run them faster, upgrade them easier, integrate them with CI and PRs, version them better, and much more.

Check handles:

* Autoformatting code, config files, IaC, and more
* Linting
* Static Analysis
* Optimizing images
* Flagging leaked secrets
* Flagging open-source dependencies with vulnerabilities

## What problems does Trunk Check solve?

#### If I turn on a new rule or code-checking tool, how do I handle the zillion existing issues in my repo?

'[Hold the line](under-the-hood.md#hold-the-line)' is a Trunk Check feature that works for _all_ tools Trunk Check runs. It detects which issues are preexisting or not, in a sophisticated way (we correctly handle the cases in which you modify one line of code and it causes new issues downstream of that). By default, we only call _new_ issues "blocking issues" for the purposes of gating PRs and running `trunk check` locally.

This is the #1 feature driving why large companies purchase Trunk Check licenses. Without this, turning on a new linting rule may counter-intuitively _increase_ your tech debt. This typically happens because you force every modified file to be clean of errors in pull requests. In real life, this means devs optimize for touching as few files as possible to avoid cleaning up all the issues they didn't affect. Things like renaming a class or function across many files will never be done, because a simple find+replace turns into an effort of fixing a hundred lint issues just to merge it. Plus, fixing unrelated issues to your changes is just a poor separation of responsibilities for pull requests.

#### There are more tools I could run, but they're not in the package manager my repo uses

In the world of code checking, more is more! Let's say you have a mostly javascript/typescript repo, so your package manager ecosystem is npm. You have other technologies in the repo though, maybe some bash scripts, dockerfiles, kube config, ci yaml, and all of those technologies have great checking tools that you could be running, but some are golang, some are direct downloads, some are python, and they aren't available on npm. You don't want to bring a bunch of new package managers into your repo for these 1-off tools. That's where Trunk Check comes in. You version these tools in `.trunk/trunk.yaml`, and trunk can fetch them and run them from all the package managers or direct downloads you _don't_ use in your repo.

#### Static analysis is slow

Trunk Check has a daemon that checks code as you modify files in your repo, runs linting in batches, and caches off the results for many linters. Since it's git-aware, it knows what you've changed, and by adding batched execution and caching, you end up with a much faster and smoother way to run these tools.

#### PRs often fail our "Lint" CI job and need one or more extra iterations to fix it

PR iterations kill productivity. Every time a dev updates a PR, even trivially, they have to context switch, break out of flow, reviewers also context switch to look at it, and that's not to mention the CI time to run a new suite of jobs.

`trunk check` shows the _same_ results locally and [on CI](check-cloud-ci-integration/). It can optionally also function as a[git-hooks.md](actions/git-hooks.md "mention") manager to reject `git push`es unless they're passing `trunk check`.

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

When you modify a file, Trunk Check has a feature called Hold The Line, which only flags the _new_ issues. It does this by being git-aware and using sophisticated heuristics (to handle the case where you change one line of code and new issues pop up somewhere else because of it).

This feature is critical for eng orgs because it allows you to start leveling up your codebase without making devs fix every preexisting issue in every file they touch, which would dramatically slow down development and cause a lot of frustration. Without this feature, it's impractical to turn on new rules in existing code-checking tools, but it's also impractical to add new tools to your code-checking arsenal. With it, adding a new tool is as easy as `trunk check enable <linter>`, and you can start being better going forward and tackle your tech debt incrementally, on your own terms.

## Supported Linters, Formatters, and Security Tools

We integrate new linters every release. Stop by on [Slack](https://slack.trunk.io) and let us know what you'd like next! All tool integrations are open-source [here](https://github.com/trunk-io/plugins).

Enable the following tools:

```bash
trunk check enable <linter>
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

Trunk downloads everything it needs to run on demand and caches it in `~/.cache/trunk`. We run linters in parallel, in the background, and function as a [language server](https://microsoft.github.io/language-server-protocol) to show results inline in VSCode via the [Trunk VSCode Extension](./#install-the-vscode-extension).

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

Note: if you have not modified any files, `trunk check` will not check anything. See the [CLI usage docs](usage/) for more info on basic `trunk` usage.
