---
description: Prettier - Code Formatter
---

# Prettier

Prettier is a formatter for JavaScript.

You can enable the Prettier plugin with

```shell
trunk check enable prettier
```

# Settings

Prettier uses the same config files as the 
upstream [Prettier](https://prettier.io/) project, so you can continue to use any
existing configuration files (ex: `.prettierrc`, `.prettierrc.json`, `.prettierrc.yml`).

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/prettier) if your project does not already have one,
which you can see in our [open source plugins repo](https://github.com/trunk-io/plugins/tree/main).


By default, Trunk uses Prettier to autoformat many languages/config formats, including markdown. To line wrap within markdown, you need to set the following in your [Prettier config](https://prettier.io/docs/en/configuration.html) `.prettierrc.yaml`, etc.

```yaml
proseWrap: always
```
You may also want to configure `printWidth` to your liking.



