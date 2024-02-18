# setup.py
#
# See:
# https://packaging.python.org/guides/distributing-packages-using-setuptools/
# https://github.com/pypa/sampleproject
#
# Copyright (C) 2020 jumanjiman (Paul Morgan) <jumanjiman@gmail.com>
#
# This file is part of foal.
#
# foal is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# foal is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with foal.  If not, see <http://www.gnu.org/licenses/>.
################################################################################
"""FOAL (From Org Acronyms Lookup) is a tool to lookup acronyms from a set of YAML files."""
from setuptools import find_packages
from setuptools import setup

from foal.version import URL
from foal.version import VERSION

# Get the long description from the README.
with open("README.md") as f:
    README_CONTENT = f.read()

setup(
    name="foal",
    version=VERSION,
    description="Merge and lookup acronyms from a directory tree of definitions.",
    long_description=README_CONTENT,
    long_description_content_type='text/markdown',
    license="GPLv3+",
    author="Paul Morgan",
    author_email="jumanjiman@gmail.com",
    keywords="acronyms lookup",
    url=URL,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "Intended Audience :: End Users/Desktop",
        "Environment :: Console",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
    ],
    python_requires=">=3.5, <4",
    install_requires=[
        "identify>=2.5.35, <3",
        "ruamel.yaml>=0.16.10, <1",
    ],
    packages=find_packages(),
    package_data={
        "foal": [
            "data/*.yaml",
            "schema/*.yaml",
        ],
    },
    entry_points={
        "console_scripts": [
            "foal=foal.__main__:main",
        ],
    },
)
