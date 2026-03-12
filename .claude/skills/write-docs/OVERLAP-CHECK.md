# Duplicate & Overlap Check

Run these checks before starting any work. Stop and ask the user if any match is found.

## Step 1: Check for existing PRs/branches from this draft

1. Derive the expected branch topic from the draft filename (e.g., `flag-as-flaky.md` -> `flag-as-flaky`). Get the username prefix from `git config user.name` (kebab-cased).

2. Search for open PRs matching the branch:
   ```bash
   gh pr list --repo trunk-io/docs --state open --head "<username>/<topic>" --json number,title,url,headRefName
   ```
   Also search by topic keyword:
   ```bash
   gh pr list --repo trunk-io/docs --state open --json number,title,url,headRefName | jq '.[] | select(.headRefName | contains("<topic>"))'
   ```

3. Check local branches:
   ```bash
   git branch --list "*<topic>*"
   ```

4. **If a match is found**: Show the user the existing PR/branch and ask:
   - (a) Update the existing PR
   - (b) Close it and start fresh
   - (c) Skip this draft

   Do NOT proceed until the user responds.

## Step 2: Check for overlapping PRs from other authors

1. Read the draft to identify target docs files/product area.

2. List all open PRs:
   ```bash
   gh pr list --repo trunk-io/docs --state open --json number,title,headRefName,url --limit 50
   ```

3. For any PR that looks related (by title or branch name matching the same product area), check file overlap:
   ```bash
   gh pr view <number> --repo trunk-io/docs --json files --jq '[.files[].path]'
   ```

4. **If overlapping PRs are found**: Show the user the overlapping PR and affected files, then ask:
   - (a) Proceed anyway (changes will likely conflict)
   - (b) Wait for that PR to merge first
   - (c) Skip this draft

   Do NOT proceed until the user responds.

5. **If no overlaps found**: Continue to Phase 1.
