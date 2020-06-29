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

import defs
import socket

class Device:
    
    def connect(self, ):
        # create an INET, STREAMing socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((defs.DEV_HOST, defs.DEV_PORT))
        return s
    
    def login(self, socket, username, api_ver, dev_id):
        write_buffer = username + '$' + api_ver + '$' + dev_id + '\n'
        socket.send(write_buffer)

    def req_chan_info(self, socket, ):