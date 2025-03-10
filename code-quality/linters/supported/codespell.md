---
description: Codespell fixes common misspellings in text files. It's designed primarily to check misspelled words in source code.







title: Trunk | How to run codespell
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

# codespell

[**codespell**](https://github.com/codespell-project/codespell#readme) is a linter for All.

You can enable the codespell linter with:

```shell
trunk check enable codespell
```
![codespell example output](/.gitbook/assets/codespell.gif)
## Auto Enabling

codespell will be auto-enabled if a `.codespellrc` config file is present.

## Settings

codespell supports the following config files:
* `.codespellrc`

You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linters](../configure-linters.md#moving-linters) for more info.




## Links

- [codespell site](https://github.com/codespell-project/codespell#readme)
- codespell Trunk Code Quality [integration source](https://github.com/trunk-io/plugins/tree/main/linters/codespell)
- Trunk Code Quality's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
