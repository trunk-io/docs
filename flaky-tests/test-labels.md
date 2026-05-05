---
description: Organize and categorize test cases with organization-scoped labels.
---

# Test Labels

Test labels are organization-scoped tags you can apply to individual test cases to organize, filter, and categorize your test suite. Labels are applied manually today; see [Automatic labeling from monitors](#automatic-labeling-from-monitors) for what's coming.

<figure><img src="../.gitbook/assets/test-details-labels.png" alt="Labels applied to a test on details page"><figcaption></figcaption></figure>

### Manage labels

Labels are created, edited, and deleted at **Settings > Organization > Test Labels**. Each label has a name, an optional description, and a color used for its chip in the UI. The settings page also shows how many test cases each label is currently applied to.

{% hint style="warning" %}
Deleting a label removes it from every test case it's applied to; this cannot be undone.
{% endhint %}

<figure><img src="../.gitbook/assets/test-labels-settings.png" alt="Settings page to manage test labels"><figcaption></figcaption></figure>

### Apply and remove labels on a test case

You apply and remove labels from a test case using the label picker on the test case detail page. The picker lets you search existing labels, toggle them on or off, and create a new label inline if one doesn't already exist. Each assignment records who applied the label and when.

<figure><img src="../.gitbook/assets/test-details-label-picker.png" alt="Label picker on test details page"><figcaption></figcaption></figure>

### Filter tests by label

On the tests list, you can filter the table down to test cases that have a particular label applied. This makes labels useful for slicing the view by the categories your team cares about.

<figure><img src="../.gitbook/assets/tests-list-filtered-by-label.png" alt="Filter tests to those that have specified label applied"><figcaption></figcaption></figure>

### Automatic labeling from monitors

Monitors can automatically apply and remove labels on test cases based on test behavior. When a monitor activates (detects a flaky or broken test), it applies any configured labels to that test case. When the monitor resolves, it removes those labels.

You configure label actions in the **Actions** section of the monitor edit dialog. Use the **Add label** button to select the labels to apply when the monitor fires. You can configure separate sets of labels to apply on activation and remove on resolution.

The monitor list view shows label action chips on any monitor that has a label action configured, so you can see at a glance which monitors are set up to auto-label.

#### How label cleanup works

- **When you disable or delete a monitor:** any labels that monitor had applied are automatically removed from all affected test cases.
- **When you change the label set on a monitor's label action:** Trunk reconciles the existing label assignments to match the new configuration.
- **Deleting a label is blocked** if it is still configured in a label action on an active monitor. Remove it from the monitor's label action first.

{% hint style="info" %}
Automatic labeling from monitors is available on paid plans. If you don't see the label action option in your monitor config, contact support to confirm access.
{% endhint %}

### Related

* [Managing detected flaky tests](managing-detected-flaky-tests.md) — a step-by-step process for handling detected flaky tests
* [Flake Detection](detection/) — monitors that classify tests as flaky or broken
