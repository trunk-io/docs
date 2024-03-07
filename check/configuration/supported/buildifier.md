---
description: buildifier is a linter for Bazel, Starlark
---

**buildifier** is a linter for Bazel, Starlark.

You can enable the buildifier plugin with

```shell
trunk check enable buildifier
```

# Settings

buildifier uses the same config files as the
upstream [buildifier](https://github.com/bazelbuild/buildtools/blob/master/buildifier/README.md) project, so you can continue to use any
existing configuration files (ex: `.buildifier.json`, `.buildifier-tables.json`).
    

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/buildifier) if your project does not already have one,
which you can see in our [open source plugins repo](https://github.com/trunk-io/plugins/tree/main).
