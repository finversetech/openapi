#!/usr/bin/env python3
import sys
import semver 
import subprocess


def git(*args):
    return subprocess.check_output(["git"] + list(args))


def bump(latest):
    ver = semver.VersionInfo.parse(latest)
    commit_message = git("log", "--oneline", "-1").decode().strip()
    if "bump-major" in commit_message:
        return ver.bump_major()
    if "bump-minor" in commit_message:
        return ver.bump_minor()
    return ver.bump_patch() 

def main():
    try:
        latest = git("describe", "--tags").decode().strip()
    except subprocess.CalledProcessError:
        # No tags in the repository
        version = "0.0.1"
    else:
        # Skip already tagged commits
        if '-' not in latest:
            print(latest)
            return 0

        version = bump(latest)
    print(version)

    git("tag", str(version))
    return 0


if __name__ == "__main__":
    sys.exit(main())

