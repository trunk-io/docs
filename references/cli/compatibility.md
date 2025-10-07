# Compatibility

### Linux

Trunk will run on most Linux flavors, including Ubuntu, Arch, and others. We do require glibc version 2.19 or later. Alpine Linux is not supported.

### macOS

Trunk will run on macOS version 10.15 or later.

### Windows

Trunk only supports Windows with the following versions and above:

<table><thead><tr><th width="112.33333333333331">Tool</th><th width="397">Where to Modify</th><th>Minimum Required Version</th></tr></thead><tbody><tr><td>CLI</td><td><code>cli</code> <code>version</code> in <code>.trunk/trunk.yaml</code></td><td><code>1.13.0</code></td></tr><tr><td>Plugins</td><td><code>ref</code> for the <code>trunk</code> plugin in <code>.trunk/trunk.yaml</code></td><td><code>v1.0.0</code></td></tr><tr><td>VSCode</td><td>Reload VSCode to update</td><td><code>3.4.4</code></td></tr></tbody></table>

You will also need to install [C and C++ runtime libraries](https://aka.ms/vs/17/release/vc_redist.x64.exe) to run some linters.

#### Getting in touch

Thank you for being a beta tester of Trunk Check on Windows! We are actively working to improve the experience. If you have any feedback or questions, please contact us directly on [Slack](https://slack.trunk.io/).

If you want to override a repo-wide setting just for your Windows machine, you can modify your [`.trunk/user.yaml`](configuration/per-user-overrides.md).

#### Supported features

We intend to bring full feature support to Windows for Trunk. Currently, the following features are supported:

* [Trunk Code Quality](../../code-quality/code-quality.md)
* Non-interactive [Trunk Actions](getting-started/actions/) and [git-hooks](getting-started/actions/git-hooks.md)
* [VSCode](../../code-quality/ide-integration/vscode.md)

### Plugin compatibility

{% hint style="info" %}
This section was last updated for Plugins v1.2.0
{% endhint %}

Trunk runs most linters on all platforms. However, some linters are not yet supported on Windows. For a full list of all linters, see our [Plugins repo](https://github.com/trunk-io/plugins).

<table data-full-width="false"><thead><tr><th>Linter</th><th>Plans for Support</th></tr></thead><tbody><tr><td>ansible-lint</td><td>Only supported on WSL</td></tr><tr><td>clang-format</td><td>Long-term plans for LLVM linter support</td></tr><tr><td>clang-tidy</td><td>Long-term plans for LLVM linter support</td></tr><tr><td>detekt-gradle</td><td>Long-term plans for support</td></tr><tr><td>include-what-you-use</td><td>Long-term plans for LLVM linter support</td></tr><tr><td>nixpkgs-fmt</td><td>Long-term plans for support</td></tr><tr><td>perlcritic</td><td>No immediate plans for support</td></tr><tr><td>perltidy</td><td>No immediate plans for support</td></tr><tr><td>scalafmt</td><td>No download available for Windows</td></tr><tr><td>semgrep</td><td>No download available for Windows</td></tr><tr><td>shellcheck</td><td>No download available for Windows</td></tr><tr><td>stringslint</td><td>Only supported on MacOS</td></tr><tr><td>swiftformat</td><td>Only supported on MacOS</td></tr><tr><td>swiftlint</td><td>Only supported on MacOS</td></tr><tr><td>taplo</td><td>No download available for Windows</td></tr></tbody></table>

### Backward compatibility

We generally strive to maintain backward compatibility between the [Trunk Launcher](install.md#the-trunk-launcher) and the Trunk binary, but you may need to occasionally upgrade the launcher to support the newest version of Trunk.
