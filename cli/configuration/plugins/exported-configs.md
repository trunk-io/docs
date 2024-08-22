---
description: Reusing linter configs across projects.
---

# Exporting Linter Configs

Plugin repositories can also export their own linter config files in order to keep configuration synced across an organization. Simply add an `exported_configs` section to a `plugin.yaml`, with paths to all of the config files you want to export, relative to the repository root. For example:

```yaml
lint:
  exported_configs:
    - configs:
        - .eslintrc.yaml
        - .trunk/configs/.shellcheckrc
```

These config files will be available for linters that enumerate them in `affects_cache`or `direct_configs` to reference. These files are automatically symlinked into the repository root during linter execution. The set of applicable config files can be viewed in the details yaml file listed when running `trunk check --verbose`.

Plugin-exported configs are sourced in lockstep with the plugin itself, so you will need to update\
the `ref` field in order to use the latest configs.

Note that if you're using an IDE Extension like clangd with an LSP that relies on those configs being in the root, you will need to manually create a symlink to the plugin's config. You can do this by running `ln -s .trunk/plugins/<plugin-id>/<path-to-config> <name-of-config>`.

For an example of a plugin repo with config files, see our own [configs](https://github.com/trunk-io/configs) repo.

### Importing Configs

This process can also be reversed in order to import config files from a plugins repository which\
does not explicitly export them. Given a plugin sourced with id `trunk`, the sourcing repository can\
achieve the same effect by including the following in its `.trunk/trunk.yaml`.

```yaml
lint:
  exported_configs:
    - plugin_id: trunk
      configs:
        - .eslintrc.yaml
        - .trunk/configs/.shellcheckrc
```
