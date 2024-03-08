---
description: perlcritic is a linter for Perl
title: Trunk | How to run perlcritic
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

# perlcritic

[**perlcritic**](https://metacpan.org/pod/Perl::Critic) is a linter for Perl.

You can enable the perlcritic linter with:

```shell
trunk check enable perlcritic
```

## Settings

**perlcritic** uses the same config files as the
upstream [perlcritic](https://metacpan.org/pod/Perl::Critic) project, so you can continue to use any
existing configuration files (ex: `.perlcriticrc`).You can move these files to `.trunk/configs` and `trunk check` will still find them. [See Moving Linter Configs ](..#moving-linter-configs) for more info.

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/perlcritic) if your project does not already have one,
which you can see in our [open source plugins repo]().



## Links

* [perlcritic site](https://metacpan.org/pod/Perl::Critic)
* perlcritic Trunk Check [integration source](https://github.com/trunk-io/plugins/tree/main/linters/perlcritic)
* Trunk Check's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
