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

## Auto Enabling

scalafmt will be auto-enabled if a `.scalafmt.conf` config file is present.

## Settings

scalafmt supports the following config files:
* `.scalafmt.conf`

You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linters](../configure-linters#moving-linters) for more info.




## Links

- [scalafmt site](https://github.com/scalameta/scalafmt#readme)
- scalafmt Trunk Code Quality [integration source](https://github.com/trunk-io/plugins/tree/main/linters/scalafmt)
- Trunk Code Quality's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
