# GitLab Quickstart

### Precondition

Your CI machine needs to have the following tools installed:

* Bash
* Curl

You will need to have ports open for:

* api.trunk.io:443
* api.trunk.io:8443\


<details>

<summary>Create a trunk organization</summary>



</details>

<details>

<summary>Get your organization's API Token</summary>

### Get your organization's API Token

In the web app, click on your user avatar, then select settings

<img src="https://files.readme.io/8c5f295-image.png" alt="Open settings in the top-right corner" data-size="original">

In the settings menu, (if you are an admin of your organization), you should be able to view your Token. If upon clicking "view" the token is still empty, click reset to populate one.

<img src="../.gitbook/assets/image (10).png" alt="" data-size="original">

Copy or take note of the API token. It will be used in our example workflow in the entry marked by a \[1]

<img src="../.gitbook/assets/image (11).png" alt="" data-size="original">

Copy or take note of your organization slug. It will be used in our example workflow in entry marked by a \[2]

<img src="../.gitbook/assets/image (12).png" alt="" data-size="original">

</details>

<details>

<summary>Create a breakpoint</summary>

In the CI DEBUGGER tab, click Add Breakpoint

<img src="../.gitbook/assets/image (13).png" alt="" data-size="original">

Give it a name, it will be referred in our example as \[3]

Set the breakpoint condition. Here in this example, we set it to run on a non-zero exit code.

<img src="https://files.readme.io/980a194-image.png" alt="" data-size="original">

### Setup Your Workflow

</details>

### Setup Your GitLab Workflow

Here is an example workflow for the breakpoint. Replace the three values in the example with the ones specific to your setup.

Here the TRUNK\_TOKEN is pasted directly. In a real environment, it should be managed as a secret.

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
