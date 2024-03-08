---
description: SQLFluff is a dialect-flexible and configurable SQL linter.


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

**SQLFluff** is a linter for SQL.

You can enable the SQLFluff plugin with

```shell
trunk check enable sqlfluff
```

## Settings


**SQLFluff** uses the same config files as the
upstream [SQLFluff](https://github.com/sqlfluff/sqlfluff) project, so you can continue to use any
existing configuration files (ex: `.sqlfluff`).
    

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/sqlfluff) if your project does not already have one,
which you can see in our [open source plugins repo](https://github.com/trunk-io/plugins/tree/main).

Sqlfluff is only configured as a linter by default because its formatting capabilities are limited. To turn sqlfluff formatting on, enable its subcommand:

```yaml
lint:
  enabled:
    - sqlfluff@<version>:
      commands: [lint, fix]
```


