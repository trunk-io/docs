---
description: Instructions for enabled dynamic parallel queues powered by your bazel graph
---

# Bazel

Leveraging [parallel mode](../../merge-queue.md#single-mode-vs.-parallel-mode) for Trunk Merge Queue is easy for Bazel-enabled repos because Bazel already knows the structure of your code and can automatically generate a dependency graph. Merge can use this information in parallel mode to create dynamic parallel queues enabling your pull requests to run through your Merge Queue faster.\
\
**How do we create parallel queues?**\
By understanding which Bazel targets a pull request affects, we can build a real-time graph and detect intersection points and where distinct non-overlapping graphs exist. This information is essentially a list of unique target names, which can then be used in real time to understand along which targets pull requests might overlap.

**Calculating impacted targets in GitHub Actions**\
Trunk ships a [GitHub action](https://github.com/trunk-io/bazel-action) that will generate the list of impacted targets for a pull request and post that information to the Trunk Merge Queue service.

```yaml
name: Upload and Test Impacted Targets
on: pull_request

jobs:
  impacted_targets:
    name: Impacted Targets
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v3

      - name: Upload and Test Impacted Targets
        uses: trunk-io/bazel-action@v1
        with:
          upload-targets: "true"
          ### store your trunk api token to authenticate with merge service
          trunk-token: ${{ secrets.TRUNK_API_TOKEN }}
          ### (optional if your bazel setup is not in the root of your repo)
          # workspace-path: {your bazel workspace path}
```

The above sample GitHub action code will calculate the impacted targets of your pull request and post that information to the trunk merge service. That data will be used to run your trunk merge queue in parallel mode.
