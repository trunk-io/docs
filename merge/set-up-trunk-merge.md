---
description: How to set up Trunk Merge for your project
---

# Set Up Trunk Merge

## Connect your Trunk Organization to GitHub

Sign up at [app.trunk.io](https://app.trunk.io/), create a Trunk organization, and connect it to your GitHub repositories. If your repository is already connected to your Trunk organization, this step can be skipped.

Select the repository you would like to use and click **Get Started.**

<figure><img src="../.gitbook/assets/image (4) (1) (1).png" alt=""><figcaption></figcaption></figure>

## Set Up Trunk Merge

Go to the Merge tab. You will see the "Set Up Trunk Merge" page. From there, you can specify:

1. The name of the branch that Trunk Merge should help manage merging PRs into
2. The number of Pull Requests that Merge can test at the same time
3. The [mode](configuration.md#single-parallel-mode) that Trunk Merge Queues will start in

<figure><img src="../.gitbook/assets/image.png" alt="" width="414"><figcaption></figcaption></figure>

### Define Status Conditions

Tell Trunk Merge how to determine whether a pull request can be merged by specifying the name of the [GitHub status checks](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/collaborating-on-repositories-with-code-quality-features/about-status-checks) or [jobs](https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions#jobs) that must pass in the `.trunk/trunk.yaml` in your repository.

```yaml
version: 0.1 
cli:
  version: 1.16.0
merge: 
  required_statuses:
    - Trunk Check 
    - Unit tests and test coverage
    # Add more required statuses here
```

### Configure Merge Requirements

Ensure the checks and jobs in `merge.required_statuses` from `.trunk/trunk.yaml` specified in step 2 run whenever Trunk Merge tests a PR. Trunk Merge creates branches with the prefix `trunk-merge/` in order to test PRs, so this means configuring your CI provider to run then whenever a branch with that prefix is pushed to.

For GitHub Actions, that'll mean setting up a `push`-triggered workflow, filtered to `trunk-merge/**` branches, like so:

```yaml
name: Run Required Checks
run-name: PR Checks for ${{ github.ref_name }}

# Trigger jobs whenever Trunk Merge tests a PR using a `trunk-merge/` branch
on:
  push:
    branches:
      - trunk-merge/**

jobs:
  trunk_check:
    runs-on: ubuntu-latest
    # "Trunk Check" is specified in merge.required_status above
    name: Trunk Check
    steps:
      - name: Checkout
        uses: actions/checkout@v3

  unit_tests:
    runs-on: ubuntu-latest
    # "Unit tests & test coverage" is specified in merge.required_status above
    name: Unit tests & test coverage
    steps:
      - name: Checkout
        uses: actions/checkout@v3

    # Add more steps here..    
```

Now you are ready to submit [your first PR](testing-pull-requests.md). Let's go!
