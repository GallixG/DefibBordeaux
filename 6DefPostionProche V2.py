# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 09:17:21 2020

@author: alexandre.wargnier and pialleport.lucas
"""
#importation des librairy nécéssaire :

import json, requests
from math import *

#----------------------

url = 'http://odata.bordeaux.fr/v1/databordeaux/defibrillateurs/?format=json' #téléchargement de la base de donnée
resp = requests.get(url, verify=True)
dico = resp.json()

def calculD(xa,ya):
    """
    Fonction qui calcule les distatances entre chaque défibrilateurs et l'utilisateur, puis les retournent sous forme de liste.
    argument : position xa et xb de l'utilisateur
    sortie : liste des distances qui sépare l'utilisateur des défibrilateur
    """

    for key in dico.keys():

        #Récuparation des x et y
        donnees = dico.get(key)
        xb = [] #Coordonnées X
        yb = [] #Coordonnées Y

        for i in range(len(donnees)): #Balayage des données du fichier JSON
            xb.append(donnees[i].get("x_long")) #Récupère tous les x (longitudes)
            yb.append(donnees[i].get("y_lat")) #Récupère tous les x (latitudes)

        #Calcul des distances
        calculDistance = []
        for i in range(len(donnees)):
            calculDistance.append(sqrt((xa-float(xb[i]))**2 + (ya-float(yb[i]))**2))

    return calculDistance


def bornesProches(calculDistance):
    """
    Fonction qui cherche le défibrilateurs le plus proche de l'utilisateur, puis les retournent sous forme de liste.
    argument : liste des distance de chaque defibrilauteur
    sortie : liste des défibrilateur les plus proche de l'utilisateur
    """

    dico = resp.json()

    #Adressage Dico

    for key in dico.keys():
        donnees = dico.get(key)

    listKey = []
    affUser = []

    for i in range(len(donnees)):
        dico[calculDistance[i]] = str(donnees[i].get("adresse"))

    listKey = calculDistance
    listKey.sort()

    for i in range(6):
        affUser.append(dico[listKey[i]])

    return affUser

affichage = [] #definition
affichage = bornesProches(calculD(float(input("Valeur de la longitude ?")),float(input("Valeur de la latitude ?"))))

print("Les défibrilateurs les plus proche de votre position sont les suivants : \n")

for i in range(len(affichage)):
    print(affichage[i])