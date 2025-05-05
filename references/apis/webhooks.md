---
description: Comprehensive reference on the webhooks provided by Trunk, including event types, guides, and testing tips.
---

# Webhooks Reference

Webhooks let Trunk notify your systems in real-time about important events. When something changes — like a test becoming flaky or a merge queue advancing — Trunk can send an HTTP POST payload to your configured endpoint. You can then trigger automated workflows in response.

If you're integrating Trunk into your CI/CD pipelines or internal tools, webhooks are the recommended way to stay in sync.

<figure><img src="../../.gitbook/assets/webhook-event-catalog (1).png" alt="Trunk webhook event catalog"></figure>

## Available Webhook Events

Trunk uses [Svix](https://www.svix.com/) to deliver webhook events. You can browse the full list of available events, including their payload structure and versions, in the Trunk Webhook Events Catalog:

{% embed url="https://www.svix.com/event-types/us/org_2eQPL41Ew5XSHxiXZIamIUIXg8H" %}

You'll find events such as:

| Event Type                      | Description                               |
| -------------------------------- | ----------------------------------------- |
| `flaky_test.created`             | A new flaky test is detected.             |
| `merge_queue.entry_added`        | A PR is added to the merge queue.         |
| `merge_queue.entry_merged`       | A PR in the queue is successfully merged. |

Refer to the catalog for a complete and up-to-date event list with example payloads.

## Guides and Examples

To help you get started, we’ve prepared specific guides for different Trunk products. These walk you through configuring and consuming webhook events.

| Webhook Type           | Documentation |
| ---------------------- | ------------- |
| Webhooks for Flaky Tests | [Read guide →](../../flaky-tests/webhooks/) |
| Merge Queue Webhooks    | [Read guide →](../../merge-queue/webhooks.md) |

Each guide includes payload examples, security notes, and tips on setting up retries and handling idempotency.

## Testing Your Webhook Integration

Before deploying your webhook handlers to production, it's a good idea to test them using a webhook inspection tool. This way, you can verify that you're parsing the payloads correctly and handling retries or failures as expected.

You can use:

- [Beeceptor](https://beeceptor.com) — create a custom endpoint, inspect incoming requests, and simulate different responses.
- [Pipedream RequestBin](https://pipedream.com/requestbin) — capture requests, inspect headers and bodies, and even trigger downstream workflows.

Testing tools like these help ensure your webhook consumer is robust before going live.
