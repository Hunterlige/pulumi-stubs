#!/usr/bin/env python3

import os
import subprocess
import shutil


def generate_stubs():
    packages = [
        "pulumi-aws",
        "pulumi-gcp",
        "pulumi-azure-native",
    ]
    for package in packages:
        package_name = package.replace("-", "_")
        shutil.rmtree(
            f"packages/{package}-stubs/src/{package_name}",
            ignore_errors=True,
        )
        _ = subprocess.run(
            [
                "pyright",
                "--createstub",
                f"{package_name}",
            ],
            check=True,
        )
        _ = subprocess.run(
            [
                "touch",
                f"typings/{package_name}/__init__.py",
            ],
            check=True,
        )
        _ = subprocess.run(
            [
                "mv",
                f"typings/{package_name}",
                f"packages/{package}-stubs/src/{package_name}",
            ],
            check=True,
        )
    _ = subprocess.run(
        [
            "ruff",
            "check",
            "packages",
            "--fix",
            "--unsafe-fixes",
        ],
        check=False,
    )
    _ = subprocess.run(
        [
            "ruff",
            "format",
            f"packages",
        ],
        check=False,
    )
    os.rmdir("typings")


if __name__ == "__main__":
    generate_stubs()
