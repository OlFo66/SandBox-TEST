#!/usr/bin/python
# -*- coding: utf-8 -*

import sys, getopt
from parametres import *
import csv

def HowTo():
    print "La commande s'utilise de la manière suivante:"
    print "./genCampagneCSV.py <NOM-DE-LA-CAMPAGNE>"
    print "exemple: ./generationFichierCSV.py Campagne_P_J_1"
    sys.exit(1)

if len(sys.argv) != 2:
    HowTo()
    
Fichier_CSV="./fichiers_csv/"+str(sys.argv[1])+"_"+str(TODAY)+".csv"

try:
    fichier = csv.writer(open(str(Fichier_CSV), "wb"))
    fichier.writerow(["Groupe","Machine","Errata","Type Errata","Date Errata","Details Errata"])
except:
    print "Impossible d'ouvrir le fichier"+Fichier_CSV+".\nVérifiez que le dossier existe et que le droit d'écriture soit bien positionné."
    sys.exit(1)
    
try:
    Groupe = Client.systemgroup.listAllGroups(Key)
    for group in Groupe:
        fichier.writerow([str(group.get('name')),'','','','',''])
        for host in Client.systemgroup.listSystems(Key,str(group.get('name'))):
            fichier.writerow(['',str(host.get('hostname')),'','','',''])
            for errata in Client.system.getRelevantErrataByType(Key,host.get('id'),'Security Advisory'):
                fichier.writerow(['','',str(errata.get('advisory_name')),str(errata.get('advisory_type')),str(errata.get('date')),str(errata.get('advisory_synopsis'))])
            for errata in Client.system.getRelevantErrataByType(Key,host.get('id'),'Bug Fix Advisory'):
                fichier.writerow(['','',str(errata.get('advisory_name')),str(errata.get('advisory_type')),str(errata.get('date')),str(errata.get('advisory_synopsis'))])
    print "Le fichier "+str(Fichier_CSV)+" a été généré avec succès."
    print "Merci de le vérifier et de l'envoyer aux responsables de projets pour valider la mise à jour de leurs serveurs."
except:
    print "Erreur lors de la génération du fichier CSV.\nMerci de prévenir l'administrateur.\nFin du script"
    sys.exit(1)

Client.auth.logout(Key)