# Repository lists

List of the repositories in `hsf-training` together with their category.
Useful to execute bulk commands.

## Getting all repositories

```bash
 gh repo list hsf-training|awk -F ' ' '{ print $1 }'
 ```
