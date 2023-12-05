# GitLab Quickstart

### Requirements

Your CI machine needs to have the following tools installed:

* Bash,
* Curl

You will need to have ports open for:

* api.trunk.io:443
* api.trunk.io:8443

### Create a trunk organization

To use the CI Debugger, you must first create a trunk organization. See this [document](broken-reference) for detailed instructions.

### Create a breakpoint in the trunk app

{% @supademo/embed demoId="PEuiLCcC1etLxXgcOf-cu" url="https://app.supademo.com/demo/PEuiLCcC1etLxXgcOf-cu" %}

### Setup your Organization API Token

In order for the CI Debugger to communicate with the trunk web app, it needs to be able to authenticate from the GitHub Action instance to the trunk web application.

{% @supademo/embed demoId="LPJsDyJYAsyvUabvkphHK" url="https://app.supademo.com/demo/LPJsDyJYAsyvUabvkphHK" %}

### Setup Your GitLab Workflow

Here is an example GitLab workflow. Replace the three values in the example with the ones specific to your setup.

Here the TRUNK\_TOKEN is pasted directly. In a real environment, it should be managed as a secret.

{% code overflow="wrap" %}
```yaml
stages:          # List of stages for jobs, and their order of execution
  - test

unit-test-job:   # This job runs in the test stage.
  stage: test    # It only starts when the job in the build stage completes successfully.
  variables:
    TRUNK_TOKEN: <INSERT YOUR TRUNK TOKEN HERE [1]>
  script:
    - echo "Installing Trunk"
    - curl https://get.trunk.io -fsSL | bash -s -- -y
    - echo "Done"
    - echo "Testing"
    - trunk breakpoint --org=<INSERT YOUR ORG NAME HERE [2]> --id=<Breakpoint Name [3]> -- /bin/false
    - echo "Done"
```
{% endcode %}
