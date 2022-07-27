#!/usr/bin/env python3
from pathlib import Path

_shared_files = [
    ".github/FUNDING.yml",
    ".github/ISSUE_TEMPLATE.md",
    ".github/PULL_REQUEST_TEMPLATE.md",
    ".travis.yml",
]
shared_files = [Path(f) for f in _shared_files]


def remove(path: Path) -> None:
    if path.exists():
        # will fail for directories
        path.unlink()
    else:
        print(f"{path} does not exist")


if __name__ == "__main__":
    for p in shared_files:
        remove(p)
