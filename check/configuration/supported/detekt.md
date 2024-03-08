---
description: Static code analysis for Kotlin
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

**Detekt** is a linter for Kotlin.

You can enable the Detekt plugin with

```shell
trunk check enable detekt
```

## Settings


**Detekt** uses the same config files as the
upstream [Detekt](https://github.com/detekt/detekt) project, so you can continue to use any
existing configuration files (ex: `.detekt.yaml`).
    

Trunk provides a [default configuration](https://github.com/trunk-io/plugins/tree/main/linters/detekt) if your project does not already have one,
which you can see in our [open source plugins repo](https://github.com/trunk-io/plugins/tree/main).

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


