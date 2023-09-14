---
description: >-
  Trunk Tools is a hermetic runtime and CLI tool manager. Seamlessly specify,
  install, and upgrade the tooling in your repository with Trunk Tools.
---

# Tools

#### Command Line

| trunk tools \<command>         | description                                                                    |
| ------------------------------ | ------------------------------------------------------------------------------ |
| list                           | list all available tools in the repository and whether they are enabled or not |
| install                        | install your enabled tools into `.trunk/tools`                                 |
| enable `<tool-name>[@version]` | enable the provided tool, optionally at a specified version                    |
| disable `<tool-name>`          | disable the provided tool                                                      |

#### Discovering Tools

The trunk [plugins](https://github.com/trunk-io/plugins) repo ships with a collection of tools that can help supercharge your repository and provide examples for how to write your own. To see a list of tools that you can enable in your own repo run:

```shell
trunk tools list
```



<figure><img src="../.gitbook/assets/image (7).png" alt=""><figcaption><p>list of available and enabled tools</p></figcaption></figure>

#### Running Tools

`Trunk` installs your enabled tools into the `.trunk/tools` directory. Each tool exposes as list of **shims** (these may or may not be identically named to the tool - most typically a tool has one shim matching the name of the tool). Each shim is installed into the `.trunk/tools` directory.

You can run your tools by referring to the path `<path to your workspace>/.trunk/tools/<shim name>` but this is unwieldy. We highly recommend using our shell hooks to manage your PATH. You can do so by adding to the config in your repo:

.trunk/trunk.yaml (For every user in repo)
.trunk/user.yaml  (Only for current user)
```
cli:
  shell_hooks:
    enforce: true
```
You will need to run a trunk command (like check or fmt) and it will update your shell RC file to load our hooks. 

After reloading your shell, whenever you're inside your repo at the command line, you can just run shims installed by `trunk tools` directly by name.

N.B. There is a known incompatibility with direnv. If you use direnv in your project, make sure that the direnv hooks are included AFTER the trunk hooks in your rc file.

Example:
```
test -f $HOME/.cache/trunk/shell-hooks/zsh.rc && source $HOME/.cache/trunk/shell-hooks/zsh.rc;
eval "$(direnv hook zsh)" # This needs to be second
```
