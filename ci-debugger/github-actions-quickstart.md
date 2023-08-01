# GitHub Actions Quickstart

### Requirements

Your CI machine needs to have the following tools installed:

* Bash,&#x20;
* Curl

You will need to have ports open for:

* api.trunk.io:443
* api.trunk.io:8443

### Create a trunk organization

To use the CI Debugger, you must first create a trunk organization. See this [document](broken-reference) for detailed instructions.&#x20;

### Setup your Organization API Token

In order for the CI Debugger to communicate with the trunk web app it needs to be able to authenticate from the GitHub Action instance to the trunk web application.&#x20;

{% embed url="https://app.supademo.com/demo/LPJsDyJYAsyvUabvkphHK" %}

### Add your token to GitHub secrets

Securely store the TRUNK\_TOKEN in your GitHub repo so it can be referenced securely during a GitHub action run.

{% embed url="https://app.supademo.com/demo/2UWXR9ccwhP4ng5-orZPG" %}
Add your token to GitHub secrets
{% endembed %}

### Wrap one of your GitHub steps in a `trunk breakpoint`

Now for the magic 🪄. Open an existing GitHub Action and wrap one of your existing steps with a `trunk breakpoint` like this [(example here)](https://github.com/trunk-io/debugger-demo/blob/main/.github/workflows/pr.yml):

```yaml
name: Pull Request
on:
  - pull_request

jobs:
  test:
    name: Test
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v2

      - name: Testing
        uses: trunk-io/breakpoint@v1
        with:
          breakpoint-id: run-tests
          run: ./run_tests.sh
          trunk-token: ${{ secrets.TRUNK_DEBUGGER_TOKEN }}
          org: {INSERT_YOUR_TRUNK_ORGANIZATION}
```

### Create the corresponding breakpoint in the trunk app

Finally we setup this breakpoint in the trunk web app. And create rules that will trigger a breakpoint when on exit.

{% embed url="https://app.supademo.com/demo/PEuiLCcC1etLxXgcOf-cu" %}
