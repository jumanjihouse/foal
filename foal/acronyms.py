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
"""Library to merge acronyms from YAML files."""
import glob
import logging
import os
import sys

from identify import identify
from ruamel.yaml import YAML

# This filename takes precedence over all others.
ROOT_GLOBAL = "global.yaml"


class Acronyms:
    """
    Read acronyms from all YAML files in a directory tree.

    From the user perspective, "first acronym definition wins".
    """

    def __init__(self, prefer_files=None, exclude_files=None):
        """Return a new Acronyms object to use for lookups."""
        self.search_list = self._search_list(prefer_files, exclude_files)
        self.merged_acronyms = dict(sorted(self._merged_acronyms().items()))

    def get(self, acronyms=None, ignorecase=False):
        """Get definitions for acronynms (or all definitions if acronyms is empty)."""
        result = self.merged_acronyms
        if not acronyms:
            return result

        if ignorecase:
            return {
                k: v for k, v in result.items()
                if k.lower() in [a.lower() for a in acronyms]
            }

        return {k: v for k, v in result.items() if k in acronyms}

    @staticmethod
    def acronyms_from(path):
        """Load definitions from a file. Return a dictionary."""
        try:
            with open(path, "r") as stream:
                content = YAML(typ="safe").load(stream)
        except FileNotFoundError as err:
            # File has disappeared or was incorrectly put in exclude_flies or prefer_files.
            logging.error("%s: %s", err.strerror, err.filename)
            sys.exit(1)

        acronyms = content.get("acronyms", {})
        for _, val in acronyms.items():
            val["source"] = path  # Show where acronym came from.
        return acronyms

    @staticmethod
    def base_filename(path):
        """Strip directory and file extension from path."""
        basename = os.path.basename(path)
        filename = os.path.splitext(basename)[0]
        return filename

    @staticmethod
    def is_yaml(path):
        """Return True if path is a YAML file."""
        try:
            result = "yaml" in identify.tags_from_path(path)
        except OSError:
            result = False
        return result

    def _merged_acronyms(self):
        """Return a single dictionary that merges acronyms from the search list."""
        # Start with an empty dict.
        result = {}
        # Parse files in reverse order since python dict.update() is "last one wins".
        for filename in reversed(self.search_list):
            result.update(self.acronyms_from(filename))
        return result

    def _search_list(self, prefer_files=None, exclude_files=None):
        """Return an ordered list of files in which to look for acronyms."""
        logging.debug("build search list in: %s", os.getcwd())
        if exclude_files:
            logging.warning("exclude files: %s", repr(exclude_files))
        else:
            exclude_files = []
        if prefer_files:
            logging.warning("prefer files: %s", repr(prefer_files))
        else:
            prefer_files = []

        # Fail early if user requests an impossible combination.
        if any(item in exclude_files for item in prefer_files):
            logging.error("One or more files is both excluded and preferred")
            sys.exit(1)

        # Find all yaml files.
        all_yamls = glob.glob("**/*", recursive=True)
        all_yamls = [f for f in all_yamls if self.is_yaml(f)]
        all_yamls.sort()
        logging.debug("All YAMLs: %s", repr(all_yamls))

        # Find YAML files with basename "global" in any subdirectory.
        # Ensure ROOT_GLOBAL comes first in the list of globals.
        global_yamls = [f for f in all_yamls if self.base_filename(f).lower() == "global"]
        if ROOT_GLOBAL in global_yamls:
            global_yamls = [g for g in global_yamls if g != ROOT_GLOBAL]
            global_yamls.insert(0, ROOT_GLOBAL)
        logging.debug("Global YAMLs: %s", repr(global_yamls))

        # Get the list of "other" yamls.
        other_files = all_yamls
        other_files = [f for f in other_files if f not in global_yamls]   # subtract globals
        other_files = [f for f in other_files if f not in prefer_files]   # subtract preferred files
        other_files = [f for f in other_files if f not in exclude_files]  # subtract excluded files
        logging.debug("Other YAMLs: %s", repr(other_files))

        # Construct search list.
        result = global_yamls        # Globals come first.
        result.extend(prefer_files)  # Preferred files come next.
        result.extend(other_files)   # Other files come last.
        logging.debug("Search list: %s", repr(result))
        return result
