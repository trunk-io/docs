---
description: >-
  Triage your flaky tests faster by creating automatically assigned and labeled
  tickets in your ticketing system
---

# Ticketing integrations

You can integrate directly with your ticketing systems to automatically create tickets when Trunk [detects a broken or flaky test](../detection.md).

### Ticket content

Flaky Tests automatically generates tickets complete with a title and description. If you’re connected to Linear or Jira, you can also assign default issue types, teams, or assignees.

The ticket description contains the following information:

* Identifier of the test
* Since when has the test been labeled flaky
* The last time this test failed
* The impact when run on PRs
* The impact when run on branches
* Quarantine status
* Most common failure reasons
* Code owners, according to the [CODEOWNERS](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners) file in your repository

### Integration setup

Currently, Ticket Creation supports integrations with Linear and Jira. However, the automatically generated ticket content is formatted in Markdown and can be copied to other platforms like Asana or GitHub issues.

<table data-card-size="large" data-view="cards"><thead><tr><th align="center"></th><th data-hidden data-card-cover data-type="files"></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td align="center"><a data-footnote-ref href="#user-content-fn-1"><strong>Linear</strong></a></td><td><a href="../../.gitbook/assets/linear-v2.png">linear-v2.png</a></td><td><a href="linear-integration.md">linear-integration.md</a></td></tr><tr><td align="center"><strong>Jira</strong></td><td><a href="../../.gitbook/assets/jira.png">jira.png</a></td><td><a href="jira-integration.md">jira-integration.md</a></td></tr></tbody></table>

[^1]: 
