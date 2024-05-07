---
title: Configuring jest
description: Configuring Jest
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

# Jest

Jest is a popular testing framework for JavaScript and Typescript.

### Enabling XML output

Configure Jest to produce [JUnit XML](https://github.com/testmoapp/junitxml) output.

1. Install [jest-junit](https://github.com/jest-community/jest-junit)

```bash
npm install --save-dev jest-junit
```

Update your Jest config (`jest.config.json` or [similar file)](https://jestjs.io/docs/configuration) to use the `jest-junit` reporter.

`jest.config.json`

```json
{
    "reporters": [ "default", "jest-junit" ]
}
```

With this configuration, Jest runs will by default output a `junit.xml` file in the working directory. To further configure the reporter, consult the detailed [documentation on GitHub](https://github.com/jest-community/jest-junit?tab=readme-ov-file#jest-junit).

## Test Suite naming and output

The `jest-junit` reporter will automatically fill in values for the and `name` and `class` attributes using the _description_ parameters to the tests. The `testsuites.name` attribute is set to `jest tests` by default. For example, this test:

```javascript
describe('addition', () => {
    describe('positive numbers', () => {
        it('should add up', () => {
            expect(1 + 2).toBe(3);
        });
    });
});
```

would produce output that looks like this:

```xml
<testsuites name="jest tests">
    <testsuite name="addition">
        <testcase classname="addition positive numbers should add up"
            name="addition positive numbers should add up">
        </testcase>
    </testsuite>
</testsuites>
```

The default attributes can be changed using `jest-junit` [configuration settings](https://github.com/jest-community/jest-junit?tab=readme-ov-file#configuration).
