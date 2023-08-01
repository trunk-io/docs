# Jenkins Quickstart

### Requirements

Your CI machine needs to have the following tools installed:

* Bash,&#x20;
* Curl

You will need to have ports open for:

* api.trunk.io:443
* api.trunk.io:8443

### Create a trunk organization

To use the CI Debugger, you must first create a trunk organization. See this [document](broken-reference) for detailed instructions.&#x20;

### Create a breakpoint in the trunk app

{% embed url="https://app.supademo.com/demo/PEuiLCcC1etLxXgcOf-cu" %}

### Setup your Organization API Token

In order for the CI Debugger to communicate with the trunk web app, it needs to be able to authenticate from the GitHub Action instance to the trunk web application.&#x20;

{% embed url="https://app.supademo.com/demo/LPJsDyJYAsyvUabvkphHK" %}

### Setup Your Jenkins Workflow

Here is an example Jenkins workflow. Replace the three values in the example with the ones specific to your setup.

Here the TRUNK\_TOKEN is pasted directly. In a real environment, it should be managed as a secret.

{% code overflow="wrap" %}
```yaml
pipeline {
    environment {
        TRUNK_TOKEN = '<INSERT YOUR TRUNK TOKEN HERE [1]>'
    }
    stages {
        stage('Install Trunk') {
            steps {
                echo "Installing Trunk"
                curl https://get.trunk.io -fsSL | bash -s -- -y
            }
        }
        stage('Test') {
            steps {
                echo "Testing"
                trunk breakpoint --org=<INSERT YOUR ORG NAME HERE [2]> --id=<Breakpoint Name [3]> -- /bin/false
            }
        }
    }
}
```
{% endcode %}

