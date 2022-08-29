#!/usr/bin/env bash

set -euo pipefail
IFS=$'\n\t'

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

cp "${SCRIPT_DIR}/Gemfile" .

echo -e "\n\nremote_theme: hsf-training/hsf-training-theme" >> _config.yml
