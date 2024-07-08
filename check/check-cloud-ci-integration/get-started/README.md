---
description: Automate your code quality enforcement with just a few clicks.
---

# GitHub Integration

Now that you have `trunk check` running on your local computer, your next step is to run Trunk automatically in the cloud and share notifications with your whole team. _Start by connecting your Trunk organization to GitHub._

## Connect your Trunk organization to GitHub

Sign up at [app.trunk.io](https://app.trunk.io), create a Trunk organization, and connect it to your repositories. You will need to grant the following [GitHub App permissions](../../../administration/github-app-permissions.md).

{% @supademo/embed demoId="HXyBmoBn0_OX9Xite2fqd" url="https://app.supademo.com/demo/HXyBmoBn0_OX9Xite2fqd" %}

## Set Up Trunk Check

Once your Trunk organization is connected to GitHub, create a .trunk repo in your account or organization and grant Trunk permissions to access the repo.  The .trunk repo will hold the workflows to scan your codebase and pull requests. [Learn more about the .trunk repo](https://docs.trunk.io/check/check-cloud-ci-integration/get-started/github-integration#what-is-a-.trunk-repository).

{% @supademo/embed demoId="pRr_eDzh-klIQdK_yW3se" url="https://app.supademo.com/demo/pRr_eDzh-klIQdK_yW3se" %}

## Configure Slack Notifications (optional)

If you would like to receive notifications for new issues Trunk finds in your repo, you can configure Trunk to be connected to Slack.

{% @supademo/embed demoId="cllpdjqhy1jf1051a1nff1a3y" url="https://app.supademo.com/demo/cllpdjqhy1jf1051a1nff1a3y" %}

## Use it!

### Ensure that PRs are free of issues

Check out [this example](https://github.com/trunk-io/plugins/pull/424/checks?check\_run\_id=15730277425) in our `plugins` repository!

<div data-full-width="true">

<figure><img src="../../../.gitbook/assets/image (35).png" alt=""><figcaption><p>Trunk Check identifying a security issue in one of Trunk's own repositories</p></figcaption></figure>

</div>

### Explore issues in your repository

Keep track of pre-existing issues in your repository without creating noise in commits and PRs. Track your code base health over time and find ways to incrementally improve code quality.&#x20;

<figure><img src="../../../.gitbook/assets/Screenshot 2023-08-23 173119.png" alt=""><figcaption><p>Trunk Check showing all the issues present in trunk-demo1/sass</p></figcaption></figure>

### Get Slack notifications about new issues in your repository

Not only do our daily scans allow you to browse and triage the issues in your repository, but they can also notify you when new security issues are discovered in packages you already depend on.

<div data-full-width="true">

<figure><img src="../../../.gitbook/assets/Screenshot 2023-08-23 173252.png" alt=""><figcaption><p>Slack notification showing newly discovered issues with rustls-webpki in trunk-io/trunk</p></figcaption></figure>

</div>

## Learn more

[Read the documentation about our GitHub integration to learn more.](github-integration.md)

If you don't host your source code on GitHub, we recommend setting[ up Trunk locally](broken-reference).
