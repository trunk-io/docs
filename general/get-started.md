# Get Started

### Step 1: Install Trunk

To use `trunk` locally, run:

```bash
curl https://get.trunk.io -fsSL | bash
```

For other installation options (`npm`, `brew`, direct download, etc) and details on exactly what we install or how to uninstall, see the [Install Trunk](doc:install) doc.

### Step 2: Initialize Trunk in a git repo

From the root of a git repo, run:

```bash
trunk init
```

This will bring you into a flow to start getting results from [Trunk Check](../check/overview.md). For more details, see [here](../cli/init-in-a-git-repo.md).

### Step 3: Sign up for a Trunk account (optional)

[Sign up for a Trunk account](https://app.trunk.io/signup), then run:

```bash
trunk login
```

To use [Trunk Merge](../merge/overview.md) and certain other Trunk features, you'll need an account on [trunk.io](https://app.trunk.io), but [Trunk Check](../check/overview.md) and [Trunk Actions](../actions/overview.md) can be used entirely locally without depending on hosted services or having a Trunk account.

### Help & Feedback

Join the [Trunk Slack Community](https://slack.trunk.io) for help and to give feedback ([more info](doc:community)).
