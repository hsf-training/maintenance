#!/usr/bin/env xonsh

from dataclasses import dataclass
from enum import Enum, auto
from pathlib import Path
import os
import shutil

this_dir = Path(__file__).resolve().parent
cwd = Path(os.getcwd()).resolve()


class ExistAction(Enum):
    OVERWRITE = auto()
    EXCEPTION = auto()
    SKIP = auto()


@dataclass
class SharedFile:
    path: Path
    exist_action: ExistAction = ExistAction.EXCEPTION


files_to_add = [
    SharedFile(Path(".github/config.yml"), exist_action=ExistAction.OVERWRITE),
    SharedFile(Path(".github/stale.yml"), exist_action=ExistAction.OVERWRITE),
    SharedFile(Path("codespell.txt"), exist_action=ExistAction.SKIP),
    SharedFile(Path(".pre-commit-config.yaml"), exist_action=ExistAction.SKIP),
]


def add_file(sf: SharedFile) -> None:
    target = cwd / sf.path
    source = this_dir / sf.path
    if target.is_file():
        if sf.exist_action == ExistAction.OVERWRITE:
            pass
        elif sf.exist_action == ExistAction.SKIP:
            print(f"Skipping {sf.path}")
            return
        elif target.read_text() == source.read_text():
            print(f"{filename} already exists and is up to date")
            return
        else:
            raise FileExistsError(
                f"{target} already exists. Manual action needed."
            )
    assert source.is_file()
    target.parent.mkdir(exist_ok=True, parents=True)
    shutil.copy(source, target)


if __name__ == "__main__":
    for filename in files_to_add:
        add_file(filename)
