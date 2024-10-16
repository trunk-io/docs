---
description: Static code analysis for Kotlin
title: Trunk | How to run Detekt
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

# Detekt

[**Detekt**](https://github.com/detekt/detekt) is a linter for Kotlin.


detekt is composed of several linter commands.
    
`detekt` runs detekt with the built-in default config and any overrides in `.detekt.yaml`.

You can enable the `detekt` linter with:

```shell
trunk check enable detekt
```

`detekt-explicit` disables the default config and uses `.detekt.yaml` as the source of truth.

You can enable the `detekt-explicit` linter with:

```shell
trunk check enable detekt-explicit
```

`detekt-gradle` runs detekt using Gradle. Only use if you already are using Gradle for the rest of your build setup.

You can enable the `detekt-gradle` linter with:

```shell
trunk check enable detekt-gradle
```


## Auto Enabling

Detekt will never be auto-enabled. It must be enabled manually.

## Settings

Detekt supports the following config files:
* `.detekt.yaml`

You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linters](../configure-linters#moving-linters) for more info.


## Usage Notes

Detekt is usually invoked through gradle, which allows specifying additional configuration in `build.gradle`. We do not yet automatically parse your Gradle scripts to infer your `detekt` configuration; instead, what we do is this:

* `detekt` invokes [`detekt-cli`](https://detekt.github.io/detekt/cli.html) with the `--build-upon-default-config` flag (this appears to be [more common](https://cs.github.com/?q=%2FbuildUponDefaultConfig.*%28true%29%2F+detekt) than the alternative).

* `detekt-explicit` invokes [`detekt-cli`](https://detekt.github.io/detekt/cli.html) without the `--build-upon-default-config` flag.

You will also need to provide a valid detekt config as `.detekt.yaml` (an empty `.detekt.yaml` is valid, if you don't want to configure `detekt`). If you already have a detekt config, then you can symlink it like so:

```bash
ln -s path/to/existing/detekt-config.yml .detekt-config.yaml
```
To use `./gradlew detekt` to invoke Detekt, you can add `detekt-gradle@SYSTEM` to your `enabled` list. Note that since you're running Detekt via Gradle, you should also add the paths to your Detekt configurations to `direct_configs`, e.g.

```undefined
direct_configs: ["lib/detekt.yaml"]
```




## Links

- [Detekt site](https://github.com/detekt/detekt)
- Detekt Trunk Code Quality [integration source](https://github.com/trunk-io/plugins/tree/main/linters/detekt)
- Trunk Code Quality's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
