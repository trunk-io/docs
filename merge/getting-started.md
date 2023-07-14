# Getting Started

This setup guide will walk you through the initial setup for Trunk Merge.

1. Create a Trunk Account [here](https://app.trunk.io/signup).
2. Follow the onboarding flow to create an Organization and install the [Trunk Github app](https://github.com/apps/trunk-io).
3. Select the repository you would like to use and click Get Started. \[block:image] { "images": \[ { "image": \[ "https://files.readme.io/f48ece6-Screen\_Shot\_2022-09-11\_at\_9.17.11\_PM.png", "Screen Shot 2022-09-11 at 9.17.11 PM.png", 611, 461, "#000000" ] } ] } \[/block]
4. Navigate to Merge using the navigation pane on the left side of the screen.
5. Enter the name of the target branch and the number of pull requests that can be tested in parallel.

\[block:image] { "images": \[ { "image": \[ "https://files.readme.io/5ca83fe-Screen\_Shot\_2022-09-11\_at\_9.33.24\_PM.png", "Screen Shot 2022-09-11 at 9.33.24 PM.png", 407, 597, "#000000" ] } ] } \[/block] 6. Merge uses [GitHub status checks](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/collaborating-on-repositories-with-code-quality-features/about-status-checks) to determine whether a pull request can be merged. Configure these checks by adding them to the `trunk.yaml` configuration file in your repository:

\[block:code] { "codes": \[ { "code": "version: 0.1\ncli:\n version: 1.1.0\nmerge:\n required\_statuses:\n - Trunk Check\n - Unit tests & test coverage\n - Integration tests", "language": "yaml", "name": "trunk.yaml" } ] } \[/block] 7. Set up the required checks by configuring your CI provider to run the required jobs whenever a branch is pushed to your GitHub repository with the special prefix `trunk-merge/`.

8. Submit a pull request, either using the Trunk CLI or in the GitHub Pull Request UI

With the Trunk CLI: after authenticating the CLI by running `$ trunk login`, run the command `trunk merge {pr-number}` \[block:image] { "images": \[ { "image": \[ "https://files.readme.io/3bb6347-Screen\_Shot\_2022-09-11\_at\_10.43.28\_PM.png", "Screen Shot 2022-09-11 at 10.43.28 PM.png", 544, 80, "#000000" ] } ] } \[/block] GitHub Pull Request UI: Comment `/trunk merge` on a pull request \[block:image] { "images": \[ { "image": \[ "https://files.readme.io/11f4ff9-Screen\_Shot\_2022-09-11\_at\_10.43.57\_PM.png", "Screen Shot 2022-09-11 at 10.43.57 PM.png", 671, 160, "#000000" ] } ] } \[/block]
