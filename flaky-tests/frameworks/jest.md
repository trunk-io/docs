# Jest

### Enabling XML output <a href="#enabling-xml-output" id="enabling-xml-output"></a>

To integrate cleanly with CI systems and other testing tools, Jest can be configured to produce [JUnit XML](https://github.com/testmoapp/junitxml) output. Add the [jest-junit](https://github.com/jest-community/jest-junit) package to your codebase and modify the config file (`jest.config.json` or [similar file)](https://jestjs.io/docs/configuration) to add it as a reporter.

```
npm install --save-dev jest-junit
```

`jest.config.json`

```
{
  "reporters": [ "default", "jest-junit" ]
}
```

Now you can run Jest from the command line with&#x20;

```
jest
```

And from within your CI system with

```
jest --ci --reporters=default --reporters=jest-junit
```

\
