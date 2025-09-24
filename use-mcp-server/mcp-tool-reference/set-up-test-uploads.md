---
description: 'MCP tool reference: setup-trunk-uploads'
---

# Set up test uploads

### Overview

The `setup-trunk-uploads` tool helps configure test result uploads to Trunk for flaky test detection and enhanced CI Autopilot analysis. This tool provides step-by-step instructions tailored to your specific test framework and CI provider combination.



The tool guides you through a 4-step process:

* [ ] &#x20;**Configure Test Framework** - Modify your test configuration to output JUnit XML reports
* [ ] **Run Tests** - Execute at least one test to generate reports
* [ ] **Test Upload** - Manually upload a test report to verify connectivity
* [ ] **Configure CI** - Set up automated uploads in your CI pipeline

\
**Return Type:** Structured setup plan to generate test reports and upload to Trunk. Structure: project analysis and setup plan



### Parameters

{% hint style="warning" %}
This agent needs to be called **once per test framework** used in your repository. If your repository uses multiple test frameworks (e.g., Jest for frontend, pytest for backend), call this tool once for each framework with the same `ci_provider`.
{% endhint %}

#### Required Parameters

| Parameter       | Type   | Description                                                                                                          |
| --------------- | ------ | -------------------------------------------------------------------------------------------------------------------- |
| `testFramework` | string | The test framework used in your repository (e.g., `jest`, `pytest`,  `mocha`)                                        |
| `ciProvider`    | string | Your CI provider (e.g., `github`, `circleci`)                                                                        |
| `orgSlug`       | string | Your organization slug. If not provided and you belong to multiple organizations, you'll be prompted to specify one. |



### Supported Values

#### Test Frameworks

* `android` - Android testing framework
* `bazel` - Bazel test runner
* `cypress` - Cypress end-to-end testing
* `gotestsum` - Go testing with gotestsum
* `jasmine` - Jasmine testing framework
* `jest` - Jest testing framework
* `karma` - Karma test runner
* `maven` - Maven Surefire/Failsafe testing
* `minitest` - Ruby minitest framework
* `mocha` - Mocha testing framework
* `phpunit` - PHPUnit testing framework
* `playwright` - Playwright testing framework
* `pytest` - Python pytest framework
* `rspec` - Ruby RSpec testing framework
* `rust` - Rust testing with cargo test
* `swift-testing` - Swift Testing framework
* `vitest` - Vitest testing framework
* `xctest` - Xcode XCTest framework

#### CI Providers

* `buildkite` - Buildkite pipelines
* `circleci` - CircleCI pipelines
* `drone` - Drone CI
* `github` - GitHub Actions
* `gitlab` - GitLab CI/CD
* `semaphore` - Semaphore CI
* `travis` - Travis CI
* `other` - Other CI providers (manual configuration)



### Usage Examples

#### Basic Setup

```
Use the setup-trunk-uploads tool with testFramework="jest" and ciProvider="github"
```

#### With Organization Slug

```
Use the setup-trunk-uploads tool with testFramework="pytest", ciProvider="circleci", and orgSlug="my-company"
```

#### Multiple Test Frameworks

```
Use the setup-trunk-uploads tool with testFramework="jest" and ciProvider="github"
Use the setup-trunk-uploads tool with testFramework="playwright" and ciProvider="github"
```



### Sample Response

The tool returns detailed setup instructions as plain text:

```
Project Analysis
- Test Framework: Vitest (detected from package.json and vitest.config.mts)
- CI Provider: GitHub Actions (detected from repository URL)
- Repository: agraebe/ci-autopilot-sample

Setup Plan
To enable flaky test uploads to Trunk, you'll need to complete these 4 steps:

1. Configure Vitest to output JUnit reports
Update your vitest.config.mts to include the JUnit reporter that will generate XML test reports.

2. Run tests with the new configuration
Execute your tests to generate the JUnit XML report.

3. Send a test upload to Trunk
Run a command to upload your first test results to Trunk using your API token.

4. Configure GitHub Actions
Add a step to your GitHub Actions workflow to automatically upload test results on every CI run.
```



### Error Handling

| Error                                      | Cause                                         | Resolution                                             |
| ------------------------------------------ | --------------------------------------------- | ------------------------------------------------------ |
| `Test framework is required`               | `testFramework` parameter missing             | Provide a supported test framework from the list above |
| `CI provider is required`                  | `ciProvider` parameter missing                | Provide a supported CI provider from the list above    |
| `User is not authenticated`                | Missing or invalid authentication             | Ensure you're properly authenticated with Trunk        |
| `User is not a member of any organization` | No organization access                        | Create or join a Trunk organization                    |
| `No organizations found`                   | No accessible organizations                   | Create an organization in the Trunk app                |
| Multiple organizations note                | User belongs to multiple orgs, none specified | Provide explicit `orgSlug` parameter                   |
