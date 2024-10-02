---
description: >-
  The Trunk CLI procides command-line acccess to your merge queue.
---

# Merge from the CLI

### Command Line

| trunk merge \<command>           | Description                                                                    |
| -------------------------------- | ------------------------------------------------------------------------------ |
| `status`                           | list status of the merge queue, provides a snapshot of current activity in the merge queue |
| `{PR_NUMBER}`                        | Insert the specified pull request into the merge queue |
| `cancel <pr-number>` | Remove the specified pull request from the merge queue |


### Login 

The Trunk [plugins repo](https://github.com/trunk-io/plugins) ships with a collection of tools that can help supercharge your repository and provide examples for how to write your own. To see a list of tools that you can enable in your own repo run:

```shell
trunk tools list
```

<figure><img src="../../../.gitbook/assets/image (7) (1).png" alt=""><figcaption><p>list of available and enabled tools</p></figcaption></figure>

