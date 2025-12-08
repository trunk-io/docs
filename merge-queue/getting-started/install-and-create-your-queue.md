# Install and create your queue

This guide walks you through setting up Trunk Merge Queue for your repository. The setup process involves installing the GitHub App, creating a queue, and configuring branch protection rules to allow the merge queue to function properly.

### Prerequisites

Before you begin, make sure you have:

* [ ] Admin access to your GitHub organization
* [ ] A repository you want to protect with Merge Queue

{% hint style="warning" %}
**You must be a GitHub admin to complete the following steps.** If you are not a GitHub admin in your organization, go to `Settings` → `Team Members` to invite a GitHub admin to your Trunk organization so they can complete the following.

The GitHub App installation must be initiated from the Trunk web app to properly associate your Trunk organization with the GitHub App. If you have previously installed the Trunk GitHub App directly through GitHub, you'll need to uninstall it first and then reinstall it by starting the installation process from the Trunk web app as described below.
{% endhint %}

### Install the Trunk GitHub App

1. [Sign in to app.trunk.io](https://app.trunk.io/login) and navigate to the **Merge Queue** tab. (First-time users will [create an organization](../../setup-and-administration/connecting-to-trunk.md) before accessing Merge Queue.)
2. Click the **Create New Queue** button at the top right corner of the window.

{% hint style="info" %}
**The Trunk GitHub App is required for Merge Queue to function.** It grants Trunk Merge Queue the necessary permissions to create test branches, read CI results, and merge PRs in your repository. View [detailed permissions and what Trunk uses them for](../../setup-and-administration/github-app-permissions.md).

If the GitHub App is already installed, step 3 will be skipped automatically.
{% endhint %}

3. If the Trunk GitHub App is not already installed, you'll be prompted to install it.
   1. Click **Install GitHub App** and follow the installation flow:
      1. Select whether to install on all repositories or only specific ones
      2. Review and approve the required permissions
      3. Complete the installation
      4. After the GitHub App installation is complete, you'll be returned to the Trunk dashboard.

### Create your first queue

4. In the **Merge Queue** tab, click the **Create New Queue** button at the top right corner of the window.
5. Select a repository from the dropdown and enter the target branch to merge into. Click **Create Queue.**

<figure><img src="../../.gitbook/assets/merge-add-repo (1).png" alt=""><figcaption></figcaption></figure>

### What you just did

You've installed the Trunk GitHub App on your organization and created your first merge queue for the specified branch (`main` in the example above). Trunk is now connected to your repository and ready to be configured. Your queue won't start processing pull requests until you complete the branch protection setup in the next step.

### Next steps

→ [**Configure branch protection**](configure-branch-protection.md) - Set up GitHub rules so Trunk can safely manage your merges

_Having trouble?_ See our [Troubleshooting guide](../reference/troubleshooting.md) for common installation issues.



