# Merge

Custom `required_statuses` defined in the `.trunk/trunk.yaml` file take precedence over the GitHub required status checks from branch protection.

Use custom `required_statuses` when your checks don't match what you configure on GitHub one-to-one.

```
version: 0.1 
```

```
cli:
  version: 1.16.0
merge: 
  required_statuses:
    - Trunk Check 
    - Unit tests & test coverage
    # Add more required statuses here
```
