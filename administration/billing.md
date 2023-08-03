# Billing

### Pricing Overview

Trunk offers a monthly subscription plan using a per-seat model. We calculate the number of users using Trunk at the end of every billing period, and update the next month’s invoice to reflect the latest user count.

If you are the admin of your organization, you can view your current billing settings by navigating to Settings > Billing.

### Calculating User Counts

A user is defined as someone who has contributed to the main branch of your private repositories in the last 90 days. Specifically, we look at their username; if someone changes their username on Git, we would consider that a separate user.

For example, consider Alice, Bob, and Charlie are all in the same organization, which owns two private repos: `abc/repo1` and `abc/repo2`. Given the following timeline of events:

| Day 1                              | Day 35                           | Day 42                               |
| ---------------------------------- | -------------------------------- | ------------------------------------ |
| Alice commits code to `abc/repo1`. | Bob commits code to `abc/repo2`. | Charlie commits code to `abc/repo1`. |

On Day 30, the user count would be 1: just Alice.\
On Day 40, the user count would be two: Alice and Bob, since the same organization owns both private repos.\
On Day 50, the user count would be three: Alice, Bob, and Charlie.\
On Day 90, the user count would be three. We consider days 1 thru 90 (inclusive), which includes Alice's, Bob's, and Charlie's commits.\
On Day 91, the user count would be two. We consider days 2 thru 91 (inclusive), which only includes Bob's and Charlie's commits.

### Calculating an Invoice

At the end of every billing cycle, Trunk calculates what the next invoice should be. Trunk determines which products are billing eligible, then charges you for the number of users using that product. A product is billing eligible if you are already paying for that product, or if you have exceeded your [free tier usage limits](../administration/billing.md#free-plans-and-trials) . See our section on [calculating user counts](../administration/billing.md#calculating-user-counts) to determine how much we charge per product.

For example, consider a team of 19 that owns many repositories. Assume that they are currently paying for Merge and Check, but are trying out CI Analytics.

For the first billing cycle, their invoice would look something like this:

![](https://files.readme.io/63bc876-Screen_Shot_2023-01-17_at_8.01.43_PM.png)

At the beginning of the next billing cycle, they have exceeded their [free tier usage](../administration/billing.md#free-plans-and-trials) of CI Analytics. In that case, we would see three invoice line items; one for Merge, one for Check, and another for CI Analytics. The quantity per product would also be reflected with the [latest user counts](../administration/billing.md#calculating-user-counts).

### Free Plans and Trials

**Free Plans**

Trunk offers a free plan to experiment with each of our products. Each product has a free-tier limit; after exceeding this limit, the product is automatically added to any ongoing subscription, and will be billed on the next cycle. If there is no ongoing subscription, we prompt you to upgrade to a paying subscription.

For example, this user is already paying for 19 users for Check and Merge, but was not paying for CI Analytics. On the next billing cycle, the user will start to be charged for CI Analytics.

![](https://files.readme.io/f12daf8-Screen_Shot_2023-01-17_at_8.04.29_PM.png)

**Free Tier Limits**

Similar to [calculating user counts]../administration/billing.md#calculating-user-counts), our free tier limits are calculated based on a 30 day rolling window.

| Product      | Free Tier Limit         |
| ------------ | ----------------------- |
| Check        | 100,000 Files Checked   |
| Merge        | 100 PRs Merged          |
| CI Analytics | 14 Days of CI Analytics |

CI Analytics is calculated slightly differently; we ingest 14 days of data for free.

**Trials**

Trunk offers you to trial products, either standalone or alongside a paying subscription. To enable a trial, please contact [sales@trunk.io](mailto:sales@trunk.io). At the end of a trial, the product will be automatically added to any ongoing paying subscription; to extend or cancel the trial, please contact [sales@trunk.io](mailto:sales@trunk.io).

### Editing Payment Details

You can edit your payment details by navigating to Settings > Billing, and clicking on the pencil icon of the credit card. Trunk accepts both Credit Card and ACH; if you have a different preferred payment method, please contact us at sales@trunk.io

![](https://files.readme.io/d7adf4f-Screen_Shot_2023-01-17_at_8.08.17_PM.png)

### Cancelling a Plan

You can cancel an active Trunk subscription by navigating to Settings > Billing and clicking the “Cancel Subscription” button. Your plan will transition back into the [free tier](../administration/billing.md#free-plans-and-trials); if you want to re-enable this plan, please contact us at sales@trunk.io.

> 🚧
>
> Cancelling a Trunk Plan may result in a degraded product experience. Please contact us at sales@trunk.io to re-enable any canceled plan.

### A Note on Security

Your security is important to us. We do not store your credit card information anywhere in our systems. Online payments are processed using Stripe, which is PCI compliant in accordance with industry standards.
