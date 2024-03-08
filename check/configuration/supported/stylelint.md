---
description: stylelint is a linter for CSS, SCSS
title: Trunk | How to run stylelint
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

# stylelint

[**stylelint**](https://github.com/stylelint/stylelint#readme) is a linter for CSS, SCSS.

You can enable the stylelint linter with:

```shell
trunk check enable stylelint
```

## Settings

**stylelint** uses the same config files as the
upstream [stylelint](https://github.com/stylelint/stylelint#readme) project, so you can continue to use any
existing configuration files (ex: `stylelint.config.js`, `.stylelintrc.js`, `stylelint.config.mjs`).You can move these files to `.trunk/configs` and `trunk check` will still find them. [See Moving Linter Configs ](..#moving-linter-configs) for more info.

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/stylelint) if your project does not already have one,
which you can see in our [open source plugins repo]().



## Links

* [stylelint site](https://github.com/stylelint/stylelint#readme)
* stylelint Trunk Check [integration source](https://github.com/trunk-io/plugins/tree/main/linters/stylelint)
* Trunk Check's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
