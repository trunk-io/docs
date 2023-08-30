---
description: How to integrate Trunk CI Analytics with Jenkins CI/CD
---

# Jenkins

## Compatibility

The minimum supported version for Jenkins is **2.387.3**. If you need support for older versions, please contact our community slack at [slack.trunk.io](https://slack.trunk.io) or support at [support@trunk.io](mailto:support@trunk.io).

The [Trunk Plugin for Jenkins](https://plugins.jenkins.io/trunk-io/) requires the [**GitHub** plugin](https://plugins.jenkins.io/github/). Installing the Trunk Plugin will install the GitHub plugin.

## Install the Jenkins Plugin

{% @supademo/embed demoId="H4ryiMPBDHuW6WNJtyMt4" url="https://app.supademo.com/demo/H4ryiMPBDHuW6WNJtyMt4" %}

## Configure the Jenkins plugin

### Copy your API Token

{% @supademo/embed demoId="BILCaBxa05Hkol0Ck4Z-y" url="https://app.supademo.com/demo/BILCaBxa05Hkol0Ck4Z-y" fullWidth="false" %}

### Configure a Secret for Jenkins

{% @supademo/embed demoId="EFdbnIsoWIs8oGCtVUft7" url="https://app.supademo.com/demo/EFdbnIsoWIs8oGCtVUft7" %}

## Upload Data

{% @supademo/embed demoId="ASgoJj670db1p-MjXwsZ-" url="https://app.supademo.com/demo/ASgoJj670db1p-MjXwsZ-" %}

If for any reason you don't see your pipeline runs in the Trunk app after 3 minutes. Please contact our support at [https://slack.trunk.io](https://slack.trunk.io).&#x20;

## Troubleshooting

The Trunk Plugin for Jenkins will also log errors to the Jenkins System Log. You can find these by navigating to **Manage Jenkins** > **System Log**. If you need additional help debugging, please contact our community slack at [slack.trunk.io](https://slack.trunk.io) or support at [support@trunk.io](mailto:support@trunk.io)

