---
description: Trunk Subscription Plans
---

# Billing

### Plans

#### **Free Plans**

Trunk offers a free plan to experiment with each of our features. Each feature has a free-tier limit; after exceeding this limit, we prompt you to upgrade to a paid subscription.

Similar to [calculating user counts](billing.md#calculating-user-counts), our free tier limits are calculated based on a 30-day rolling window.

<table><thead><tr><th width="155">Feature</th><th width="257">Metric</th><th>Free Tier Limit</th></tr></thead><tbody><tr><td>All</td><td>Users</td><td>5 commiters per month, unlimited on public repos</td></tr><tr><td>Code Quality</td><td>Quality &#x26; security metrics</td><td>Up to 100k issues uploaded</td></tr><tr><td>Merge Queue</td><td>PRs merged per month</td><td>100 PRs merged per month</td></tr><tr><td>Flaky Tests</td><td>Number of <a data-footnote-ref href="#user-content-fn-1">test spans</a></td><td>5 committers and 5M test spans per month</td></tr><tr><td></td><td>Data backfilling</td><td>Up to 30 days</td></tr></tbody></table>

#### Team Plans

Trunk Team Plans offers a monthly subscription plan using a per-seat model. At the end of every billing period, we calculate the number of users using Trunk and update the next month’s invoice to reflect the latest user count. Each seat has access to all of Trunk's features.

<table><thead><tr><th width="155">Feature</th><th width="257">Metric</th><th>Limits</th></tr></thead><tbody><tr><td>Code Quality</td><td>Quality &#x26; security metrics</td><td>Unlimited</td></tr><tr><td>Merge Queue</td><td>PRs merged per month</td><td>Unlimited</td></tr><tr><td>Flaky Tests</td><td>Number of <a data-footnote-ref href="#user-content-fn-1">test spans</a></td><td><p>1 million test spans per seat per month.</p><p>$3 for each additional 1 million test spans.</p></td></tr></tbody></table>

#### **Enterprise Plans**

Trunk Enterprise offers powerful admin controls, dedicated support, access to custom billing or terms, and features like SSO. If your team is interested in an enterprise plan, please contact [sales@trunk.io](mailto:sales@trunk.io).

**Trials**

You and your team can trial Trunk before signing up for an Enterprise or Team plan. To try Trunk, please contact [sales@trunk.io](mailto:sales@trunk.io). To extend or cancel the trial, please contact [sales@trunk.io](mailto:sales@trunk.io).

### Calculating User Counts

A user is a non-bot user who has made a commit to a private repo with Trunk enabled in the last 30 days. Specifically, we look at their username; if someone changes their username on Git, _we would consider that a separate user_. We do not count contributions to public (open source) repos. Contributor counts are displayed on **Settings** > **Billing**.

{% hint style="danger" %}
Trunk requires the [Trunk GitHub App](https://github.com/apps/trunk-io) to be installed in your repo to count seats.
{% endhint %}

For example, consider Alice, Bob, and Charlie are all in the same organization, which owns two private repos: `abc/repo1` and `abc/repo2`. Given the following timeline of events:

| Day 1                              | Day 15                           | Day 22                               |
| ---------------------------------- | -------------------------------- | ------------------------------------ |
| Alice commits code to `abc/repo1`. | Bob commits code to `abc/repo2`. | Charlie commits code to `abc/repo1`. |

On Day 1, the user count would be **one**: just Alice.\
On Day 15, the user count would be **two**: Alice and Bob, since the same organization owns both private repos.\
On Day 22, the user count would be **three**: Alice, Bob, and Charlie.\
On Day 30, the user count would be **three**. We consider days 1 through 30 (inclusive), which include Alice's, Bob's, and Charlie's commits.\
On Day 31, the user count would be **two**. We consider days 2 through 31 (inclusive), which only includes Bob's and Charlie's commits.

### Calculating an Invoice

At the end of every billing cycle, Trunk calculates what the next invoice should be. Trunk determines feature usage and the number of seats used over the [free tier usage limits](billing.md#free-plans-and-trials) . See our section on [calculating user counts](billing.md#calculating-user-counts) to determine how much we charge per feature usage.

### Editing Payment Details

You can edit your payment details by navigating to **Settings** > **Billing** and clicking on the pencil icon on the credit card. Trunk accepts both credit card and ACH; if you require a different payment method, please contact us at [sales@trunk.io](mailto:sales@trunk.io).

![](https://files.readme.io/d7adf4f-Screen_Shot_2023-01-17_at_8.08.17_PM.png)

### Cancelling a Plan

You can cancel an active Trunk subscription by navigating to **Settings** > **Billing** and clicking the **Cancel Subscription** button. Your plan will transition back into the [free tier](billing.md#free-plans-and-trials); if you want to re-enable this plan, please contact us at [sales@trunk.io](mailto:sales@trunk.io).

{% hint style="danger" %}
Cancelling a Trunk Plan may result in a degraded product experience. Please contact us at [sales@trunk.io](mailto:sales@trunk.io) to re-enable any canceled plan.
{% endhint %}

### A Note on Security

Your security is important to us. We do not store your credit card information anywhere in our systems. Online payments are processed using Stripe, which is PCI-compliant in accordance with industry standards.

[^1]: The number of test case results uploaded.
