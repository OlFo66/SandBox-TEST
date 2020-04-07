#!/usr/bin/python
# -*- coding: utf-8 -*

'''
import xmlrpclib
from datetime import datetime,date, timedelta
import sys
import iso8601
'''

config = configparser.ConfigParser()
config.read('setup.conf')
data = config['DEFAULT']

try:
	Client = xmlrpclib.Server(data.get('SATELLITE_URL'), verbose=0)
	Key = Client.auth.login(data.get('SATELLITE_LOGIN'), data.get('SATELLITE_PASSWORD'))
except:
	print("Error trying to connect to Spacewalk server.")
	print("Verify SATELLITE_URL, SATELLITE_LOGIN or SATELLITE_PASSWORD values.")
	sys.exit(1)

try:
	formatter_string = "%Y-%m-%d"
	TODAY =  datetime.now().strftime(formatter_string)
except:
	print("Error setting date.")
	print("Verify datetime module installation or configuration.")
	sys.exit(1)

try:
	# reset PATCH_FORMAT using HOUR_OF_PATCH from setup.conf value
	PATCH_FORMAT = "%Y%m%dT"+str(data.get('HOUR_OF_PATCH'))
	#PATCH_HOUR = datetime.now() + timedelta(days=1)
	HOUR = datetime.now() + timedelta(days=1)
	PATCH_HOUR=HOUR.strftime(PATCH_FORMAT)
	PATCH_TIME=iso8601.parse_date(PATCH_HOUR)
	PATCH_CONTROL = datetime.now().strftime(PATCH_FORMAT)
except:
	print("Error setting path hour.")
	print("Verify datetime or time module installation.")
	sys.exit(1)

try:
	# reset PATCH_FORMAT using HOUR_OF_REBOOT from setup.conf value
	REBOOT_FORMAT = "%Y%m%dT"+str(data.get('HOUR_OF_REBOOT'))
	DATE_PATCH = datetime.now()
	TOMOROW = DATE_PATCH + timedelta(days=1)
	REBOOT_HOUR = TOMOROW.strftime(REBOOT_FORMAT)
	REBOOT_TIME = iso8601.parse_date(REBOOT_HOUR)
	REBOOT = 1
except:
	print("Error setting reboot hour.")
	print("Verify datetime or time module installation.")
	sys.exit(1)