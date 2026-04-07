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

After connecting to Jira, you can specify a default issue type for new tickets and a default assignee for new tickets.

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

If you are connected to Jira, you can click the **Create Jira Ticket** button at the end of the modal, which will automatically create a ticket with the configured labels and assignees.

#### Link existing tickets to tests

If you already have a ticket in Jira that you want to link to a test in the dashboard, you can use the [Link Ticket to Test Case API](../flaky-tests.md#post-flaky-tests-link-ticket-to-test-case).

### Custom Fields

Trunk Flaky Tests supports Jira custom fields for ticket creation. Admins can configure default values for any supported Jira field on a per-issue-type basis, and users can override those defaults when creating individual tickets.

#### Configure default custom field values

Admins set default custom field values in the ticketing integration settings. These defaults apply to all tickets created through Trunk Flaky Tests for the configured issue type.

1. Navigate to **Settings** → **Repositories** → **Ticketing Integration**
2. Under your Jira connection, select the issue type you want to configure
3. The form will load the available fields for that issue type, including any custom fields your Jira project exposes
4. Fill in default values for the fields you want pre-populated on new tickets
5. Save your changes

Supported field types include text fields, dropdowns, user pickers, version pickers, and other standard Jira field types.

#### Override custom fields when creating a ticket

When creating a ticket from the Trunk dashboard, the create ticket modal shows all configured fields for the selected issue type. Values pre-filled from your defaults can be changed before submitting.

To create a ticket with custom field values:

1. Open the create ticket dialog for a flaky test
2. Review and update any pre-filled custom field values
3. Fill in any additional fields as needed
4. Click **Create Jira Ticket**

#### If required fields are missing

If your Jira project requires a custom field that isn't appearing in the Trunk settings form, check that the field is assigned to the issue type you're using. Jira custom fields are scoped per issue type — a field may be required for "Bug" but not for "Task". If the field still doesn't appear after verifying your Jira configuration, contact [support@trunk.io](mailto:support@trunk.io).

#### Alternative: Remove field requirements in Jira

You can also modify your Jira project settings to make custom fields optional rather than required. This lets Trunk create tickets without specifying those fields.

1. Navigate to **Project Settings** in your Jira project
2. Select **Issue Types** from the sidebar
3. Choose the issue type you're using for flaky test tickets
4. Click **Fields** and locate the required custom field
5. Uncheck **Required** and save your changes

{% hint style="info" %}
You may need Jira Administrator permissions to modify project settings.
{% endhint %}
