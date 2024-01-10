---
description: How to generate JUnit Reports for common test runners
---

# Generating JUnit Reports

## Jest

1. Install [`jest-junit`](https://github.com/jest-community/jest-junit)

```bash
$ npm install jest-junit --save-dev
```

2. Update your Jest config to use the `jest-junit` reporter

```json
{
  "reporters": [ "default", "jest-junit" ]
}
```

With this configuration, Jest runs will by default output a `junit.xml` file in the working directory. To further configure the reporter, consult the detailed [documentation on GitHub](https://github.com/jest-community/jest-junit?tab=readme-ov-file#jest-junit).
