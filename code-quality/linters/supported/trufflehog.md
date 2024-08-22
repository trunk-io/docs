---
description: >-
  Discover Trufflehog with our detailed guide. Learn installation,
  configuration, usage, and how to integrate it with other linters for optimal
  code security.
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

# Trufflehog

[**Trufflehog**](https://github.com/trufflesecurity/trufflehog) is a linter for Security.

trufflehog is composed of several linter commands.

`trufflehog` runs trufflehog normally.

You can enable the `trufflehog` linter with:

```shell
trunk check enable trufflehog
```

`trufflehog-git` also runs trufflehog on the git history.

You can enable the `trufflehog-git` linter with:

```shell
trunk check enable trufflehog-git
```

## Auto Enabling

Trufflehog will be auto-enabled if any _ALL_ files are present.

## Links

* [Trufflehog site](https://github.com/trufflesecurity/trufflehog)
* Trufflehog Trunk Code Quality [integration source](https://github.com/trunk-io/plugins/tree/main/linters/trufflehog)
* Trunk Code Quality's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
