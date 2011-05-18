# browsershots.org - Test your web design in different browsers
# Copyright (C) 2007 Johann C. Rocholl <johann@browsershots.org>
#
# Browsershots is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# Browsershots is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""
GUI-specific interface functions for X11.
"""

__revision__ = "$Rev: 3048 $"
__date__ = "$Date: 2008-09-03 03:28:56 +0530 (Wed, 03 Sep 2008) $"
__author__ = "$Author: johann $"


import os
from shotfactory04.gui import linux as base
from shotfactory04.inifile import IniFile


class Gui(base.Gui):
    """
    Special functions for NetFront.
    """

    def reset_browser(self):
        """
        Reset crashed state and delete browser cache.
        """
        pass

    scroll_attempts = 20
    def scroll_down(self, good_offset):
        self.down()

    def scroll_bottom(self):
        for dummy in range(100):
            self.down()
