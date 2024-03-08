---
description: Explore our guide on Actionlint, the linter for Github Actions. Learn about its features, installation, and configuration.
title: Trunk | How to run Actionlint
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

# Actionlint

[**Actionlint**](https://github.com/rhysd/actionlint) is a linter for GitHub.

You can enable the Actionlint linter with:

```shell
trunk check enable actionlint
```

## Auto Enabling

Actionlint will be auto-enabled if any of the following filetypes are present: *github-workflow*

## Settings

Actionlint supports the following config files:
* `.github/actionlint.yaml`
* `.github/actionlint.yml`

 Unlike with most tools under `trunk check`, these files cannot be moved.





## Links

- [Actionlint site](https://github.com/rhysd/actionlint)
- Actionlint Trunk Check [integration source](https://github.com/trunk-io/plugins/tree/main/linters/actionlint)
- Trunk Check's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
