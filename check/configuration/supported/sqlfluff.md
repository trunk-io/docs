---
description: SQLFluff is a dialect-flexible and configurable SQL linter.


title: Trunk | How to run SQLFluff
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

# SQLFluff

[**SQLFluff**](https://github.com/sqlfluff/sqlfluff) is a linter for SQL.

You can enable the SQLFluff linter with:

```shell
trunk check enable sqlfluff
```

## Auto Enabling

SQLFluff will be auto-enabled if any of its config files are present: *`.sqlfluff`*

## Settings

SQLFluff supports the following config files:
* `.sqlfluff`

 You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linter Configs](..#moving-linter-configs) for more info.Trunk check provides a default `.sqlfluff` if your project does not already have one.

Sqlfluff is only configured as a linter by default because its formatting capabilities are limited. To turn sqlfluff formatting on, enable its subcommand:

```yaml
lint:
  enabled:
    - sqlfluff@<version>:
      commands: [lint, fix]
```




## Links

- [SQLFluff site](https://github.com/sqlfluff/sqlfluff)
- SQLFluff Trunk Check [integration source](https://github.com/trunk-io/plugins/tree/main/linters/sqlfluff)
- Trunk Check's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
