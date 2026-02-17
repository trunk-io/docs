---
description: >-
  Configure GitHub IP allow lists to work with the Trunk GitHub App for
  organizations using GitHub Enterprise Cloud.
---

# GitHub IP Allow Lists

If your GitHub organization uses [IP allow lists](https://docs.github.com/en/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-allowed-ip-addresses-for-your-organization) to restrict access, you need to allow Trunk's server IP addresses so the Trunk GitHub App can communicate with your repositories.

Organizations that enable GitHub's IP allow list feature without configuring access for Trunk will see failures when installing or using the Trunk GitHub App.

## How it works

When you install the Trunk GitHub App on a GitHub organization that has IP allow lists enabled, the app can automatically add Trunk's IP addresses to your organization's allow list. These entries appear in your GitHub IP allow list settings as **Managed by the trunk.io GitHub app**.

{% hint style="info" %}
Automatic IP allow list management requires that you enable the **Allow GitHub Apps to manage IP allow list entries** setting in your GitHub organization. See [GitHub's documentation](https://docs.github.com/en/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-allowed-ip-addresses-for-your-organization#allowing-access-by-github-apps) for details.
{% endhint %}

## Setup

### Step 1: Enable GitHub App IP allow list management

1. Go to your GitHub organization's **Settings**.
2. In the left sidebar, click **Security** > **Authentication security**.
3. Under "IP allow list", check the box for **Enable IP allow list configuration for installed GitHub Apps**.
4. Click **Save**.

This setting allows installed GitHub Apps, including the Trunk GitHub App, to automatically add their required IP addresses to your organization's allow list.

### Step 2: Install the Trunk GitHub App

If you have not already installed the Trunk GitHub App, follow the standard installation process:

1. Sign in to [app.trunk.io](https://app.trunk.io).
2. Go to **Settings** > **Organization** > **GitHub**.
3. Click **Install GitHub App** and follow the prompts.

For detailed installation instructions, see [Trunk GitHub App](github-app-permissions.md).

### Step 3: Verify the configuration

After installing the Trunk GitHub App with the IP allow list setting enabled:

1. Go to your GitHub organization's **Settings**.
2. Navigate to **Security** > **Authentication security**.
3. Under "IP allow list", you should see entries labeled **Managed by the trunk.io GitHub app**.

These entries are automatically maintained by the Trunk GitHub App and will stay up to date if Trunk's IP addresses change.

## Trunk server IP addresses

If you prefer to manually manage your IP allow list, or if your organization's security policy requires explicit approval of all allow list entries, add the following Trunk server IP addresses to your GitHub organization's IP allow list:

<!-- TODO: Replace these placeholder IPs with the actual Trunk server IP addresses.
     The actual IPs are visible in the Linear ticket TRUNK-16633 screenshots.
     Contact the Trunk infrastructure team for the current list. -->

| IP Address | Description |
| --- | --- |
| `35.85.238.158/32` | Trunk production server |
| `44.233.210.179/32` | Trunk production server |
| `44.238.78.236/32` | Trunk production server |

{% hint style="warning" %}
The IP addresses listed above are subject to change. If you manually manage your allow list, subscribe to Trunk's [status page](https://status.trunk.io) for notifications about infrastructure changes. For the most current list, contact [support@trunk.io](mailto:support@trunk.io).
{% endhint %}

To add these manually:

1. Go to your GitHub organization's **Settings**.
2. Navigate to **Security** > **Authentication security**.
3. Under "IP allow list", click **Add IP address** for each address above.
4. Enter the IP address and a description (for example, "Trunk.io server").
5. Click **Add**.

## Troubleshooting

### Trunk GitHub App installation fails

If the Trunk GitHub App fails to install or connect to your repositories, and your organization has IP allow lists enabled:

1. Verify that the **Enable IP allow list configuration for installed GitHub Apps** checkbox is enabled in your GitHub organization settings (see [Step 1](#step-1-enable-github-app-ip-allow-list-management)).
2. If you manage your allow list manually, confirm that all Trunk server IP addresses listed above have been added.
3. After updating the allow list, retry the GitHub App installation from [app.trunk.io](https://app.trunk.io).

### Trunk features stop working after IP allow list changes

If Trunk features (such as Merge Queue or Flaky Tests PR comments) stop working after changes to your IP allow list:

1. Check that the Trunk-managed entries have not been removed from your organization's IP allow list.
2. If you disabled the **Enable IP allow list configuration for installed GitHub Apps** setting, either re-enable it or manually add Trunk's server IP addresses.

### Need help?

If you continue to experience issues, contact [support@trunk.io](mailto:support@trunk.io) or reach out on our [Community Slack](https://slack.trunk.io).
