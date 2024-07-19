---
description: Detailed install instructions for the Trunk CLI
---

# Install Trunk



The below commands install the Trunk Launcher, a bash script that downloads the appropriate Trunk CLI version and runs it. The launcher invisibly runs the Trunk CLI version specified in a project's `.trunk/trunk.yaml` file. The actual Trunk CLI is a single binary that is cached locally in `~/.cache/trunk` and is updated automatically.

Run one of the following commands to install the Trunk Launcher, or add it as a dev dependency to your project if you use `npm`, `pnpm`, or `yarn`. You can also commit the Trunk launcher directly into your repo (see below).

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

For use on Windows, check out our [Windows (beta)](windows-beta.md) page.

## Commit the Trunk Launcher (optional)

To allow your teammates to use `trunk` without installing anything, the launcher can be committed directly into your repo:

```
curl -LO https://trunk.io/releases/trunk
chmod +x ./trunk
git commit ./trunk -m "Commit Trunk to our repo"
```

This makes it much easier for you to share Trunk with your colleagues!

## Uninstall instructions

#### From your system

Trunk has a very minimal installation, and therefore, there's not much to uninstall. The two system paths we use are:

* `/usr/local/bin/trunk`: the [Trunk Launcher](../../reference/components.md#trunk-launcher)
* `~/.cache/trunk`: cached versions of the trunk cli, linters, formatters, etc.

You can delete those two paths to uninstall.

#### From a repo

To cleanly remove Trunk from a particular repo, run:

```bash
trunk deinit
```

#### VS Code extension

To uninstall the Trunk VS Code extension, do so as you would any extension ([docs](https://code.visualstudio.com/docs/editor/extension-marketplace)). Then reload VS Code.

## Binary download (not recommended)

You can directly download the `trunk` binary. _We don't recommend this mode of operation because your ability to version the tool through_ `trunk.yaml` _will not function when launching_ `trunk` _directly from a downloaded binary._ Regardless you can bypass the launcher support by downloading the prebuilt binaries here:

<table><thead><tr><th width="178">variable</th><th>options</th></tr></thead><tbody><tr><td>version</td><td>the semver of the binary you want to download</td></tr><tr><td>platform</td><td>'darwin', 'linux'</td></tr></tbody></table>

```bash
# for example https://trunk.io/releases/1.0.0/trunk-1.0.0-linux-x86_64.tar.gz
https://trunk.io/releases/${version}/trunk-${version}-${platform}-x86_64.tar.gz
```

## Pre-installing tools

Trunk hermetically manages all the tools that it runs. To do this, it will download and install them into its cache folder only when they are needed. If you would like to ensure that all tools are installed ahead of time, then you can use the `trunk install` command. This may be useful if you want to prepare to work offline or if you would like to include the tools in a docker image. On Linux and macOS you may find the cache folder at `$HOME/.cache/trunk`.
