# Managing Your Organization

### Organization Slug and Token

Integrating with Trunk through [Webhooks](../../flaky-tests/webhooks/), [APIs](../../references/apis/), or [CLI](../../references/cli/) will require authentication using your organization's Trunk organization slug and token.

You can find your organization slug and token by going to **Settings** > **Manage** > **Organization**.&#x20;

{% tabs %}
{% tab title="Slug" %}
<figure><picture><source srcset="../../.gitbook/assets/org-slug-dark.png" media="(prefers-color-scheme: dark)"><img src="../../.gitbook/assets/org-slug-light.png" alt=""></picture><figcaption><p>Make sure you are getting your <em>Organization Slug</em>, not the Organization Name.</p></figcaption></figure>
{% endtab %}

{% tab title="Token" %}
<figure><picture><source srcset="../../.gitbook/assets/org-token-dark.png" media="(prefers-color-scheme: dark)"><img src="../../.gitbook/assets/org-token-light.png" alt=""></picture><figcaption><p>Ensure you get your <em>Organization API Token</em>, <em><strong>not your repo token</strong></em>.</p></figcaption></figure>
{% endtab %}
{% endtabs %}

### Trunk GitHub App

The Trunk GitHub app lets you integrate various Code Quality, Merge Queue, and Flaky Test features with your GitHub repos. It can help you[ lint commits and PRs](../../code-quality/ci-setup/github-integration.md), manage [merge queue branches](../../merge-queue/set-up-trunk-merge/), and post [PR comments about your test results](../../flaky-tests/github-pull-request-comments.md).

You can install the Trunk GitHub App by going to **Settings** > **Manage** > **Connect GitHub** and clicking **Connect**. You'll be redirected to GitHub to select the repositories where the GitHub app will be installed.

You can also [read more about the required permissions for the Trunk GitHub App](github-app-permissions.md).

### Team Domains

If your team uses emails managed by Google or Microsoft under a common domain, you can grant access to your team using **Team Domains**. When a team member creates a Trunk account with an email under you configured team domain, they will be granted access to your Trunk organization and repositories.

You can enable team domains under **Settings** > **Team Members** > **Team Domains** and clicking **Add**.

{% hint style="success" %}
Trunk also supports SSO login. If you wish to use SSO, please contact us at support@trunk.io.
{% endhint %}

### Inviting Team Members

You can invite individual members manually by navigating to **Settings** > **Team Members** > **Team Members** and clicking the :heavy\_plus\_sign: plus icon. An email will be sent to the invitee's inbox.

### Managing Team Members

You can manage a team member's role and remove team members by navigating to **Settings** > **Team Members** > **Team Members** and clicking on the name of a team member. You can change the role of a team member between user and admin, as well as removing the user from your organization.
