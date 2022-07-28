#!/usr/bin/env python3

"""Multi-gitter will show partial urls of the form "org/repo #pr_number".
You will not get git notifications of the PRs because you opened them yourself.
This script will take the output of multi-gitter and open all of the PRs in the browser for you.
"""


import webbrowser


def get_multiline_input() -> list[str]:
    # From https://stackoverflow.com/a/38223253
    print("Enter/Paste your content. Ctrl-D or Ctrl-Z ( windows ) to save it.")
    contents = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        contents.append(line)
    return contents


def get_url(line: str) -> str:
    org_repo, pr_number = line.split(" ")
    pr_number = pr_number.lstrip("#")
    return f"https://github.com/{org_repo}/pull/{pr_number}"


def open_url(url: str) -> None:
    webbrowser.open(url)


if __name__ == "__main__":
    inpt = get_multiline_input()
    for line in inpt:
        if line := line.strip():
            open_url(get_url(line))
