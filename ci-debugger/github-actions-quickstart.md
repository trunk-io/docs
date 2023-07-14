# GitHub Actions Quickstart

### Create a trunk organization

To use the CI Debugger, you first need to create a trunk organization. See this document for detailed instructions. Note: You do not need to install the Trunk GitHub App to use the CI Debugger.

### Setup your Trunk Repo Token in GitHub Actions

In order for the CI Debugger to communicate with the trunk web app it needs to be able to authenticate from the GitHub Action instance to the trunk web application. Follow these instructions to setup a secret inside your repository:

\[block:embed] { "html": false, "url": "https://scribehow.com/embed/Setup\_Trunk\_Repository\_API\_Token\_\_mY0ukXczRquh0Qe3S7aQ5g?skipIntro=true\&removeLogo=true", "provider": "scribehow.com", "href": "https://scribehow.com/embed/Setup\_Trunk\_Repository\_API\_Token\_\_mY0ukXczRquh0Qe3S7aQ5g?skipIntro=true\&removeLogo=true", "typeOfEmbed": "iframe", "height": "600px", "width": "100%", "iframe": true } \[/block]





{% tabs %}
{% tab title="First Tab" %}

{% endtab %}

{% tab title="Second Tab" %}

{% endtab %}
{% endtabs %}

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

\[block:embed] { "html": false, "url": "https://scribehow.com/embed/How\_to\_define\_a\_breaking\_in\_Trunks\_CI\_Debugger\_\_tybjplT2SwKLsUvOUyqtWw?skipIntro=true\&removeLogo=true", "provider": "scribehow.com", "href": "https://scribehow.com/embed/How\_to\_define\_a\_breaking\_in\_Trunks\_CI\_Debugger\_\_tybjplT2SwKLsUvOUyqtWw?skipIntro=true\&removeLogo=true", "typeOfEmbed": "iframe", "height": "600px", "width": "100%", "iframe": true } \[/block]
