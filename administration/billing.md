---
description: Trunk Subscription Plans
---

# Billing

### Pricing Overview

Trunk offers a monthly subscription plan using a per-seat model. We calculate the number of users using Trunk at the end of every billing period, and update the next month’s invoice to reflect the latest user count.

If you are the admin of your organization, you can view your current billing settings by navigating to **Settings** > **Billing**.

### Calculating User Counts

\
A user is a non-bot user who have made a commit to a private repo with Trunk enabled in the last 30 days. Specifically, we look at their username; if someone changes their username on Git, _we would consider that a separate user_. We do not count contributions to public (open source) repos. Contributor counts are displayed on **Settings** > **Billing**.

For example, consider Alice, Bob, and Charlie are all in the same organization, which owns two private repos: `abc/repo1` and `abc/repo2`. Given the following timeline of events:

| Day 1                              | Day 15                           | Day 22                               |
| ---------------------------------- | -------------------------------- | ------------------------------------ |
| Alice commits code to `abc/repo1`. | Bob commits code to `abc/repo2`. | Charlie commits code to `abc/repo1`. |

On Day 1, the user count would be **one**: just Alice.\
On Day 15, the user count would be **two**: Alice and Bob, since the same organization owns both private repos.\
On Day 22, the user count would be **three**: Alice, Bob, and Charlie.\
On Day 30, the user count would be **three**. We consider days 1 thru 30 (inclusive), which includes Alice's, Bob's, and Charlie's commits.\
On Day 31, the user count would be **two**. We consider days 2 thru 31 (inclusive), which only includes Bob's and Charlie's commits.

### Calculating an Invoice

At the end of every billing cycle, Trunk calculates what the next invoice should be. Trunk determines which products are billing eligible, then charges you for the number of users using that product. A product is billing eligible if you are already paying for that product, or if you have exceeded your [free tier usage limits](billing.md#free-plans-and-trials) . See our section on [calculating user counts](billing.md#calculating-user-counts) to determine how much we charge per product.

For example, consider a team of 19 that owns many repositories. Assume that they are currently paying for Merge and Check, but are trying out CI Analytics.

For the first billing cycle, their invoice would look something like this:

![](https://files.readme.io/63bc876-Screen\_Shot\_2023-01-17\_at\_8.01.43\_PM.png)

At the beginning of the next billing cycle, they have exceeded their [free tier usage](billing.md#free-plans-and-trials) of CI Analytics. In that case, we would see three invoice line items; one for Merge, one for Check, and another for CI Analytics. The quantity per product would also be reflected with the [latest user counts](billing.md#calculating-user-counts).

### Free Plans and Trials

**Free Plans**

Trunk offers a free plan to experiment with each of our products. Each product has a free-tier limit; after exceeding this limit, the product is automatically added to any ongoing subscription, and will be billed on the next cycle. If there is no ongoing subscription, we prompt you to upgrade to a paid subscription.

For example, this user is already paying for 19 users for Check and Merge, but was not paying for CI Analytics. On the next billing cycle, the user will start to be charged for CI Analytics.

![](https://files.readme.io/f12daf8-Screen\_Shot\_2023-01-17\_at\_8.04.29\_PM.png)

**Free Tier Limits**

Similar to [calculating user counts](billing.md#calculating-user-counts), our free tier limits are calculated based on a 30 day rolling window.

<table><thead><tr><th width="155">Product</th><th width="257">Metric</th><th>Free Tier Limit</th></tr></thead><tbody><tr><td>All</td><td>Users</td><td>5 commiters per month, unlimited on public repos</td></tr><tr><td>Check</td><td>Quality &#x26; security metrics</td><td>Up to 100k issues uploaded</td></tr><tr><td>Merge</td><td>PRs merged per month</td><td>100 PRs merged per month</td></tr><tr><td>CI Analytics</td><td>Real-time ingestion of data</td><td><p>14 days per repo</p><p></p></td></tr><tr><td></td><td>Data backfilling</td><td>Up to 30 days</td></tr></tbody></table>

**Trials**

Trunk offers you to trial products, either standalone or alongside a paying subscription. To enable a trial, please contact [sales@trunk.io](mailto:sales@trunk.io). At the end of a trial, the product will be automatically added to any ongoing paying subscription; to extend or cancel the trial, please contact [sales@trunk.io](mailto:sales@trunk.io).

#### Open Source

Trunk is also free for open-source projects. If you're a open source project maintainer and maintain your project in a public repo, you can use Trunk products at any scale without limitations.

### Editing Payment Details

You can edit your payment details by navigating to Settings > Billing, and clicking on the pencil icon of the credit card. Trunk accepts both Credit Card and ACH; if you have a different preferred payment method, please contact us at sales@trunk.io

![](https://files.readme.io/d7adf4f-Screen\_Shot\_2023-01-17\_at\_8.08.17\_PM.png)

### Cancelling a Plan

You can cancel an active Trunk subscription by navigating to Settings > Billing and clicking the “Cancel Subscription” button. Your plan will transition back into the [free tier](billing.md#free-plans-and-trials); if you want to re-enable this plan, please contact us at sales@trunk.io.

> 🚧
>
> Cancelling a Trunk Plan may result in a degraded product experience. Please contact us at sales@trunk.io to re-enable any canceled plan.

### A Note on Security

Your security is important to us. We do not store your credit card information anywhere in our systems. Online payments are processed using Stripe, which is PCI compliant in accordance with industry standards.
