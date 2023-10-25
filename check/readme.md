---
layout:
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
---

# Check

Trunk Check runs [80+ tools](https://github.com/trunk-io/plugins) on your repositories, which allow you to automatically

* prevent anti-patterns and bugs in application code,
* prevent misconfiguration of infrastructure code,
* enforce code formatting and style,
* flag secrets in version control, and
* detect and prevent vulnerable dependencies.

<table data-card-size="large" data-view="cards"><thead><tr><th></th><th data-hidden></th><th data-hidden></th><th data-hidden data-card-target data-type="content-ref"></th><th data-hidden data-card-cover data-type="files"></th></tr></thead><tbody><tr><td><h3>Scan your repository</h3></td><td></td><td></td><td><a href="../get-started.md">get-started.md</a></td><td><a href="../.gitbook/assets/github-logo (5).svg">github-logo (5).svg</a></td></tr><tr><td><h3>Or try it out locally</h3></td><td><h2></h2></td><td></td><td><a href="../cli/">cli</a></td><td><a href="../.gitbook/assets/terminal-icon (2).svg">terminal-icon (2).svg</a></td></tr></tbody></table>

## Features

Trunk Check is designed to work the way you expect it to work.

* Continuous integration - we run on every pull request opened in your repository to ensure that no pull request introduces new issues (GitHub users benefit from a native integration)
* Reproducibility - `trunk.yaml` pins the CLI and linter versions to ensure that `trunk check` at a given commit is always reproducible
* Automatic downloads - Check installs every linter you use, as well as their dependencies, so you don't have to install a Node toolchain just to fix a typo on your website
* New issues only - we only warn about issues that your branch would introduce into the default branch, so that existing issues don't prevent you from landing code
* Standard tools - Check runs the same standard tools that everyone uses - e.g. clang-format for C++, eslint for JS/TS - so that you can benefit from the world's shared knowledge
* Recommendations - we identify and suggest tools that you should be using, to maximize the amount of your codebase with linter coverage, as well as best-practice configurations
* Extensibility - we make it easy for you to define your own linters and contribute them back to the community, since all our linter integrations are [open-source](https://github.com/trunk-io/plugins)
* pre-commit & pre-push hooks - we ensure that checks pass when you commit or push
* Issue explorer - you can upload issues to Trunk, so that you can explore and triage the issues that exist in your repository

<div data-full-width="true">

<figure><img src="../.gitbook/assets/image (16).png" alt=""><figcaption><p>Trunk Check identifies a security issue in one of Trunk's own repositories</p></figcaption></figure>

</div>

<figure><img src="../.gitbook/assets/Screenshot 2023-08-23 173119.png" alt=""><figcaption><p>Trunk Check shows all issues present in <a href="https://github.com/trunk-demo1/sass">trunk-demo1/sass</a> at <code>1523bff</code></p></figcaption></figure>

###

