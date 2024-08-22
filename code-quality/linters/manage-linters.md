# Manage Linters

### Using the CLI

List all of the available linters

```sh
trunk check list
```

Enable a single linter

```sh
trunk check enable <linter name>
```

Disable a single linter

```sh
trunk check disable <linter name>
```

### Using Trunk Config Files

Trunk only runs linters listed in the `enabled` section; linters which are defined in `lint.definitions` but are not listed in `enabled` are not run.

When enabling a linter, you must specify a version for the linter:

```yaml
lint:
  enabled:
    # enabling a version with a linter
    - gitleaks@7.6.1
    - gofmt@1.16.7
    - golangci-lint@1.41.1
    - hadolint@2.6.0
```

Custom linters are slightly different; see [those docs](custom-linters.md) to learn more.

### Disable Linters

Trunk will continuously monitor your repository and make recommendations of additional new tools to run on your codebase. You can tell trunk not to recommend a specific linter by adding it to the disabled list.

```yaml
lint:
  disabled:
    # disabled a linter tells trunk not to recommend it during upgrade scans
    - rufo
    - tflint
```

### Upgrading Linters

Run `trunk upgrade` to update the Trunk CLI and all your plugins, linters, tools, and runtimes.
