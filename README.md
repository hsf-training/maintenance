# Maintenance snippets

[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/hsf-training/maintenance-snippets/main.svg)](https://results.pre-commit.ci/latest/github/hsf-training/maintenance-snippets/main)

> **Warning**
> Some of the scripts and snippets will be experimental. Be careful what you
> execute!

## Development setup

Please make sure to run

```bash
pre-commit install
```

before committing.

## Dispatching commands

* Install and set up [multi-gitter](https://github.com/lindell/multi-gitter/tree/master/internal).
  Note: If you run into any errors, you might need to start from a blank git config.

## Merging lots of PR

* You might want to use the `Refined github` browser extension to automatically
  delete branches after mergning if creating PRs in bulk with `multi-gitter`
  or friends
