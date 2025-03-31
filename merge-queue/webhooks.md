# Webhooks

Trunk provides a variety of webhooks to allow responding to various events from Trunk. Each event corresponds to a Trunk feature and an action within that feature (for example, a Pull Request being submitted to Trunk Merge).

### Supported Events

Trunk provides various webhooks to respond to events from Trunk Flaky Tests. Flaky Test events are named with a `pull_request` prefix, you can find the events you can respond to in the Webhook Events reference from Svix.&#x20;

{% embed url="https://www.svix.com/event-types/us/org_2eQPL41Ew5XSHxiXZIamIUIXg8H" %}

You can learn about the Svix event catalog in the [Svix docs](https://docs.svix.com/receiving/using-app-portal/event-catalog).

{% hint style="info" %}
If you don't currently have an endpoint ready to receive webhooks, you can quickly set up a URL for testing by clicking the "use Svix Play" link - you'll be able to inspect all webhook events sent there.
{% endhint %}

