---
description: remark-lint is a linter for Markdown
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

**remark-lint** is a linter for Markdown.

You can enable the remark-lint plugin with

```shell
trunk check enable remark-lint
```

## Settings


**remark-lint** uses the same config files as the
upstream [remark-lint](https://github.com/remarkjs/remark-lint#readme) project, so you can continue to use any
existing configuration files (ex: `.remarkrc`, `.remarkrc.json`, `.remarkrc.cjs`).
    

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/remark-lint) if your project does not already have one,
which you can see in our [open source plugins repo](https://github.com/trunk-io/plugins/tree/main).
