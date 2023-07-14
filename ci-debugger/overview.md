# Overview

Trunk CI Debugger (beta invite required) is available at [app.trunk.io](https://app.trunk.io). With a sprinkling of code you can enable live debugging of your CI actions enabling real-time diagnosis, troubleshooting, and of course debugging of your otherwise ephemeral CI job.

### What is it?

Similar to any traditional debugger, the Trunk CI Debugger, operates on breakpoints configured through the trunk web app. Each breakpoint is tracked with a unique id and is configured through a set of conditional rules. For example, you can specify that breakpoint 'foo' always triggers when the exit code of its command is non-zero (or failing).

\[block:embed] { "html": "\<iframe class="embedly-embed" src="//cdn.embedly.com/widgets/media.html?src=https%3A%2F%2Fwww.youtube.com%2Fembed%2FS\_l-h-qg3YA\&display\_name=YouTube\&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DS\_l-h-qg3YA\&key=7788cb384c9f4d5dbbdbeffd9fe4b92f\&type=text%2Fhtml\&schema=youtube" width="854" height="480" scrolling="no" title="YouTube embed" frameborder="0" allow="autoplay; fullscreen" allowfullscreen="true">", "url": "https://www.youtube.com/watch?v=S\_l-h-qg3YA", "favicon": "https://www.google.com/favicon.ico", "provider": "http://youtube.com", "href": "https://www.youtube.com/watch?v=S\_l-h-qg3YA", "typeOfEmbed": "youtube" } \[/block]

### How does it work?

At its most basic - the trunk ci debugger wraps the execution of whatever command you give it. This allows the debugger to break `on_enter` before running your command and `on_exit` after your command completes. This wrapper connects to the Trunk Service to determine in real time based on the conditional rules whether to trigger a breakpoint or continue execution.

#### What happens a breakpoint is triggered?

Upon triggering, the execution of your CI run will be paused and the system will attempt to notify someone that a breakpoint has been triggered. In practice when working with a pull request for example, this can be a Slack notification to the author of the PR, or a posting of a comment to the PR thread on GitHub.

The notification will include a link to connect to the debugging session and provides authenticated users with direct access to the machine that is being held.

#### What can I do during a debug session?

Anything! When connected over a debug session, you have live access to the terminal that is running your CI job; you are connecting to the live instance that is being used to run your job.

Besides running any normal shell command from the session, the debugger provides a set of command line tooling to further assist your debugging session.

| command         | what does it do                                                                                                                                             |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| retry           | runs the provided command again. upon retry the exit code of the breakpoint will be overwritten.                                                            |
| getexit         | returns the current exit code that will be returned when the debugging session terminates (by default this is the exit code of the user provided command)   |
| setexit {value} | overwrites the current exit code of the session with a user provided value. use this to change a failing execution into a passing execution (or vice versa) |
| download {file} | downloads the provided file to your local machine                                                                                                           |
| continue        | resumes execution; returns the current exit code, and allows CI process execution to proceed                                                                |
