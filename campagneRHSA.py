#!/usr/bin/python
# -*- coding: utf-8 -*

import sys, getopt
from parametres import *
import re

def HowTo():
    print ""
    print "Ce script sert à mettre à jour les serveurs attachés à SpaceWalk."
    print "Le script s'utilise de la manière suivante:"
    print "./campagneRHSA.py <NOM-DU-GROUPE-A-PATCHER>"
    print "exemple: ./campagneRHSA.py Campagne_P_J_1"
    print ""
    sys.exit(1)

if len(sys.argv) != 2:
    HowTo()
    
if re.match('([A-Z]+[a-z]+)_([A-Z])_J_(.)', str(sys.argv[1])):
    REBOOT = 0

try:
    Groupe = Client.systemgroup.listSystems(Key,str(sys.argv[1]))
    for host in Groupe:
        for errata in Client.system.getRelevantErrataByType(Key,host.get('id'),'Security Advisory'):
            #
            # Code pour application de patch de sécurité.
            #
            Client.system.scheduleApplyErrata(Key,host.get('id'),errata.get('id'),PATCH_TIME)
            print "Le patch "+errata.get('advisory_name')+" a été programmé pour s'intaller le "+str(PATCH_TIME)+" sur "+host.get('hostname')+"."
            #
            # Code pour application de patch de correction de bug.
            #        
        for errata in Client.system.getRelevantErrataByType(Key,host.get('id'),'Bug Fix Advisory'):
            Client.system.scheduleApplyErrata(Key,host.get('id'),errata.get('id'),PATCH_TIME)
            print "Le patch "+errata.get('advisory_name')+" a été programmé pour s'intaller le "+str(PATCH_TIME)+" sur "+host.get('hostname')+"."
        #
        # Configuration du reboot de la machine.
        #
        if ( REBOOT == 1 ) :
            Client.system.scheduleReboot(Key,host.get('id'),REBOOT_TIME)
            print "Le redémarrage de "+host.get('hostname')+" est programmé pour demain à 06:00."
except:
    print ""
    print "Erreur lors de la programmation de l'installation des patches ou du reboot de la machine."
    print "Peut-être que le groupe "+str(sys.argv[1])+" n'existe pas."
    HowTo()

Client.auth.logout(Key)