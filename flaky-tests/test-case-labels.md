---
description: Organize and categorize tests across your organization with custom labels
---

# Test Case Labels

Test case labels let you organize tests across your organization by attaching custom tags to individual test cases. Labels are defined at the organization level and can be applied to any test case, making it easier to filter, search, and triage flaky tests by team, product area, priority, or any other dimension that fits your workflow.

### Managing labels

Labels are managed under **Settings** -> **Organization** -> **Test Labels**.

From this page you can:

* **Create** a new label with a name, optional description, and color
* **Edit** an existing label's name, description, or color
* **Delete** labels that are no longer needed

Label names must be unique within your organization and follow standard naming conventions. Each label also supports a hex color code to help distinguish labels visually.

### Applying labels to tests

Once labels are created in org settings, you can apply them to individual test cases from the test case detail page in the Flaky Tests dashboard.

### Use cases

Labels work well for organizing tests by:

* **Team ownership** — tag tests with the team responsible for fixing them
* **Product area** — group tests by feature or service
* **Priority** — mark high-impact flakes that need immediate attention
* **Triage status** — track investigation state across multiple tests at once
