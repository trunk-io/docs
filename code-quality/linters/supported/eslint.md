---
description: eslint is a linter for JavaScript, JSON and TypeScript
title: Trunk | How to run eslint
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

# eslint

[**eslint**](https://github.com/eslint/eslint#readme) is a linter for JavaScript, JSON and TypeScript.

You can enable the eslint linter with:

```shell
trunk check enable eslint
```

## Auto Enabling

eslint will be auto-enabled if any of its config files are present: *`eslint.config.js`, `eslint.config.mjs`, `eslint.config.cjs`*.

## Settings

eslint supports the following config files:
* `eslint.config.js`
* `eslint.config.mjs`
* `eslint.config.cjs`
* `.eslintrc`
* `.eslintrc.cjs`
* `.eslintrc.js`
* `.eslintrc.json`
* `.eslintrc.mjs`
* `.eslintrc.yaml`
* `.eslintrc.yml`

You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linter Configs](..#moving-linter-configs) for more info.




## Links

- [eslint site](https://github.com/eslint/eslint#readme)
- eslint Trunk Code Quality [integration source](https://github.com/trunk-io/plugins/tree/main/linters/eslint)
- Trunk Code Quality's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
