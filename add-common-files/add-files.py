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

SHARED_START_LINE_MARKER = "CENTRALLY MAINTAINED FILE"
SHARED_STOP_LINE_MARKER = "END CENTRALLY MAINTAINED FILE"


def has_common_header(txt: str) -> bool:
    lines = txt.splitlines()
    if not lines:
        return False
    return SHARED_START_LINE_MARKER in lines[0]


def get_text_between_marker(
    txt: str, start_marker: str, end_marker: str
) -> tuple[str, str, str]:
    """

    Returns:
         before, middle, after
    """
    before = []
    after = []
    middle = []
    part = 0
    for line in txt.splitlines():
        if end_marker in line:
            # Must come first, as end_marker is also in start_marker
            assert part == 1
            part = 2
        elif start_marker in line:
            part = 1

        if part == 0:
            before.append(line)
        elif part == 1:
            middle.append(line)
        elif part == 2:
            after.append(line)
    return "\n".join(before), "\n".join(middle), "\n".join(after)


def add_file(sf: SharedFile) -> None:
    target = cwd / sf.path
    source = this_dir / sf.path
    assert source.is_file()

    def replace_file(_source: Path, _target: Path) -> None:
        _target.parent.mkdir(exist_ok=True, parents=True)
        shutil.copy(_source, _target)

    def replace_shared_part(_source: Path, _target: Path) -> None:
        s_before, s_middle, s_after = get_text_between_marker(
            _source.read_text(),
            start_marker=SHARED_START_LINE_MARKER,
            end_marker=SHARED_STOP_LINE_MARKER,
        )
        t_before, _, t_after = get_text_between_marker(
            _target.read_text(),
            start_marker=SHARED_START_LINE_MARKER,
            end_marker=SHARED_STOP_LINE_MARKER,
        )
        _target.write_text(f"{t_before}\n{s_middle}\n{t_after}")

    if target.is_file():
        if sf.exist_action == ExistAction.OVERWRITE:
            return replace_file(source, target)
        elif (
            sf.exist_action == ExistAction.OVERWRITE_IF_HEADER
            and has_common_header(target.read_text())
        ):
            return replace_shared_part(source, target)
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
