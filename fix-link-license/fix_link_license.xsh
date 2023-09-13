#!/usr/bin/env xonsh

$RAISE_SUBPROC_ERROR = True

from pathlib import Path

def main():
    license = Path("LICENSE.md")
    if not license.exists():
        return
    license_txt = license.read_text()
    license_txt = license_txt.replace("http://communityin.org/", "https://communityinitiatives.org/")
    license.write_text(license_txt)

if __name__ == "__main__":
    git config user.name 'Kilian Lieret'
    git config user.email 'kilian.lieret@posteo.de'
    git config user.signingkey 08A9D21798F687A7656FF8E7DCE690F4156F4F7C
    git config commit.gpgsign true
    main()
