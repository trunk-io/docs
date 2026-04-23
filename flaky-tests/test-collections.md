---
description: >-
  Organize your flaky tests into named collections to track and analyze specific
  subsets of your test suite.
---

# Test Collections

Test Collections let you group tests from any repository into named sets. Use collections to focus on a subset of your test suite, such as tests owned by a specific team, tests covering a critical service, or any grouping that matters to your workflow.

Each collection has its own view of tests, uploads, and settings, separate from the full test suite view.

## Create a collection

Only organization admins can create collections.

1. Navigate to **Flaky Tests** > **Collections** in the Trunk web app.
2. Click **Create Collection**.
3. Enter a **Name** and optional **Description**.
4. Click **Create collection**.

After creation, you land on the collection detail page. The **Tests** and **Uploads** tabs are disabled until you upload test results to the collection.

## Upload tests to a collection

To populate a collection with test data, include the collection's short ID in your uploader configuration. The collection short ID appears in the URL when viewing the collection:

```
https://app.trunk.io/<org>/flaky-tests/collections/<short-id>
```

Pass the short ID when uploading results using the Trunk CLI:

```bash
trunk flakytests upload --collection <short-id> ...
```

See the [Uploader reference](uploader.md) for full upload options.

## View collection tests and uploads

Once tests are uploaded to a collection, the **Tests** and **Uploads** tabs become active on the collection detail page.

* **Tests** tab: Shows all tests associated with this collection, with their flaky status, failure rates, and labels.
* **Uploads** tab: Shows the history of test uploads sent to this collection.
* **Overview** tab: Shows setup instructions and the upload configuration for this collection.

## Edit a collection

Only organization admins can edit collection settings.

1. Navigate to the collection detail page.
2. Click the **Settings** tab.
3. Update the **Name** or **Description**.
4. Click **Save changes**.

## Delete a collection

Only organization admins can delete collections.

1. Navigate to the collection's **Settings** tab.
2. Click **Delete Collection**.
3. Confirm deletion in the dialog.

Deleting a collection removes it from the Collections list. Test data uploaded to the collection is not deleted from your overall test suite.

## Permissions

| Action | Admin | Member |
|---|---|---|
| View collections | Yes | Yes |
| Create collection | Yes | No |
| Edit collection settings | Yes | No |
| Delete collection | Yes | No |

Members can browse existing collections and view tests and uploads, but cannot create, edit, or delete collections.
