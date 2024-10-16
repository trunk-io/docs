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

SQLFluff will be auto-enabled if a `.sqlfluff` config file is present.

## Settings

SQLFluff supports the following config files:
* `.sqlfluff`

You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linters](../configure-linters#moving-linters) for more info.
Trunk Code Quality provides a default `.sqlfluff` if your project does not already have one.

## Usage Notes

Sqlfluff is only configured as a linter by default because its formatting capabilities are limited. To turn sqlfluff formatting on, enable its subcommand:

```yaml
lint:
  enabled:
    - sqlfluff@<version>:
      commands: [lint, fix]
```




## Links

- [SQLFluff site](https://github.com/sqlfluff/sqlfluff)
- SQLFluff Trunk Code Quality [integration source](https://github.com/trunk-io/plugins/tree/main/linters/sqlfluff)
- Trunk Code Quality's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
