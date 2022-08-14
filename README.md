# Maintenance scripts

[![gitmoji](https://img.shields.io/badge/gitmoji-%20😜%20😍-FFDD67.svg)](https://gitmoji.dev)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/hsf-training/maintenance/main.svg)](https://results.pre-commit.ci/latest/github/hsf-training/maintenance/main)

> **Warning**
> Some of the scripts and snippets will be experimental. Be careful what you
> execute!

## Development setup

```bash
pip3 install -r requirements.txt
pre-commit install
gitmoji -i
```

before committing.

## Dispatching commands

> **Warning**
> * Please be really careful when dispatching commands to all repositories.
> * Please always test scripts on `hsf-training/repository-maintenance-test` first
> * Please always run `multi-gitter` with `--dry-run` first.

Install and set up [multi-gitter](https://github.com/lindell/multi-gitter/tree/master/internal).
You will find instructions for how to run it in their readme.

> **Note**
> If you run into any errors like [this one](https://github.com/gruntwork-io/git-xargs/issues/82), you might need
> to use a simplified git config. You can use `helpers/switch_out_gitconfig.py` to toggle between your usual config
> and the simplified one.

## Helpful notes

* You might want to use the `Refined github` browser extension to automatically
  delete branches after mergning if creating PRs in bulk with `multi-gitter`
  or friends
* Files ending with `.xsh` are for the [xonsh](https://xon.sh/) shell.
