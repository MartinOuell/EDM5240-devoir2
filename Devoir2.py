# coding: utf-8
# "Martin Ouellet-Diotte"
import json
import csv
import requests

fichier = "banq.csv" #NOMMER LE FICHIER QUI SERA CREE

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
		if (banq["typesDoc"][0]) == "Audio":
		
				s = []
				s.append(banq["titre"][:(x.find("/"))])
				s.append(banq["createurs"][0])
				s.append(banq["dateCreation"])
				s.append(banq["descriptionMat"])
				try:
					s.append(banq["bitstreams"]["racine"]["fils"][0]["formats"][0]["url"])
				except KeyError:
					print("Pas d'url!")
				# print(banq["titre"])
				# print(banq["createurs"][0])
				# print(banq["dateCreation"])
				# print(banq["descriptionMat"])
				# print(banq["bitstreams"]["racine"]["fils"][0]["formats"][0]["url"])
				print(s)
				print("~"*80)

				f2 = open(fichier,"a")
				banq = csv.writer(f2)
				banq.writerow(s)
			

	else:
		print("Cet url semble défectueux")
