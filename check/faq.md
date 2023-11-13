---
description: Frequently Asked Questions
---

# FAQ

## What linters should I be using?

The best set of linters depends on your particular needs and which tech stack you are using (C/C++, Javascript, Rust, Python, etc). By default Trunk Check will detect your project type and select a recommended set of linters for that type, ESLint for a Javascript project or `clang-tidy` for C++ projects. There are plenty more linters you can use, however. You can see all possible (built in) linters with&#x20;

```sh
trunk check list
```

&#x20;and enable a new linter with&#x20;

```sh
trunk check enable cool_new_linter
```

See more about our [supported linters here](https://docs.trunk.io/check/supported-linters).&#x20;

## Why aren't issues showing up anymore?&#x20;

If you aren’t seeing any issues the likely cause is that your local repo is clean. By default Trunk Check only processes new changes to your codebase (read about [hold-the-line](https://docs.trunk.io/check/under-the-hood)).  To scan older changes try running:

```sh
trunk check --samples=5 
```

to look at the last five changes or&#x20;

```sh
trunk check --all
```

&#x20;to scan all files, whether changed or not. [More on CLI options](https://docs.trunk.io/check/command-line).

## There are too many issues showing up

One reason for seeing too many issues is that you may have multiple linters configured which are all printing output. Try running just one linter at a time with the `--filter=some_linter` option.

Another reason may be that linters are running on files they should skip, such as generated code from other tools.  [These docs explain how to configure linters to ignore certain files.](https://docs.trunk.io/check/configuration#ignoring-files)&#x20;

Linters are usually configured to be very aggressive and flag many potential bugs and security risks. Sometimes you may want to tell a linter “Trust me, I know what I’m doing”. If that is the case you can configure [a linter to ignore certain issues](https://docs.trunk.io/check/ignoring-issues).

A final possible reason for excess issues is that one of your linters is misconfigured. For example, when using ESlint on a TypeScript project it will flag code that is perfectly fine for TypeScript, but incorrect for JavaScript. In this case make sure that your `.eslintrc` file is correctly set up to handle TypeScript. Also make sure the `extends` section lists the `typescript` defaults after the `eslint:recommended` ones, since ESLint uses _last one wins_ priority.

[More on the CLI options](https://docs.trunk.io/check/command-line).

## My linters are failing or not running as expected

When your linters aren’t working the way you expect, first check their configuration. Trunk’s [list of supported linters](https://docs.trunk.io/check/supported-linters#linter-specific-configuration) provides some specific tips for certain linters. You can see the full default configuration of every linter in [Trunk’s public plugin repo](https://github.com/trunk-io/plugins/tree/main).

You can also try running `trunk check --verbose` to see what’s going on under the hood. If that still doesn’t work then please reach out to us on [our community Slack](https://trunkcommunity.slack.com/ssb/redirect) with the output of `trunk check --verbose`.

\
