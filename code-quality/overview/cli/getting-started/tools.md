# Tools

You can use the Trunk CLI to manage tools used by your repo. Trunk CLI can install the tools needed for a project according to what's configured in the `trunk.yaml` config file and let your teammates easily install the same versions of the tools. Trunk will also help you expose those installed tools by dynamically adding them to your `PATH` when you enter the project directory, but will not pollute your `PATH` outside of the project.

### Command line

| trunk tools \<command>           | Description                                                                    |
| -------------------------------- | ------------------------------------------------------------------------------ |
| `list`                           | list all available tools in the repository and whether they are enabled or not |
| `install`                        | install your enabled tools into `.trunk/tools`                                 |
| `enable` `<tool-name>[@version]` | enable the provided tool, optionally at a specified version                    |
| `disable` `<tool-name>`          | disable the provided tool                                                      |

### Discovering tools

The Trunk [plugins repo](https://github.com/trunk-io/plugins) ships with a collection of tools that can help supercharge your repository and provide examples for how to write your own. To see a list of tools that you can enable in your own repo run:

```shell
trunk tools list
```

<figure><img src="../../../../.gitbook/assets/image (17).png" alt=""><figcaption><p>list of available and enabled tools</p></figcaption></figure>

### Configuring shell hooks

Before running any tools managed by Trunk, enable shell hooks. With shell hooks, Trunk can manage your path variable dynamically, which lets you install tools used only in specific repos without polluting your shell by installing global tools. This is especially useful if you work on two repos using the same tool, but locked to different versions.

You can enable shell hooks by running `trunk shellhooks install`, which will install the Trunk hooks to the config file of your $SHELL. You can also run `trunk shellhooks install <shell_name>` to install a specific shell hook.

Supported shells:

* bash
* zsh
* tcsh
* fish
* elvish

For organizations that want to require the use of the hooks, they can add to the config file:

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

Paths can either be absolute, or relative to the workspace using the special `${workspace}` variable.

### Running tools

With shell hooks enabled, you can just run your tools by their name. For example, if you have run `trunk tools install grpcui` to install the GRPC UI tool, you can run it with:

<pre><code><strong>grpcui 
</strong></code></pre>

#### Running tools without shell hooks

Trunk installs your enabled tools into the `.trunk/tools` directory. Each tool exposes a list of **shims** (these may or may not be identically named to the tool - most typically a tool has one shim matching the name of the tool). Each shim is installed into the `.trunk/tools` directory.

You can run your tools by referring to the path `<path-to-workspace>/.trunk/tools/<shim-name>` but this is unwieldy. We highly recommend using our shell hooks to manage your PATH.

### Troubleshooting linters

Tools enable you to run your linter binaries on the command line independent of `trunk check` and test and troubleshoot your integrations more easily.

Tools are configured in the `tools` section of `trunk.yaml`. As with other settings, you can override these values in your [User YAML](configuration/per-user-overrides.md).

```yaml
tools:
  auto_sync: false # whether shims should be hot-reloaded off config changes.
  enabled:
    - bazel@6.0.0
    - mypy@1.4.1
    - ibazel@0.22.0
    - helm@3.9.4
    - eksctl@0.74.0
    - asciinema@2.1.0
  disabled:
    - gt
  definitions:
    - name: gh
      download: gh
      known_good_version: 2.27.0
      environment:
        - name: PATH
          list: ["${tool}/bin"]
      shims: [gh]
```

Like with actions and linters, we have a (versioned) `enabled` section and a `disabled` section, which can be manipulated using `trunk tools enable/disable`. There is also a list of `definitions`, which are merged across your `trunk.yaml`, `user.yaml`, as well as any plugins that you use.

`auto_sync` controls whether or not Trunk automatically installs your tools for you when your config changes. This defaults to `true`. Note that the daemon must be running with the monitor in order for this to function properly.
