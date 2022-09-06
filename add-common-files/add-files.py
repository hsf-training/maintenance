#!/usr/bin/env python3

from dataclasses import dataclass
from enum import Enum, auto
from pathlib import Path
import os
import shutil

this_dir = Path(__file__).resolve().parent
cwd = Path(os.getcwd()).resolve()


class ExistAction(Enum):
    OVERWRITE = auto()
    # If a common header is there, it will be overwritten
    OVERWRITE_IF_HEADER = auto()
    EXCEPTION = auto()
    SKIP = auto()


class DoesNotExistAction(Enum):
    SKIP = auto()
    CREATE = auto()


@dataclass
class SharedFile:
    path: Path
    #: Action to take if the file already exists but is different
    exist_action: ExistAction = ExistAction.EXCEPTION
    does_not_exist_action: DoesNotExistAction = DoesNotExistAction.CREATE


files_to_add = [
    SharedFile(
        Path(".github/config.yml"), exist_action=ExistAction.OVERWRITE_IF_HEADER
    ),
    SharedFile(
        Path(".github/stale.yml"), exist_action=ExistAction.OVERWRITE_IF_HEADER
    ),
    SharedFile(Path("codespell.txt"), exist_action=ExistAction.SKIP),
    SharedFile(
        Path(".pre-commit-config.yaml"),
        exist_action=ExistAction.OVERWRITE_IF_HEADER,
    ),
    SharedFile(
        Path("CONTRIBUTING.md"),
        exist_action=ExistAction.OVERWRITE,
        does_not_exist_action=DoesNotExistAction.SKIP,
    ),
]


def has_common_header(txt: str) -> bool:
    lines = txt.splitlines()
    if not lines:
        return False
    return "CENTRALLY MAINTAINED FILE" in lines[0]


def add_file(sf: SharedFile) -> None:
    target = cwd / sf.path
    source = this_dir / sf.path
    assert source.is_file()

    def replace_file(_source: Path, _target: Path) -> None:
        _target.parent.mkdir(exist_ok=True, parents=True)
        shutil.copy(_source, _target)

    if target.is_file():
        if sf.exist_action == ExistAction.OVERWRITE:
            return replace_file(source, target)
        elif (
            sf.exist_action == ExistAction.OVERWRITE_IF_HEADER
            and has_common_header(target.read_text())
        ):
            return replace_file(source, target)
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
    elif sf.does_not_exist_action == DoesNotExistAction.CREATE:
        return replace_file(source, target)


if __name__ == "__main__":
    for filename in files_to_add:
        add_file(filename)
