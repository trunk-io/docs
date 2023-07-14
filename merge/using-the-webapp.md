# Using the Webapp

The Trunk web app has a UI for inspecting the status of pull requests or your queue health.

## Queue Overview

The queue overview shows you which pull requests are currently in flight. \[block:image] { "images": \[ { "image": \[ "https://files.readme.io/6ab3d25-Screen\_Shot\_2022-09-12\_at\_8.28.08\_AM.png", "Screen Shot 2022-09-12 at 8.28.08 AM.png", 776, 889, "#000000" ] } ] } \[/block] In this view, you can see all the pull requests currently being tested, along with their progress. Merge waits for all [required status checks](https://docs.trunk.io/docs/reference#required-status-checks) to pass before merging a pull request. You can also see any pull requests that have not begun to merge, along with which statuses they are waiting on.

## Failures View

\[block:image] { "images": \[ { "image": \[ "https://files.readme.io/cfdb3af-Screen\_Shot\_2022-09-12\_at\_8.43.28\_AM.png", "Screen Shot 2022-09-12 at 8.43.28 AM.png", 1150, 681, "#000000" ] } ] } \[/block] Pull requests that fail to merge, or are canceled, do not show in the Queue Overview. Instead, they are viewable by clicking the Failures tab.

## Pull Request Details

Clicking on a pull request in the queue overview will open a sidebar pane with relevant details for the status of that pull request.

\[block:image] { "images": \[ { "image": \[ "https://files.readme.io/1a14dd0-Screen\_Shot\_2022-09-12\_at\_8.29.27\_AM.png", "Screen Shot 2022-09-12 at 8.29.27 AM.png", 418, 601, "#000000" ] } ] } \[/block] Clicking "View History" will give you a full audit trail for a pull request. \[block:image] { "images": \[ { "image": \[ "https://files.readme.io/2a8b592-Screen\_Shot\_2022-09-12\_at\_8.36.39\_AM.png", "Screen Shot 2022-09-12 at 8.36.39 AM.png", 852, 582, "#000000" ] } ] } \[/block] This view displays a timeline for a pull request, including when it was submitted, when it began testing, and details about any time it had to restart tests. For pull requests that failed and had to be resubmitted, you'll also be able to view the timeline of each submission.
