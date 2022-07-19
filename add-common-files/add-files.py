#!/usr/bin/env xonsh

from pathlib import Path
import os
import shutil

this_dir = Path(__file__).resolve().parent
cwd = Path(os.getcwd()).resolve()

files_to_add = [
    ".github/config.yml",
    ".github/stale.yml",
]


def add_file(filename: str) -> None:
    target = cwd / filename
    source = this_dir / filename
    if target.is_file():
        if target.read_text() == source.read_text():
            print(f"{filename} already exists and is up to date")
            return
        raise FileExistsError(f"{target} already exists. Manual action needed.")
    assert source.is_file()
    shutil.copy(source, target)


if __name__ == "__main__":
    for filename in files_to_add:
        add_file(filename)
