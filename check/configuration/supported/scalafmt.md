---
description: scalafmt is a linter for Scala
---

**scalafmt** is a linter for Scala.

You can enable the scalafmt plugin with

```shell
trunk check enable scalafmt
```

# Settings

scalafmt uses the same config files as the
upstream [scalafmt](https://github.com/scalameta/scalafmt#readme) project, so you can continue to use any
existing configuration files (ex: `.scalafmt.conf`).
    

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/scalafmt) if your project does not already have one,
which you can see in our [open source plugins repo](https://github.com/trunk-io/plugins/tree/main).
