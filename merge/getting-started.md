# Getting Started

Now that you have `trunk check` running on your local computer, your next step is to run trunk automatically in the cloud and share notifications with your whole team. Start by connecting your trunk organization to GitHub.

## Connect your Trunk organization to GitHub

Sign up at [app.trunk.io](https://app.trunk.io), create a Trunk organization, and connect it to your GitHub repositories.

{% embed url="https://app.supademo.com/edit/clooqw5kf2dfapeudipknagml" %}
Connect your Trunk organization to GitHub
{% endembed %}

## Set Up Trunk Merge

1.  Specify the branch that pull requests will be merged into (usually `main` or `master`) and the number of pull requests Trunk Merge is allowed to concurrently run tests for.\


    <figure><img src="../.gitbook/assets/image (21).png" alt=""><figcaption><p>Set the target branch and maximum concurrency for Trunk Merge</p></figcaption></figure>
2.  Tell Trunk Merge how to determine whether a pull request can be merged, by specifying the [GitHub status checks](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/collaborating-on-repositories-with-code-quality-features/about-status-checks) it should check, in`.trunk/trunk.yaml` in your repository:

    ```yaml
    version: 0.1
    cli:
      version: 1.16.0
    merge:
      required_statuses:
        - Trunk Check
        - Unit tests & test coverage
        # Add more required statuses here
    ```
3.  Set up the required checks, by configuring your CI provider to run the required jobs whenever a branch is pushed to your GitHub repository with the special prefix `trunk-merge/`.\
    \
    For GitHub Actions, that'll mean setting up a `push`-triggered workflow, filtered to `trunk-merge/**` branches, like so:\


    ```yaml
    name: Run Required Checks
    run-name: PR Checks for ${{ github.ref_name }}

    on:
      push:
        branches:
          - trunk-merge/**

    jobs:
      trunk_check:
        runs-on: ubuntu-latest
        name: Trunk Check
        steps:
          - name: Checkout
            uses: actions/checkout@v3

        # Add more steps here...

      unit_tests:
        runs-on: ubuntu-latest
        name: Unit tests & test coverage
        steps:
          - name: Checkout
            uses: actions/checkout@v3

        # Add more steps here..    
    ```

## Use Trunk Merge

Now that you're done with setup, take it for a spin! You can submit a pull request to Trunk Merge by either commenting `/trunk merge` on the PR in GitHub or using the CLI.

{% tabs %}
{% tab title="GitHub Pull Request View" %}
Comment `/trunk merge` on a pull request

<figure><img src="../.gitbook/assets/image (7) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Trunk CLI" %}
```bash
# Authenticate with trunk service
$ trunk login
# Queue pull request for merge
$ trunk merge {pr-number}
```
{% endtab %}
{% endtabs %}

## Debugging Trunk Merge

If Trunk Merge is having issues creating branches, running tests, or merging pull requests:

* Make sure you've followed every step in "Set Up Trunk Merge".
* Ensure that there are no branch protection rules affecting `trunk-temp/*` and `trunk-merge/*` branches. If branch protection is configured in GitHub for any branch matching those formats (e.g. if there is a `*/*` branch protection rule), then that will prevent Trunk Merge from running tests for pull requests.

If there are any questions or help is needed, reach out on our [community slack](https://slack.trunk.io/)!
