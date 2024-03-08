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

## Auto Enabling

deno will be auto-enabled if any of its config files are present: *`deno.json`, `deno.jsonc`*

## Settings

deno supports the following config files:
* `deno.json`
* `deno.jsonc`

 You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linter Configs](..#moving-linter-configs) for more info.



## Links

- [deno site](https://deno.land/manual)
- deno Trunk Check [integration source](https://github.com/trunk-io/plugins/tree/main/linters/deno)
- Trunk Check's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
