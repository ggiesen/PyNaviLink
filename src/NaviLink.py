################################################################################
# PyNaviLink: a library for communicating with a Navien NaviLink interface to 
# Navien Domestic Hot Water Heaters and Boilers
# Copyright (C) 2018  Gary T. Giesen
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
# 
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
################################################################################

import socket
import sys

class NaviLink(object):
    def __init__(self, address, port, username, password):
        self._events = None  # create this JIT so no socket reuse
        self._reconnect_thread = None
        
        try:
            self.conn = socket.socket.connect(address, port)

        except ValueError as e:
            self._connected = False
            try:
                self.log.error(e.message)
            except AttributeError:
                self.log.error(e.args[0])

        else:
            self._connected = True