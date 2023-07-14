# Integration for Slack

Trunk Merge integrates with Slack to push relevant information to your team so you can stay up to date with the status of your pull requests.

## Setup Integration with Slack

After you have Merge set up and running in your repository, you can set up your integration with Slack in Settings > Repositories.

![](https://files.readme.io/9fd48c3-Screen\_Shot\_2022-09-13\_at\_2.19.48\_PM.png)

Click "Connect" to install the Trunk Slack application and receive Merge notifications in a specific channel. Once you have authorized the app to post to a channel, you will be redirected to your settings page.

## Configuring Your Integration with Slack

After you have connected to a Slack channel, you can select which notifications you would like to receive. By default, all Merge notifications are enabled.

![](https://files.readme.io/8171abe-Screen\_Shot\_2022-09-13\_at\_2.47.00\_PM.png)

| Notification                                     | Description                                                                                                                                                                                                                                              |
| ------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Merge is paused or resumed                       | Receive a notification when merging has been paused or resumed.                                                                                                                                                                                          |
| Pull request is merged                           | Receive a notification when a pull request is merged into the target branch.                                                                                                                                                                             |
| Pull request is canceled                         | Receive a notification when a pull request is canceled.                                                                                                                                                                                                  |
| Pull request fails                               | Receive a notification when a pull request fails tests or otherwise fails to merge into the target branch.                                                                                                                                               |
| Pull request is merged without using Trunk Merge | Receive a notification when a user merges directly to the target branch without submitting to Trunk Merge. This will cause any in-progress pull requests to be restarted, and typically should only be done in emergencies by designated administrators. |
