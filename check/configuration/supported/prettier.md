---
description: Explore  Prettier, the powerful code formatter. Learn how to install, configure, and effectively use Prettier to enhance your coding workflow.
title: Trunk | How to run Prettier
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

# Prettier

[**Prettier**](https://prettier.io/) is a formatter for CSS, SCSS, JavaScript, JSON, Markdown, TypeScript, GraphQL and YAML.

You can enable the Prettier formatter with:

```shell
trunk check enable prettier
```

## Settings

**Prettier** uses the same config files as the
upstream [Prettier](https://prettier.io/) project, so you can continue to use any
existing configuration files (ex: `.prettierrc`, `.prettierrc.json`, `.prettierrc.yml`).You can move these files to `.trunk/configs` and `trunk check` will still find them. [See Moving Linter Configs ](..#moving-linter-configs) for more info.

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/prettier) if your project does not already have one,
which you can see in our [open source plugins repo]().



By default, Trunk uses Prettier to autoformat many languages/config formats, including markdown. To line wrap within markdown, you need to set the following in your [Prettier config](https://prettier.io/docs/en/configuration.html) `.prettierrc.yaml`, etc.

```yaml
proseWrap: always
```
You may also want to configure `printWidth` to your liking.





## Links

* [Prettier site](https://prettier.io/)
* Prettier Trunk Check [integration source](https://github.com/trunk-io/plugins/tree/main/linters/prettier)
* Trunk Check's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
