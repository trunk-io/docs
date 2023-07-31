# Jenkins Quickstart

### Precondition

Your CI machine needs to have the following tools installed:

* Bash
* Curl

You will need to have ports open for:

* api.trunk.io:443
* api.trunk.io:8443

### Create a trunk organization

To use the CI Debugger, you first need to create a trunk organization. See this document for detailed instructions.

### Get your organization's API Token

In the web app, click on your user avatar, then select settings

![](https://files.readme.io/8c5f295-image.png)

In the settings menu, if you are an admin of your organization, you should be able to view your Token. If upon clicking "view" the token is still empty, click reset to populate one.

Copy or take note of the API token. It will be used in our example workflow in the entry marked by a \[1]



[https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F61Ep9MrYBkJa0Yq3zS1s%2Fuploads%2F392GQh7h7F4ezhvoS2gZ%2Fimage.png?alt=media\&token=817d5c69-441d-4a29-9618-aa18c0e9b461](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F61Ep9MrYBkJa0Yq3zS1s%2Fuploads%2F392GQh7h7F4ezhvoS2gZ%2Fimage.png?alt=media\&token=817d5c69-441d-4a29-9618-aa18c0e9b461)

Copy or take note of you organization slug. It will be used in our example workflow in entry marked by a \[2]

\[block:image] { "images": \[ { "image": \[ "https://files.readme.io/961aa72-Org-Slug.png", null, "" ], "align": "center" } ] } \[/block]

### Create A Breakpoint

In the CI DEBUGGER tab, click Add Breakpoint

\[block:image] { "images": \[ { "image": \[ "https://files.readme.io/c623258-image.png", null, "" ], "align": "center" } ] } \[/block]

Give it a name, it will be referred in our example as \[3]

Set some breakpoint condition. Here in this example, we set it to run on a non-zero exit code.

![](https://files.readme.io/980a194-image.png)

### Setup Your Workflow

Here is an example workflow for the breakpoint. Replace the three values in the example to the ones specific to your setup.

Here the TRUNK\_TOKEN is pasted directly. In a real environment it should be managed as a secret.

```
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
