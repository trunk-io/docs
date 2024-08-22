---
description: Configure team settings and invite team members
---

# Manage Members & Organizations

The Trunk App is available at [app.trunk.io](https://app.trunk.io/). In the app, you can view the health of your repositories, browse issues detected by [Code Quality](../code-quality/), configure merge queues with [Merge](../merge-queue/), monitor CI with [CI Analytics](../ci-analytics/), and catch flaky tests detected by [Flaky Tests](../flaky-tests/).

## Creating a Trunk Organization <a href="#creating-a-trunk-organization" id="creating-a-trunk-organization"></a>

_Trunk Organizations_ are how you organize your repositories and your collaborators on [app.trunk.io](https://app.trunk.io/). You'll be asked to **Connect GitHub to your Organization** when you first log in.

1. Create or log in to your Trunk account at [app.trunk.io](https://app.trunk.io/).
2. If you are creating a new account, you will be prompted to connect to GitHub. This will automatically create a Trunk organization attached to the GitHub user or organization. If you need to add another organization, click on your profile on the top right, go to **Settings > Organization >** Click the plus icon.
3. In the "Create New Organization" modal, enter your organization's name.

## Adding your GitHub Repositories to your Trunk Organization (optional) <a href="#adding-your-github-repositories-to-your-trunk-organization-optional" id="adding-your-github-repositories-to-your-trunk-organization-optional"></a>

1. Create or log in to your Trunk account at [app.trunk.io](https://app.trunk.io/).
2. Navigate to the organization to which you'd like to add your GitHub repositories using the\
   Organization selector UI in the top left-hand corner.
3. Click the "Connect to GitHub" button
   1. You'll be redirected to Github.com to install the trunk.io Github app. Click the organization\
      or account you'd like to connect with Trunk.
   2. Select all the repositories you'd like to be able to connect to Trunk.
   3. On a successful installation, you'll be redirected back to\
      [app.trunk.io](https://app.trunk.io/) and Trunk will import your GitHub repository\
      data.

## Adding Team Members <a href="#inviting-teammates-to-your-trunk-organization" id="inviting-teammates-to-your-trunk-organization"></a>

Team members can be added automatically by setting the email domain or by individually inviting team members through email invites.

### Setting Your Trunk Organization's Email Domain <a href="#inviting-teammates-to-your-trunk-organization" id="inviting-teammates-to-your-trunk-organization"></a>

* Navigate to Settings → Team Members.
* Add your team's email domain. This will automatically add any existing and future Trunk users with an email in your domain to your Organization. This will not send invitations to any users to\
  confirm being added.

<figure><img src="../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

### Adding teammates by email.

You can invite users individually by clicking the `+` button in the "Team Members" section.\
This will allow you to invite members by specifying their email accounts. These users\
won't be automatically added to your Trunk organization. Instead, they will receive an email to\
opt-in to the organization. These users must create a Trunk account to accept the\
email invitation.

## SAML

Trunk does not currently support SAML. If you are interested in SAML support, please contact [sales@trunk.io](mailto:sales@trunk.io).
