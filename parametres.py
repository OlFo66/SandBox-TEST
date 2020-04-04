#!/usr/bin/python
# -*- coding: utf-8 -*

import xmlrpclib
from datetime import datetime,date, timedelta
import sys
import iso8601

try:
	SATELLITE_URL = "https://xxxxxx/rpc/api"
	SATELLITE_LOGIN = "xxxxx"
	SATELLITE_PASSWORD = "xxxx"
	URL_DETAILS = "https://xxxxxxx/rhn/schedule/ActionDetails.do?aid="
except:
	print "Erreur lors de l'affectation des variables pour la connexion au serveur."
	print "Vérifier les informations de connexion."
	sys.exit(1)
	
try:
	Client = xmlrpclib.Server(SATELLITE_URL, verbose=0)
	Key = Client.auth.login(SATELLITE_LOGIN, SATELLITE_PASSWORD)
except:
	print "Erreur lors de la connexion au Spacewalk."
	print "Vérifiez l'URL de connexion et les ID/PASSWORD..."
	sys.exit(1)

try:
	formatter_string = "%Y-%m-%d"
	TODAY =  datetime.now().strftime(formatter_string)
except:
	print "Erreur lors de la configuration de la date."
	print "Vérifiez que le module datetime soit bien installé sur la machine."
	sys.exit(1)

try:
	PATCH_FORMAT = "%Y%m%dT05:00:00"
	#PATCH_HOUR = datetime.now() + timedelta(days=1)
	HOUR = datetime.now() + timedelta(days=1)
	PATCH_HOUR=HOUR.strftime(PATCH_FORMAT)
	PATCH_TIME=iso8601.parse_date(PATCH_HOUR)
	PATCH_CONTROL = datetime.now().strftime(PATCH_FORMAT)
except:
	print "Erreur lors de la configuration de l'heure de patch."
	print "Vérifiez que les modules datetime ou time soient bien installés sur la machine."
	sys.exit(1)

try:
	REBOOT_FORMAT = "%Y%m%dT07:00:00"
	DATE_PATCH = datetime.now()
	TOMOROW = DATE_PATCH + timedelta(days=1)
	REBOOT_HOUR = TOMOROW.strftime(REBOOT_FORMAT)
	REBOOT_TIME = iso8601.parse_date(REBOOT_HOUR)
	REBOOT = 1
except:
	print "Erreur lors de la configuration de l'heure de reboot."
	print "Vérifiez que les modules datetime ou time soient bien installés sur la machine."
	sys.exit(1)