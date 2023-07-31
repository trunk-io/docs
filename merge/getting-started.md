# Getting Started

This setup guide will walk you through the initial setup for Trunk Merge.

1. Create a Trunk Account [here](https://app.trunk.io/signup).
2. Follow the onboarding flow to create an Organization and install the [Trunk Github app](https://github.com/apps/trunk-io).
3.  Select the repository you would like to use and click Get Started. \


    <figure><img src="../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>
4. Navigate to Merge using the navigation pane on the left side of the screen.
5.  Enter the name of the target branch and the number of pull requests that can be tested in parallel.\


    <figure><img src="../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>


6.  Merge uses [GitHub status checks](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/collaborating-on-repositories-with-code-quality-features/about-status-checks) to determine whether a pull request can be merged. Configure these checks by adding them to the `trunk.yaml` configuration file in your repository:\


    ```yaml
    version: 0.1
    cli:
      version: 1.13.0
    merge:
      required_statuses:
        - Trunk Check
        - Unit tests & test coverage
        - Integration tests
    ```


7. Set up the required checks by configuring your CI provider to run the required jobs whenever a branch is pushed to your GitHub repository with the special prefix `trunk-merge/`.
8. Submit a pull request, either using the Trunk CLI or in the GitHub Pull Request UI\


{% tabs %}
{% tab title="GitHub Pull Request View" %}
Comment `/trunk merge` on a pull request

<figure><img src="../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>
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
