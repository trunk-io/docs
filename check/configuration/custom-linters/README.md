---
description: Custom linter configuration overview
---

# Custom Linters

Trunk Check's linter integrations are fully configurable. This means that you can easily tune 
existing linters or leverage our caching and
[hold-the-line](../../reference/under-the-hood.md#hold-the-line) 
solution with your own custom linters. Let's walk through how a linter
integration works.


## Execution Model

Running `trunk check` tells `trunk` to do the following:

* compute the set of modified files (by comparing the current working tree and `upstream-ref`,\
  usually your `main` or `master` branch)
* compute the set of lint actions to run based on the modified files
  * each enabled linter is invoked once per [applicable modified file](./files.md#applicable-filetypes);
* [download](./dependencies.md) and install any newly enabled linters/formatters
* execute uncached lint actions
* parse linter [outputs](./output-types.md) into configurable output types
* determine which lint issues are new, existing, or fixed
* present the list of issues to the user


# Lint Config Definitions

Lint configuration is done in the `lint` section of the trunk.yaml file. There are three parts:

* [Lint Config](./lint-config.md)
* [Linter Definition](./linter-definition.md)
* [Linter Command Definition](./command-definition.md).

The top part represents the configuration of overall linting. Inside that
is the definition of individual linters. And inside *that* is the definition of the particular
command used to invoke the actual binary executable of the underlying tool.

The final config used at runtime is created by importing `.yaml` files from the plugins
repo for each linter, merging them into a tree structure, then overriding values
from your repo's `trunk.yaml` file to yield the final configuration.

## Linter Definition

Every linter defined in `lint.definitions` must specify at least a name, the types of files it 
will run on, at least [one command](commands.md), and `success_codes` or `error_codes`. A complete linter 
definition defines the following attributes of the linter.

* **Enabling:** When to auto-enable the linter. Should the linter be enabled when certain
config files are available? See [Enabling](common.md) for more.
* **Dependencies:** Where to get the linter and its dependencies from? If the linter uses a runtime like Python or NodeJS, then Trunk also needs to know what versions it needs, and any support packages. See [Dependencies](dependencies.md) for more.
* **Files:** When to use the linter. This includes which filetypes the linter
uses, which files could potentially affect caching, and if the linter
is idempotent. See [Files](files.md) for more.
* **Commands:** Once the final set of files are computed Trunk will invoke one of
the linter's commands. A command defines the input targets,
input sources, and the actual binary that is run for the command, and the exit codes to indicate success. See [Commands](commands.md) for more.
* **Outputs:** Trunk supports commands which produce output in one of [several
standard formats](output-types.md#output-types). 
* **Custom Parsers:** Linters can also use [custom parsers](custom-parsers.md) if needed. 



## Reference

* [reference of all YAML fields](reference.md)
* [Full Tutorial](https://trunk.io/blog/integrating-your-own-custom-tools-with-trunk-check) on creating a linter form scratch in NodeJS
* [JSON schema for `trunk.yaml`](https://static.trunk.io/pub/trunk-yaml-schema.json).
