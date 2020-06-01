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
"""CLI utility to lookup acronyms from merged YAML files."""
import argparse
import logging
import os
import sys
from textwrap import dedent

from ruamel.yaml import YAML

from .acronyms import Acronyms
from .version import URL
from .version import VERSION

DEFAULT_DATA_DIR = os.path.join(os.path.dirname(__file__), "data")

DESCRIPTION = dedent(
    """\
    Merge acronyms from YAML files in directory tree
    """,
)

EPILOG = dedent(
    """\
    search order:
      If an acronym is defined in multiple files, the first definition wins.
      The order is determined by the search list as follows:
        global.yaml in current directory
      + global.yaml in subdirectories
      + preferred files in order provided (-p)
      + all other YAMLs
      - excluded files (-x)
      ----------------------------------------------
      = search list

    environment variables:
      DEBUG=anything      Show verbose program operation
    """,
)


class OutputFormatter(YAML):
    """Trivial subclass of ruamel.yaml."""

    def __init__(self, **kwargs):
        """Create a YAML() instance from ruamel.yaml with settings as an output formatter."""
        super().__init__()
        self.indent(
            mapping=kwargs.get("mapping", 4),
            sequence=kwargs.get("sequence", 6),
            offset=kwargs.get("offset", 4),
        )
        self.explicit_start = kwargs.get("explicit_start", True)
        self.explicit_end = kwargs.get("explicit_end", False)
        self.width = kwargs.get("width", None)
        self.preserve_quotes = kwargs.get("preserve_quotes", False)
        self.top_level_colon_align = kwargs.get("colons", False)


class Cli:
    """Provide a command-line-interface for foal."""

    def __init__(self):
        """Return a new instance of the CLI."""
        self.build_parser()
        logging.basicConfig(
            format="[%(levelname)s] %(message)s",
            level=logging.DEBUG if "DEBUG" in os.environ else logging.WARNING,
        )

    def main(self):
        """Run the CLI."""
        args = self.parser.parse_args()

        try:
            original_dir = os.getcwd()
            if args.directory == DEFAULT_DATA_DIR:
                logging.warning("Using built-in data at %s", DEFAULT_DATA_DIR)
            os.chdir(args.directory)
            output = {}
            output["acronyms"] = Acronyms(
                args.prefer_files,
                args.exclude_files,
            ).get(args.acronyms, args.ignorecase)
            os.chdir(original_dir)
        except OSError as err:
            logging.error("%s: %s", err.strerror, err.filename)
            sys.exit(1)

        outfile = args.outfile
        try:
            outfile = open(outfile, "w")
        except OSError as err:
            logging.error("%s: %s", err.strerror, err.filename)
            sys.exit(1)
        except TypeError:
            outfile = sys.stdout

        OutputFormatter().dump(output, outfile)
        outfile.close()  # no effect on stdout

    def build_parser(self):
        """Private method to return the CLI argument parser."""
        parser = argparse.ArgumentParser(
            description=DESCRIPTION,
            epilog=EPILOG,
            formatter_class=argparse.RawDescriptionHelpFormatter,
        )
        parser.add_argument(
            "-v",
            "--version",
            action="version",
            version=f"foal {VERSION} {URL}",
        )
        parser.add_argument(
            "-a",
            metavar="ACRONYM",
            dest="acronyms",
            default=None,
            action="append",
            help="acronyms to find, can be used multiple times (default: all unique acronyms)",
        )
        parser.add_argument(
            "-i",
            dest="ignorecase",
            action="store_true",
            help="ignore case of acronyms",
        )
        parser.add_argument(
            "-o",
            metavar="FILENAME",
            dest="outfile",
            default=sys.stdout,
            help="output to FILENAME (default: STDOUT)",
        )
        parser.add_argument(
            "-p",
            metavar="FILENAME",
            dest="prefer_files",
            default=[],
            action="append",
            help="prefer FILENAME before other YAML files, can be used multiple times",
        )
        parser.add_argument(
            "-x",
            metavar="FILENAME",
            dest="exclude_files",
            default=None,
            action="append",
            help="exclude FILENAME, can be used multiple times  (cannot exclude global.yaml)",
        )
        parser.add_argument(
            metavar="DIRECTORY",
            dest="directory",
            nargs="?",
            default=DEFAULT_DATA_DIR,
            help=f"data directory (default: {DEFAULT_DATA_DIR})",
        )
        self.parser = parser
