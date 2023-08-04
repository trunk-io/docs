---
description: >-
  The CI Debugger can be used from non-CI machines. For example your local
  terminal or any machine under your control.
---

# Command Line Example

### Requirements

Your machine needs to have the following tools installed:

* Bash,
* Curl

You will need to have ports open for:

* api.trunk.io:443
* api.trunk.io:8443

### Create a trunk organization

To use the CI Debugger, you must first create a trunk organization. See this [document](../web-app/) for detailed instructions.

### Create a breakpoint in the trunk app

{% embed url="https://app.supademo.com/demo/PEuiLCcC1etLxXgcOf-cu" %}

### Setup your Organization API Token

In order for the CI Debugger to communicate with the trunk web app, it needs to be able to authenticate from the GitHub Action instance to the trunk web application.

{% embed url="https://app.supademo.com/demo/LPJsDyJYAsyvUabvkphHK" %}

### Setup Your Buildkite Workflow

Here is an example command of running the debugger directly from any command line. Replace the three values in the example with the ones specific to your setup.\
\
In this example we are downloading the trunk tool and then running the '/bin/false' command which will immediately fail and trigger a breakpoint.

{% code overflow="wrap" %}
```yaml
curl https://get.trunk.io -fsSL | bash -s -- -y
export TRUNK_TOKEN=<Insert your API key [1]>
trunk breakpoint --org=<INSERT YOUR ORG NAME HERE [2]> --id=<Breakpoint Name [3]> -- /bin/false
```
{% endcode %}
