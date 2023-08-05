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

Trunk Check manages, downloads, and runs dozens of linters, formatters, static analyzers, and security tools. It's also a platform to write your own custom checks and integrate them to run as hpart of your repo's check suite.

Use it via:

* [Trunk CLI](../cli/)
* [VSCode Extension](https://marketplace.visualstudio.com/items?itemName=trunk.io)
* [GitHub Action](https://github.com/marketplace/actions/trunk-check)
* [Web App (app.trunk.io)](https://app.trunk.io)

We currently support over 75 unique linters and we are adding new and updating old linters every sprint.

### Hold-the-line

Trunk Check distinguishes new from existing issues, which allows you to introduce new linters and checks without any hassle.

This is traditionally a very painful process, because running a new linter or check in your CI means that you have to either fix all existing issues, which requires a huge upfront time investment, or only run the check on modified files, which adds unpredictable overhead to PRs and discourages engineers from making simple changes like typo fixes.

By integrating with Git, Trunk Check can hold-the-line: that is, it allows you to leave existing issues alone, and simply enforces that you never introduce _new_ lint issues in a pull request.

Formatting linters behave slightly differently under hold-the-line than other tools. Since formatters apply to entire files they will be run across the entirety of any changed file and their recommendations must be applied before landing.

#### A short story

*   `src/adder.js`, which has 12 pre-existing issues, has a typo in a comment:

    ```javascript
    // Thsi method adds too numbers together
    ```
*   Engineer sees this typo and corrects it:

    ```javascript
    // This method adds two numbers together
    ```
* Engineer pushes this super-simple, no-code-change Pull Request (PR)
* PR is checked for formatting/lint issues on CI

**Without `trunk`**

* Engineer receives fail-mail and fail-slacks about their PR
* Engineer wonders what in the world could've failed in a PR that fixes a typo in a comment
* Engineer opens the failure notifications and starts going down the rabbit hole
* 2 hours later, engineer finally understands how much work it would be to fix all the pre-existing issues
* Engineer abandons PR
* Not only has a good chunk of the day been blown, but now the engineer is significantly less inclined to ever do this in the future

**With `trunk`**

* `trunk check` CI succeeds on their PR
* Engineer merges their PR

### Issue severity

Trunk Check currently supports over 75 linters, each of which has it own issue severity classification system. We surface these as either Low, Medium, or High priority. This is not always a 1-to-1 translation of the linter's natively defined severity - many have more than 3 severity levels - but we've found that this provides the best signal for the end user.

By default, all issues reported by a linter are considered when evaluating if a pull request is `passing`. We have taken this approach because `trunk` is presenting a holistic view of a codebase, across all its languages and technologies, and we don't believe `trunk` should be in the business of making severity recommendations for individual linters.

If a linter believes an issue is worth reporting, we consider it worth blocking for. If that issue is not interesting for your repo - we suggest you completely disable that rule for that linter in its configuration.
