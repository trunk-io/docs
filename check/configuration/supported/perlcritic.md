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

## Auto Enabling

perlcritic will be auto-enabled if any of its config files are present: *`.perlcriticrc`*

## Settings

perlcritic supports the following config files:
* `.perlcriticrc`

 You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linter Configs](..#moving-linter-configs) for more info.Trunk check provides a default `.perlcriticrc` if your project does not already have one.



## Links

- [perlcritic site](https://metacpan.org/pod/Perl::Critic)
- perlcritic Trunk Check [integration source](https://github.com/trunk-io/plugins/tree/main/linters/perlcritic)
- Trunk Check's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
