---
description: >-
  Triage your flaky tests faster by creating automatically assigned and labeled
  tickets with the Jira integration
---

# Jira integration

When Trunk Flaky Tests [detects a flaky test](../detection/), you can create an automatically generated Jira ticket for your team to pick up and fix the test.

Webhook payloads will also contain ticket information when a Jira ticket is created with the integration or when [existing tickets are linked](jira-integration.md#link-existing-tickets-to-tests).

### Connecting to Jira

<figure><picture><source srcset="../../.gitbook/assets/jira-connect-form-dark.png" media="(prefers-color-scheme: dark)"><img src="../../.gitbook/assets/jira-connect-form-light.png" alt=""></picture><figcaption></figcaption></figure>

To connect a Jira Cloud project, navigate to **Settings** -> **Repositories** -> **Ticketing Integration** and select **Jira** as your Ticketing System.

Then complete the form and click Connect to Jira Cloud with the following information.

<table data-full-width="false"><thead><tr><th width="176">Field Name</th><th width="266">Description</th><th>Examples</th></tr></thead><tbody><tr><td>Jira URL</td><td>The URL to your Jira Cloud project.</td><td><code>https://trunk-io.atlassian.net</code></td></tr><tr><td>Project Key</td><td>The project key for your Jira project.</td><td><code>KAN</code></td></tr><tr><td>Email</td><td>The email associated with your Jira API token.</td><td><code>johndoe@example.com</code></td></tr><tr><td><a href="jira-integration.md#api-token-permissions">Jira API token</a></td><td><a href="https://id.atlassian.com/manage-profile/security/api-tokens">Create your Jira API token here.</a></td><td><code>ATATT*****19FNY5Q</code></td></tr><tr><td>Default label(s) for new tickets</td><td>Labels applied to new Jira tickets created through Trunk Flaky Tests</td><td><code>flaky-test, debt</code></td></tr></tbody></table>

After connecting to Jira, you can specify a default issue type for new tickets. Once an issue type is selected, the form fetches all available fields for that type and lets you configure default values for each one.

#### API Token permissions

Your Jira user account must have the following project permissions to create a Jira API token that allows Trunk to read, create, and assign tickets automatically:

* _Create issues_
* _Assign issues_ OR _Browse users and groups_ (global permission)
* _Browse projects_
  * If issue-level security is configured, issue-level security permissions must be granted to read issues.

You need to create an API token with the following scopes:

* Required scopes (classic)
  * `read:jira-work`
  * `write:jira-work`
  * `read:jira-user`
* Required scopes (granular):
  * `read:issue:jira`
  * `read:issue-meta:jira`
  * `read:issue-security-level:jira`
  * `read:issue.vote:jira`
  * `read:issue.changelog:jira`
  * `read:avatar:jira`
  * `read:status:jira`
  * `read:user:jira`
  * `read:field-configuration:jira`
  * `read:application-role:jira`
  * `read:group:jira`
  * `read:issue-type:jira`
  * `read:project:jira`
  * `read:project.property:jira`
  * `read:issue-type-hierarchy:jira`
  * `read:project-category:jira`
  * `read:project-version:jira`
  * `read:project.component:jira`
  * `read:permission:jira`
  * `write:issue:jira`
  * `write:comment:jira`
  * `write:comment.property:jira`
  * `write:attachment:jira`

{% hint style="info" %}
Jira tokens cannot last longer than 365 days. Once the token expires, you will need to generate a new API token.
{% endhint %}

### Create a new ticket

You can create a new ticket for any test listed in Trunk Flaky Tests.

There are 2 ways to create a new ticket in the Flaky Tests dashboard:

* Click on the options menu for any test case on the repo overview dashboard

<figure><picture><source srcset="../../.gitbook/assets/create-ticket-button-dark.png" media="(prefers-color-scheme: dark)"><img src="../../.gitbook/assets/create-ticket-button-light.png" alt=""></picture><figcaption></figcaption></figure>

* Use the Create ticket button in the top left corner of the [test case details](../dashboard.md#test-case-details) page.

Before you create the ticket, you will have a preview of the title and description.

<figure><picture><source srcset="../../.gitbook/assets/jira-ticket-creation-dark.png" media="(prefers-color-scheme: dark)"><img src="../../.gitbook/assets/jira-ticket-creation-light.png" alt=""></picture><figcaption></figcaption></figure>

#### Create with Jira

If you are connected to Jira, you can click the **Create Jira Ticket** button at the end of the modal. Any custom field defaults you configured in Settings are pre-filled in the modal. You can override them before submitting.

#### Link existing tickets to tests

If you already have a ticket in Jira that you want to link to a test in the dashboard, you can use the [Link Ticket to Test Case API](../flaky-tests.md#post-flaky-tests-link-ticket-to-test-case).

### Custom fields

The Trunk Flaky Tests Jira integration supports dynamic custom fields. When you select an issue type in Settings, Trunk fetches all configurable fields from Jira's API for that type and surfaces them in the form. Admins can set organization-wide defaults; users can override them when creating individual tickets.

#### Configure custom field defaults

1. Navigate to **Settings** -> **Repositories** -> **Ticketing Integration**
2. Select or update your issue type. The form reloads and displays all configurable fields for that type.
3. For each field, enter a default value. Fields marked as required in Jira must have either a default value or the **Require user to fill at creation** option checked.
4. Save your settings.

#### Supported field types

| Jira schema | Input |
| --- | --- |
| `string` | Text input |
| `number` | Number input |
| `option` | Searchable dropdown |
| `user` | Searchable dropdown (populated from your Jira project's assignable users) |
| `array` of `string` | Chip input (press Enter or comma to add values) |
| `textarea` | Multiline text input |

The following fields are always excluded because they are set automatically: `summary`, `description`, `project`, `issuetype`, `attachment`, `issuelinks`, and `parent`.

#### Required fields

If a field is marked required in Jira, you have two options:

* **Set a default value** — Trunk fills the field automatically on every ticket.
* **Require user to fill at creation** — The field appears blank in the create ticket modal and the user must fill it before submitting.

{% hint style="info" %}
Jira always marks the `reporter` field as required, but Jira auto-populates it with the API token owner if not provided. Trunk treats `reporter` as optional so it appears as an override rather than a blocking required field.
{% endhint %}

#### Override defaults at ticket creation

When creating a ticket, any field that has a configured default or is required at creation is shown in the modal. You can edit the pre-filled values before submitting.
