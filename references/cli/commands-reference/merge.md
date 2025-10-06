---
hidden: true
---

# Merge

### Trunk Merge

`trunk merge`: Submit a pull request to merge at `https://app.trunk.io/merge`.

#### **Usage** **example**

```
trunk merge [options] [subcommand]
```

#### **Options**

* `--skip-the-line`: Whether this item should be inserted ahead of all pull requests already waiting to merge
* `-p, --priority`: The priority this item should be enqueued with (0-255, 0 is highest)
* `--version`: Display the version
* `--monitor`: Enable the trunk daemon to monitor file changes in your repo
* `--ci`: Run in continuous integration mode
* `--no-progress`: Don't show progress updates
* `--ci-progress`: Rate limit progress updates to every 30s (implied by --ci)
* `--action_timeout`: Timeout for downloads, lint runs, etc
* `-v, --verbose`: Output details about what's happening under the hood
* `--color`: Enable/disable color output

### Trunk Merge Status

`trunk merge status`: Check the status of a submitted merge request.

#### **Usage** **example**

```
trunk merge status [pr] [options]
```

### Trunk Merge Cancel

`trunk merge cancel`: Cancel a pull request from merging.

#### **Usage** **example**

```
trunk merge cancel [pr] [options]
```

### Trunk Merge Pause

`trunk merge pause`: \[admin only] Pauses the queue from merging pull requests.

#### **Usage** **example**

```
trunk merge cancel [pr] [options]
```

### Trunk Merge Resume

`trunk merge resume`: \[admin only] Resumes merging pull requests in the queue.

#### **Usage** **example**

```
trunk merge resume [pr] [options]
```
