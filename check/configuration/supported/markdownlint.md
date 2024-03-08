---
description: Markdownlint is a tool designed to enforce consistency for Markdown files. It can include checks for headings, lists, line length, and syntax preferences. 
title: Trunk | How to run Markdownlint
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

# Markdownlint

[**Markdownlint**](https://github.com/DavidAnson/markdownlint) is a linter for Markdown.

You can enable the Markdownlint linter with:

```shell
trunk check enable markdownlint
```

## Settings

**Markdownlint** uses the same config files as the
upstream [Markdownlint](https://github.com/DavidAnson/markdownlint) project, so you can continue to use any
existing configuration files (ex: `.markdownlint.json`, `.markdownlint.yaml`, `.markdownlint.yml`).You can move these files to `.trunk/configs` and `trunk check` will still find them. [See Moving Linter Configs ](..#moving-linter-configs) for more info.

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/markdownlint) if your project does not already have one,
which you can see in our [open source plugins repo]().

Older versions of `markdownlint` had a bug where it printed plaintext output even when run with `--json`. We rely on JSON output so we can parse and ingest the results from markdownlint. The package we use for markdownlint is actually [markdownlint-cli ](https://www.npmjs.com/package/markdownlint-cli) `>= 0.29.0` is verified to work.





## Links

* [Markdownlint site](https://github.com/DavidAnson/markdownlint)
* Markdownlint Trunk Check [integration source](https://github.com/trunk-io/plugins/tree/main/linters/markdownlint)
* Trunk Check's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
