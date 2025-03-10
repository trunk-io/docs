---
description: Trunk Code Quality supports over 100 linters and formatters
---

# Supported Linters

{% hint style="info" %}
#### 📘 Our linter integrations are open-source!

You can find them at [`trunk-io/plugins`](https://github.com/trunk-io/plugins), contributions are welcome!
{% endhint %}

Enable any of the following tools with:

```
trunk check enable <linter>
```

| Technology      | Linters                                                                                                                                                                                                                                                   |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| All             | [codespell](codespell.md), [cspell](cspell.md), [git-diff-check](git-diff-check.md), [gitleaks](gitleaks.md), [pre-commit-hooks](pre-commit-hooks.md)                                                                                                     |
| Ansible         | [ansible-lint](ansible-lint.md)                                                                                                                                                                                                                           |
| Apex            | [pmd](pmd.md)                                                                                                                                                                                                                                             |
| Bash            | [shellcheck](shellcheck.md), [shfmt](shfmt.md)                                                                                                                                                                                                            |
| Bazel, Starlark | [buildifier](buildifier.md)                                                                                                                                                                                                                               |
| C#              | [dotnet-format](dotnet-format.md)                                                                                                                                                                                                                         |
| C, C++          | [clang-format](clang-format.md), [clang-tidy](clang-tidy.md), [cmake-format](cmake-format.md), [iwyu](iwyu.md), [pragma-once](pragma-once.md)                                                                                                             |
| CircleCI Config | [circleci](circleci.md)                                                                                                                                                                                                                                   |
| Cloudformation  | [cfnlint](cfnlint.md), [checkov](checkov.md)                                                                                                                                                                                                              |
| CSS, SCSS       | [prettier](prettier.md), [stylelint](stylelint.md)                                                                                                                                                                                                        |
| Cue             | [cue-fmt](cue-fmt.md)                                                                                                                                                                                                                                     |
| Dart            | [dart](dart.md)                                                                                                                                                                                                                                           |
| Docker          | [checkov](checkov.md), [hadolint](hadolint.md)                                                                                                                                                                                                            |
| Dotenv          | [dotenv-linter](dotenv-linter.md)                                                                                                                                                                                                                         |
| GitHub          | [actionlint](actionlint.md)                                                                                                                                                                                                                               |
| Go              | [gofmt](gofmt.md), [gofumpt](gofumpt.md), [goimports](goimports.md), [gokart](gokart.md), [golangci-lint](golangci-lint.md), [golines](golines.md), [semgrep](semgrep.md)                                                                                 |
| GraphQL         | [graphql-schema-linter](graphql-schema-linter.md), [prettier](prettier.md)                                                                                                                                                                                |
| HAML            | [haml-lint](haml-lint.md)                                                                                                                                                                                                                                 |
| HTML Templates  | [djlint](djlint.md)                                                                                                                                                                                                                                       |
| Java            | [google-java-format](google-java-format.md), [pmd](pmd.md), [semgrep](semgrep.md)                                                                                                                                                                         |
| JavaScript      | [biome](biome.md), [deno](deno.md), [eslint](eslint.md), [prettier](prettier.md), [rome](rome.md), [semgrep](semgrep.md)                                                                                                                                  |
| JSON            | [deno](deno.md), [eslint](eslint.md), [prettier](prettier.md), [semgrep](semgrep.md)                                                                                                                                                                      |
| json            | [biome](biome.md)                                                                                                                                                                                                                                         |
| jsx             | [biome](biome.md)                                                                                                                                                                                                                                         |
| Kotlin          | [detekt](detekt.md), [ktlint](ktlint.md)                                                                                                                                                                                                                  |
| Kubernetes      | [kube-linter](kube-linter.md)                                                                                                                                                                                                                             |
| Lua             | [stylua](stylua.md)                                                                                                                                                                                                                                       |
| Markdown        | [deno](deno.md), [markdown-link-check](markdown-link-check.md), [markdown-table-prettify](markdown-table-prettify.md), [markdownlint](markdownlint.md), [markdownlint-cli2](markdownlint-cli2.md), [prettier](prettier.md), [remark-lint](remark-lint.md) |
| Nix             | [nixpkgs-fmt](nixpkgs-fmt.md)                                                                                                                                                                                                                             |
| package.json    | [sort-package-json](sort-package-json.md)                                                                                                                                                                                                                 |
| Perl            | [perlcritic](perlcritic.md), [perltidy](perltidy.md)                                                                                                                                                                                                      |
| PHP             | [php-cs-fixer](php-cs-fixer.md), [phpstan](phpstan.md)                                                                                                                                                                                                    |
| PNG             | [oxipng](oxipng.md)                                                                                                                                                                                                                                       |
| PowerShell      | [psscriptanalyzer](psscriptanalyzer.md)                                                                                                                                                                                                                   |
| Prisma          | [prisma](prisma.md)                                                                                                                                                                                                                                       |
| prose           | [vale](vale.md)                                                                                                                                                                                                                                           |
| Protobuf        | [buf](buf.md), [clang-format](clang-format.md), [clang-tidy](clang-tidy.md)                                                                                                                                                                               |
| Python          | [autopep8](autopep8.md), [bandit](bandit.md), [black](black.md), [flake8](flake8.md), [isort](isort.md), [mypy](mypy.md), [pylint](pylint.md), [pyright](pyright.md), [ruff](ruff.md), [semgrep](semgrep.md), [sourcery](sourcery.md), [yapf](yapf.md)    |
| Rego            | [opa](opa.md), [regal](regal.md)                                                                                                                                                                                                                          |
| Renovate        | [renovate](renovate.md)                                                                                                                                                                                                                                   |
| Ruby            | [brakeman](brakeman.md), [rubocop](rubocop.md), [rufo](rufo.md), [semgrep](semgrep.md), [standardrb](standardrb.md)                                                                                                                                       |
| Rust            | [clippy](clippy.md), [rustfmt](rustfmt.md)                                                                                                                                                                                                                |
| Scala           | [scalafmt](scalafmt.md)                                                                                                                                                                                                                                   |
| Security        | [checkov](checkov.md), [dustilock](dustilock.md), [nancy](nancy.md), [osv-scanner](osv-scanner.md), [terrascan](terrascan.md), [tfsec](tfsec.md), [trivy](trivy.md), [trufflehog](trufflehog.md)                                                          |
| SQL             | [sql-formatter](sql-formatter.md), [sqlfluff](sqlfluff.md), [sqlfmt](sqlfmt.md), [squawk](squawk.md)                                                                                                                                                      |
| SVG             | [svgo](svgo.md)                                                                                                                                                                                                                                           |
| Swift           | [stringslint](stringslint.md), [swiftformat](swiftformat.md), [swiftlint](swiftlint.md)                                                                                                                                                                   |
| Terraform       | [checkov](checkov.md), [terraform](terraform.md), [terrascan](terrascan.md), [tflint](tflint.md), [tfsec](tfsec.md), [tofu](tofu.md)                                                                                                                      |
| Terragrunt      | [terragrunt](terragrunt.md)                                                                                                                                                                                                                               |
| Terrascan       | [terrascan](terrascan.md)                                                                                                                                                                                                                                 |
| Textproto       | [txtpbfmt](txtpbfmt.md)                                                                                                                                                                                                                                   |
| TOML            | [taplo](taplo.md)                                                                                                                                                                                                                                         |
| TypeScript      | [biome](biome.md), [deno](deno.md), [eslint](eslint.md), [prettier](prettier.md), [rome](rome.md), [semgrep](semgrep.md)                                                                                                                                  |
| YAML            | [prettier](prettier.md), [semgrep](semgrep.md), [yamllint](yamllint.md)                                                                                                                                                                                   |

{% hint style="success" %}
#### Can't find a linter you need?

Chat with Trunk's engineers and suggest your ideas. Join us and 1500+ fellow engineers [on Slack](https://slack.trunk.io/).
{% endhint %}

