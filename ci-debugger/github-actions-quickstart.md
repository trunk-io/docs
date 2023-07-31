# GitHub Actions Quickstart

### Create a trunk organization

To use the CI Debugger, you first need to create a trunk organization. See this document for detailed instructions. Note: You do not need to install the Trunk GitHub App to use the CI Debugger.

### Setup your Trunk CI Debugger API Token

In order for the CI Debugger to communicate with the trunk web app it needs to be able to authenticate from the GitHub Action instance to the trunk web application. Follow these instructions to setup a secret inside your repository:

{% embed url="https://scribehow.com/embed/Setup_Trunk_CI_Debugger_API_Token__mY0ukXczRquh0Qe3S7aQ5g?removeLogo=true&skipIntro=true" %}

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

Finally we setup this breakpoint in the trunk web app. And create rules that will trigger a breakpoint when the command fails:

{% embed url="https://scribehow.com/embed/How_to_define_a_breaking_in_Trunks_CI_Debugger__tybjplT2SwKLsUvOUyqtWw?removeLogo=true&skipIntro=true" %}
