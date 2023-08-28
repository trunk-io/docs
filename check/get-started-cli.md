---
description: Install the Trunk CLI to start automating your code quality checks.
---

# Install the CLI

{% hint style="info" %}
If you use VSCode, [click here to install our VSCode extension](vscode:extension/Trunk.io). Read more about it [here](https://marketplace.visualstudio.com/items?itemName=Trunk.io).
{% endhint %}

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

For more details, see [Installing the CLI](../cli/install-trunk.md).

## Initialize `trunk`

From the root of a git repo, run:

```bash
trunk init
```

This will scan your repository and create a `.trunk/trunk.yaml` which enables all the linters, formatters, and security analyzers that [Trunk Check](./) recommends. For more details, see [here](../cli/init-in-a-git-repo.md).

{% hint style="info" %}
Security-conscious users may want to also record the signature of the CLI, which the  [Trunk Launcher](../reference/components.md#trunk-launcher) will use to verify the CLI's provenance:

```
trunk init --lock
```
{% endhint %}

## Run `trunk check --sample`&#x20;

`trunk check` by default only checks the changes you've made in your branch, ignoring issues in the default branch. This means that if you haven't made any changes, `trunk check` will come back empty, so to get a sense of what `trunk check` can do, we suggest running:

```bash
trunk check --sample 5
```

For more information on the sample flag see [here](command-line.md#sample)

## (optional) Install the VSCode Extension

[Click here to install the VSCode extension](vscode:extension/Trunk.io). Read more about it [here](https://marketplace.visualstudio.com/items?itemName=Trunk.io).

## (optional) Commit the launcher

To allow your teammates to use `trunk` without installing anything, the launcher can be committed directly into your repo:

```
curl -LO https://trunk.io/releases/trunk
chmod +x ./trunk
git commit ./trunk -m "Commit Trunk to our repo"
```

This makes it much easier for you to share Trunk with your colleagues!
