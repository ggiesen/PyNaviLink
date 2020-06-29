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


PORTAL_URL = 'https://uscv2.naviensmartcontrol.com'
ANDROID_PUSH_URL = 'https://uspush.naviensmartcontrol.com'
IOS_PUSH_URL = 'https://uscv2.naviensmartcontrol.com'
LOGIN_PATH = '/api/userLogin'
REQ_DEV_LIST_PATH = '/api/requestDeviceList'
FIND_USER_ID_PATH = '/api/userFindId'
REG_SUBUSER_PATH = '/api/SubUserJoin'
UNREG_USER_PATH = '/api/userWithdrawal'
DEV_INFO_CHANGE_PATH = '/api/deviceInfoChange'
IOS_PUSH_NOTIFICATION_PATH = '/api/PushDevice'

# NaviLink Binary API Host
DEV_HOST = 'uscv2.naviensmartcontrol.com'
# NaviLink Binary API Port
DEV_PORT = 6001
# NaviLink Binary API Version?
DEV_API_VER = '$iPhone1.0$'

# Start transmission
STX = b'\x07'
# ???
DID = b'\x99'
# ???
RESERVED = b'\x00'
# Command
CMD = b'\xa6'
# ???
DSID = b'\x00'

# Length of Channel Information response in bytes
LEN_CHAN_INFO = 52
# Length of State response in bytes
LEN_STATE = 272
# Length of Trend Sample response in bytes
LEN_TREND_MONTH = 39
# Length of Trend Month response in bytes
LEN_TREND_MONTH = 703
# Length of Trend Year response in bytes
LEN_TREND_YEAR = 549
