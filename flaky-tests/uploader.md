# Uploader CLI Reference

Trunk Flaky Tests detects and tracks flaky tests in your repos by receiving uploads from your test runs in CI. Trunk Flaky Tests takes the [JUnit XML format](https://github.com/testmoapp/junitxml) for uploads. These uploads happen in the CI jobs used to run tests in your nightly CI, post-commit jobs, and your PR checks.

If you're setting up Trunk Flaky Tests for the first time, you can follow the guides for your CI provider and test framework.

<table data-card-size="large" data-view="cards"><thead><tr><th></th><th data-hidden></th><th data-hidden></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td>Guides by Test Frameworks</td><td></td><td></td><td><a href="get-started/frameworks/">frameworks</a></td></tr><tr><td>Guides by CI Provider</td><td></td><td></td><td><a href="get-started/ci-providers/">ci-providers</a></td></tr></tbody></table>

### Installing the CLI

The CLI should be downloaded as part of your test workflow in your CI system. This can be done with the following command:

```bash
curl -fsSLO --retry 3 https://trunk.io/releases/trunk && chmod +x trunk
```

and then invoked like this. The `trunk` binary will already be marked executable.

```bash
./trunk flakytests upload --junit-paths "test_output.xml" \
   --org-url-slug <TRUNK_ORG_SLUG> \
   --token $TRUNK_API_TOKEN
```

### Uploading from the CLI

{% hint style="info" %}
The uploaded tests are processed by Trunk periodically, not in real-time. Wait for at least an hour after the initial upload before they’re displayed in Trunk. Multiple uploads are required before a test can be accurately detected as broken or flaky.
{% endhint %}

The `trunk` command-line tool can upload and analyze test results. All of the following subcommands and arguments are to the `trunk flakytests` command.

Run the command line with one of the following commands

| Command  | Description                                          |
| -------- | ---------------------------------------------------- |
| `test`   | Test the upload process, but do not upload any data. |
| `upload` | Upload data to Trunk Flaky Tests                     |
| `help`   | Print the help message                               |

The `upload` command uses the following arguments

| Argument                                            | Description                                                                                 |
| --------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `--junit-paths <JUNIT_PATHS>`                       | a comma separated list of paths containing the test output files. File globs are supported. |
| `--org-url-slug <ORG_URL_SLUG>`                     | Trunk Org slug, from the settings page.                                                     |
| `--token <TOKEN>`                                   | Trunk Org (not repo) token, from the settings page.                                         |
| `-h, --help`                                        | Additional detailed description of the `upload` command.                                    |
| `--repo-root`                                       | Path to the repository root. Defaults to the current directory.                             |
| `--repo-url <REPO_URL>`                             | Value to override URL of repository. **Optional**.                                          |
| `--repo-head-sha` `<REPO_HEAD_SHA>`                 | Value to override SHA of repository head. **Optional**.                                     |
| `--repo-head-branch <REPO_HEAD_BRANCH>`             | Value to override branch of repository head. **Optional**.                                  |
| `--repo-head-commit-epoch <REPO_HEAD_COMMIT_EPOCH>` | Value to override commit epoch of repository head. **Optional**.                            |
| `--tags <TAGS>`                                     | Comma separated list of custom tag=value pairs. **Optional**.                               |
| `--print-files`                                     | Print files which will be uploaded to stdout.                                               |
| `--dry-run`                                         | Run metrics CLI without uploading to API. **Optional**.                                     |
| `--team` `<TEAM>`                                   | Value to tag team owner of upload. **Optional**.                                            |
| `--codeowners-path <CODEOWNERS_PATH>`               | Value to override CODEOWNERS file or directory path. **Optional**.                          |
| `--use-quarantining`                                | Run commands with the quarantining step.                                                    |

## Troubleshooting

As a general rule you should download the release on every CI run. **Do not bake the CLI into a container or VM.** This ensures your CI runs are always using the latest build.

The `trunk` binary should be run from the repository root. If you need to run the binary from another location, you must provide the path to the repo root using the `--repo-root`argument. The `--junit-paths` argument accepts the XML file locations as both a list of globs or absolute paths.

### Organization not found

If you receive an error that the org slug or API token is not found, double check that the secrets stored in your CI provider are the same as the Organization settings by navigating to **Settings** -> **Manage** -> **Organization** on [app.trunk.io](https://app.trunk.io/login/?intent=flaky+tests).

Make sure you are getting your _Organization Slug_, not the Organization Name.

<figure><picture><source srcset="../.gitbook/assets/org-slug-dark.png" media="(prefers-color-scheme: dark)"><img src="../.gitbook/assets/org-slug-light.png" alt=""></picture><figcaption><p>Get the Organization Slug</p></figcaption></figure>

Ensure you get your _Organization API Token_, _**not your repo token**_.

<figure><picture><source srcset="../.gitbook/assets/org-token-dark.png" media="(prefers-color-scheme: dark)"><img src="../.gitbook/assets/org-token-light.png" alt=""></picture><figcaption></figcaption></figure>



### Test results aren't uploading

If the test results aren't uploading from your CI system then one possible cause is malformed XML. Try modifying your job to run `./trunk flakytests validate`. Also try using `--dry-run` and `--print-files` to show which files will be uploaded.
