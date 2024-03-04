# Supported Linters

> 📘 Our linter integrations are open-source!
>
> You can find them at [`trunk-io/plugins`](https://github.com/trunk-io/plugins).

Enable any of the following tools with:

```
trunk check enable <linter>
```

[//]: #
[//]: # "1. Support for Detekt is under active development; see our [docs](https://docs.trunk.io/docs/check-supported-linters#detekt) for more details."
[//]: # "2. [Module inspection](https://github.com/terraform-linters/tflint/blob/master/docs/user-guide/module-inspection.md), [deep checking](https://github.com/terraform-linters/tflint-ruleset-aws/blob/master/docs/deep_checking.md), and setting variables are not currently supported."
[//]: #
[//]: # "### Linter-specific Configuration"
[//]: #
[//]: # "Some linters require a bit more modification to properly set up. View page for the particular linter for more info."

| Technology | Linters |
| ---------- | ------- |
| All | [codespell](https://github.com/codespell-project/codespell#readme), [cspell](https://github.com/streetsidesoftware/cspell#readme), [git-diff-check](https://git-scm.com/docs/git-diff), [gitleaks](./gitleaks.md), [pre-commit-hooks](https://pre-commit.com/hooks.html)|
| Ansible | [ansible-lint](./ansible-lint.md)|
| Apex | [pmd](https://pmd.github.io/)|
| Bash | [shellcheck](./shellcheck.md), [shfmt](https://github.com/mvdan/sh#readme)|
| Bazel, Starlark | [buildifier](https://github.com/bazelbuild/buildtools/blob/master/buildifier/README.md)|
| C# | [dotnet-format](https://github.com/dotnet/format#readme)|
| C, C++ | [clang-format](./clang-format.md), [clang-tidy](./clang-tidy.md), [include-what-you-use](https://github.com/include-what-you-use/include-what-you-use#readme), [pragma-once](https://github.com/trunk-io/plugins/blob/main/linters/pragma-once/README.md)|
| CircleCI Config | [circleci](https://github.com/CircleCI-Public/circleci-cli#readme)|
| Cloudformation | [cfnlint](https://github.com/aws-cloudformation/cfn-lint#readme), [checkov](./checkov.md)|
| CSS, SCSS | [prettier](./prettier.md), [stylelint](https://github.com/stylelint/stylelint#readme)|
| Cue | [cue-fmt](https://cuelang.org)|
| Docker | [checkov](./checkov.md), [hadolint](https://github.com/hadolint/hadolint#readme)|
| Dotenv | [dotenv-linter](https://github.com/dotenv-linter/dotenv-linter#readme)|
| GitHub | [actionlint](./actionlint.md)|
| Go | [gofmt](https://pkg.go.dev/cmd/gofmt), [gofumpt](https://pkg.go.dev/mvdan.cc/gofumpt), [goimports](https://pkg.go.dev/golang.org/x/tools/cmd/goimports), [gokart](https://github.com/praetorian-inc/gokart), [golangci-lint](./golangci-lint.md), [golines](https://pkg.go.dev/github.com/segmentio/golines), [semgrep](https://github.com/returntocorp/semgrep#readme)|
| GraphQL | [graphql-schema-linter](https://github.com/cjoudrey/graphql-schema-linter#readme), [prettier](./prettier.md)|
| HAML | [haml-lint](https://github.com/sds/haml-lint#readme)|
| HTML Templates | [djlint](https://github.com/Riverside-Healthcare/djlint#readme)|
| Java | [google-java-format](https://github.com/google/google-java-format#readme), [pmd](https://pmd.github.io/), [semgrep](https://github.com/returntocorp/semgrep#readme)|
| Javascript | [deno](https://deno.land/manual), [eslint](./eslint.md), [prettier](./prettier.md), [rome](https://github.com/rome/tools#readme), [semgrep](https://github.com/returntocorp/semgrep#readme)|
| JSON | [deno](https://deno.land/manual), [eslint](./eslint.md), [prettier](./prettier.md), [semgrep](https://github.com/returntocorp/semgrep#readme)|
| Kotlin | [detekt](./detekt.md), [ktlint](https://github.com/pinterest/ktlint#readme)|
| Kubernetes | [kube-linter](https://github.com/stackrox/kube-linter#readme)|
| Lua | [stylua](https://github.com/JohnnyMorganz/StyLua/tree/main)|
| Markdown | [deno](https://deno.land/manual), [markdown-lint-check](https://github.com/tcort/markdown-link-check#readme), [markdownlint](./markdownlint.md), [prettier](./prettier.md), [remark-lint](https://github.com/remarkjs/remark-lint#readme)|
| Nix | [nixpkgs-fmt](https://github.com/nix-community/nixpkgs-fmt)|
| package.json | [sort-package-json](https://github.com/keithamus/sort-package-json#readme)|
| Perl | [perlcritic](https://metacpan.org/pod/Perl::Critic), [perltidy](https://metacpan.org/dist/Perl-Tidy/view/bin/perltidy)|
| PNG | [oxipng](./oxipng.md)|
| Prisma | [prisma](https://github.com/prisma/prisma#readme)|
| Protobuf | [buf](https://github.com/bufbuild/buf#readme), [clang-format](./clang-format.md), [clang-tidy](./clang-tidy.md)|
| Python | [autopep8](https://github.com/hhatto/autopep8#readme), [bandit](./bandit.md), [black](./black.md), [flake8](./flake8.md), [isort](./isort.md), [mypy](https://github.com/python/mypy#readme), [pylint](./pylint.md), [pyright](https://github.com/microsoft/pyright), [ruff](./ruff.md), [semgrep](https://github.com/returntocorp/semgrep#readme), [sourcery](https://sourcery.ai/), [yapf](https://github.com/google/yapf#readme)|
| Renovate | [renovate](https://github.com/renovatebot/renovate#readme)|
| Ruby | [brakeman](./brakeman.md), [rubocop](https://github.com/rubocop/rubocop#readme), [rufo](https://github.com/ruby-formatter/rufo#readme), [semgrep](https://github.com/returntocorp/semgrep#readme), [standardrb](https://github.com/testdouble/standard#readme)|
| Rust | [clippy](./clippy.md), [rustfmt](./rustfmt.md)|
| Scala | [scalafmt](https://github.com/scalameta/scalafmt#readme)|
| Security | [checkov](./checkov.md), [dustilock](https://github.com/Checkmarx/dustilock), [nancy](https://github.com/sonatype-nexus-community/nancy#readme), [osv-scanner](./osv-scanner.md), [terrascan](https://github.com/tenable/terrascan#readme), [tfsec](https://github.com/aquasecurity/tfsec), [trivy](./trivy.md), [trufflehog](./trufflehog.md)|
| SQL | [sql-formatter](https://github.com/sql-formatter-org/sql-formatter#readme), [sqlfluff](./sqlfluff.md), [sqlfmt](https://github.com/tconbeer/sqlfmt#readme)|
| SVG | [svgo](./svgo.md)|
| Swift | [stringslint](https://github.com/dral3x/StringsLint#readme), [swiftformat](https://github.com/nicklockwood/SwiftFormat#readme), [swiftlint](https://github.com/realm/SwiftLint#readme)|
| Terraform | [checkov](./checkov.md), [terraform](./terraform.md), [terrascan](https://github.com/tenable/terrascan#readme), [tflint](https://github.com/terraform-linters/tflint#readme), [tfsec](https://github.com/aquasecurity/tfsec)|
| Terragrunt | [terragrunt](https://terragrunt.gruntwork.io/docs/getting-started/quick-start/)|
| Terrascan | [terrascan](https://github.com/tenable/terrascan#readme)|
| Textproto | [txtpbfmt](https://github.com/protocolbuffers/txtpbfmt/)|
| TOML | [taplo](https://github.com/tamasfe/taplo#readme)|
| Typescript | [deno](https://deno.land/manual), [eslint](./eslint.md), [prettier](./prettier.md), [rome](https://github.com/rome/tools#readme), [semgrep](https://github.com/returntocorp/semgrep#readme)|
| YAML | [prettier](./prettier.md), [semgrep](https://github.com/returntocorp/semgrep#readme), [yamllint](./yamllint.md)|
