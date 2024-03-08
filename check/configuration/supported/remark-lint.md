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

## Settings

**remark-lint** uses the same config files as the
upstream [remark-lint](https://github.com/remarkjs/remark-lint#readme) project, so you can continue to use any
existing configuration files (ex: `.remarkrc`, `.remarkrc.json`, `.remarkrc.cjs`).You can move these files to `.trunk/configs` and `trunk check` will still find them. [See Moving Linter Configs ](..#moving-linter-configs) for more info.

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/remark-lint) if your project does not already have one,
which you can see in our [open source plugins repo]().



## Links

* [remark-lint site](https://github.com/remarkjs/remark-lint#readme)
* remark-lint Trunk Check [integration source](https://github.com/trunk-io/plugins/tree/main/linters/remark-lint)
* Trunk Check's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
