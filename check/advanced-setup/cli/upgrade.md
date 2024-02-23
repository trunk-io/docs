---
description: Upgrading the Trunk CLI for new versions and features
---

# Upgrade

Run `trunk upgrade` to update the Trunk CLI and all of your plugins linters, tools, and runtimes.

### Upgrade Scopes

Upgrades can be filtered to different scopes by adding them to `trunk upgrade <scopes>`:

`cli`

Only upgrade the Trunk CLI to the latest version.

`plugins`

Upgrade any [plugins](../plugins/) that you have sourced to their latest public release. The latest version must be compatible with your current `cli` version in order for the upgrade to be applied.

`check`

Upgrade any linters that you have enabled. Linters will be upgraded to the latest validated version that have passed tests in our [plugins](https://github.com/trunk-io/plugins) repo. Additional recommended linters can also be enabled by running with `-y`.

`tools`

Upgrade any [tools](../tools/) that you have enabled. Tools will be upgraded to their latest public release. Note that any enabled linters that share a name with an enabled tool must keep their versions synced.

`runtimes`

Upgrade any [runtimes](../runtimes.md) that you have enabled. Runtimes will be upgraded to their recommended version for running linters, as specified by Trunk.

### Automatic Upgrades

You can configure a GitHub workflow to automatically create PRs with the latest Trunk upgrades by following the instructions [here](https://github.com/trunk-io/trunk-action#automatic-upgrades). Note that this requires the creation of a privileged GitHub token in order to run necessary workflows on PRs.

When running locally, Trunk automatically checks for upgrades in the background on a regular cadence. You'll see notifications for these upgrades appear in the VSCode Extension or at the end of a `trunk check` run. To stop seeing these notifications, you can run `trunk actions disable trunk-upgrade-available`.

When running in [single-player mode](init-in-a-git-repo.md#single-player-mode), Trunk will automatically upgrade itself in the background and stay up to date.

### Pinning Versions

If you don't want a linter, tool, or runtime to be upgraded, you can pin its version by appending `!` to the version in your `.trunk/trunk.yaml`. For example:

```yaml
lint:
  enabled:
    - pylint@2.17.5!
```

### Plugin Repos and user.yaml

By default, upgrades are only applied to your repo's `.trunk/trunk.yaml`. If you're using a [plugin](../plugins/) repo that enables linters/tools, or if you would like upgrades to be applied to your [`.trunk/user.yaml`](../../reference/user-yaml.md) file, you can run `trunk upgrade --apply-to <path>` to see upgrades applied there.
