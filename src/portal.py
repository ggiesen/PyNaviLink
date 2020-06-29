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
import requests

class Portal:

    def login(self, username, password):
        r = requests.post(defs.PORTAL_URL + defs.LOGIN_PATH, data = {'userID':username, 'password':password})
        return r.text

    def req_dev_list(self, username, password):
        r = requests.post(defs.PORTAL_URL + defs.REQ_DEV_LIST_PATH, data = {'userID':username, 'password':password})
        return r.text

    def find_user_id(self, fullname, email):
        r = requests.post(defs.PORTAL_URL + defs.FIND_USER_ID_PATH, data = {'name':fullname, 'email':email})
        return r.text
    
    def dev_info_change(self, dev_id, nickname, postal_code, tz, installtype, installer_phone):
        r = requests.post(defs.PORTAL_URL + defs.DEV_INFO_CHANGE_PATH, data = {'deviceID':dev_id, 
            'nickName':nickname, 'zipCode':postal_code, 'timeZone':tz, 'deviceInfo':installtype, 
            'installerInfo':installer_phone})
        return r.text
    
    def req_subuser_list(self, username, password):
        r = requests.post(defs.PORTAL_URL + defs.REQ_DEV_LIST_PATH, data = {'userID':username, 'password':password})
        return r.text
    
    def req_subuser_otp(self, main_username):
        r = requests.post(defs.PORTAL_URL + defs.REQ_DEV_LIST_PATH, data = {'mainUserID':main_username})
        return r.text
    
    def reg_subuser(self, otp_code, username, password, fullname, email, main_username):
        r = requests.post(defs.PORTAL_URL + defs.REG_SUBUSER_PATH, data = {'otpCode':otp_code, 'userID':username, 'name':fullname, 'password':password, 'email':email, 'mainUserID':main_username})
        return r.text
    
    def unreg_user(self, username, email):
        r = requests.post(defs.PORTAL_URL + defs.UNREG_USER_PATH, data = {'userID':username, 'email':email})
        return r.text
    
    def get_push_notification_settings(self, username, dev_id, smartphone_id, server_type):
        payload = {'user_id':username, 'device_id':dev_id, 'smartphone_id':smartphone_id, 'server_type':server_type}
        r = requests.get(defs.IOS_PUSH_URL + defs.IOS_PUSH_NOTIFICATION_PATH, params=payload)
        return r.text
    
    def unreg_push_notifications(self, username, server_type):
        payload = {'user_id':username, 'server_type':server_type}
        r = requests.delete(defs.IOS_PUSH_URL + defs.IOS_PUSH_NOTIFICATION_PATH, params=payload)
        return r.text
    
    