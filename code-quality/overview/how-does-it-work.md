# How does it work?

### The CLI Tool

Trunk Code Quality still runs your favorite open-source linting, formatting, and static analysis tools and uses the same config files.

Trunk gives superpowers to these tools by installing, managing, running, and re-throwing consistent output from them with the **Trunk CLI.** The Trunk CLI written in C++ is free, fully configurable, extensible, lightweight, and fast. It runs the tools according to Trunk's config files and can run these tools only on the lines or files change, which makes it **practical for large code bases**.

[Learn more about the Trunk CLI.](../../references/cli/)

### Hold-the-line

**Hold The Line** (HTL) is the principle that Trunk Code Quality will _only run on new changes_ in your codebase rather than every file in the whole repo. This allows you to use Check to improve your codebase **incrementally** rather than having to address all of the issues at once. HTL also runs checks much faster than scanning the entire codebase would.

_Hold The Line_ **works at the line level** of your source code. For example, if a single line has multiple pre-existing issues and a new linter is added, which reports the new issue, then Trunk Code Quality will report just the new issue and not the previous ones.

By default, Trunk runs in hold-the-line mode:

```
trunk check foo.file
```

You can still run on all files.

```
trunk check --all
```

_**Hold the Line**_ is built into Trunk Code Quality itself. This means existing linters that do not support line-by-line functionality will still work with _Hold the Line_. Even [custom linters](../linters/custom-linters.md) you write yourself.

### Daemon

The Trunk CLI, specifically `trunk check`, runs a daemon that monitors relevant file changes and triggers jobs to precompute in the background while you work. The daemon is used both to support real-time background checking in supported extensions such as [VSCode](../ide-integration/vscode.md) and [Neovim](../ide-integration/neovim.md), and to precompute check results for faster commits/pushes.

Some native linters are more compute/memory intensive and `check` allows you to disable background linting for those tools. By default, linters run whenever a file is modified in the background. You can override this behavior by editing the [`run_when`](../../references/cli/configuration/lint/commands.md#run_when) configuration for a tool.

### Hermetic tools and runtime management

Trunk hermetically installs the static analysis tools you run and their required runtimes. This means these tools are installed and managed by the Trunk CLI, and are unaffected by your systems environment.

If a tool requires `python 3.10` but the projects you're working on require `python 3.7`, Trunk will manage that tool and its `python 3.10` runtime automatically and not affect the `python 3.7` environment. This means Trunk will not modify or pollute your machine.

Trunk manages the hermetic installation of all required runtimes. You can also specifically pin a version of a runtime you'd like Trunk to use, or tell Trunk to re-use an already-installed runtime on the system.

### Plugin system

Trunk is fully extensible and configurable through the [Trunk Plugins Repo](https://github.com/trunk-io/plugins/). When installing a plugin through Trunk, the definition of a plugin's behavior, including install, run, and report instructions, is defined in the Plugins Repo.

This can be overridden by defining your own plugin repo to import, overriding individual linter definitions locally, and even writing your own custom linters.

[Learn more about the plugin system.](../../references/cli/configuration/plugins/)

### Run on every PR

Trunk works in CI. Trunk Code Quality provides [GitHub integration](../ci-setup/github-integration.md) and can run in any other CI environment. This lets you check Code Quality in every PR with consistent config and consistent results.

[Learn more about Code Quality in CI.](../setup-and-installation/prevent-new-issues.md)
