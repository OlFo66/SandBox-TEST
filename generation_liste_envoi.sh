#!/usr/bin/bash
##############################
#
#	Script pour la génération du fichier CSV et l'envoie de celui-ci
#
##############################

EXPEDITEUR="spacewalk@domain.tld"
DESTINATAIRE="user1@domain.tld,user2@domain.tld"

DATE=$(date '+%Y%m%d_%Hh%M')
FICLOG="./log/generation_liste_envoi.log"

MOIS=$(date '+%B_%Y')
SUJET="Campagne_de_patch_Linux"
MAJ=""
QUIET="n"

LISTNOGRP="/exploitation/procedures/output/systemes_hors_campagne.csv"
LIST="/exploitation/procedures/output/campagne.csv"

HowTo(){
	echo -e "La commande s'utilise de la maniÃ¨re suivante:"
	echo -e "./generation_liste_envoi.sh <NOM_DE_LA_CAMPAGNE>"
	echo -e "Exemple: ./generation_liste_envoi.sh Campagne_P_J_1"
	exit 1
}

if [[ $# -ne 1 ]]
then
	HowTo
fi

echo -e "\n${DATE} : Lancement du script de génération et d'envoi des listes de ${SUJET} de ${MOIS}" | tee -a ${FICLOG}

# Generation rapport

REP="n"
echo -e "\nGénérer les listes de campagne de patch ? (yYoO) - non par défaut \c"
read REP
case $REP in
	[yYoO])
		
		echo -e "Génération des listes de campagne...\n\t${LISTNOGRP}\n\t${LIST}" | tee -a ${FICLOG}
		/usr/bin/python ./generationFichierCSV.py ${1}
		
		if [ $? -eq 0 ] ; then
			echo "Liste générée" | tee -a ${FICLOG}
			echo "Envoyer la liste? (yYoO) - non par défaut"
			read ENVOI
			
			case $ENVOI in
				[yYoO])
					echo "Envoi de la liste aux responsables"
					/usr/bin/python ./envoi_mail.py ${DESTINATAIRE} ${EXPEDITEUR} ${SUJET} "./fichiers_csv/${1}_$(date +%Y-%m-%d).csv" ${MOIS}
					if [ $? -eq 0 ] ; then
						echo "Liste envoyée" | tee -a ${FICLOG}
					else 
						echo "ProblÃ¨me lors de l'envoi." | tee -a ${FICLOG}
						exit 1
					fi
					;;
				*)
					echo "Liste non (re)envoyée" | tee -a ${FICLOG}
				;;
			esac		
		else
			echo "Erreur lors de la génération des listes"  | tee -a ${FICLOG}
			exit 1
		fi
		;;
	*)
		echo "Listes non (re)générées" | tee -a ${FICLOG}
	;;
esac
