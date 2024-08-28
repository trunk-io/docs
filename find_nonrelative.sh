#!/bin/bash
set -euo pipefail
LINT_TARGET="${1}"
TODO_REGEX="docs.trunk.io"
GREP_FORMAT="([^:]*):([0-9]+):(.*)"
PARSER_FORMAT="\1:\2:0: [error] Found docs.trunk.io in line (LINK)"

grep -o -E "${TODO_REGEX}" --line-number --with-filename "${LINT_TARGET}" | sed -E "s/${GREP_FORMAT}/${PARSER_FORMAT}/"
