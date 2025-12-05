---
description: Trunk Code Quality for OpenAI Codex
---

# OpenAI Codex Support

This document provides guidance for integrating Trunk Code Quality into OpenAI Codex environments.

### Requirements

Ensure you’re running the following minimum versions in your `.trunk/trunk.yaml` file:

* Trunk CLI: v1.24.0 or later
* Trunk Plugins: v1.7.0 or later

### Installation

In your Codex environment setup script, include:

```
# Install Trunk CLI and dependent tools
curl https://get.trunk.io -fsSL | bash
trunk install
```

It's important to pre-install all trunk dependencies during the setup because codex environments are network-isolated post-setup.

#### Debugging installation

If the environment setup is slow, run the following to diagnose:

```
trunk install --debug
```

This command will detail installation timings and potential bottlenecks.

### Handling network isolation

Codex environments are network-isolated post-setup. Linters requiring network access must be excluded from running explicitly:

Example:

```
trunk check --filter=-trufflehog,-semgrep
```

### Teaching Codex how to use Trunk

Codex can automatically run trunk commands for you, by informing it to do so in your AGENTS.md file:

```
## AGENTS Instructions

### Formatting and Linting
- Run `trunk check -y --filter=-trufflehog,-semgrep` after modifying code to format and fix linting issues.
- Review and verify changes before committing.
- If only formatting is required, run `trunk fmt`.
- Exclude linters requiring network access by adding them to the negative filter list as shown above.
```
