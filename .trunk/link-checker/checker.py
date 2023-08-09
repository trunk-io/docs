#!/usr/bin/env python3
import os
import re
import requests
import yaml
from pathlib import Path
from urllib.parse import urlparse

import argparse
from enum import Enum


class Result(Enum):
    PASS = 1
    FAIL_404 = "Could not find url: '{}' with description: '{}'"
    FAIL_RELATIVE = "'{}' should be relative"
    FAIL_FRAGMENT = "Could not find fragment '{}' in '{}'"
    FAIL_UNKNOWN = "Failed to detect url: '{}' with description '{}'"


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

parser = argparse.ArgumentParser()
parser.add_argument("filename", nargs=1)
args = parser.parse_args()
filename = args.filename[0]

def check_fragment(link_dest, fragment):
    if fragment in ALLOW_LIST_FRAGMENTS:
        return (Result.PASS, None)
    fragment_regex = r"# [`*_]*{}".format(fragment.replace("-", "."))
    with open(link_dest, "r") as target:
        if re.search(fragment_regex, target.read(), re.IGNORECASE) is None:
            return (Result.FAIL_FRAGMENT, fragment)
        return (Result.PASS, None)


def validate_link(path, url):
    if url in ALLOW_LIST_URLS:
        return (Result.PASS, None)
    if url.startswith("https://docs.trunk.io/"):
        return (Result.FAIL_RELATIVE, None)
    if url.startswith("http"):
        stripped_url = (
            urlparse(url, allow_fragments=False)
            ._replace(query="", fragment="")
            .geturl()
        )
        if requests.head(stripped_url).status_code == 404:
            return (Result.FAIL_404, None)
        return (Result.PASS, None)

    fragment_index = url.find("#")
    if fragment_index > 0:
        filename = url[:fragment_index]
        fragment = url[fragment_index + 1 :]
        from_file_path = path.parent.joinpath(filename)
        from_root_path = filename

        if filename == "." or filename == "./":
            return check_fragment(path.parent.joinpath("README.md"), fragment)
        if os.path.exists(from_file_path):
            return check_fragment(from_file_path, fragment)
        if os.path.exists(from_root_path):
            return check_fragment(from_root_path, fragment)
        return (Result.FAIL_UNKNOWN, None)
    else:
        if os.path.exists(path.parent.joinpath(url)) or os.path.exists(url):
            return (Result.PASS, None)

    return (Result.FAIL_UNKNOWN, None)


# Iterate through markdown file and check links
path = Path(filename)
with open(path, "r") as file:
    file_lines = file.read().splitlines()
    for line_num, line in enumerate(file_lines, 1):
        matches = re.findall(LINK_REGEX, line)
        if len(matches) == 0:
            continue
        for match in matches:
            result, details = validate_link(path, match[1])
            if result == Result.FAIL_FRAGMENT:
                fail = True
                message = result.value.format(details, match[1])
                print("{}:{}: {}".format(filename, line_num, message))
            elif result != Result.PASS:
                fail = True
                message = result.value.format(match[1], match[0])
                print("{}:{}: {}".format(filename, line_num, message))

if fail:
    exit(1)
