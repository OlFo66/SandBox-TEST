#!/usr/bin/python
# -*- coding: utf-8 -*

import sys, getopt
from setup import *

def HowTo():
    print("")
    print("Ce script sert à relever les patchs de mise à jour qui ne se sont pas bien installés.")
    print("Le script s'utilise de la manière suivante:")
    print("./rapportCampagneRHSA.py <NOM-DU-GROUPE-A-PATCHER>")
    print("exemple: ./rapportCampagneRHSA.py Campagne_P_J_1")
    print("")
    sys.exit(1)

if len(sys.argv) != 1:
    HowTo()

failed_Action = Client.schedule.listFailedActions(Key)

print("Rapport de campagne de la nuit.")
    
for fail in failed_Action:
    """
    print("Infos sur l'action en erreur:")
    print("Action id: "+str(fail.get('id')))
    print("Name: "+str(fail.get('name')))
    print("Type: "+str(fail.get('type')))
    print("User: "+str(fail.get('scheduler')))
    print("Date: "+str(fail.get('earliest')))
    print("Nombre de system OK: "+str(fail.get('completedSystems')))
    print("Nombre de system failed: "+str(fail.get('failedSystems')))
    print("Nombre de system en cours: "+str(fail.get('inProgressSystems')))
    print("")
    """
    if str(fail.get('earliest')) == PATCH_CONTROL:
        failed_Client = Client.schedule.listFailedSystems(Key,fail.get('id'))
        for details in failed_Client:
                print("")
                print("La mise à jour ",str(fail.get('id'))," a échoué:")
                print("Machine impactée: ",str(details.get('server_name')))
                print("Détails: ",str(data.get('URL_DETAILS'))+str(fail.get('id')))