---
description: Let's look at how to configure Trunk Tools.
---

# Configuration

Tools are configured in the `tools` section of [`trunk.yaml`](../reference/trunk-yaml/). As with other settings, you can override these values in your [User YAML](../reference/user-yaml.md).

```yaml
tools:
  auto_sync: false # whether shims should be hot-reloaded off config changes.
  enabled:
    - bazel@6.0.0
    - mypy@1.4.1
    - ibazel@0.22.0
    - helm@3.9.4
    - eksctl@0.74.0
    - asciinema@2.1.0
  disabled:
    - gt
  definitions:
    - name: gh
      download: gh
      known_good_version: 2.27.0
      environment:
        - name: PATH
          list: ["${tool}/bin"]
      shims: [gh]
```

Like with actions and linters, we have a (versioned) `enabled` section and a `disabled` section, which can be manipulated using `trunk tools enable/disable`. There is also a list of `definitions`, which are merged across your `trunk.yaml`, `user.yaml`, as well as any plugins that you use.

`auto_sync` controls whether or not Trunk automatically installs your tools for you when your config changes. This defaults to `true`. Note that the daemon must be running with the monitor in order for this to function properly.

### Tool definitions

Each tool definition shares a set of attributes:

<table><thead><tr><th width="237">Field</th><th></th></tr></thead><tbody><tr><td><code>name</code></td><td>The name of the tool. Must be unique.</td></tr><tr><td><code>known_good_version</code></td><td>The default version to initialize the tool at (required).</td></tr><tr><td><code>shims</code></td><td>A list of binaries exposed by the tool. Each of these will correspond to one identically named executable installed in <code>.trunk/tools.</code>In the most common case, there is exactly one shim matching the name of the tool. We'll discuss other cases below.</td></tr><tr><td><code>environment</code></td><td>You can specify an environment for the tool. We provide the <code>${tool}</code> template argument that resolves to the installation directory of the tool. By default, we prepend this to <code>$PATH</code> within the shim script, so this is used to locate the binary. For legacy reasons, <code>${linter}</code> also resolves to this directory.</td></tr></tbody></table>

> Note: If the tool has a `runtime` attribute, the runtime's environment is merged in to its environment (discussed in the examples below).

Broadly speaking, there are 3 kinds of tools - download, package, and runtime-based tools. We'll look at each one in turn:

### Download-based tools

Download-based tools are straightforward: They reference a named download configuration in the global `downloads` section. Here is an example:

```yaml
downloads:
  - name: gh
    downloads:
      - os:
          linux: linux
        cpu:
          x86_64: amd64
          arm_64: arm64
        url: https://github.com/cli/cli/releases/download/v${version}/gh_${version}_${os}_${cpu}.tar.gz
        strip_components: 1
      - os:
          windows: windows
        cpu:
          x86_64: amd64
          arm_64: arm64
        url: https://github.com/cli/cli/releases/download/v${version}/gh_${version}_${os}_${cpu}.zip
        strip_components: 1
      # macOS releases since 2.28.0 started using .zip instead of .tar.gz
      - os:
          macos: macOS
        cpu:
          x86_64: amd64
          arm_64: arm64
        url: https://github.com/cli/cli/releases/download/v${version}/gh_${version}_${os}_${cpu}.zip
        strip_components: 1
        version: ">=2.28.0"
      - os:
          macos: macOS
        cpu:
          x86_64: amd64
          arm_64: arm64
        url: https://github.com/cli/cli/releases/download/v${version}/gh_${version}_${os}_${cpu}.tar.gz
        strip_components: 1
tools:
  definitions:
    - name: gh
      download: gh
      known_good_version: 2.27.0
      environment:
        - name: PATH
          list: ["${tool}/bin"]
      shims: [gh]
```

Note that for the downloaded archive, the binary named `gh` is inside the `bin` directory, so we use the environment to point the `$PATH` there.

### Package-based tools

Package-based tools depend on specified `package` and `runtime` attributes. Here is an example of configuring `mypy` as a tool:

```yaml
tools:
  definitions:
    - name: mypy
      runtime: python
      package: mypy
      shims: [mypy]
      known_good_version: 0.931
      extra_packages:
      	- types-six@1.16.21
        - types-request
```

`extra_packages` behaves equivalently to a package file like `requirements.txt` for Python or `package.json` for Node. They can be optionally pinned at versions.

The version of the primary package (in this case, `mypy`) is specified in the `tools.enabled`. So to enable the `mypy` tool at `1.4.0`, list it as `- mypy@1.4.0`.

If you don't want to include additional packages in the tool definition, you can instead make them explicit in the enabled section of your `.trunk/trunk.yaml` as you would for [linters](../configuration/#installing-additional-packages), for example:

```yaml
tools:
  enabled:
    - mypy@1.4.0:
        packages:
          - types-six@1.16.21
```

### Runtime-based tools

Runtime-based tools are a special case that are not explicitly defined. Rather, each runtime object exposes a set of `shims` (just like `tool` definitions).

If the runtime is enabled and listed in `tools.runtimes`, then shims exposed by that runtime are automatically installed in the `.trunk/tools` directory alongside those of other tools (`trunk tools enable <runtime_tool>` does that for you). Thus you can run `python`, `pip`, etc as `trunk`-managed tools.

Example:

```yaml
tools:
  runtimes:
    - python
```

If this is disruptive to your workflow, simply remove the runtime's name `(go, node, python,...)` from `tools.runtimes` section or run `trunk tools disable <runtime_name>` which will handle it for you. Runtimes cannot be enabled or versioned via the `tools.enabled` section, however, and runtimes must be enabled in the `runtimes` section to be available to have their shims installed.
