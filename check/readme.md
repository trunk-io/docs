---
layout:
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
---

# Check

Trunk Check runs [80+ tools](https://github.com/trunk-io/plugins) on your repositories, locally and in the cloud, which allow you to automatically

* Keep bugs and security vulnerabilities out of your code base
* Enforce code formatting and style
* Flag secrets
* and much more

The Trunk **Check** command line tool runs locally on your developer machine, right where your code is. Later you can automatically scan your repo using Trunk Check Cloud.

Check will automatically keep tools up to date, suggest standard tools for your project type (eg: `clang-format` for C++, `eslint` for JS/TS), and pin versions in the `trunk.yaml` file to ensure trunk check is always working and reproducible.

## Install the CLI

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
<pre class="language-bash"><code class="lang-bash"><strong>yarn add -D @trunkio/launcher
</strong></code></pre>
{% endtab %}
{% endtabs %}

## Initialize `trunk`

From the root of a git repo, run:

```bash
trunk init
```

This will scan your repository and create a `.trunk/trunk.yaml` which enables all the linters, formatters, and security analyzers that [Trunk Check](./) recommends. For more details, see [here](cli/init-in-a-git-repo.md).

{% hint style="info" %}
Security-conscious users may want to also record the signature of the CLI, which the [Trunk Launcher](reference/components.md#trunk-launcher) will use to verify the CLI's provenance:

```
trunk init --lock
```
{% endhint %}

## [<img src="../.gitbook/assets/image (2).png" alt="" data-size="line">](vscode:extension/Trunk.io) Install the VSCode Extension

If you run VSCode you can also install the [trunk VSCode extension](vscode:extension/Trunk.io). Read more about it [here](https://marketplace.visualstudio.com/items?itemName=Trunk.io).
