---
description: Fast Go linters runner. It runs linters in parallel, uses caching, supports yaml config, has integrations with all major IDE and has dozens of linters included.
title: Trunk | How to run golangci-lint
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

# golangci-lint

[**golangci-lint**](https://github.com/golangci/golangci-lint) is a linter for Go.

You can enable the golangci-lint linter with:

```shell
trunk check enable golangci-lint
```

## Settings

**golangci-lint** uses the same config files as the
upstream [golangci-lint](https://github.com/golangci/golangci-lint) project, so you can continue to use any
existing configuration files (ex: `.golangci.json`, `.golangci.toml`, `.golangci.yaml`).You can move these files to `.trunk/configs` and `trunk check` will still find them. [See Moving Linter Configs ](..#moving-linter-configs) for more info.

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/golangci-lint) if your project does not already have one,
which you can see in our [open source plugins repo]().

Make sure your go version in `go.mod` matches Trunk's go runtime version. At the time of this writing, Trunk's default go runtime version is `1.21.0`. You can find out what it is via `trunk print-config`, and look for the `runtime` section, and you can override the default version in your `trunk.yaml` via:

```yaml
runtimes:
  enabled:
    - go@1.21.0
```




## Links

* [golangci-lint site](https://github.com/golangci/golangci-lint)
* golangci-lint Trunk Check [integration source](https://github.com/trunk-io/plugins/tree/main/linters/golangci-lint)
* Trunk Check's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
