---
description: graphql-schema-linter is a linter for GraphQL
title: Trunk | How to run graphql-schema-linter
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

# graphql-schema-linter

[**graphql-schema-linter**](https://github.com/cjoudrey/graphql-schema-linter#readme) is a linter for GraphQL.

You can enable the graphql-schema-linter linter with:

```shell
trunk check enable graphql-schema-linter
```

## Settings

**graphql-schema-linter** uses the same config files as the
upstream [graphql-schema-linter](https://github.com/cjoudrey/graphql-schema-linter#readme) project, so you can continue to use any
existing configuration files (ex: `.graphql-schema-linter.config.js`, `.graphql-schema-linterrc`).You can move these files to `.trunk/configs` and `trunk check` will still find them. [See Moving Linter Configs ](..#moving-linter-configs) for more info.

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/graphql-schema-linter) if your project does not already have one,
which you can see in our [open source plugins repo]().



## Links

* [graphql-schema-linter site](https://github.com/cjoudrey/graphql-schema-linter#readme)
* graphql-schema-linter Trunk Check [integration source](https://github.com/trunk-io/plugins/tree/main/linters/graphql-schema-linter)
* Trunk Check's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
