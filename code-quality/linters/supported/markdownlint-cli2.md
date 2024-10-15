---
description: markdownlint-cli2 is a linter for Markdown
title: Trunk | How to run markdownlint-cli2
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

# markdownlint-cli2

[**markdownlint-cli2**](https://github.com/DavidAnson/markdownlint-cli2) is a linter for Markdown.

You can enable the markdownlint-cli2 linter with:

```shell
trunk check enable markdownlint-cli2
```

## Auto Enabling

markdownlint-cli2 will be auto-enabled if any of its config files are present: *`.markdownlint-cli2.jsonc`, `.markdownlint-cli2.yaml`, `.markdownlint-cli2.cjs`*.

## Settings

markdownlint-cli2 supports the following config files:
* `.markdownlint-cli2.jsonc`
* `.markdownlint-cli2.yaml`
* `.markdownlint-cli2.cjs`
* `.markdownlint-cli2.mjs`

You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linter Configs](..#moving-linter-configs) for more info.




## Links

- [markdownlint-cli2 site](https://github.com/DavidAnson/markdownlint-cli2)
- markdownlint-cli2 Trunk Code Quality [integration source](https://github.com/trunk-io/plugins/tree/main/linters/markdownlint-cli2)
- Trunk Code Quality's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
