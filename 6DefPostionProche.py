# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 09:17:21 2020

@author: alexandre.wargnier/lucas.pialleport
"""

import json, requests
from math import *

url = 'http://odata.bordeaux.fr/v1/databordeaux/defibrillateurs/?format=json'
resp = requests.get(url, verify=True)
dico = resp.json()

xa = float(input("Valeur de la longitude ?"))
ya = float(input("Valeur de la latitude ?"))

#BOUCLE GENERALE
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

    #Adressage Dico
    dico = {}
    listKey = []
    for i in range(len(donnees)):
        dico[calculDistance[i]] = str(donnees[i].get("adresse"))

    listKey = calculDistance
    listKey.sort()

    print("Les défibrilateurs les plus proche de votre position sont les suivants : ")
    print("")
    for i in range(6):
        print("-",dico[listKey[i]])