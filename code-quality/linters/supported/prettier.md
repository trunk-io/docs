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
![prettier example output](/.gitbook/assets/prettier.gif)
## Auto Enabling

Prettier will be auto-enabled if any *TypeScript, Yaml, Css, Postcss, Sass, Html, Markdown, Json, JavaScript, Graphql or Prettier_supported_configs* files are present.

## Settings

Prettier supports the following config files:
* `.prettierrc`
* `.prettierrc.json`
* `.prettierrc.yml`
* `.prettierrc.yaml`
* `.prettierrc.json5`
* `.prettierrc.js`
* `.prettierrc.cjs`
* `.prettierrc.mjs`
* `prettier.config.js`
* `prettier.config.cjs`
* `prettier.config.mjs`
* `.prettierrc.toml`
* `.prettierignore`

You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linters](../configure-linters#moving-linters) for more info.


## Usage Notes



By default, Trunk uses Prettier to autoformat many languages/config formats, including markdown. To line wrap within markdown, you need to set the following in your [Prettier config](https://prettier.io/docs/en/configuration.html) `.prettierrc.yaml`, etc.

```yaml
proseWrap: always
```
You may also want to configure `printWidth` to your liking.





## Links

- [Prettier site](https://prettier.io/)
- Prettier Trunk Code Quality [integration source](https://github.com/trunk-io/plugins/tree/main/linters/prettier)
- Trunk Code Quality's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
