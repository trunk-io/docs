---
description: haml-lint is a linter for HAML
title: Trunk | How to run haml-lint
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

# haml-lint

[**haml-lint**](https://github.com/sds/haml-lint#readme) is a linter for HAML.

You can enable the haml-lint linter with:

```shell
trunk check enable haml-lint
```

## Auto Enabling

haml-lint will be auto-enabled if any of the following filetypes are present: *haml*

## Settings

haml-lint supports the following config files:
* `.haml-lint.yml`

 You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linter Configs](..#moving-linter-configs) for more info.



## Links

- [haml-lint site](https://github.com/sds/haml-lint#readme)
- haml-lint Trunk Check [integration source](https://github.com/trunk-io/plugins/tree/main/linters/haml-lint)
- Trunk Check's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
