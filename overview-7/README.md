# Overview

Trunk CI Debugger (beta invite required) is available at [app.trunk.io](https://app.trunk.io). With a sprinkling of code you can enable live debugging of your CI actions enabling real-time diagnosis, troubleshooting, and of course debugging of your otherwise ephemeral CI job.

### What is it?

Similar to any traditional debugger, the Trunk CI Debugger, operates on breakpoints configured through the trunk web app. Each breakpoint is tracked with a unique id and is configured through a set of conditional rules. For example, you can specify that breakpoint 'foo' always triggers when the exit code of its command is non-zero (or failing).

{% embed url="https://youtube.com/watch?t=17s&v=S_l-h-qg3YA" %}

### How does it work?

At its most basic - the trunk ci debugger wraps the execution of whatever command you give it. This allows the debugger to break `on_enter` before running your command and `on_exit` after your command completes. This wrapper connects to the Trunk Service to determine in real time based on the conditional rules whether to trigger a breakpoint or continue execution.

#### What happens a breakpoint is triggered?

Upon triggering, the execution of your CI run will be paused and the system will attempt to notify someone that a breakpoint has been triggered. In practice, when working with a pull request for example, this can be a Slack notification to the author of the PR, or a posting of a comment to the PR thread on GitHub.

The notification will include a link to connect to the debugging session and provides authenticated users with direct access to the machine that is being held.

#### What can I do during a debug session?

Anything! When connected over a debug session, you have live access to the terminal running your CI job; you are connecting to the live instance being used to run your job.

Besides running any normal shell command from the session, the debugger provides a set of command line tooling to assist your debugging session further.

| command         | what does it do                                                                                                                                             |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| retry           | runs the provided command again. upon retry the exit code of the breakpoint will be overwritten.                                                            |
| getexit         | returns the current exit code that will be returned when the debugging session terminates (by default this is the exit code of the user provided command)   |
| setexit {value} | overwrites the current exit code of the session with a user provided value. use this to change a failing execution into a passing execution (or vice versa) |
| download {file} | downloads the provided file to your local machine                                                                                                           |
| continue        | resumes execution; returns the current exit code, and allows CI process execution to proceed                                                                |
