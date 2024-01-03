---
description: When using Bazel, Trunk Merge can create parallel merge queues for your PRs.
---

# Merge + Bazel

Leveraging [parallel mode](./#single-mode-vs.-parallel-mode) for Trunk Merge is easy for Bazel enabled repos. This is because Bazel already knows the structure of your code and can generate a dependency graph automatically. Then Merge can use parallel mode to run your CI tests more efficiently, eliminating checks when Bazel already knows they couldn't conflict.

### Setup Trunk Merge

Connect your GitHub repository with Trunk and set up Trunk Merge with [the standard instructions.](set-up-trunk-merge.md)

### Turn on Parallel Mode

Next [enable Parallel Mode](configuration.md) in the Trunk Merge UI.

<figure><img src="../.gitbook/assets/enable-parallel-mode" alt=""><figcaption></figcaption></figure>

### Set Up the Trunk Merge + Bazel Github Action

Trunk provides a GitHub action (workflow) that leverages Bazel to take care of generating the required[ impacted targets](impacted-targets.md) and uploading them to Merge, taking care of the heavy work for using Parallel mode.

Find your Trunk organization's API token from [app.trunk.io](https://app.trunk.io) under **Settings** > **Manage Organization** > **Organization API Token**. &#x20;

<figure><img src="../.gitbook/assets/organization-api-token" alt=""><figcaption></figcaption></figure>

Store the organization's API token as a GitHub action secret in your GitHub repo. You can find it under **Settings > Security > Secrets and Variables > Actions.** You can name the secret whatever you want, but we recommend something simple and clear like `TRUNK_REPO_API_TOKEN`.

<figure><img src="../.gitbook/assets/github-actions-secrets" alt=""><figcaption></figcaption></figure>

Now add the `trunk-io/merge-action` action in a new workflow in your repo under `.github/workflows` (eg: `.github/workflows/uploaded_impacted_targets.yaml` )&#x20;

```yaml
name: Upload Impacted Targets
run-name: Upload Impacted Targets for ${{ github.ref_name }}
on: pull_request

jobs:
  compute_impacted_targets:
    name: Compute Impacted Targets
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v3
        with:
          lfs: true

      - name: Compute Impacted Targets
        uses: trunk-io/merge-action@v1
        with:
          # Use your Trunk repo or org API token to authenticate impacted targets uploads.
          # This secret should be provided as a GitHub secret.
          # See https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions.
          trunk-token: ${{ secrets.TRUNK_REPO_API_TOKEN }}
```

If your Bazel setup is not in the root of your repo then you can add `bazel-workspace-path: your_workspace_path` just below the `trunk-token`. Commit the new workflow back to your repo. to make it active.&#x20;

Now you can [submit a new pull request and test it](testing-pull-requests.md). **Success!**

