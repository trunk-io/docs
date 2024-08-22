---
description: cspell is a linter for All
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

# cspell

[**cspell**](https://github.com/streetsidesoftware/cspell#readme) is a linter for All.

You can enable the cspell linter with:

```shell
trunk check enable cspell
```

![cspell example output](../../configuration/supported/cspell.gif)

## Auto Enabling

cspell will never be auto-enabled. It must be enabled manually.

## Settings

cspell supports the following config files:

* `.cspell.json`
* `cspell.json`
* `.cSpell.json`
* `cSpell.json`
* `cspell.config.js`
* `cspell.config.cjs`
* `cspell.config.json`
* `cspell.config.yaml`
* `cspell.config.yml`
* `cspell.yaml`
* `cspell.yml`

You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linter Configs](broken-reference) for more info. Trunk Code Quality provides a default `cspell.yaml` if your project does not already have one.

## Links

* [cspell site](https://github.com/streetsidesoftware/cspell#readme)
* cspell Trunk Code Quality [integration source](https://github.com/trunk-io/plugins/tree/main/linters/cspell)
* Trunk Code Quality's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
