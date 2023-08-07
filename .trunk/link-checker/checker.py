#!/usr/bin/env python3
import re
import yaml
from pathlib import Path

EXCLUDED_DIRS = ".git", ".trunk"
LINK_REGEX = r'\[(?P<display>[^\]]+)\]\((?P<link>[^ ]+)\)'

# Load the set of redirects from the gitbook config file
with open(".gitbook.yaml") as stream:
    config = yaml.safe_load(stream)

redirects = config["redirects"]
fail = False

def validate_link(path, url):
    return False

# Iterate through all markdown files and check links
for path in Path('.').rglob('*.md'):
    print(path.name)
    with open(path, "r") as file:
        matches = re.findall(LINK_REGEX, file.read())
        if len(matches) == 0:
            continue
        for match in matches:
          if not validate_link(path, match[1]):
              fail = True
              print("{}: Invalid url: '{}' with description: '{}'".format(path, match[1], match[0]))


if fail:
    exit(1)
