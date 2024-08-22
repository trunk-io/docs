---
description: stylelint is a linter for CSS, SCSS
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

## Auto Enabling

stylelint will be auto-enabled if any of its config files are present: _`stylelint.config.js`, `.stylelintrc.js`, `stylelint.config.mjs`_.

## Settings

stylelint supports the following config files:

* `stylelint.config.js`
* `.stylelintrc.js`
* `stylelint.config.mjs`
* `.stylelintrc.mjs`
* `stylelint.config.cjs`
* `.stylelintrc.cjs`
* `.stylelintrc.json`
* `.stylelintrc.yml`
* `.stylelintrc.yaml`
* `.stylelintrc`

You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linter Configs](broken-reference) for more info.

## Links

* [stylelint site](https://github.com/stylelint/stylelint#readme)
* stylelint Trunk Code Quality [integration source](https://github.com/trunk-io/plugins/tree/main/linters/stylelint)
* Trunk Code Quality's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
