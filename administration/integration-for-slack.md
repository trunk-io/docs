---
description: >-
  Trunk Check, Trunk Merge, and other Trunk products can communicate directly
  with your developer team through Slack.
---

# Integration for Slack

With the Trunk app for Slack, you can easily get notifications from all of your trunk-enabled products. This includes notifications around security issues detected by `trunk check` and workflow notifications for your pull requests as they queue and land with `trunk merge`. In this guide, we'll cover how to connect Slack with Trunk on the repository and user level, as well as the different ways you can use Trunk in Slack.

## Add Trunk to your Slack Workspace (admin privileges required)

To receive notifications and/or interact with Trunk from Slack, an admin needs to add Trunk to your organization's Slack workspace. To do this:

1.  Navigate to [https://app.trunk.io](https://app.trunk.io). Select the repo you would like to Manage. Click "Settings" > "Connect"\\

    <figure><img src="https://files.readme.io/14d4355-image.png" alt=""><figcaption></figcaption></figure>
2. This will open a window where you can sign in to your Slack team.

<figure><img src="../.gitbook/assets/PermissinoPage.png" alt="" width="375"><figcaption></figcaption></figure>

3. Once you press "Allow," Trunk will connect to your Slack automatically and begin pushing updates to the channel you have selected.

## Set repo-level notification preferences

Now that you've connected your Slack account with Trunk, you will choose the type of notifications you want to receive from Trunk in Slack. You can manage your repository notifications under your repo settings.

{% tabs %}
{% tab title="trunk merge" %}
<figure><img src="../.gitbook/assets/MergeOptions.png" alt=""><figcaption><p>Configure notifications for <code>trunk merge</code></p></figcaption></figure>
{% endtab %}

{% tab title="trunk check" %}
<figure><img src="../.gitbook/assets/CheckOptions.png" alt=""><figcaption><p>Configure notifications for <code>trunk check</code></p></figcaption></figure>
{% endtab %}
{% endtabs %}

## Set your user-level notification preferences

To set your individual user Slack notifications go to Settings > Account > Connect

![](https://files.readme.io/3491658-SCR-20230605-efb-2.png)

[Privacy Policy](https://trunk.io/privacy)
