---
description: List of major components of Trunk Check
---

# Components

### Trunk Binary

The `trunk` binary is a native executable that contains all the client-side code required to run `trunk check`, `trunk actions`, and local `trunk merge` commands.

### Trunk Launcher

The Trunk Launcher is a bash script that enables users to easily switch between multiple versions of `trunk`. The Trunk Launcher will read a repo's pinned version of `trunk` from `.trunk/trunk.yaml`, download the matching binary to cache and run that executable. This ensures that all users of `trunk` in a repo are using the same version.

The launcher can be installed on a machine (`/usr/local/bin`) or committed in your repository (e.g. in a `tools/` directory).

### Cache

As needed `trunk` will download and cache components onto a machine for use. The cache will contain the `trunk` binary itself (including multiple versions as needed by the machine), the linters/actions enabled in trunk-managed repositories, and the requisite runtimes needed to run those tools. The location of the Trunk cache is user configurable and honors the following environment variables:

* `$TRUNK_CACHE`
* `$XDG_CACHE_HOME/trunk`
* `$HOME/.cache/trunk`
