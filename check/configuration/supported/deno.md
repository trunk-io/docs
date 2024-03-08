---
description: deno is a linter for JavaScript, JSON, TypeScript and Markdown
title: Trunk | How to run deno
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

# deno

[**deno**](https://deno.land/manual) is a linter for JavaScript, JSON, TypeScript and Markdown.

You can enable the deno linter with:

```shell
trunk check enable deno
```

## Settings

**deno** uses the same config files as the
upstream [deno](https://deno.land/manual) project, so you can continue to use any
existing configuration files (ex: `deno.json`, `deno.jsonc`).You can move these files to `.trunk/configs` and `trunk check` will still find them. [See Moving Linter Configs ](..#moving-linter-configs) for more info.

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/deno) if your project does not already have one,
which you can see in our [open source plugins repo]().



## Links

* [deno site](https://deno.land/manual)
* deno Trunk Check [integration source](https://github.com/trunk-io/plugins/tree/main/linters/deno)
* Trunk Check's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
