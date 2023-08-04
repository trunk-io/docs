# Windows Beta

> 📘 Trunk Check is available for beta on Windows!
>
> Try it out by following the instructions below.

### Getting Started

From **`git-bash` or `msys2`**, download the Bash launcher and add it to your `PATH`:

```bash
curl https://get.trunk.io -fsSL | bash
```

From **`powershell`**, download the powershell launcher:

```Text
Invoke-RestMethod -Uri https://trunk.io/releases/trunk.ps1 -OutFile trunk.ps1
```

Ensure you can execute powershell scripts:

```Text
Set-ExecutionPolicy Bypass -Scope CurrentUser
```

You can then execute trunk as `.\trunk.ps1`.

To use the Trunk **VSCode Extension**, merge the following into `.vscode/settings.json`:

```Text
{
  "trunk.enableWindows": true
}
```

Trunk only supports Windows with the following versions and above:

<table><thead><tr><th width="112.33333333333331">Tool</th><th width="397">Where to Modify</th><th>Minimum Required Version</th></tr></thead><tbody><tr><td>CLI</td><td><code>cli</code> <code>version</code> in <code>.trunk/trunk.yaml</code></td><td><code>1.13.0</code></td></tr><tr><td>Plugins</td><td><code>ref</code> for the <code>trunk</code> plugin in <code>.trunk/trunk.yaml</code></td><td><code>v1.0.0</code></td></tr><tr><td>VSCode</td><td>Reload VSCode to update</td><td><code>3.4.4</code></td></tr></tbody></table>

You will also need to install [C and C++ runtime libraries](https://aka.ms/vs/17/release/vc\_redist.x64.exe) in order to run some linters.

### Getting Help

Thank you for being a beta tester of Trunk Check on Windows! We are actively working to improve the experience. If you have any feedback or questions, please reach out to us directly on [Slack](https://slack.trunk.io/).

If you want to override a repo-wide setting just for your Windows machine, you can modify your [`.trunk/user.yaml`](../reference/user-yaml.md).

### Supported Features

We intend to bring full feature support to Windows for Trunk. Currently, the following features are supported:

* [Trunk Check](../check/)
* Non-interactive [Trunk Actions](../actions/) and [git-hooks](../actions/git-hooks.md)
* [VSCode](../reference/vs-code.md)

### Unsupported Linters

Trunk runs most linters on all platforms. However, some linters are not yet supported on Windows. For a full list of all linters, see our [Plugins repo](https://github.com/trunk-io/plugins).

| Linter               | Plans for Support                       |
| -------------------- | --------------------------------------- |
| ansible-lint         | Only supported on WSL                   |
| brakeman             | Long-term plans for ruby linter support |
| buf-breaking         | Short-term plans for support            |
| buf-format           | Short-term plans for support            |
| buf-lint             | Short-term plans for support            |
| checkov              | Short-term plans for support            |
| clang-format         | Long-term plans for LLVM linter support |
| clang-tidy           | Long-term plans for LLVM linter support |
| detekt               | Short-term plans for support            |
| detekt-explicit      | Short-term plans for support            |
| detekt-gradle        | Short-term plans for support            |
| graphql-schema       | Short-term plans for support            |
| haml-lint            | Long-term plans for ruby linter support |
| include-what-you-use | Long-term plans for LLVM linter support |
| ktlint               | Long-term plans for support             |
| mypy                 | Short-term plans for support            |
| nixpkgs-fmt          | Long-term plans for support             |
| perlcritic           | No immediate plans for support          |
| perltidy             | No immediate plans for support          |
| remark-lint          | Long-term plans for support             |
| rubocop              | Long-term plans for ruby linter support |
| rufo                 | Long-term plans for ruby linter support |
| scalafmt             | No download available for Windows       |
| semgrep              | No download available for Windows       |
| shellcheck           | No download available for Windows       |
| sort-package-json    | Long-term plans for support             |
| standardrb           | Long-term plans for ruby linter support |
| stringslint          | Only supported on MacOS                 |
| swiftformat          | Only supported on MacOS                 |
| swiftlint            | Only supported on MacOS                 |
| taplo                | No download available for Windows       |
