#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 00:49:22 2023

@author: kylian
"""
import random
import math

def renvoyerMots(mot1, mot2, mot3, res):
    fichier = open('Enigme2.txt', 'r')
    mot1Liste = []
    mot2Liste = []
    mot3Liste = []
    resListe = []
    cpt = 1
    nbLignes = len(fichier.readlines())
    fichier.seek(0)
    car = fichier.read(1)
    print(car)
    while car:
        if car == '\n':
            cpt += 1
        if 'A' <= car <= 'Z':
            if cpt == 1:
                mot1Liste.append(car)
            elif cpt == 2:
                mot2Liste.append(car)
            elif cpt == 4 and nbLignes == 4:
                resListe.append(car)
            elif cpt == 3 and nbLignes == 5:
                mot3Liste.append(car)
            elif cpt == 5 and nbLignes == 5:
                resListe.append(car)
        car = fichier.read(1)

    mot1 = ''.join(mot1Liste)
    mot2 = ''.join(mot2Liste)
    mot3 = ''.join(mot3Liste)
    res = ''.join(resListe)

    return mot1,mot2,mot3,res

def convertirMotsEtTestResultats(mot1,mot2,mot3,res,dictValeurs):

    if mot3 == "":
        valeurMot1 = []
        valeurMot2 = []
        valeurRes = []
        nb1 = 0
        nb2 = 0
        nbRes = 0
        for c in mot1:
            valeurMot1.append(dictValeurs[c])
        for c in mot2:
            valeurMot2.append(dictValeurs[c])
        for c in res:
            valeurRes.append(dictValeurs[c])
        i = len(mot1) - 1
        puissance = 0
        while i >= 0:
            nb1 += valeurMot1[i] * math.pow(10,puissance)
            puissance += 1
            i -= 1

        i = len(mot2) - 1
        puissance = 0
        while i >= 0:
            nb2 += valeurMot2[i] * math.pow(10,puissance)
            puissance += 1
            i -= 1

        i = len(res) - 1
        puissance = 0
        while i >= 0:
            nbRes += valeurRes[i] * math.pow(10,puissance)
            puissance += 1
            i -= 1

        if (int(nb1)+int(nb2)) == int(nbRes):

            return True
        else :
            print("mauvais résultat")
            return False


    else:
        valeurMot1 = []
        valeurMot2 = []
        valeurMot3 = []
        valeurRes = []
        nb1 = 0
        nb2 = 0
        nb3 = 0
        nbRes = 0
        for c in mot1:
            valeurMot1.append(dictValeurs[c])
        for c in mot2:
            valeurMot2.append(dictValeurs[c])
        for c in mot3:
            valeurMot3.append(dictValeurs[c])
        for c in res:
            valeurRes.append(dictValeurs[c])

        i = len(mot1) - 1
        puissance = 0
        while i >= 0:
            nb1 += valeurMot1[i] * math.pow(10,puissance)
            puissance += 1
            i -= 1

        i = len(mot2) - 1
        puissance = 0
        while i >= 0:
            nb2 += valeurMot2[i] * math.pow(10,puissance)
            puissance += 1
            i -= 1

        i = len(mot3) - 1

        puissance = 0
        while i >= 0:
            nb3 += valeurMot3[i] * math.pow(10,puissance)
            puissance += 1
            i -= 1

        i = len(res) - 1
        puissance = 0
        while i >= 0:
            nbRes += valeurRes[i] * math.pow(10,puissance)
            puissance += 1
            i -= 1

        if (int(nb1)+int(nb2)+int(nb3)) == int(nbRes):

            return True
        else :
            print("mauvais résultat")
            return False



def trouverCleMots(mot1, mot2, mot3, res):

    dictValeurs = dict()
    resCorrect = False
    if mot3 == "":
        listeMots = [mot1,mot2,res]
    else:
        listeMots = [mot1,mot2,mot3,res]

    while not resCorrect:
        dictValeurs.clear()
        for mot in listeMots:
            for index in range(0,len(mot)):
                if mot[index] not in dictValeurs.keys():
                    if index == 0:
                        nbAleatoire = random.randint(1,9)
                        while nbAleatoire in dictValeurs.values():
                            nbAleatoire = random.randint(1,9)
                        dictValeurs[mot[index]] = nbAleatoire
                    else:
                        nbAleatoire = random.randint(0,9)

                        while nbAleatoire in dictValeurs.values():
                            nbAleatoire = random.randint(1,9)

                        dictValeurs[mot[index]] = nbAleatoire
        print(dictValeurs)
        resCorrect = convertirMotsEtTestResultats(mot1,mot2,mot3,res,dictValeurs)

    print("-------------------------")
    print("Le bon résultat a été trouvé et il s'agit du dictionnaire suivant : ")
    print(dictValeurs)
    print("-------------------------")

mot1 = ""
mot2 = ""
mot3 = ""
res = ""

mot1,mot2,mot3,res = renvoyerMots(mot1,mot2,mot3,res)
trouverCleMots(mot1,mot2, mot3, res)