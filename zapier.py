import locale
from datetime import datetime
from datetime import timedelta

# on récupère la date du mail reçu
locale.setlocale(locale.LC_ALL, 'en_US')
date_sent1 = input['date'].split(' +')[0]
date_sent = datetime.strptime(date_sent1, "%a, %d %b %Y %H:%M:%S")

# on récupère la date du voyage dans le sujet du mail
locale.setlocale(locale.LC_ALL, 'fr_FR')
txt = input['subject']
date_aller = txt[txt.find("aller le ") + len("aller le "):].split(",")[0]
try:
    date_retour = txt[txt.find("retour le ") + len("retour le "):].split(",")[0]
    date_retour = date_retour + " " + str(date_sent.year)
except:
    date_retour = ""
lieu_depart, lieu_arrivee = txt[txt.find("votre voyage ") + len("votre voyage "):].split(",")[0].split(" - ")

# on ajoute l'année
date_aller = date_aller + " " + str(date_sent.year)
date_aller_d = datetime.strptime(date_aller, "%d %b %Y")
if date_retour != "":
    date_retour_d = datetime.strptime(date_retour, "%d %b %Y")
# si le mois du mail est > au mois du voyage, c'est qu'il faut ajouter une année
if (date_sent.month > date_aller_d.month):
    date_aller_d = date_aller_d + timedelta(365/12)
    if date_retour != "":
        date_retour_d = date_retour_d + timedelta(365/12)

# on récupère les heures dans le corps du mail
texte = input['body']
n = texte.find('Aller\n')
heure_depart_aller = texte[n+6:n+12]
date_aller_depart = date_aller_d + timedelta(hours=int(heure_depart_aller.split("h")[0]), minutes=int(heure_depart_aller.split("h")[1]))

heure_arrivee_aller = texte[n:][texte[n:].find(lieu_arrivee)-7:texte[n:].find(lieu_arrivee)-1]
date_aller_arrivee = date_aller_d + timedelta(hours=int(heure_arrivee_aller.split("h")[0]), minutes=int(heure_arrivee_aller.split("h")[1]))

return {'trajet_aller':lieu_depart + '->' + lieu_arrivee, 'date_aller_depart': str(date_aller_depart), 'date_aller_arrivee': str(date_aller_arrivee)}
