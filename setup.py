"""
    Project: Shinigami CLI (https://github.com/shinigamilib/cli)
    Author: azazelm3dj3d (https://github.com/azazelm3dj3d)
    License: BSD 2-Clause
"""

import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "shinigami-cli",
    version = "0.1.4",
    author = "azazelm3dj3d",
    description = "Basic CLI showing off the Shinigami library.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/shinigamilib/cli",
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    packages = [
        "src"
    ],
    install_requires=[
        "argparse",
        "shinigami"
    ],
    scripts=["src/cli.py"],
    entry_points={
        'console_scripts': ["shinigami-cli=src.cli:ShinigamiCli.run"]
    },
    python_requires = ">=3.6"
)