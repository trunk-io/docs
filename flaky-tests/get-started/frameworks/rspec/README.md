---
description: >-
  A guide for generating Trunk-compatible test reports for RSpec using Trunk's
  RSpec plugin
---

# RSpec

You can automatically [detect and manage flaky tests](../../../detection.md) in your projects running RSpec by integrating with Trunk. This document explains how to use Trunk's RSpec plugin to upload test results to Trunk.

### Checklist

By the end of this guide, you should achieve the following before proceeding to the [next steps](./#next-step) to configure your CI provider.

* [ ] Set up and installed Trunk's RSpec plugin
* [ ] Disable retries for better detection accuracy
* [ ] Test uploads locally

{% hint style="info" %}
Using the plugin is the best way to accurately detect flaky RSpec tests.&#x20;

You can also [manually generate and upload](manual-uploads.md) test results in RSpec, however, **manual RSpec uploads are not recommended.**&#x20;
{% endhint %}

### Installing the plugin

Trunk detects flaky tests by analyzing test reports automatically uploaded from your CI jobs. You can do this for your Rspec tests using Trunk's RSpec plugin.

To install the plugin in your project, add the `rspec_trunk_flaky_tests` gem to your `Gemfile`:

{% code title="Gemfile" %}
```shell
gem "rspec_trunk_flaky_tests"
```
{% endcode %}

Install the plugin:

```sh
bundle install
```

Then, load the plugin in `spec_helper.rb`:

{% code title="spec/spec_helper.rb" %}
```shell
require "trunk_spec_helper"
```
{% endcode %}

#### Disable Retries

You need to disable automatic retries if you previously enabled them. Retries compromise the accurate detection of flaky tests.&#x20;

If you have a step in CI to rerun failed tests with the `--only-failures` option, or you're using a package like [rspec-retry](https://github.com/NoRedInk/rspec-retry), remember to disable them.

### Try It Locally

#### Test Upload

Before modifying your CI jobs to automatically upload test results to Trunk, try uploading a single test run manually.

You make an upload to Trunk using the following command:

```sh
TRUNK_ORG_URL_SLUG=<TRUNK_ORG_URL_SLUG> \
TRUNK_API_TOKEN=<TRUNK_ORG_TOKEN> \
bundle exec rspec
```

You can find your Trunk organization URL slug and token in the **Settings** or by following these [instructions](https://docs.trunk.io/flaky-tests/get-started/ci-providers/otherci#id-1.-store-a-trunk_token-secret-in-your-ci-system).

After your upload, you can verify that Trunk has received and processed it successfully in the **Uploads** tab. Warnings will be displayed if the test report uploaded by the plugin has issues.

<figure><picture><source srcset="../../../../.gitbook/assets/data-uploads-dark.png" media="(prefers-color-scheme: dark)"><img src="../../../../.gitbook/assets/data-uploads-light.png" alt=""></picture><figcaption></figcaption></figure>

### Next Steps

Configure your CI to upload test runs to Trunk. Find the guides for your CI framework below:

{% include "../../../../.gitbook/includes/ci-providers.md" %}



