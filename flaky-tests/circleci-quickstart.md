# CircleCI Quickstart

## Getting Started

You can use the analytics test uploader within your [CircleCI](https://circleci.com/) workflows to upload your test results.

{% hint style="info" %}
The Trunk Flaky Tests uploader currently only supports Linux x64. If you have another use case, please get in touch with support at [https://slack.trunk.io](https://slack.trunk.io/). For the best results, you'll need to validate that your test invocation doesn't use cached test results and doesn't automatically retry failing tests.
{% endhint %}

1. Create a CircleCI workflow that runs the tests you want to monitor. In order for us to use the results, these tests **must** produce a test report in [JUnit XML](https://github.com/testmoapp/junitxml) format.&#x20;

## Find Organization Slug and Token

Next you will need your Trunk **organization slug** and **token.** Navigate to [app.trunk.io](http://app.trunk.io). Once logged in navigate to Settings -> Manage -> Organization.  Copy your organization slug. You can find your Trunk token by navigating to Settings → Manage Organization → Organization API Token and clicking "View."  Copy this token.

{% @supademo/embed demoId="clvmr1w3d19ac769dnukc5ywg" url="https://app.supademo.com/demo/clvmr1w3d19ac769dnukc5ywg" %}

In your CircleCI dashboard, store your Trunk token in a secret named TRUNK\_TOKEN. Update your CircleCI workflow to download and run the test uploader binary after you've run your tests.&#x20;

***

If you're interested in better understanding this binary or want to contribute to it, you can find the open source repo [here](https://github.com/trunk-io/analytics-cli).

\
