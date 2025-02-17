---
description: Learn how to use flaky test webhooks to power Slack notifications
---

# Slack Integration

Trunk allows you to create custom workflows to send customized messages to Slack through webhooks.&#x20;

<figure><picture><source srcset="../../.gitbook/assets/example-slack-message (1).png" media="(prefers-color-scheme: dark)"><img src="../../.gitbook/assets/example-slack-message.png" alt=""></picture><figcaption></figcaption></figure>

This guide will walk you through sending Slack messages using event-triggered webhooks. By the end of this tutorial, you'll receive Slack messages for test status changes. This guide should take 10 minutes to complete.

### 1. Configure Slack Webhooks

Trunk uses Svix to integrate with other services, such as Slack, through webhooks.&#x20;

You can add the new Slack Webhook URL to Svix by following these steps:

1. Login to [Trunk Flaky Tests](https://app.trunk.io/login/?intent=flaky+tests)
2. From your profile on the top right, navigate to **Settings**
3.  Under **Organization > Webhooks**, click **Slack**&#x20;

    <figure><img src="../../.gitbook/assets/example-webhook-connector-light.png" alt=""><figcaption></figcaption></figure>
4.  Click **Connect to Slack** and select the server and channel to connect to.

    <figure><img src="../../.gitbook/assets/example-webhook-connector-slack (1).png" alt=""><figcaption></figcaption></figure>
5. Review the transformation code automatically generated for GitHub issues. You can customize this transformation at any time. Learn more about [customizing transformations](slack-integration.md#id-2.-customize-your-transformation).
6. By default, this connection will send messages about Trunk Merge and Flaky Tests events. If you only want Flaky Test events, unselect all events other than `test_case.status_changed`.
7. Create the new endpoint. You will be redirected to the endpoint configuration view.

If you're having trouble adding a new webhook endpoint with Svix, please see the [Adding Endpoint docs from Svix](https://docs.svix.com/receiving/using-app-portal/adding-endpoints).

### 2. Customize Your Transformation

Transformations are custom code snippets you can write to customize the Slack messages sent by the webhook. A working template transformation will be added automatically for your webhook, but you can further customize the behavior of this webhook.

1. In the endpoint configuration view, navigate to the **Advanced** tab. Under **Transformation**, toggle the **Enabled** switch.
2. Click **Edit transformation** to update your transformation code, and click **Save** to update the transformation.
3. You can test the transformation by selecting the `test_case.status_changed` payload and clicking **Run Test**. This will test the transformation but not send a message. You will learn to send a test message in [step 3](slack-integration.md#id-3.-test-your-webhook).

An example transformation script is provided below and you can customize your Slack integration by following the [Slack](https://api.slack.com/messaging/webhooks) and [Svix transformations](https://docs.svix.com/transformations#using-transformations) documentation.&#x20;

```javascript
/**
 * @param webhook the webhook object
 * @param webhook.method destination method. Allowed values: "POST", "PUT"
 * @param webhook.url current destination address
 * @param webhook.eventType current webhook Event Type
 * @param webhook.payload JSON payload
 * @param webhook.cancel whether to cancel dispatch of the given webhook
 */
function handler(webhook) {
  const payload = {"text": summarizeTestCase(webhook.payload)}
  
  webhook.payload = payload
  return webhook
}

function summarizeTestCase(payload) {
    if (!payload || typeof payload !== 'object' || !payload.test_case) {
        return "Error: Invalid or missing payload.";
    }

    const {
        test_case: {
            name = "N/A",
            file_path = "N/A",
            status = {},
            quarantine = false,
            repository = {},
            codeowners = [],
            failure_rate_last_7d = 0,
            most_common_failures = [],
            pull_requests_impacted_last_7d = 0,
            ticket = {},
            html_url = "N/A"
        }
    } = payload;

    const statusSummary = `Status: ${status.value || "Unknown"} `
        + `(Reason: ${status.reason?.trim() || "N/A"}, `
        + `Updated: ${status.timestamp ? new Date(status.timestamp).toLocaleString() : "Unknown"})`;

    const quarantineStatus = quarantine 
        ? "This test is currently quarantined." 
        : "This test is not quarantined.";

    const failureSummary = most_common_failures.map(failure =>
        `- ${failure.summary} (${failure.occurrence_count || 0} occurrences, `
        + `last seen: ${failure.last_occurrence ? new Date(failure.last_occurrence).toLocaleString() : "Unknown"})`
    ).join("\n");

    const repoLink = `Repository: ${repository.html_url || "N/A"}`;
    const testLink = `Test Details: ${html_url}`;
    const ticketLink = `Related Ticket: ${ticket.html_url || "N/A"}`;
    const ownerSummary = `Codeowners: \`${codeowners.join(", ") || "None"}\``;
    const statsSummary = `Failure rate (last 7 days): ${(failure_rate_last_7d * 100).toFixed(1)}% `
        + `| PRs Impacted: ${pull_requests_impacted_last_7d}`;

    return [
        `Test Name: \`${name}\``,
        `File Path: \`${file_path}\``,
        statusSummary,
        quarantineStatus,
        `Most Common Failures:\n${failureSummary}`,
        ownerSummary,
        statsSummary,
        repoLink,
        testLink,
        ticketLink
    ].join("\n");
}
```

### 3. Test Your Webhook

You can send test messages to your Slack channels as you make updates. You can do this by:

1. In the endpoint configuration view, navigate to the **Testing** tab and select a **Send event**
2. Under **Subscribed events,** select `test_case.status_changed`as the event type to send.
3. Click **Send Example** to test your webhook

### 4. Monitoring Webhooks

{% include "../../.gitbook/includes/monitoring-webhooks (1).md" %}

### Congratulations!

<figure><picture><source srcset="../../.gitbook/assets/example-slack-message (1).png" media="(prefers-color-scheme: dark)"><img src="../../.gitbook/assets/example-slack-message.png" alt=""></picture><figcaption></figcaption></figure>

You should now receive notifications in your Slack workspace when a test's status changes. You can further modify your transformation script to customize your messages.&#x20;

[See the Trunk webhook event catalog](https://www.svix.com/event-types/us/org_2eQPL41Ew5XSHxiXZIamIUIXg8H/#test_case.status_changed)

[Learn more about consuming webhooks in the Svix docs](https://docs.svix.com/receiving/introduction)

[Learn more about the Slack API](https://api.slack.com/messaging/webhooks)
