---
title: Trunk | How to run standardrb
description: standardrb is a linter for Ruby
---

# standardrb

[**standardrb**](https://github.com/testdouble/standard#readme) is a linter for Ruby.

You can enable the standardrb linter with:

```shell
trunk check enable standardrb
```

## Auto Enabling

standardrb will be auto-enabled if a `.standard.yml` config file is present.

## Settings

standardrb supports the following config files:

* `.standard.yml`

You can move these files to `.trunk/configs` and `trunk check` will still find them. See [Moving Linters](../configure-linters.md#moving-linters) for more info.

To keep the configuration usable by both Trunk and any locally bundled or externally invoked `standard` binary (for example when running `bundle exec standardrb` or using editor integrations), it is recommended to keep `.standard.yml` in the repository root rather than under `.trunk/configs`.

### Customization

By default, Trunk uses the `standardrb` integration shipped from the [`trunk-io/plugins`](https://github.com/trunk-io/plugins) repository. If you need to control how `standardrb` is installed (for example, to add additional Ruby plugins such as `standard-rails`, `standard-performance`, or `rubocop-capybara`), you can override the tool definition in your `.trunk/trunk.yaml`.

The example below configures `standardrb` as a Ruby runtime-based tool, installs the `standard` gem, exposes the `standardrb` shim, and asks Trunk to install a set of extra plugin gems into the same hermetic runtime. Trunk will manage these dependencies for you, independent of your system Ruby.

`.trunk/trunk.yaml`

```yaml
tools:
  definitions:
    - name: standardrb
      runtime: ruby
      package: standard
      shims: [standardrb]
      extra_packages:
        - standard-rails
        - standard-performance
        - rubocop-capybara
lint:
  enabled:
    - standardrb
  ignore:
    - linters: [standardrb]
      paths:
        - bin/**
        - db/**
        - vendor/**
        - tmp/**
        - log/**
        - storage/**
        - coverage/**
        - uploads/**
```

The `lint.ignore` block tells Trunk not to run `standardrb` on third-party or cached code. These ignore patterns are evaluated by Trunk and live alongside any ignores you configure directly for `standardrb`.

`.standard.yml`

```yaml
fix: true
parallel: true
format: progress

plugins:
  - standard-rails
  - standard-performance
  - rubocop-capybara

ignore:
  - bin/**/*
  - db/*
  - vendor/**/*
  - tmp/**/*
  - log/**/*
  - storage/**/*
  - coverage/**/*
  - uploads/**/*
```

## Links

* [standardrb site](https://github.com/testdouble/standard#readme)
* standardrb Trunk Code Quality [integration source](https://github.com/trunk-io/plugins/tree/main/linters/standardrb)
* Trunk Code Quality's [open source plugins repo](https://github.com/trunk-io/plugins/tree/main)
