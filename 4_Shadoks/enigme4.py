# GA = 0 , BU = 1 , ZO = 2 , MEU = 3
"""
Les nombres s'écriraient en puissance de 4 soit des nombres en base 4
"""


def convertisseurShadoks(nomFichier):
    nombreShadoks = []
    with open(nomFichier, "r") as fichier:
        for ligne in fichier:
            nombreShadoks = ligne.split(" ")

    somme = 0
    for i in range(0, len(nombreShadoks)):
        if nombreShadoks[i] == "GA":
            mult = 0
        elif nombreShadoks[i] == "BU":
            mult = 1
        elif nombreShadoks[i] == "ZO":
            mult = 2
        elif nombreShadoks[i] == "MEU":
            mult = 3
        else:
            print("Erreur!")
            exit(1)

        somme = somme + mult * pow(4, len(nombreShadoks) - i - 1)

    return somme


print(convertisseurShadoks("Enigme4.txt"))
