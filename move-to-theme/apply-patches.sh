#!/usr/bin/env bash

set -euo pipefail
IFS=$'\n\t'

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

git apply "${SCRIPT_DIR}/0001-Switch-to-using-the-Jekyll-theme.patch"
