---
description: Organize and categorize test cases with organization-scoped labels.
---

# Test Labels

Test labels are organization-scoped tags you can apply to individual test cases to organize, filter, and categorize your test suite. Labels can be applied manually or automatically by monitors.

<figure><img src="../../.gitbook/assets/test-details-labels.png" alt="Labels applied to a test on details page"><figcaption></figcaption></figure>

### Manage labels

Labels are created, edited, and deleted at **Settings > Organization > Test Labels**. Each label has a name, an optional description, and a color used for its chip in the UI. The settings page also shows how many test cases each label is currently applied to.

{% hint style="warning" %}
Deleting a label removes it from every test case it's applied to; this cannot be undone.
{% endhint %}

<figure><img src="../../.gitbook/assets/test-labels-settings.png" alt="Settings page to manage test labels"><figcaption></figcaption></figure>

### Apply and remove labels on a test case

You apply and remove labels from a test case using the label picker on the test case detail page. The picker lets you search existing labels, toggle them on or off, and create a new label inline if one doesn't already exist. Each assignment records who applied the label and when.

<figure><img src="../../.gitbook/assets/test-details-label-picker.png" alt="Label picker on test details page"><figcaption></figcaption></figure>

### Filter tests by label

On the tests list, you can filter the table down to test cases that have a particular label applied. This makes labels useful for slicing the view by the categories your team cares about.

<figure><img src="../../.gitbook/assets/tests-list-filtered-by-label.png" alt="Filter tests to those that have specified label applied"><figcaption></figcaption></figure>

### Automatic labeling from monitors

Monitors can automatically apply labels to test cases when the monitor activates. This lets you tag tests as they accumulate failures without any manual triage.

When creating a failure count or failure rate monitor, you choose the **action type**:

* **Classify test status** — the monitor marks tests as flaky or broken (the default behavior)
* **Apply labels** — the monitor tags matching tests with one or more labels when it activates

The action type is set at creation and cannot be changed afterward. If you need to switch a monitor's action type, create a new monitor with the desired type and disable the old one.

To configure automatic labeling:

1. Go to **Flaky Tests** > select your repository > **Monitors**
2. Click **Add** next to the monitor type you want to create
3. In the creation form, select **Apply labels** as the action type
4. Choose one or more labels to apply when the monitor activates
5. Complete the rest of the monitor configuration and save

Tests that the monitor flags will have the selected labels applied automatically. You can still apply or remove labels manually on top of what monitors set.

### Related

* [Managing detected flaky tests](managing-detected-flaky-tests.md) — a step-by-step process for handling detected flaky tests
* [Flake Detection](../detection/) — monitors that classify tests as flaky or broken
