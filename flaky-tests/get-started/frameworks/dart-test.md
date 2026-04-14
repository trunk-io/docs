---
description: A guide for generating Trunk-compatible test reports for Dart tests
---

# Dart Test

You can automatically [detect and manage flaky tests](../../detection/) in your Dart projects by integrating with Trunk Flaky Tests.

{% include "../../../.gitbook/includes/checklist.md" %}

### Generating Reports

Before you can upload to Trunk, you need to output a Trunk-compatible report. Dart supports JUnit outputs by using the `tojunit` library. You can install the `tojunit` library using the following command:

```sh
dart pub global activate junitreport
```

Then, you can convert test reports to a JUnit format by piping it to `tojunit`and piping the output to a file like this:

<pre class="language-sh"><code class="lang-sh"><strong>dart test &#x3C;TEST_PATH> --reporter json | tojunit > junit.xml
</strong></code></pre>

#### Report File Path

The JUnit report is written to the location specified by the `tojunit >` pipe. In the example above, the test results will be written to `./junit.xml`.

{% include "../../../.gitbook/includes/retries.md" %}

Dart provides retries through the [retry class annotations](https://pub.dev/documentation/test/latest/test/Retry-class.html). Disable retry, use Trunk to [detect](../../detection/)[ flaky tests](../../detection/), and use Quarantining to isolate flaky tests dynamically at run time.

{% include "../../../.gitbook/includes/try-it-locally.md" %}

### Next Steps

Configure your CI to upload test runs to Trunk. Find the guides for your CI provider below:

{% include "../../../.gitbook/includes/ci-providers.md" %}
