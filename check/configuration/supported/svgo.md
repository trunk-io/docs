---
description: SVGO, or Scalable Vector Graphics Optimizer, is a tool designed to optimize SVG files, making them smaller and more efficient without compromising on quality.
---

**SVGO** is a linter for SVG.

You can enable the SVGO plugin with

```shell
trunk check enable svgo
```

# Settings

SVGO uses the same config files as the
upstream [SVGO](https://github.com/svg/svgo) project, so you can continue to use any
existing configuration files (ex: `svgo.config.js`, `svgo.config.mjs`, `svgo.config.cjs`).
    

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/svgo) if your project does not already have one,
which you can see in our [open source plugins repo](https://github.com/trunk-io/plugins/tree/main).
