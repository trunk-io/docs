---
description: ESLint statically analyzes your code to quickly find problems.
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

# ESLint

**ESLint** is a linter for JavaScript, JSON and TypeScript.

You can enable the ESLint plugin with

```shell
trunk check enable eslint
```

## Settings


**ESLint** uses the same config files as the
upstream [ESLint](https://eslint.org/) project, so you can continue to use any
existing configuration files (ex: `.eslintrc`, `.eslintrc.cjs`, `.eslintrc.js`).
    

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/eslint) if your project does not already have one,
which you can see in our [open source plugins repo](https://github.com/trunk-io/plugins/tree/main).

Most ESLint users use a number of plugins, custom parsers, etc. Trunk has the ability to turn sandboxing and caching on or off for each linter, and we've turned it off for ESLint so it can use your repo's installed packages for ESLint plugins and other required ESLint packages. Trunk does control the ESLint version itself, but otherwise ESLint looks for all plugins, configs, etc. based on the path of source file it is linting. **This all means you do need to have ****npm/yarn install****'d in your repo as a prerequisite before running ESLint via trunk**.

We recommend you disable all Prettier rules in your ESLint config and let Trunk run Prettier automatically on your files. It's much nicer to just autoformat a file than to see a lint error for every missing space.

You can easily do this by adding the `eslint-config-prettier` package and in your ESLint config's `extends` section adding `prettier` as the last element. For example, your `extends` list might look like:



```yaml
extends:
  # Order matters, later configs purposefully override settings from earlier configs
  - eslint:recommended
  - airbnb
  - plugin:@typescript-eslint/recommended
  - plugin:import/recommended
  - plugin:import/typescript
  - plugin:node/recommended
  - plugin:mocha/recommended
  - plugin:react/recommended
  - prettier # this actually turns OFF all Prettier rules running via ESLint
```


