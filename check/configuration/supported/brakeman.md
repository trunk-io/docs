---
description: Brakeman is a static analysis tool designed for Ruby on Rails applications. It statically analyzes Rails application code to find security issues.
title: Trunk | How to run Brakeman
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

# Brakeman

[**Brakeman**](https://github.com/presidentbeef/brakeman) is a linter for Ruby.

You can enable the Brakeman linter with:

```shell
trunk check enable brakeman
```

## Settings

**Brakeman** uses the same config files as the
upstream [Brakeman](https://github.com/presidentbeef/brakeman) project, so you can continue to use any
existing configuration files (ex: `brakeman.ignore`).You can move these files to `.trunk/configs` and `trunk check` will still find them. [See Moving Linter Configs ](..#moving-linter-configs) for more info.

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/brakeman) if your project does not already have one,
which you can see in our [open source plugins repo]().



## Links

* [Brakeman site](https://github.com/presidentbeef/brakeman)
* Brakeman Trunk Check [integration source](https://github.com/trunk-io/plugins/tree/main/linters/brakeman)
* Trunk Check's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
