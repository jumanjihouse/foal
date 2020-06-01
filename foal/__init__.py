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
"""FOAL (From Official Acronyms Lookup) is a tool to lookup acronyms from a set of YAML files."""
# If you "import foal", you pollute your global namespace with these modules:
from .acronyms import Acronyms
from .cli import Cli
from .cli import OutputFormatter

__all__ = [
    "Acronyms",
    "Cli",
    "OutputFormatter",
]
