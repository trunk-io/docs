---
description: >-
  Trunk Tools is a hermetic runtime and CLI tool manager. Seamlessly specify,
  install, and upgrade the tooling in your repository with Trunk Tools.
---

# Tools

### Command Line

| trunk tools \<command>           | Description                                                                    |
| -------------------------------- | ------------------------------------------------------------------------------ |
| `list`                           | list all available tools in the repository and whether they are enabled or not |
| `install`                        | install your enabled tools into `.trunk/tools`                                 |
| `enable` `<tool-name>[@version]` | enable the provided tool, optionally at a specified version                    |
| `disable` `<tool-name>`          | disable the provided tool                                                      |

### Discovering Tools

The Trunk [plugins repo](https://github.com/trunk-io/plugins) ships with a collection of tools that can help supercharge your repository and provide examples for how to write your own. To see a list of tools that you can enable in your own repo run:

```shell
trunk tools list
```

<figure><img src="../../../.gitbook/assets/image (17).png" alt=""><figcaption><p>list of available and enabled tools</p></figcaption></figure>

### Running Tools

Trunk installs your enabled tools into the `.trunk/tools` directory. Each tool exposes a list of **shims** (these may or may not be identically named to the tool - most typically a tool has one shim matching the name of the tool). Each shim is installed into the `.trunk/tools` directory.

You can run your tools by referring to the path `<path-to-workspace>/.trunk/tools/<shim-name>` but this is unwieldy. We highly recommend using our shell hooks to manage your PATH.

Starting with CLI version `1.18.0`, you can do so by running `trunk shellhooks install`, which will install the Trunk hooks to the config file of your $SHELL. You can also run `trunk shellhooks install <shell_name>` to install a specific shell hook.

Supported shells:

* bash
* zsh
* tcsh
* fish
* elvish

For organization that want to require the use of the hooks, they can add to the config file:

```yaml
# .trunk/trunk.yaml:
version: 0.1
cli:
  shell_hooks:
    enforce: true
```

On the next Trunk command (like check or fmt), it will update your shell RC file to load our hooks.

After reloading your shell, whenever you're inside your repo at the command line, you can just run shims installed by `trunk tools` directly by name.

N.B. There is a known incompatibility with direnv when using PATH\_ADD. To use our hooks, remove PATH\_ADD from your .envrc and add them to your Trunk config as such:

```yaml
version: 0.1
cli:
  shell_hooks:
    path_add:
      - "${workspace}/tools"
```

Paths can either be absolute, or relative to the workspace using the special `${workspace}` variable

### Troubleshooting Linters

Tools enable you to run your linter binaries on the command line independent of `trunk check` and test and troubleshoot your integrations more easily. Read about [custom linters and hermetic installs](../../configuration/custom-linters/#hermetic-installs) for more info.
