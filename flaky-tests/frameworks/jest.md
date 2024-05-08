---
description: ${meta_desc}
title: Configuring jest
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

Jest is a testing framework for JavaScript and TypeScript.

# Enabling XML Output
Configure Jest to produce [JUnit XML](https://github.com/testmoapp/junitxml) output. 

* Install the [jest-junit.](https://github.com/jest-community/jest-junit)

```bash
npm install --save-dev jest-junit
```
Update your Jest config (`jest.config.json` or [similar file)](https://jestjs.io/docs/configuration) to add `jest-junit` as a reporter.

`jest.config.json`

```json
{
  "reporters": [ "default", "jest-junit" ]
}
```
With this configuration, Jest runs with by default output a `junit.xml` file in the working directory. To further configure the reporter, consult the [detailed documentation on GitHub](https://github.com/jest-community/jest-junit?tab=readme-ov-file#jest-junit).



# Test Suite Naming

The `jest-junit` reporter will automatically fill in values for the _<testcase>_ and _<testsuite>_ `name` and `class` attributes using the _description_ parameters to the tests. The `testsuites.name` is set to `jest tests` by default. 

For example, this test:

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



# Further Configuration

Jest is highly customizable. See more at the [Jestjs.io](https://jestjs.io/) homepage.




