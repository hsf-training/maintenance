#!/usr/bin/env bash

set -euo pipefail
IFS=$'\n\t'

rm -r _includes
rm -r _layouts
rm -r assets
rm -r bin
rm -rf _episodes_rmd
rm -f .travis.yml

# Remove folders that only contain ".gitkeep"
if [[ $(ls data|wc -l|xargs) == "0" ]]; then rm -r data; fi
if [[ $(ls code|wc -l|xargs) == "0" ]]; then rm -r code; fi
if [[ $(ls files|wc -l|xargs) == "0" ]]; then rm -r files; fi
