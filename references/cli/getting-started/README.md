# Getting Started

Initializing Trunk in a git repo is as simple as running:

```bash
trunk init
```

This will scan your repository and create a `.trunk/trunk.yaml` file which enables all the linters, formatters, and security analyzers that [Trunk C](../../../code-quality/code-quality.md)[ode Quality ](../../../code-quality/code-quality.md)recommends.

{% hint style="info" %}
Security-conscious users may want to also record the signature of the CLI, which the [Trunk Launcher](../install.md#the-trunk-launcher) will use to verify the CLI's provenance:

```
trunk init --lock
```
{% endhint %}

### Discover CLI Use Cases

<table data-view="cards"><thead><tr><th data-card-target data-type="content-ref"></th><th data-hidden></th><th data-hidden></th><th data-hidden></th></tr></thead><tbody><tr><td><a href="../../../code-quality/code-quality.md">code-quality.md</a></td><td></td><td></td><td></td></tr><tr><td><a href="../../../merge-queue/managing-merge-queue/command-line.md">command-line.md</a></td><td></td><td></td><td></td></tr><tr><td><a href="tools.md">tools.md</a></td><td></td><td></td><td></td></tr><tr><td><a href="actions/">actions</a></td><td></td><td></td><td></td></tr><tr><td><a href="announce.md">announce.md</a></td><td></td><td></td><td></td></tr></tbody></table>

### Tweak the Configuration

Trunk is completely controlled through the `trunk.yaml` file. If for example you are not using the `check` tool you can safely remove the `lint` section from the file.

[Learn more about CLI configuration](../configuration/)

### Single-player Mode

If you want to run `trunk` inside your repository but are not ready to roll it out team-wide, you can run `trunk` in what we call single-player mode.

When in single-player mode, the `.trunk` directory will be listed in `.git/info/exclude`, which will cause git to ignore its contents. When trunk is automatically initialized by the vscode extension, you will be started in this mode. You can also initialize this way explicitly with the `trunk init --single-player-mode` command. If at any time you wish to toggle single-player mode on or off, it can be done with the following two commands:

```bash
# Turn single-player mode on.
trunk config hide
```

```bash
# Turn single-player mode off.
trunk config share
```

### Only enabling detected tools

`trunk init` supports the flags `--only-detected-formatters` and `--only-detected-linters`. Each of these flags limits `trunk init` to only enable tools that we detect you are already using.

We provide support for running `trunk` in GitHub Codespaces.

[Github Codespaces](https://github.com/features/codespaces) are fully configured virtual containers for developing your GitHub repositories.
