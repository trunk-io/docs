---
description: Learn more about the Trunk CLI
---

# Trunk CLI

### Getting Started

To use `trunk` locally, install via:

{% tabs %}
{% tab title="bash" %}
```bash
curl https://get.trunk.io -fsSL | bash
```
{% endtab %}

{% tab title="bash (no prompts)" %}
```bash
curl https://get.trunk.io -fsSL | bash -s -- -y
```
{% endtab %}

{% tab title="brew" %}
```bash
brew install trunk-io
```
{% endtab %}

{% tab title="npm" %}
```bash
npm install -D @trunkio/launcher
```
{% endtab %}

{% tab title="pnpm" %}
```bash
pnpm add -D @trunkio/launcher
```
{% endtab %}

{% tab title="yarn" %}
```bash
yarn add -D @trunkio/launcher
```
{% endtab %}
{% endtabs %}

### What can it do?

The Trunk CLI can be used for:

* [Trunk Code Quality](../../): a pluggable superlinter with a builtin language server and pre-existing issue detection
* [Trunk Tools:](../tools/) hermetic runtime and CLI tool manager
* [Trunk Actions](../actions/): local workflow automation and githooks manager
* [Trunk Merge Queue](../../../merge-queue/): a merge queue to make merging code in github safer and easier

[Trunk Code Quality](../../) and [Trunk Actions](../actions/) can be used entirely locally without depending on hosted services or even having a Trunk account

### Initialize Trunk in your repo

Whether you aim to use [Trunk Code Quality](../../), [Trunk Merge Queue](../../../merge-queue/), [Trunk Actions](../actions/), or all of the above, the first step is to initialize Trunk in your git repo:

```bash
trunk init
```

Note: for an extra layer of security you can optionally run `trunk init --lock` instead of `trunk init` which adds sha256s of the trunk cli to the trunk config file. This is then used by the Trunk Launcher when it downloads the `trunk` binary.

`init` scans the files in your repo and generates a `.trunk/trunk.yaml` configuration file tailored to your repo (it may also generate linter-specific config files, such as `.shellcheckrc`). The scan will identify all the particular languages and technologies you use and automatically configure the correct set of linters / formatters to run.

If you only want to use [Trunk Merge Queue](../../../merge-queue/), you can safely ignore the linter setup, or even strip enabled linters from `.trunk/trunk.yaml`. You will additionally need to login to use [Trunk Merge Queue](../../../merge-queue/) via `trunk login`.
