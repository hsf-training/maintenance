# Remove organization wide files

Files like the issue template are now shared via the `.github` repository.
Therefore they should not exist/be overwritten in the individual repositories.

## Multi-gitter run

> **Caution**
> Careful!

```bash
multi-gitter run ./remove-organization-wide-files.sh -O hsf-training -m "Remove organization wide shared files" -B remove-organization-wide-files
```
