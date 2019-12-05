#!/usr/bin/env python3
"""Helper script to make a release."""

import re
import os
import sys
import glob
import logging
import argparse
import subprocess
from pathlib import Path
from datetime import datetime
from packaging.version import Version, InvalidVersion

_LOGGER = logging.getLogger(__name__)

CHANGES_TEMPLATE = """CHANGES
=======

{version}
{separators}

Changes:

REMOVE ME

Notes:

REMOVE ME

"""


def bail(message, *args):
    """Log error and exit script."""
    _LOGGER.error(message.format(args))
    sys.exit(1)


def sanity_check():
    """Perform basic checks before running script."""
    if not os.path.exists("setup.py"):
        bail("You must run this script from repo root")

    if not os.getenv("VIRTUAL_ENV"):
        bail("Please run from a virtual environment")


def call(cmd, *args, show_output=False):
    """Call a shell command."""
    result = subprocess.run(
        cmd.format(*args), shell=True, check=True,
        stdout=subprocess.PIPE if not show_output else None)
    return None if show_output else result.stdout.decode("utf-8")


def verify_dist():
    """Verify that dist/ is empty or remove files."""
    _LOGGER.info("Verifying dist...")
    if os.path.exists("dist"):
        content = glob.glob("dist/*")
        if content:
            for filename in content:
                _LOGGER.debug("Removing %s", filename)
                os.unlink(filename)

    if glob.glob("dist/*"):
        bail("The dist directory must be empty!")


def install_dependencies():
    """Install python dependencies."""
    for package in ["wheel", "twine"]:
        _LOGGER.info("Installing package %s", package)
        call("pip3 install {0}", package, show_output=False)


def update_version(version):
    """Update version constants in const.py."""
    from pyatv import const
    _LOGGER.info("Current version is: %s", const.__version__)
    _LOGGER.info("Updating with new version: %s", version)

    output = Path("pyatv/const.py").read_text()
    splitted = version.split(".")
    for i, component in enumerate(["MAJOR", "MINOR", "PATCH"]):
        output = re.sub(
            "(" + component + "_VERSION =).*",
            "\\1 '" + splitted[i] + "'",
            output)

    with open("pyatv/const.py", "w") as wh:
        wh.write(output)


def generate_outputs():
    """Generate ouput artifacts for pypi."""
    _LOGGER.info("Generating outputs")
    call("python3 setup.py sdist bdist_wheel", show_output=False)


def insert_changes(version):
    """Insert changelog entry into CHANGES.rst."""
    _LOGGER.info("Adding entry to CHANGES.rst")
    changes = Path("CHANGES.rst").read_text().split("\n")

    if changes[3].startswith(version):
        _LOGGER.info("Changelog entry already present")
    else:
        version_str = "{0} ({1})".format(
            version, datetime.now().strftime("%Y-%m-%d"))

        with open("CHANGES.rst", "w") as fw:
            fw.write(CHANGES_TEMPLATE.format(
                version=version_str,
                separators="=" * len(version_str)))
            fw.write("\n".join(changes[3:]))


def verify_changes(version):
    """Verify that CHANGES.rst is valid."""
    _LOGGER.info("Verifying CHANGES.rst")

    changes = Path("CHANGES.rst").read_text()
    if version not in changes:
        bail("Version {0} not in CHANGES.rst", version)

    if "REMOVE ME" in changes:
        bail("CHANGES.rst contains bad content!")


def verify_and_create_commit(version):
    """Verify git commits."""
    if version in call("git --no-pager log -10"):
        bail("A release commit already seems to exist!")

    if "Changes to be committed:" not in call("git status"):
        bail("No files staged for commit! Add files first.")

    _LOGGER.info("Trying to create release commit")
    call('git commit -m "Release {0}"', version)

    expected_files = ["CHANGES.rst", "pyatv/const.py"]
    content = call("git --no-pager show", show_output=False)
    for filename in expected_files:
        if "+++ b/{0}".format(filename) not in content:
            bail("Missing file {0} in commit", filename)


def create_tag(version):
    """Create a git tag for the release."""
    if version.is_prerelease:
        _LOGGER.info("Not creating tag for pre-release")
    else:
        raise NotImplementedError()


def main():
    """Script starts here."""
    logging.basicConfig(
        level=logging.INFO, format="[%(levelname)s] %(message)s")

    parser = argparse.ArgumentParser(description="release maker")
    parser.add_argument("version", help="version to release")
    parser.add_argument("--skip-dependencies", default=False,
                        action="store_true",
                        help="skip installing dependencies")
    parser.add_argument("--skip-update-version", default=False,
                        action="store_true",
                        help="skip updating version")
    parser.add_argument("--skip-changes", default=False,
                        action="store_true",
                        help="skip updating CHANGES.rst")
    parser.add_argument("--skip-verify-changes", default=False,
                        action="store_true",
                        help="skip verify content in CHANGES.rst")
    parser.add_argument("--skip-commit", default=False,
                        action="store_true",
                        help="skip git commit")
    parser.add_argument("--skip-outputs", default=False,
                        action="store_true",
                        help="do not generate outputs")
    parser.add_argument("--skip-tag", default=True,
                        action="store_true",
                        help="skip creating git tag")

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-p", default=False, action="store_true",
                       dest="prepare_release",
                       help="prepare a release")
    group.add_argument("-m", default=False, action="store_true",
                       dest="make_release",
                       help="make a release")

    args = parser.parse_args()

    try:
        version = str(Version(args.version))
    except InvalidVersion:
        _LOGGER.error("Invalid version format")
        return 1

    sanity_check()

    if args.prepare_release:
        _LOGGER.info("Preparing to release %s", version)
        if not args.skip_dependencies:
            install_dependencies()
        if not args.skip_update_version:
            update_version(version)
        if not args.skip_changes:
            insert_changes(version)
        _LOGGER.info(
            "Update CHANGES.rst and add files to include with git add")
    elif args.make_release:
        _LOGGER.info("Making release %s", version)
        if not args.skip_verify_changes:
            verify_changes(version)
        if not args.skip_commit:
            verify_and_create_commit(version)
        if not args.skip_outputs:
            verify_dist()
            generate_outputs()
        if not args.skip_tag:
            create_tag(Version(args.version))

    _LOGGER.info("Done")

    return 0


if __name__ == '__main__':
    sys.exit(main())
