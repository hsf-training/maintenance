# Remove organization wide files

Files like the issue template are now shared via the `.github` repository.
Therefore they should not exist/be overwritten in the individual repositories.

## Multi-gitter run

> **Warning**
> Careful!

> **Note**
> Because of a [bug](https://github.com/lindell/multi-gitter/issues/266) in
> multi-gitter, use `--git-type=cmd`.

```bash
multi-gitter run ./remove-organization-wide-files.py -O hsf-training -m "Remove organization wide shared files" -B remove-organization-wide-files --git-type=cmd
```
