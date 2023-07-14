# Overview

A plugins repository provides users the ability to expand the core capabilities of trunk check and trunk actions. A plugin repo contains a set of custom linter and action definitions.

#### Importing a plugin repository

By default trunk imports the trunk-io/plugins repository. To import a repo add it to the `plugins` list. Each repo requires a URI and ref.

```yaml
plugins:
  sources:
    - id: trunk
      uri: https://github.com/trunk-io/plugins
      ref: v0.0.15
      import_to_global: true
```

| field                              | description                                                                                                                                   |
| ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| id                                 | unique identifier for this repository                                                                                                         |
| uri                                | address used to clone the target repository                                                                                                   |
| ref                                | commit id or tag to checkout                                                                                                                  |
| local                              | path to local (on-disk) repository                                                                                                            |
| import\_to\_global (default: true) | import content into the global namespace. If set to false actions and linters defined in the plugin must be referenced by {plugin\_id}.{name} |

#### Custom linters and actions

The root of a plugin repository can have any number of `plugin.yaml` files where linters and actions are defined. The `plugin.yaml` files look a lot like a standard `trunk.yaml` file with the addition of a special field `required_trunk_version` at the root level `plugin.yaml`, which indicates the minimum trunk version required to use that repo. All configuration is then merged into one composite plugin configuration.

Beyond the `required_trunk_version` the definition of an action or linter is no different in a plugin repository.

\[block:tutorial-tile] { "backgroundColor": "#118cfd", "emoji": "🕹️", "id": "63c7408c98071300a4fd3236", "link": "https://docs.trunk.io/v0.17.0-beta/recipes/define-a-new-action", "slug": "define-a-new-action", "title": "Define a new action" } \[/block]

\[block:tutorial-tile] { "backgroundColor": "#fecb3e", "emoji": "🚀", "id": "63c7408c98071300a4fd3237", "link": "https://docs.trunk.io/v0.17.0-beta/recipes/define-a-new-linter", "slug": "define-a-new-linter", "title": "Define a new linter" } \[/block]

#### Add a plugin to your `trunk.yaml` file

To add a plugin from GitHub:

```
trunk plugins add https://github.com/trunk-io/plugins --id=trunk
```

To add a plugin from GitHub at a specific version:

```
trunk plugins add https://github.com/trunk-io/plugins v0.0.16 --id=trunk
```

To add a plugin from a local repository:

```
trunk plugins add /home/user/self/hello-world --id=hello-world
```

#### Contributing to a published plugin repository

Let's quickly walk through how to modify/add to an existing remote repository. In this case we'll make an edit to the trunk-io/plugins repository.

1. Clone the plugins repository to your local disk - `git clone git@github.com:trunk-io/plugins.git`
2. Make sure the `local` field in your `trunk.yaml` file points to your local instance. If a plugin source includes a `local` field, it will supercede the remote uri/ref values.

```yaml
plugins:
  sources:
    - id: trunk
      uri: https://github.com/trunk-io/plugins
      ref: v0.0.15
      local: .
```

3. Edit the entries in the local version of the plugin repository.
4. Push your changes to the remote version of the plugin repo.

#### Plugins scope

Plugins are merged serially, in the order that they are sourced, and can override almost any Trunk\
configuration. This allows organizations to provide a set of overrides and definitions in one\
central place.

For instance, you can create your own `my-plugins` repository with `plugin.yaml`:

```yaml
version: 0.1
lint:
  definitions:
    - name: trufflehog
      commands:
        - name: lint
          # override trufflehog to use '--only-verified'
          run: trufflehog filesystem --json --fail --only-verified ${target}
  enabled:
    - ruff@0.0.256
```

sourced in a `.trunk/trunk.yaml` file from another repository as follows:

```yaml
version: 0.1
plugins:
  sources:
    - id: trunk
      uri: https://github.com/trunk-io/plugins
      ref: v0.0.15
    - id: my-plugins
      local: ../my-plugins
```

When a user runs `trunk` in the sourcing repository, they will already have ruff enabled, along with\
any overrides and definitions enumerated in the `my-plugins` repository.

Note that private GitHub plugin repositories are not currently supported.

#### Excluded fields

Plugin `sources`, as well as the `cli` `version`, are not merged from plugin repositories to ensure\
that config merging occurs in a predictable, stable fashion.
