---
description: A guide for generating Trunk-compatible test reports for NUnit
---

# NUnit

## 1. Install NUnit XML Test Result Adapter

Ensure you have NUnit3TestAdapter, which allows NUnit to output results in JUnit XML format:

```sh
dotnet add package NUnit3TestAdapter
dotnet add package Microsoft.NET.Test.Sdk
dotnet restore
```

## 2. Run Tests with JUnitXML Output

```sh
dotnet test --logger "trx;LogFileName=test-results.trx"
```

This generates a .trx file in the test project’s output folder.

## 3. Convert `.trx` to JUnit.xml format

NUnit does not output JUnit format directly, so you need to convert the `.trx` file to JUnit XML. Use the `trx2junit` tool:

Install `trx2junit` using:

```sh
dotnet tool install -g trx2junit
```

Convert the .trx file to a JUnit.xml using:

```sh
trx2junit test-results.trx
```

## 4. Output Location

The JUnit report will be written to the location of the source `.trx` file. In the example above, it would be at `test-results.xml`.

## Disable Retries

You need to disable automatic retries if you previously included them. Retries compromise the accurate detection of flaky tests.&#x20;

Omit `[Retry(n)]` from tests to disable retries.

## Next Step

JUnit files generated with NUnit are compatible with Trunk Flaky Tests. See [CI Providers](https://docs.trunk.io/flaky-tests/get-started/ci-providers) for a guide on how to upload test results to Trunk.
