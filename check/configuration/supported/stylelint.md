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

**stylelint** is a linter for CSS, SCSS.

You can enable the stylelint plugin with

```shell
trunk check enable stylelint
```

## Settings


**stylelint** uses the same config files as the
upstream [stylelint](https://github.com/stylelint/stylelint#readme) project, so you can continue to use any
existing configuration files (ex: `stylelint.config.js`, `.stylelintrc.js`, `stylelint.config.mjs`).
    

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/stylelint) if your project does not already have one,
which you can see in our [open source plugins repo](https://github.com/trunk-io/plugins/tree/main).
