# Why Code Quality?

### Why you need to lint everything

Most projects will run linters and formatters for their primary language but neglect to run any static analysis on the build scripts, IaC (infrastructure-as-code), config, and docs files. These are the "hard to clean corners" of your code base, where coding standards fall apart and vulnerabilities accumulate unnoticed.

These bits of unlinted code accumulate unused dependencies, deprecated method calls, poorly formatted code, and known antipatterns, which will spread as your project ages from copy-pasting. They become bits of code that no one wants to touch or own.

Worse is the accumulation of [unnoticed security vulnerabilities](https://trunk.io/blog/shifting-security-left-with-trunk-check). A 2017 study by Northeastern University aptly named [_Thou Shalt Not Depend on Me: Analysing the Use of Outdated JavaScript Libraries on the Web_](https://arxiv.org/pdf/1811.00918.pdf) revealed that **37% of 133,000 websites used a JavaScript library with known vulnerabilities.** [More recently](https://www.synopsys.com/content/dam/synopsys/sig-assets/reports/rep-ossra-2023.pdf)[, in a study by Synopsys](https://www.synopsys.com/content/dam/synopsys/sig-assets/reports/rep-ossra-2023.pdf), **84% of 1,703 reviewed codebases had at least one such vulnerability.**

Now factor in your IaC files, CI config, and build scripts; these are the places that you should lint regularly because of the likelihood of newly discovered vulnerabilities in your dependency chain. This is why you **need a metalinter** that can lint all of your files.

### Why it's hard to lint everything

Having good linter coverage in any modern project is difficult because there isn't just one language and technology. There are tons of scripts, images, config files, docs, and IaC files to lint.&#x20;

The tools required to lint everything installs, runs, outputs, upgrades, and configures differently. Now consider the tools that require dependencies and runtimes, such as [nancy](https://docs.trunk.io/code-quality/configuration/supported/nancy) and [actionlint](https://docs.trunk.io/code-quality/configuration/supported/actionlint) that depends on Go, or [bandit](https://trunk.io/linters/python/bandit) and [sqlfmt](https://docs.trunk.io/code-quality/configuration/supported/sqlfmt) that depend on Python. You have to maintain **version pinned tools** and their **runtimes**.

These tools are also prone to tool-rot, where dependencies become old, deprecated, or known vulnerabilities are discovered. In fact, [82% of open-source projects suffer from tool-rot](https://trunk.io/blog/82-of-open-source-projects-suffer-from-tool-rot). Keeping these tools up to date is a Sisyphean task. It's better to have a metalinter handle all of it.

### Why it's hard to lint giant code bases

Giant code bases are hard to lint without good tooling. Imagine introducing a new Python linter to lint over 1 million lines of code. No one will wait tens of minutes or hours for linters to run. Now, considering a polyglot mono repo with millions of lines of code and many languages, the problem only grows.

Trunk Code Quality solves this by being [Git aware](how-does-it-work.md#hold-the-line) and linting only the lines and files that have changed in your repo on commit or PR.

### **Why not just write a script?**&#x20;

[ESLint](https://github.com/eslint/eslint) adopted Trunk Code Quality to replace their [linter script](https://github.com/eslint/eslint/pull/18643/files#diff-3fc6364bd19a0e4ee8d1e0fe312541201418d80f9d1b08015db4d11e7dbde39e) because it's difficult to maintain. Writing a script that can do everything a metalinter does is not trivial. You need to handle per-line and file properly ignores, adapt to the many config and output formats of different tools, support different OS and architectures, lint in a way that's [git-aware](how-does-it-work.md#hold-the-line) so it can run on large code bases quickly, and adapt to breaking changes or newly added linters.

That code is outside of a project's core goals and is bound to become debt. Code Quality is free to run locally and in CI, and reporting to the [Web App](broken-reference) is free for open-source teams.&#x20;

### Who uses Trunk Code Quality?

Popular open-source repos like [ESLint](https://github.com/eslint/eslint) and[ Realm.js](https://github.com/realm/realm-js) use Trunk Code Quality to lint their source code. They use Trunk Code Quality as their metalinter because it's difficult to maintain and run the many linters they run, especially when open-source maintainers need to run and install them individually.

Trunk Code Quality lets them easily manage consistent config and tooling for their repo and achieve full linter coverage.
