---
description: How to upload test results for Android tests
---

# Android

## Enabling XML Output

Android tests run with Gradle generate XML output by default.

<table><thead><tr><th width="208">Unit Test Type</th><th>Output Path</th></tr></thead><tbody><tr><td>Local unit test</td><td><mark style="color:purple;">path_to_your_project</mark>/<mark style="color:purple;">module_name</mark>/build/test-results/</td></tr><tr><td>Instrumented unit test</td><td><mark style="color:purple;">path_to_your_project</mark>/<mark style="color:purple;">module_name</mark>/build/test-results/connected/</td></tr></tbody></table>

See the [Android Developer Docs](https://developer.android.com/studio/test/command-line) for more info.

## Example Analytics CLI Usage

If you had test results from a debug build of instrumented unit tests, your upload command would look something like this:&#x20;

```
$ ./trunk-analytics-cli upload \ 
     --junit-paths "./app/build/outputs/androidTest-results/connected/debug/*.xml" \
     --org-url-slug "$ORG_SLUG" \
     --token "$TOKEN"
```
