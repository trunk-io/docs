---
description: When using Nx, Trunk Merge can create parallel merge queues for your PRs.
---

# Parallel Mode with Nx

Leveraging [parallel mode](../#single-mode-vs.-parallel-mode) for Trunk Merge is easy for Nx enabled repos because Nx already knows the structure of your code and can automatically generate a [dependency graph](https://nx.dev/nx-api/nx/documents/dep-graph). Merge can use this information in parallel mode to run your CI tests more efficiently; eliminating checks when Nx already knows they cannot conflict.

### Setup Trunk Merge

Connect your GitHub repository with Trunk and set up Trunk Merge with [the standard instructions.](./)

### Turn on Parallel Mode

Next [enable Parallel Mode](configuration.md) in the Trunk Merge UI.

<figure><img src="../../.gitbook/assets/enable-parallel-mode" alt="screenshot of Trunk Merge configuration screen"><figcaption><p>Enabling Parallel Mode</p></figcaption></figure>

### Set Up the Github Action

Trunk provides an [Nx Merge GitHub action](https://github.com/trunk-io/nx-action) (workflow) that leverages Nx to take care of generating the required[ impacted targets](impacted-targets.md) and uploading them to Merge, taking care of the heavy work for using Parallel mode. In order for GitHub to communicate with Trunk Merge, it needs to be able to authenticate from the GitHub Action instance to the Trunk web application using your **Trunk Organization API Token**.

#### Get your Organization API Token

{% @supademo/embed demoId="LPJsDyJYAsyvUabvkphHK" url="https://app.supademo.com/demo/LPJsDyJYAsyvUabvkphHK" %}

#### Store your Organization Token as a GitHub Secret

{% @supademo/embed demoId="2UWXR9ccwhP4ng5-orZPG" url="https://app.supademo.com/demo/2UWXR9ccwhP4ng5-orZPG" %}

#### Add merge action with Trunk Org Token

Now add the [`trunk-io/nx-action`](https://github.com/trunk-io/nx-action) action in a new workflow in your repo under `.github/workflows` (eg: `.github/workflows/uploaded_impacted_targets.yaml` )&#x20;

```yaml
name: Upload Impacted Targets
on: pull_request

jobs:
  compute_impacted_targets:
    name: Compute Impacted Targets
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v3

      - name: Compute Impacted Targets
        uses: trunk-io/nx-action@v1
        with:
          # Use your Trunk repo or org API token to authenticate impacted targets uploads.
          # This secret should be provided as a GitHub secret.
          # See https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions.
          trunk-token: ${{ secrets.TRUNK_API_TOKEN }}
```

If your Nx setup is not in the root of your repo then you can add `workspace-path: your_workspace_path` just below the `trunk-token`. Commit the new workflow back to your repo. to make it active.&#x20;

Now you can [submit a new pull request and test it](../reference.md#submitting-and-cancelling-pull-requests). **Success!**

