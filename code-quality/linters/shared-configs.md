# Shared Configs

## Single Repo

Linters are automatically shared with all developers for a repository using the [`.trunk/trunk.yaml` file](../../cli/configuration/).  This file is committed to the repo, so whenever anyone checks out the code, they will get the same configuration and linters. See the [Trunk YAML guide](../../cli/configuration/) for more details.

## Per User Config

If you wish to customize a linter for just one developer (say, disable a slow linter on a slow machine), you can create a per-user config in the `.trunk/user.yaml` file, which should **not** be committed to the repo.&#x20;

## Multiple Repos

If you wish to share linters between different repos, copy the config manually or create a shared Plugin repo. This is a set of configuration and code that is imported into the `plugins` section of a project's `./trunk/trunk.yaml` .
