#!/usr/bin/env bash

# Source this file to make your github token available.

TOKEN_FILE=$HOME/gh_token.txt


if [[ -f "${TOKEN_FILE}" ]]; then
    export GITHUB_TOKEN=$(cat $HOME/gh_token.txt)
else
    >&2 echo "Did not find ${TOKEN_FILE}"
fi
