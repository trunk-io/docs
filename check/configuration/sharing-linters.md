---
description: Different ways to share linters between projects.
---

# Sharing Linters

## Single Repo

Linters are automatically shared with all developers for a repository using the [`.trunk/trunk.yaml` file](../reference/trunk-yaml/).  This file is committed to the repo so whenever anyone else checks out the code they will get the same configuration, and therefore the same linters. See the [Trunk YAML guide](../reference/trunk-yaml/) for more details.

## Per User Config

If you wish to customize a linter for just one developer (say, disable a slow linter on a slow machine), you can create a per-user config in the `.trunk/user.yaml` file, which should \*not\* be committed to the repo. See the [User YAML guide](../reference/user-yaml.md) for more details.

## Multiple Repos

If you wish to share linters between different repos, you can either copy the config manually, or create a shared Plugin repo. This is a set of configuration and code that is imported into the `plugins` section of a project's `./trunk/trunk.yaml` See the [Plugins guide](../advanced-setup/plugins/) for more details.
