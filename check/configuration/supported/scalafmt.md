---
description: scalafmt is a linter for Scala
title: Trunk | How to run scalafmt
layout:
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
---

# scalafmt

[**scalafmt**](https://github.com/scalameta/scalafmt#readme) is a linter for Scala.

You can enable the scalafmt linter with:

```shell
trunk check enable scalafmt
```

## Settings

**scalafmt** uses the same config files as the
upstream [scalafmt](https://github.com/scalameta/scalafmt#readme) project, so you can continue to use any
existing configuration files (ex: `.scalafmt.conf`).You can move these files to `.trunk/configs` and `trunk check` will still find them. [See Moving Linter Configs ](..#moving-linter-configs) for more info.

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/scalafmt) if your project does not already have one,
which you can see in our [open source plugins repo]().



## Links

* [scalafmt site](https://github.com/scalameta/scalafmt#readme)
* scalafmt Trunk Check [integration source](https://github.com/trunk-io/plugins/tree/main/linters/scalafmt)
* Trunk Check's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
