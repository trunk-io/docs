### Add Uploader to Testing Workflow

You can upload test results to Flaky Tests with
the [`trunk-analytics-uploader`](https://github.com/trunk-io/analytics-uploader) by running it in a stage after
your tests are complete. There are five different OS/arch builds of the uploader in the latest release.
Pick the one you need for your testing platform and be sure to download the release on every CI run.
Do not bake the CLI into a container or VM. This ensures your CI runs are always using the latest build.

Right click and copy the appropriate link from this table.

| CPU Architecture    | link                                                                                                                                                   |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| MacOS Intel         | [x68_64-apple-darwin](https://github.com/trunk-io/analytics-cli/releases/latest/download/trunk-analytics-cli-x86_64-apple-darwin.tar.gz)               |
| MacOS Apple Silicon | [aarch64-apple-darwin](https://github.com/trunk-io/analytics-cli/releases/latest/download/trunk-analytics-cli-aarch64-apple-darwin.tar.gz)             |
| Arm64 Linux         | [aarch64-unknown-linux-musl](https://github.com/trunk-io/analytics-cli/releases/latest/download/trunk-analytics-cli-aarch64-unknown-linux-musl.tar.gz) |
| Intel Linux (musl)  | [x86_64-unknown-linux-gnu](https://github.com/trunk-io/analytics-cli/releases/latest/download/trunk-analytics-cli-x86_64-unknown-linux-gnu.tar.gz)     |
| Intel Linux (gnu)   | [x86_64-unknown-linux-musl](https://github.com/trunk-io/analytics-cli/releases/latest/download/trunk-analytics-cli-x86_64-unknown-linux-musl.tar.gz)   |

