---
description: remark-lint is a linter for Markdown
title: Trunk | How to run remark-lint
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

# remark-lint

[**remark-lint**](https://github.com/remarkjs/remark-lint#readme) is a linter for Markdown.

You can enable the remark-lint linter with:

```shell
trunk check enable remark-lint
```

## Auto Enabling

remark-lint will be auto-enabled if any of its config files are present: *`.remarkrc`, `.remarkrc.json`, `.remarkrc.cjs`*.

## Settings

remark-lint supports the following config files:
* `.remarkrc`
* `.remarkrc.json`
* `.remarkrc.cjs`
* `.remarkrc.mjs`
* `.remarkrc.js`
* `.remarkrc.yaml`
* `.remarkrc.yml`

You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linter Configs](..#moving-linter-configs) for more info.
Trunk check provides a default `.remarkrc.yaml` if your project does not already have one.



## Links

- [remark-lint site](https://github.com/remarkjs/remark-lint#readme)
- remark-lint Trunk Check [integration source](https://github.com/trunk-io/plugins/tree/main/linters/remark-lint)
- Trunk Check's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
