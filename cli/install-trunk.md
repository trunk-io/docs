# Install Trunk

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

## (optional) Commit the launcher

To allow your teammates to use `trunk` without installing anything, the launcher can be committed directly into your repo:

```
curl -LO https://trunk.io/releases/trunk
chmod +x ./trunk
git commit ./trunk -m "Commit Trunk to our repo"
```

This makes it much easier for you to share Trunk with your colleagues!

## (optional) Uninstalling

Trunk has a very minimal installation, and therefore there's not much to uninstall. The two system paths we use are:

* `/usr/local/bin/trunk`: the [Trunk Launcher](../reference/components.md#trunk-launcher)
* `~/.cache/trunk`: cached versions of the trunk cli, linters, formatters, etc.

To cleanly uninstall:

```bash
trunk deinit
```

To uninstall the Trunk VS Code extension, do so as you would any extension ([docs](https://code.visualstudio.com/docs/editor/extension-marketplace)).

#### Binary download (not recommended)

You can directly download the trunk binary. \*\*We don't recommend this mode of operation because your ability to version the tool through `trunk.yaml` will not function when launching `trunk` directly from a downloaded binary. Regardless you can bypass the launcher support by downloading the prebuilt binaries here:

<table><thead><tr><th width="178">variable</th><th>options</th></tr></thead><tbody><tr><td>version</td><td>the semver of the binary you want to download</td></tr><tr><td>platform</td><td>'darwin', 'linux'</td></tr></tbody></table>

```bash
# for example https://trunk.io/releases/1.0.0/trunk-1.0.0-linux-x86_64.tar.gz
https://trunk.io/releases/${version}/trunk-${version}-${platform}-x86_64.tar.gz
```

#### Next Steps:

<table data-view="cards"><thead><tr><th></th><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th><th data-hidden data-card-cover data-type="files"></th></tr></thead><tbody><tr><td><strong>Check</strong></td><td></td><td>An extendable superlinter with a builtin language server and pre-existing issue detection</td><td><a href="../check/">check</a></td><td><a href="../.gitbook/assets/Check.svg">Check.svg</a></td></tr><tr><td><strong>Actions</strong></td><td></td><td>Workflow automation for your repository</td><td><a href="../actions/">actions</a></td><td><a href="../.gitbook/assets/Actions (2).svg">Actions (2).svg</a></td></tr><tr><td><strong>Merge</strong></td><td></td><td>A merge queue to make merging code in GitHub safer and easier</td><td><a href="../merge/">merge</a></td><td><a href="../.gitbook/assets/Merge.svg">Merge.svg</a></td></tr></tbody></table>

As well as the other ways to use Trunk:

* [VSCode Extension](https://marketplace.visualstudio.com/items?itemName=trunk.io)
* [Web App (app.trunk.io)](https://app.trunk.io)
