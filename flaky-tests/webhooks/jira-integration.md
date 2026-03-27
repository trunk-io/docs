---
description: Learn how to automatically create Jira issues with Flaky Test webhooks
---

# Jira integration

Trunk allows you to automate Jira issue creation through webhooks. When a test becomes flaky and impacts enough PRs, a Jira issue is created automatically with full context including failure rates, ownership, and stack traces.

This guide will walk you through integrating Trunk Flaky Tests with Jira through webhooks. You will be able to automatically generate Jira issues for **new flaky tests** found in your repo that **impact more than 2 PRs**. This guide should take 15 minutes to complete.

Trunk also has a [built-in Jira integration](../ticketing-integrations/jira-integration.md) for manual ticket creation. You only need to use webhooks if you want to automate ticket creation or need additional customization.

### 1. Create a Jira API Token

Before you can create a webhook to automate Jira issue creation, you need to create an API token to authorize your requests.

1. Go to [Atlassian API token management](https://id.atlassian.com/manage-profile/security/api-tokens).
2. Click **Create API token**, give it a label (e.g., "Trunk Webhooks"), and click **Create**.
3. Copy the token and save it in a secure location. You'll need it later.

You'll also need to generate a Base64-encoded credential string for authentication. Run this in your terminal:

```bash
echo -n "your-email@example.com:your-api-token" | base64
```

Replace `your-email@example.com` with the email associated with your Jira account and `your-api-token` with the token you just created. Save the output for step 3.

### 2. Add a new webhook in Trunk <a href="#id-2.-add-a-webhook-url-to-the-jira-api-in-trunk" id="id-2.-add-a-webhook-url-to-the-jira-api-in-trunk"></a>

Trunk uses Svix to integrate with other services, such as creating Jira issues through webhooks.

You can create a new endpoint by:

1. Login to [Trunk Flaky Tests](https://app.trunk.io/login?intent=flaky%20tests)
2. From your profile on the top right, navigate to **Settings**
3. Under **Organization > Webhooks**, click **Automate Jira Issues Creation**.
4. Set the **Endpoint URL** to your Jira Cloud REST API endpoint: `https://<your-domain>.atlassian.net/rest/api/2/issue`. Replace `<your-domain>` with your Jira Cloud domain (e.g., `acme` if your Jira URL is `acme.atlassian.net`).
5. Review the transformation code automatically generated for Jira issues. You can customize this transformation at any time. Learn more about [customizing transformations](#5-customize-your-transformation).
6. Create the new endpoint. You will be redirected to the endpoint configuration view.

If you're having trouble adding a new webhook endpoint with Svix, please see the [Adding Endpoint docs from Svix](https://docs.svix.com/receiving/using-app-portal/adding-endpoints).

### 3. Add custom headers

The Jira REST API requires authentication headers. You can configure custom headers in the endpoint configuration:

1. Navigate to **Webhooks > Advanced > Custom Headers.**
2. Fill in the **Key** and **Value** referencing the table below, and click the **+** button to add each header.

You'll need to configure the following headers:

| Key             | Value                    |
| --------------- | ------------------------ |
| `Authorization` | `Basic <BASE64_TOKEN>`   |
| `Content-Type`  | `application/json`       |

Replace `<BASE64_TOKEN>` with the Base64-encoded string you generated in [step 1](#1-create-a-jira-api-token).

### 4. Find your Jira project key and issue type

You'll need your Jira project key and preferred issue type to configure the transformation.

**Project key:** This is the short prefix on your Jira issues (e.g., `ENG`, `PROJ`, `KAN`). You can find it in the URL when viewing your Jira project: `https://your-domain.atlassian.net/jira/software/projects/<PROJECT_KEY>/board`.

**Issue type:** The type of issue to create. Common values are `Bug`, `Task`, or `Story`. The default is `Bug`.

### 5. Customize your transformation

Transformations are custom code snippets you can write to customize the Jira issues created by the webhook. A working template transformation will be added automatically for your webhook, but you can further customize the behavior.

1. In the endpoint configuration view, navigate to the **Advanced** tab. Under **Transformation**, toggle the **Enabled** switch.
2. Click **Edit transformation** to update your transformation code, and click **Save** to update the transformation.
3. You can test the transformation by selecting the `test_case.status_changed` payload and clicking **Run Test**. This will test the transformation but not send a message. You will learn to send a test message [in step 6](#6-test-your-webhook).

The generated webhook template contains several configurable constants out of the box:

<table><thead><tr><th width="346">Constant</th><th>Description</th></tr></thead><tbody><tr><td><code>JIRA_PROJECT_KEY</code></td><td>(<strong>Required)</strong> Your Jira project key (e.g., <code>ENG</code>, <code>PROJ</code>).</td></tr><tr><td><code>JIRA_ISSUE_TYPE</code></td><td><strong>(Optional)</strong> The issue type to create. Defaults to <code>Bug</code>.</td></tr><tr><td><code>JIRA_LABELS</code></td><td>(<strong>Optional)</strong> Array of labels to add to the issue. Defaults to <code>["flaky-test"]</code>.</td></tr><tr><td><code>JIRA_CUSTOM_FIELDS</code></td><td>(<strong>Optional)</strong> Object of custom field key-value pairs for projects that require additional fields.</td></tr><tr><td><code>PRS_IMPACTED_THRESHOLD</code></td><td>Issues will be created only for flaky tests that have impacted more PRs than the <code>PRS_IMPACTED_THRESHOLD</code>.<br><br>You can adjust this value if you see many issues about low-impact flaky tests.</td></tr></tbody></table>

Here is the provided transformation for context. You can customize your Jira issues integration by following the [Jira REST API docs](https://developer.atlassian.com/cloud/jira/platform/rest/v2/api-group-issues/#api-rest-api-2-issue-post) and [Svix transformations](https://docs.svix.com/transformations#using-transformations) documentation.

{% hint style="info" %}
The default transformation only creates issues when `newStatus === "flaky"`. If you also want to create issues for tests marked as **Broken** (consistently failing at a high rate), update the filter condition. For example, change `newStatus !== "flaky"` to `newStatus !== "flaky" && newStatus !== "broken"` to handle both statuses.
{% endhint %}

```javascript
/**
 * @param webhook the webhook object
 * @param webhook.method destination method. Allowed values: "POST", "PUT"
 * @param webhook.url current destination address
 * @param webhook.eventType current webhook Event Type
 * @param webhook.payload JSON payload
 * @param webhook.cancel whether to cancel dispatch of the given webhook
 */

// Your Jira project key (e.g., "PROJ", "ENG"). This is required!
const JIRA_PROJECT_KEY = "";
// The Jira issue type to create (e.g., "Bug", "Task", "Story"). Defaults to "Bug".
const JIRA_ISSUE_TYPE = "Bug";
// Labels to add to the Jira issue. Optional.
const JIRA_LABELS = ["flaky-test"];

// Add any custom required fields your Jira project needs. Optional.
// Example: { "customfield_10042": { "value": "Platform" }, "customfield_10043": "some-value" }
const JIRA_CUSTOM_FIELDS = {};

// At least this many PRs need to be impacted for an issue to be created.
const PRS_IMPACTED_THRESHOLD = 2;

function handler(webhook) {
  const impacted_prs = webhook.payload.test_case.pull_requests_impacted_last_7d;
  const newStatus = webhook.payload.status_change.current_status.value;

  // Filter for only flaky tests that impact more than the provided threshold
  if (newStatus !== "flaky" || impacted_prs < PRS_IMPACTED_THRESHOLD) {
    webhook.payload = "canceled";
    webhook.cancel = true;
    return webhook;
  }

  const description = summarizeTestCase(webhook.payload);

  webhook.payload = {
    fields: {
      project: { key: JIRA_PROJECT_KEY },
      issuetype: { name: JIRA_ISSUE_TYPE },
      summary: `Flaky Test: ${webhook.payload.test_case.name}`,
      description: description,
      labels: JIRA_LABELS,
      ...JIRA_CUSTOM_FIELDS,
    },
  };
  return webhook;
}

function summarizeTestCase(payload) {
  const {
    status_change: { previous_status },
    test_case: {
      name, file_path, status, quarantine, repository, codeowners,
      failure_rate_last_7d, most_common_failures,
      pull_requests_impacted_last_7d, ticket, html_url
    }
  } = payload;

  const issueBody = `See all details on the [Trunk Test Detail page|${html_url}]

Transition time: ${status.timestamp}

Severity (last 7 days): ${(failure_rate_last_7d * 100).toFixed(2)}% failure rate; impacting ${pull_requests_impacted_last_7d} PRs

Ownership: this test is owned by ${(codeowners || ['@unassigned']).join(', ')}

----
*The most common failure reasons (out of ${most_common_failures.length} identified) are:*

${most_common_failures.map((failure, index) => {
  return `*Reason #${index + 1}*: "${failure.summary}" \n`
}).join('')}

View the full stack trace on the [Test Detail page|${html_url}]
  `;
  return issueBody;
}
```

{% hint style="info" %}
The description uses [Jira wiki markup](https://jira.atlassian.com/secure/WikiRendererHelpAction.jspa?section=texteffects) for formatting. Links use the `[text|url]` syntax rather than markdown.
{% endhint %}

### 6. Test your webhook

You can create test issues by delivering a mock webhook. You can do this by:

1. In the endpoint configuration view, navigate to the **Testing** tab and select a **Send event**
2. Under **Subscribed events,** select `test_case.status_changed` as the event type to send
3. Click **Send Example** to test your webhook

### 7. Monitoring webhooks

You can monitor the events and the webhook's delivery logs in the **Overview** tab of an endpoint configuration view.

You can see an overview of how many webhook deliveries have been attempted, how many are successful, how many are in flight, and how many fail in the **Attempt Delivery Status** modal.

You can see a list of past delivery attempts in the **Message Attempts** modal. You can filter this list by **Succeeded** and **Failed** status, and you can click on each message to see the **Message content**, response code, and error message of each attempt. You can learn more about [replaying messages](https://docs.svix.com/receiving/using-app-portal/replaying-messages) and [filtering logs](https://docs.svix.com/receiving/using-app-portal/filtering-logs) in the Svix docs.

### Congratulations!

A Jira issue will now be created when a test's health status changes to **flaky** and **impacts more than 2 PRs**. You can further modify your transformation script to customize your issues.

[See the Trunk webhook event catalog](https://www.svix.com/event-types/us/org_2eQPL41Ew5XSHxiXZIamIUIXg8H/#test_case.status_changed)

[Learn more about consuming webhooks in the Svix docs](https://docs.svix.com/receiving/introduction)

[Learn more about Jira's REST API](https://developer.atlassian.com/cloud/jira/platform/rest/v2/intro/)
