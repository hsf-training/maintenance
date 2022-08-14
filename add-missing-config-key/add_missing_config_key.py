#!/usr/bin/env python3
from pathlib import Path

import click


@click.command()
@click.argument("path", default=Path("."), type=Path)
def handle_repo(path: Path) -> None:
    config_path = path / "_config.yml"
    if not config_path.is_file():
        return
    txt = config_path.read_text()
    found = False
    if "hsf_site:" not in txt:
        lines = txt.splitlines()
        out_lines = []
        for line in lines:
            out_lines.append(line)
            if "cc_by_human" in line:
                out_lines.append(
                    'hsf_site: "https://hepsoftwarefoundation.org"'
                )
                found = True
        if not found:
            raise ValueError("Couldn't find right place to insert key")
    else:
        return
    config_path.write_text("\n".join(out_lines) + "\n")


if __name__ == "__main__":
    handle_repo()
