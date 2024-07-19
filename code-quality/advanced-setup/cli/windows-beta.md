---
description: Using Trunk Check on Windows
---

# Windows Support (beta)

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

### Compatibility

Trunk only supports Windows with the following versions and above:

<table><thead><tr><th width="112.33333333333331">Tool</th><th width="397">Where to Modify</th><th>Minimum Required Version</th></tr></thead><tbody><tr><td>CLI</td><td><code>cli</code> <code>version</code> in <code>.trunk/trunk.yaml</code></td><td><code>1.13.0</code></td></tr><tr><td>Plugins</td><td><code>ref</code> for the <code>trunk</code> plugin in <code>.trunk/trunk.yaml</code></td><td><code>v1.0.0</code></td></tr><tr><td>VSCode</td><td>Reload VSCode to update</td><td><code>3.4.4</code></td></tr></tbody></table>

You will also need to install [C and C++ runtime libraries](https://aka.ms/vs/17/release/vc\_redist.x64.exe) in order to run some linters.

### Getting Help

Thank you for being a beta tester of Trunk Check on Windows! We are actively working to improve the experience. If you have any feedback or questions, please reach out to us directly on [Slack](https://slack.trunk.io/).

If you want to override a repo-wide setting just for your Windows machine, you can modify your [`.trunk/user.yaml`](../../reference/user-yaml.md).

### Supported Features

We intend to bring full feature support to Windows for Trunk. Currently, the following features are supported:

* [Trunk Check](../../)
* Non-interactive [Trunk Actions](../actions/) and [git-hooks](../actions/git-hooks.md)
* [VSCode](../../ide-integration/vs-code.md)

### Unsupported Linters (as of Plugins v1.2.0)

Trunk runs most linters on all platforms. However, some linters are not yet supported on Windows. For a full list of all linters, see our [Plugins repo](https://github.com/trunk-io/plugins).

<table data-full-width="false"><thead><tr><th>Linter</th><th>Plans for Support</th></tr></thead><tbody><tr><td>ansible-lint</td><td>Only supported on WSL</td></tr><tr><td>clang-format</td><td>Long-term plans for LLVM linter support</td></tr><tr><td>clang-tidy</td><td>Long-term plans for LLVM linter support</td></tr><tr><td>detekt-gradle</td><td>Long-term plans for support</td></tr><tr><td>include-what-you-use</td><td>Long-term plans for LLVM linter support</td></tr><tr><td>nixpkgs-fmt</td><td>Long-term plans for support</td></tr><tr><td>perlcritic</td><td>No immediate plans for support</td></tr><tr><td>perltidy</td><td>No immediate plans for support</td></tr><tr><td>scalafmt</td><td>No download available for Windows</td></tr><tr><td>semgrep</td><td>No download available for Windows</td></tr><tr><td>shellcheck</td><td>No download available for Windows</td></tr><tr><td>stringslint</td><td>Only supported on MacOS</td></tr><tr><td>swiftformat</td><td>Only supported on MacOS</td></tr><tr><td>swiftlint</td><td>Only supported on MacOS</td></tr><tr><td>taplo</td><td>No download available for Windows</td></tr></tbody></table>
