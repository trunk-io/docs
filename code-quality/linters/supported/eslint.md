---
description: ESLint statically analyzes your code to quickly find problems.
title: Trunk | How to run ESLint
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

[**ESLint**](https://eslint.org/) is a linter for JavaScript, JSON and TypeScript.

You can enable the ESLint linter with:

```shell
trunk check enable eslint
```

## Auto Enabling

ESLint will be auto-enabled if any of its config files are present: *`eslint.config.js`, `eslint.config.mjs`, `eslint.config.cjs`*.

## Settings

ESLint supports the following config files:
* `eslint.config.js`
* `eslint.config.mjs`
* `eslint.config.cjs`
* `.eslintrc`
* `.eslintrc.cjs`
* `.eslintrc.js`
* `.eslintrc.json`
* `.eslintrc.mjs`
* `.eslintrc.yaml`
* `.eslintrc.yml`

Unlike with most tools under `trunk check`, these files cannot be moved.


## Usage Notes

# ESLint >= 9.x
As of ESLint v9, all of the formatters have been removed. We suggest using [prettier](https://docs.trunk.io/check/configuration/supported/prettier) to format Javascript and Typescript code. The extra package mentioned below is no longer needed for ESLint v9 and higher.

# ESlint < 8.x
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




## Links

- [ESLint site](https://eslint.org/)
- ESLint Trunk Code Quality [integration source](https://github.com/trunk-io/plugins/tree/main/linters/eslint)
- Trunk Code Quality's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
