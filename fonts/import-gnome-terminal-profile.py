#!/usr/bin/env python

import sys
import subprocess


def main():
    profile_contents = list(filter(None, sys.stdin.read().split('\n')))
    profile_id = profile_contents[0][1:-1]

    dconf_path = f"/org/gnome/terminal/legacy/profiles/{profile_id}/"

    dconf = subprocess.Popen(
        [
            "dconf",
            "load",
            dconf_path,
        ],
        stdin=subprocess.PIPE,
    )

    print("\n".join(profile_contents).encode("utf-8"))
    dconf.communicate(input="\n".join(profile_contents).encode("utf-8"))
    return 0


if __name__ == '__main__':
    sys.exit(main())
