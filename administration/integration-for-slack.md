---
description: >-
  Trunk Code Quality, Trunk Merge, and other Trunk products can communicate directly
  with your developer team through Slack.
---

# Integration for Slack

With the Trunk app for Slack, you can easily get notifications from all of your trunk-enabled products. This includes notifications around security issues detected by `trunk check` and workflow notifications for your pull requests as they queue and land with `trunk merge`. In this guide, we'll cover how to connect Slack with Trunk on the repository and user level, as well as the different ways you can use Trunk in Slack.

## Add Trunk to your Slack Workspace (admin privileges required)

To receive notifications and/or interact with Trunk from Slack, an admin needs to add Trunk to your organization's Slack workspace. To do this:

1.  Navigate to [https://app.trunk.io](https://app.trunk.io). Click **Settings** > **Repositories** > find **Connect with Slack** under the product you'd like to connect > click **Connect**

    <figure><img src="https://files.readme.io/14d4355-image.png" alt=""><figcaption></figcaption></figure>
2. This will open a window where you can sign in to your Slack workspace.

<div data-full-width="false">

<figure><img src="../.gitbook/assets/testtrunkintegration.slack.com_oauth_client_id=1523871431059.3961451315218&#x26;scope=incoming-webhook%2Cchannels%3Ajoin%2Cchannels%3Amanage&#x26;user_scope=&#x26;redirect_uri=https%3A%2F%2Fapp.trunk.io%2Fslack%2F07e100e0-5053-42ed-8d13-cd953bba3b42%3Frep.png" alt="Dialog to connect Trunk to your Slack workspace" width="563"><figcaption></figcaption></figure>

</div>

3. Once you press **Allow**, Trunk will connect to your Slack automatically and begin pushing updates to the channel you have selected.

## Set repo-level notification preferences

Now that you've connected your Slack account with Trunk, you will choose the type of notifications you want to receive from Trunk in Slack. You can manage your repository notifications under **Settings** > **Repositories >** find **Notifications** under the product you'd to manage.

{% tabs %}
{% tab title="trunk merge" %}
<figure><img src="../.gitbook/assets/Screenshot 2024-06-04 at 6.35.18 PM.png" alt=""><figcaption><p>Configure Slack notifications for Trunk Merge</p></figcaption></figure>
{% endtab %}

{% tab title="trunk check" %}
<figure><img src="../.gitbook/assets/Screenshot 2024-06-04 at 6.29.22 PM.png" alt=""><figcaption><p>Configure notifications for Trunk Code Quality</p></figcaption></figure>
{% endtab %}
{% endtabs %}

## Set your user-level notification preferences

To set your individual user Slack notifications go to **Settings** > **Account** > **Connect**

<figure><img src="../.gitbook/assets/Screenshot 2024-06-04 at 6.34.10 PM.png" alt=""><figcaption><p>Configure Slack notifications for your user.</p></figcaption></figure>

[Privacy Policy](https://trunk.io/privacy)
