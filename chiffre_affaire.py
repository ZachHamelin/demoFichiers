#TODO : Calculer le chiffre d'affaires du magasin
#TODO : et l'afficher à la console.
#Pseudocode:
#ouvrir fichier ventes
    #créer dictionnaire de ventes
#ouvrir fichier prix
    #créer dictionnaire de produits
#chiffre_affaire = 0
#pour k, v dans dict ventes
    #chiffre_affaire += v * prix[k]
#afficher chiffre_affaire

import json
import csv

dict_ventes = {}
with open("magasin/ventes.json", "r", encoding="utf-8") as inventaire: # ref : demo fichiers
    dict_ventes = json.load(inventaire)

dict_prix = {}
with open('magasin/prix.csv', 'r') as file: # réf: démo fichiers
    dict_reader = csv.DictReader(file) #Comme une liste de dictionnaires
    for row in dict_reader:
        dict_prix[row["Produit"]] = float(row["Prix"])

chiffre_affaire = 0
for k, v in dict_ventes.items():
    chiffre_affaire += v * dict_prix[k]
print(chiffre_affaire)
