# Repository lists

List of the repositories in `hsf-training` together with their category.
Useful to execute bulk commands.

## Getting all repositories

```bash
 gh repo list hsf-training|awk -F ' ' '{ print $1 }' > all_repos.txt
 ```

 You can clone all of them with

```bash
 while read p; do gh repo clone $p; done < all_repos.txt
 ```

 this will skip already existing repos.

 To pull all of them at once or do other simple broadcasting, you can use `gita`:

 ```bash
 gita add --recursive --auto-group <folder containing all repos from above>
 ```

 Now you can for example do

 ```bash
 gita super fetch <group name>
 ```

 to fetch from all repos at once.
