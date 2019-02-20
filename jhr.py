# coding: utf-8
# "Martin Ouellet-Diotte"

import json
import csv
import requests

### Ton script fonctionne parfaitement bien, Martin! Bravo!

fichier = "banq.csv" #NOMMER LE FICHIER QUI SERA CREE
fichJHR = "banqJHR.csv"

url1 = "http://collections.banq.qc.ca/api/service-notice?handle=52327/"

entete = {
	"User-agent":"Martin Ouellet-Diotte, UQAM",
	"From":"ouelletdiottem@gmail.com"
}

liste = range(1000,2001)
for a in liste:
	
	url2 = url1 + str(a)
	print(url2)

	req = requests.get(url2,headers=entete)
	# print(req)

	if req.status_code == 200:
		banq = req.json()
		x = banq["titre"]
		if (banq["typesDoc"][0]) == "Audio": ### Tu avais aussi cette info dans «banq["type"]»
		
				s = []
				s.append(banq["titre"][:(x.find("/"))])
				s.append(banq["createurs"][0])
				s.append(banq["dateCreation"])
				s.append(banq["descriptionMat"])
				try: ### Excellent!
					s.append(banq["bitstreams"]["racine"]["fils"][0]["formats"][0]["url"]) ### Voilà l'URL demandé! Bravo!
				except KeyError: ### Excellent de préciser le type d'erreur!
					print("Pas d'url!")
				# print(banq["titre"])
				# print(banq["createurs"][0])
				# print(banq["dateCreation"])
				# print(banq["descriptionMat"])
				# print(banq["bitstreams"]["racine"]["fils"][0]["formats"][0]["url"])
				print(s)
				print("~"*80)

				# f2 = open(fichier,"a") ### Je mets cette ligne en commentaire simplement pour produire mon propre CSV en corrigeant
				f2 = open(fichJHR,"a")
				banq = csv.writer(f2)
				banq.writerow(s)
			

	else:
		print("Cet url semble défectueux")
