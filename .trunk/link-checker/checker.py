#!/usr/bin/env python3
import os
import re
import requests
import yaml
from pathlib import Path
from urllib.parse import urlparse

# TODO: Create maps of frequently read files to improve performance
# TODO: Parallize for performance

LINK_REGEX = r"\[(?P<display>[^\]]+)\]\((?P<link>[^ \)]+)\)"
ALLOW_LIST_URLS = [
    "https://marketplace.visualstudio.com/items?itemName=trunk.io",
    "https://static.trunk.io/assets/vscode\_init\_trunk.png",
    "https://static.trunk.io/assets/vscode\_side\_panel.png",
    "https://static.trunk.io/assets/vscode\_hide\_explorer\_panel.jpg",
    "https://static.trunk.io/assets/vscode\_doc\_links.png",
    "https://static.trunk.io/assets/vscode\_ignore\_issue.gif",
    "mailto:support@trunk.io",
    "mailto:sales@trunk.io",
]
ALLOW_LIST_FRAGMENTS = ["sample"]

# Load the set of redirects from the gitbook config file
with open(".gitbook.yaml", "r") as stream:
    config = yaml.safe_load(stream)

redirects = config["redirects"]
fail = False


def check_fragment(source_path, link_dest, fragment):
    if fragment in ALLOW_LIST_FRAGMENTS:
        return True
    fragment_regex = r"# [`*_]*{}".format(fragment.replace("-", "."))
    with open(link_dest, "r") as target:
        if re.search(fragment_regex, target.read(), re.IGNORECASE) is None:
            print(
                ">>> Could not detect fragment '{}' in file {} pointing to from {}".format(
                    fragment, link_dest, source_path
                )
            )
            return False
        return True


def validate_link(path, url):
    if url in ALLOW_LIST_URLS:
        return True
    if url.startswith("http"):
        stripped_url = (
            urlparse(url, allow_fragments=False)
            ._replace(query="", fragment="")
            .geturl()
        )
        return requests.head(stripped_url).status_code != 404

    fragment_index = url.find("#")
    if fragment_index > 0:
        filename = url[:fragment_index]
        fragment = url[fragment_index + 1 :]
        from_file_path = path.parent.joinpath(filename)
        from_root_path = filename

        if filename == "." or filename == "./":
            return check_fragment(path, path.parent.joinpath("README.md"), fragment)
        if os.path.exists(from_file_path):
            return check_fragment(path, from_file_path, fragment)
        if os.path.exists(from_root_path):
            return check_fragment(path, from_root_path, fragment)
        return False
    else:
        if os.path.exists(path.parent.joinpath(url)) or os.path.exists(url):
            return True

    return False


# Iterate through all markdown files and check links
for path in Path(".").rglob("*.md"):
    with open(path, "r") as file:
        matches = re.findall(LINK_REGEX, file.read())
        if len(matches) == 0:
            continue
        for match in matches:
            if not validate_link(path, match[1]):
                fail = True
                print(
                    "{}: Could not find url: '{}' with description: '{}'".format(
                        path, match[1], match[0]
                    )
                )

if fail:
    exit(1)
