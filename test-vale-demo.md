---
title: Vale spellcheck demo
description: Intentionally broken file to verify Vale catches typos in CI.
---

# Vale Spellcheck Demo

This file exists only to verify that the Vale spellcheck linter catches typos
on pull requests. It should never merge.

## Expected failures

Each line below contains a deliberate issue that Vale should flag:

1. Misspelled English word: we should recieve a notification when the job completes.
2. Wrong brand casing: this repo is hosted on github and mirrored to GitHub Enterprise.
3. Unknown word: this blorftastic feature does not exist in the dictionary.

If Vale is working correctly, the `Trunk Code Quality Runner` check on this
PR should fail with three spelling errors pointing at this file.
