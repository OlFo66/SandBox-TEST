#!/usr/bin/python
# -*- coding: utf-8 -*

import sys, getopt
import os
import smtplib
 
from email import Encoders
from email.MIMEBase import MIMEBase
from email.MIMEMultipart import MIMEMultipart
from email.Utils import formatdate
from email.MIMEText import MIMEText

MOIS = sys.argv[5]

message = "Bonjour,\n\n"
message = message+"La campagne de patchs de sécurité du mois de "+MOIS+" a commencé.\n"
message = message+"Vous avez été identifé(e) comme responsable d'un projet impliquant une des machines en PJ.\n"
message = message+"Si une ou plusieurs machines ne doivent pas être patchée, merci de nous le signaler par retour de mail avant vendredi.\n"
message = message+"Cordialement,\n\n"
message = message+"L'équipe système"

def HowTo():
    print "La commande s'utilise de la manière suivante:"
    print "./envoi_mail.py <LISTE_DESTINATAIRES_AVEC_VIRGULE> <ENVOYEUR> <SUJET> <CHEMIN_VERS_PJ> <MOIS_DE_CAMPAGNE>"
    print "Exemple: ./envoi_mail.py \"user@mail.com,user2@mail.fr\" \"from@mail.de\" \"Ceci est un sujet\" \"./fichiers_csv/Campagne.csv\" AVRIL"
    sys.exit(1)   

if len(sys.argv) != 6:
    HowTo()
    
def sendEmail(TO = str(sys.argv[1]), FROM=str(sys.argv[2]), SUBJECT=str(sys.argv[3]), PJ=str(sys.argv[4])):
    HOST = "localhost"

    msg = MIMEMultipart()
    msg["From"] = FROM
    msg["To"] = TO
    msg["Subject"] = SUBJECT
    msg['Date']    = formatdate(localtime=True)
 
    msg.attach(MIMEText(message))
    
    # attach a file
    part = MIMEBase('application', "octet-stream")
    part.set_payload( open(PJ,"rb").read() )
    Encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(PJ))
    msg.attach(part)
 
    server = smtplib.SMTP(HOST)
    # server.login(username, password)  # optional
 
    try:
        failed = server.sendmail(FROM, TO, msg.as_string())
        server.close()
    except Exception, e:
        errorMsg = "Unable to send email. Error: %s" % str(e)
 
if __name__ == "__main__":
    sendEmail()