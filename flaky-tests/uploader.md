# Trunk Analytics CLI

Trunk detects and tracks flaky tests in your repos by receiving uploads from your test runs in CI, uploaded from the Trunk Analytics CLI. These uploads happen in the CI jobs used to run tests in your nightly CI, post-commit jobs, and PR checks.

### Guides

If you're setting up Trunk Flaky Tests for the first time, you can follow the guides for your CI provider and test framework.

<table data-card-size="large" data-view="cards"><thead><tr><th></th><th data-hidden></th><th data-hidden></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td>Guides by Test Frameworks</td><td></td><td></td><td><a href="get-started/frameworks/">frameworks</a></td></tr><tr><td>Guides by CI Provider</td><td></td><td></td><td><a href="get-started/ci-providers/">ci-providers</a></td></tr></tbody></table>

The CLI should be **downloaded as part of your test workflow** in your CI system. The automatic launcher is platform agnostic and will download the latest version of the uploader for your platform.

### Manual Download

You can find the list of releases on [the GitHub release page](https://github.com/trunk-io/analytics-cli/releases). We provide executables for Linux and OS X. It’s a single file inside a tar and upon downloading the tar you will find a single binary - `trunk-analytics-cli` to use.

{% tabs %}
{% tab title="Linux (x64)" %}
```bash
SKU="trunk-analytics-cli-x86_64-unknown-linux.tar.gz"
curl -fL --retry 3 \
  "https://github.com/trunk-io/analytics-cli/releases/latest/download/${SKU}" \
  | tar -xz

chmod +x trunk-analytics-cli
```
{% endtab %}

{% tab title="Linux (arm64)" %}
```bash
SKU="trunk-analytics-cli-aarch64-unknown-linux.tar.gz"
curl -fL --retry 3 \
  "https://github.com/trunk-io/analytics-cli/releases/latest/download/${SKU}" \
  | tar -xz

chmod +x trunk-analytics-cli
```
{% endtab %}

{% tab title="macOS (arm64)" %}
```bash
SKU="trunk-analytics-cli-aarch64-apple-darwin.tar.gz"
curl -fL --retry 3 \
  "https://github.com/trunk-io/analytics-cli/releases/latest/download/${SKU}" \
  | tar -xz

chmod +x trunk-analytics-cli
```
{% endtab %}

{% tab title="macOS (x64)" %}
```bash
SKU="trunk-analytics-cli-x86_64-apple-darwin.tar.gz"
curl -fL --retry 3 \
  "https://github.com/trunk-io/analytics-cli/releases/latest/download/${SKU}" \
  | tar -xz

chmod +x trunk-analytics-cli
```
{% endtab %}
{% endtabs %}

### Organization Slug and Token

The CLI requires your Trunk organization slug and token passed through `--org-url-slug` and `--token` to upload results to the correct organzation.

You can find your organization slug and token by going to **Settings** > **Manage** > **Organization**.

{% tabs %}
{% tab title="Slug" %}
<figure><picture><source srcset="../.gitbook/assets/org-slug-dark.png" media="(prefers-color-scheme: dark)"><img src="../.gitbook/assets/org-slug-light.png" alt=""></picture><figcaption><p>Make sure you are getting your <em>Organization Slug</em>, not the Organization Name.</p></figcaption></figure>
{% endtab %}

{% tab title="Token" %}
<figure><picture><source srcset="../.gitbook/assets/org-token-dark.png" media="(prefers-color-scheme: dark)"><img src="../.gitbook/assets/org-token-light.png" alt=""></picture><figcaption><p>Ensure you get your <em>Organization API Token</em>, <em><strong>not your repo token</strong></em>.</p></figcaption></figure>
{% endtab %}
{% endtabs %}

### Uploading Test Results

{% hint style="info" %}
The uploaded tests are processed by Trunk periodically, not in real-time. Wait for at least an hour after the initial upload before they’re displayed in the [Uploads tab](get-started/#id-4.-confirm-your-configuration-analyze-your-dashboard). Multiple uploads are required before a test can be accurately detected as broken or flaky.
{% endhint %}

Trunk accepts uploads in three main report formats, [XML](https://github.com/testmoapp/junitxml), [Bazel Event Protocol JSONs](https://bazel.build/remote/bep#consuming-bep-text-json), and XCode XCResult paths. You can upload each of these test report formats using the `./trunk flakytest upload` command like this:

{% tabs %}
{% tab title="XML" %}
Trunk can accept JUnit XMLs through the `--junit-paths` argument:

```
./trunk-analytics-cli upload --junit-paths "test_output.xml" \
   --org-url-slug <TRUNK_ORG_SLUG> \
   --token $TRUNK_API_TOKEN
```
{% endtab %}

{% tab title="Bazel" %}
Trunk can accept Bazel through the `--bazel-bep-path` argument:

```
./trunk flakytests upload --bazel-bep-path <BEP_JSON_PATH> \
   --org-url-slug <TRUNK_ORG_SLUG> \
   --token $TRUNK_API_TOKEN
```
{% endtab %}

{% tab title="XCode" %}
Trunk can accept XCode through the `--xcresult-path` argument:

```
./trunk flakytests upload --xcresult-path <XCRESULT_PATH> \
   --org-url-slug <TRUNK_ORG_SLUG> \
   --token $TRUNK_API_TOKEN
```
{% endtab %}
{% endtabs %}

### Running and Quarantining Tests

You can also execute tests and upload results to Trunk in a single step using the `test` command to **wrap** your test command.

This is especially useful for [Quarantining](quarantining.md), where the Trunk CLI will **override the exit code** of the test command if all failures can be quarantined, **preventing** flaky tests from failing your builds in CI.

{% tabs %}
{% tab title="XML" %}
Trunk can accept JUnit XMLs through the `--junit-paths` argument:

```
./trunk-analytics-cli test --junit-paths "test_output.xml" \
   --org-url-slug <TRUNK_ORG_SLUG> \
   --token $TRUNK_API_TOKEN \
   <YOUR_TEST_COMMAND>
```
{% endtab %}

{% tab title="Bazel" %}
Trunk can accept Bazel through the `--bazel-bep-path` argument:

```
./trunk-analytics-cli test --bazel-bep-path <BEP_JSON_PATH> \
   --org-url-slug <TRUNK_ORG_SLUG> \
   --token $TRUNK_API_TOKEN \
   <YOUR_TEST_COMMAND>
```
{% endtab %}

{% tab title="XCode" %}
Trunk can accept XCode through the `--xcresult-path` argument:

```
./trunk-analytics-cli test --xcresult-path <XCRESULT_PATH> \
   --org-url-slug <TRUNK_ORG_SLUG> \
   --token $TRUNK_API_TOKEN \
   <YOUR_TEST_COMMAND>
```
{% endtab %}
{% endtabs %}

#### Upload failure vs test failure

We use the `SOFTWARE` exit code (70) if the upload fails.

If you use the `test` command and tests fail without the failures being quarantined, we return the provided exit code from the wrapped execution.

If you use the `upload` command, we return exit code `FAILURE` or the exit code provided with the `--test_process_exit_code` argument.

### Validating reports locally

You can validate the test reports produced by your test frameworks before you set up Trunk in your CI jobs. This is currently **only available for XML reports**.

You can run the validate command like this:

```
./trunk-analytics-cli validate --junit-paths "test_output.xml"
```

The `validate` command will output any problems with your reports so you can address them before setting up Trunk in CI.

```sh
Validating the following 1 files:
  File set matching junit.xml:
    junit.xml

junit.xml - 1 test suites, 0 test cases, 0 validation errors

All 1 files are valid! ✅
Navigate to https://app.trunk.io/onboarding?intent=flaky+tests to continue using Trunk Flaky Tests! 🚀🧪
```

### Using custom CI systems

The CLI is preconfigured to work with a set [ci-providers](get-started/ci-providers/ "mention") but can be used with any CI system by passing [#environment-variables](get-started/ci-providers/otherci.md#environment-variables "mention") to the uploader.

> More information on using [otherci.md](get-started/ci-providers/otherci.md "mention") is documented here.

### Full command reference

The `trunk` command-line tool can upload and analyze test results. The `trunk-analytics-cli` command accepts the following subcommands:

| Command                              | Description                                                                                                                                                                                         |
| ------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `trunk-analytics-cli upload`         | Upload data to Trunk Flaky Tests.                                                                                                                                                                   |
| `trunk-analytics-cli validate`       | Validates if the provided JUnit XML files and prints any errors.                                                                                                                                    |
| `trunk-analytics-cli test <COMMAND>` | Runs tests using the provided command, uploads results, checks whether the failures are [quarantined](quarantining.md#using-the-trunk-cli-directly) tests, and correct the exit code based on that. |

The `upload` and `test` commands accept the following options:

<table><thead><tr><th width="265">Argument</th><th>Description</th></tr></thead><tbody><tr><td><code>--junit-paths &#x3C;JUNIT_PATHS></code></td><td>Path to the test output files. File globs are supported. Remember to wrap globs in <code>""</code> quotes</td></tr><tr><td><code>--bazel-bep-path &#x3C;BEP_JSON_PATH></code></td><td>Path to a JSON serialized <a href="https://bazel.build/remote/bep">Bazel Build Event Protocol</a>. Trunk will use the BEP file to locate test reports. Your test frameworks must still output <a href="get-started/frameworks/">compatible report formats</a>.</td></tr><tr><td><code>--xcresult-path &#x3C;XCRESULT_PATH></code></td><td>Path to a <code>.xcresult</code> directory, which contains test reports from <code>xcodebuild</code>.</td></tr><tr><td><code>--org-url-slug &#x3C;ORG_URL_SLUG></code></td><td>Trunk Organization slug, from the Settings page.</td></tr><tr><td><code>--token &#x3C;TOKEN></code></td><td>Trunk Organization (not repo) token, from the Settings page. Defaults to the <code>TRUNK_API_TOKEN</code> variable.</td></tr><tr><td><code>-h, --help</code></td><td>Additional detailed description of the <code>upload</code> command.</td></tr><tr><td><code>--repo-root</code></td><td>Path to the repository root. Defaults to the current directory.</td></tr><tr><td><code>--repo-url &#x3C;REPO_URL></code></td><td>Value to override URL of repository. <strong>Optional</strong>.</td></tr><tr><td><code>--repo-head-sha</code> <code>&#x3C;REPO_HEAD_SHA></code></td><td>Value to override SHA of repository head. <strong>Optional</strong>.</td></tr><tr><td><code>--repo-head-branch &#x3C;REPO_HEAD_BRANCH></code></td><td>Value to override branch of repository head. <strong>Optional</strong>.</td></tr><tr><td><code>--repo-head-commit-epoch &#x3C;REPO_HEAD_COMMIT_EPOCH></code></td><td>Value to override commit epoch of repository head. <strong>Optional</strong>.</td></tr><tr><td><code>--codeowners-path &#x3C;CODEOWNERS_PATH></code></td><td>Value to override CODEOWNERS file or directory path. <strong>Optional</strong>.</td></tr><tr><td><code>--allow-empty-test-results</code></td><td>Don't fail commands if test results are empty or missing. Use it when you sometimes skip all tests for certain CI jobs. Defaults to <code>true</code>.</td></tr><tr><td><code>--variant &#x3C;VARIANT_NAME></code></td><td>Upload tests to a specific variant group. <strong>Optional</strong>.</td></tr><tr><td><code>--test-process-exit-code</code> <code>&#x3C;EXIT_CODE></code></td><td>Specify the exit code of the test previously run. This is used by the upload command to identify errors that happen outside of the context of the test execution (such as build errors).</td></tr></tbody></table>

{% hint style="info" %}
**Memory Overhead**

Running tests via `trunk-analytics-cli test` adds negligible memory overhead.

This subcommand is a thin wrapper around your existing test command and doesn't modify or parallelize test execution.

During execution, it simply:

* Runs your provided test command directly.
* Records start and end times.
* Captures the exit code for quarantine decisions.

\
You can safely run the CLI even with large or memory-intensive suites, without risking additional OOMs in your CI agents.
{% endhint %}
