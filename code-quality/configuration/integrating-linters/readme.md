---
description: Overview of defining linter integrations
---

# Integrating Linters

## Linter Integration

Trunk Code Quality's linter integrations are fully configurable. This means that you can easily tune existing linters or leverage our caching and [hold-the-line](../../reference/under-the-hood.md#hold-the-line) solution with your own custom linters.

## Lint Config Definitions

Lint configuration is done in the `lint` section of the trunk.yaml file. There are three parts:

* [Lint Config](reference/lint-config.md): defines overall linting.
* [Linter Definition](reference/linter-definition.md): definition of a single linter
* [Linter Command Definition](commands/definition.md): definition of a command within the linter

The final config used at runtime is created by importing `.yaml` files from the plugins repo for each linter, merging them into a tree structure, then overriding values from your repo's `trunk.yaml` file to yield the final configuration.

### Linter Definition

Every linter defined in `lint.definitions` must specify at least a name, the types of files it will run on, at least [one command](commands/), and `success_codes` or `error_codes`.

A complete linter definition defines the following:

* [**Enabling:**](enabling.md) When to auto-enable the linter. Should the linter be enabled when certain config files are available? See [Enabling](enabling.md) for more.
* [**Dependencies:**](dependencies.md) Where to get the linter and its dependencies from? If the linter uses a runtime like Python or NodeJS, then Trunk also needs to know what versions it needs, and any support packages. See [Dependencies](dependencies.md) for more.
* [**Files:**](files.md) When to use the linter. This includes which filetypes the linter uses, which files could potentially affect caching, and if the linter is idempotent. See [Files](files.md) for more.
* [**Commands:**](commands/) Once the final set of files are computed Trunk will invoke one of the linter's commands. A command defines the input targets, input sources, and the actual binary that is run for the command, and the exit codes to indicate success. See [Commands](commands/) for more.
* [**Outputs:**](commands/output-types.md) Trunk supports commands which produce output in one of [several standard formats](commands/output-types.md#output-types).
* [**Custom Parsers:**](commands/custom-parsers.md) Linters can also use [custom parsers](commands/custom-parsers.md) if needed.

### Execution Model

Running `trunk check` tells `trunk` to do the following:

* compute the set of modified files (by comparing the current working tree and `upstream-ref`,\
  usually your `main` or `master` branch)
* compute the set of lint actions to run based on the modified files
  * each enabled linter is invoked once per [applicable modified file](files.md#applicable-filetypes);
* [download](dependencies.md) and install any newly enabled linters/formatters
* execute uncached lint actions
* parse linter [outputs](commands/output-types.md) into configurable output types
* determine which lint issues are new, existing, or fixed
* present the list of issues to the user

### Reference

* [Reference of all Lint Config YAML fields](reference/lint-config.md)
* [Reference of all Linter Definition YAML fields](reference/linter-definition.md)
* [Reference of all Command Definition YAML fields](commands/definition.md)
* [Full Tutorial](https://trunk.io/blog/integrating-your-own-custom-tools-with-trunk-check) on creating a linter form scratch in NodeJS
