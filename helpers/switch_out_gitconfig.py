#!/usr/bin/env python3

from pathlib import Path

actual_config_path = Path("~/.gitconfig").expanduser()
simple_config_path = Path("~/.simple_gitconfig").expanduser()
complex_config_path = Path("~/.complex_gitconfig").expanduser()


if __name__ == "__main__":
    if simple_config_path.exists():
        assert not complex_config_path.exists()
        actual_config_path.rename(complex_config_path)
        simple_config_path.rename(actual_config_path)
    else:
        assert complex_config_path.exists()
        assert not simple_config_path.exists()
        actual_config_path.rename(simple_config_path)
        complex_config_path.rename(actual_config_path)
