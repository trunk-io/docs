# Upgrades

Run `trunk upgrade` to update the Trunk CLI and all your plugins, linters, tools, and runtimes.

#### Upgrade Scopes

Upgrades can be filtered to different scopes by adding them to `trunk upgrade <scopes>`. The scopes available are:

<table><thead><tr><th width="133">Scope</th><th>Description</th></tr></thead><tbody><tr><td>cli</td><td>Only upgrade the Trunk CLI to the latest version.</td></tr><tr><td>plugins</td><td>Upgrade any that you have sourced to their latest public release. The latest version must be compatible with your current <code>cli</code> version in order for the upgrade to be applied.</td></tr><tr><td>check</td><td>Upgrade any linters that you have enabled. Linters will be upgraded to the latest validated version that have passed tests in our <a href="https://github.com/trunk-io/plugins">plugins</a> repo. Additional recommended linters can also be enabled by running with <code>-y</code>.</td></tr><tr><td>tools</td><td>Upgrade any that you have enabled. Tools will be upgraded to their latest public release. Note that any enabled linters that share a name with an enabled tool must keep their versions synced.</td></tr><tr><td>runtimes</td><td>Upgrade any that you have enabled. Runtimes will be upgraded to their recommended version for running linters, as specified by Trunk.</td></tr></tbody></table>

#### Automatic Upgrades

When running locally, Trunk automatically checks for upgrades in the background on a regular cadence. You'll see notifications for these upgrades appear in the VSCode Extension or at the end of a `trunk check` run. To stop seeing these notifications, you can run `trunk actions disable trunk-upgrade-available`.

When running in single-player mode, Trunk will automatically upgrade itself in the background and stay up to date.

#### Automatic Upgrades with GitHub Actions

You can configure a GitHub workflow to create PRs with the latest Trunk and tool versions automatically. Here's a sample GitHub Action:

```
name: Nightly
on:
  schedule:
    - cron: 0 8 * * 1-5
  workflow_dispatch: {}
permissions: read-all
jobs:
  trunk_upgrade:
    name: Upgrade Trunk
    runs-on: ubuntu-latest
    permissions:
      contents: write # For trunk to create PRs
      pull-requests: write # For trunk to create PRs
    steps:
      - name: Checkout
        uses: actions/checkout@v3
      # >>> Install your own deps here (npm install, etc) <<<
      - name: Trunk Upgrade
        uses: trunk-io/trunk-action/upgrade@v1
```

Then, provide permissions for this GitHub Action to [create and approve pull requests](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository#preventing-github-actions-from-creating-or-approving-pull-requests) by navigating to your repo's **Settings** > **Actions** > **General** > **Workflow permissions** > **Allow GitHub Actions to create and approve pull requests**.\
\
You can also set the `arguments` field to filter particular scopes to upgrade and set `base` to define the branch to create a PR against (default `main`).

{% hint style="warning" %}
**Triggering further workflow runs**

PRs created with this GitHub Action will not trigger further workflows by default. If you need the PRs created to trigger further GitHub Action Workflows, [follow the workarounds described here](https://github.com/peter-evans/create-pull-request/blob/main/docs/concepts-guidelines.md#triggering-further-workflow-runs).
{% endhint %}

#### Pinning Versions

If you don't want a linter, tool, or runtime to be upgraded, you can pin its version by appending `!` to the version in your `.trunk/trunk.yaml`. For example:

```yaml
lint:
  enabled:
    - pylint@2.17.5!
```

#### Plugin Repos and user.yaml

By default, upgrades are only applied to your repo's `.trunk/trunk.yaml`. If you're using a plugin repo that enables linters/tools, or if you would like upgrades to be applied to your `.trunk/user.yaml` file, you can run `trunk upgrade --apply-to <path>` to see upgrades applied there.
