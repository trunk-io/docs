# Other CI Providers Quickstart

Trunk natively supports GitHub Actions. If you use a different CI provider, you can still use Trunk Flaky Tests with a few extra steps.

After running tests, you must upload your test results to Trunk. You can do this using the analytics uploader binary.

1. Create a CI job that runs the tests you want to monitor and produces a test report in [**JUnit XML**](https://www.ibm.com/docs/en/developer-for-zos/14.1?topic=formats-junit-xml-format) format. Be careful that your test invocation doesn't use cached test results and doesn't automatically retry failing tests.
2. After the test step, download and run the test uploader binary:

```bash
$ curl -fsSL --retry 3 "https://trunk.io/releases/analytics-cli/latest" -o ./trunk-analytics-uploader
$ chmod +x ./trunk-analytics-uploader
$ ./trunk-analytics-uploader upload \
    --junit-paths "${JUNIT_PATHS}" \
    --org-url-slug "${ORG_URL_SLUG}" \
    --token "${TOKEN}" \
    --tags "${TAGS}"
```

3. To find your organization slug, you can open [app.trunk.io](http://app.trunk.io). Once you are logged in, you should be automatically redirected to a URL like [https://app.trunk.io/**my-org-slug**/repo-owner/repo-name/ci-analytics](https://app.trunk.io/my-org-slug/repo-owner/repo-name/ci-analytics).
4. You can find your Trunk token by navigating to Settings → Manage Organization → Organization API Token and clicking "View."
