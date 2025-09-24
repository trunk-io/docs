---
title: Trunk | How to run deno
description: deno is a linter for JavaScript, JSON, TypeScript and Markdown
---

# deno

[**deno**](https://deno.land/manual) is a linter for JavaScript, JSON, TypeScript and Markdown.

You can enable the deno linter with:

```shell
trunk check enable deno
```

## Auto Enabling

deno will be auto-enabled if any of its config files are present: _`deno.json`, `deno.jsonc`_.

## Settings

deno supports the following config files:

* `deno.json`
* `deno.jsonc`

You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linters](../configure-linters.md#moving-linters) for more info.

## Links

* [deno site](https://deno.land/manual)
* deno Trunk Code Quality [integration source](https://github.com/trunk-io/plugins/tree/main/linters/deno)
* Trunk Code Quality's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
