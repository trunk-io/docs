---
description: ShellCheck- Script Analysis Tool for Shell Scripts
---

# ShellCheck

ShellCheck is a linter for Bash.

You can enable the ShellCheck plugin with

```shell
trunk check enable shellcheck
```

# Settings

ShellCheck uses the same config files as the 
upstream [ShellCheck](https://www.shellcheck.net/) project, so you can continue to use any
existing configuration files (ex: `.shellcheckrc`, `shellcheckrc`).

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/shellcheck) if your project does not already have one,
which you can see in our [open source plugins repo](https://github.com/trunk-io/plugins/tree/main).
