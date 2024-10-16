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

## Auto Enabling

graphql-schema-linter will be auto-enabled if any of its config files are present: *`.graphql-schema-linter.config.js`, `.graphql-schema-linterrc`*.

## Settings

graphql-schema-linter supports the following config files:
* `.graphql-schema-linter.config.js`
* `.graphql-schema-linterrc`

You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linters](../configure-linters#moving-linters) for more info.




## Links

- [graphql-schema-linter site](https://github.com/cjoudrey/graphql-schema-linter#readme)
- graphql-schema-linter Trunk Code Quality [integration source](https://github.com/trunk-io/plugins/tree/main/linters/graphql-schema-linter)
- Trunk Code Quality's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
