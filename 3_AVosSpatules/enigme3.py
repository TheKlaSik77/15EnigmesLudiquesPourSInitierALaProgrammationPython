#Solution de l'énigme n 3 :

def estTrié(liste):

    for i in range (0,len(liste)-1):
        if (liste[i+1] < liste[i]):
            return False
        
    return True

"""
Retourne la pile de [0,indiceDernier] (indice dernier compris)
"""

def retournePile(liste,indiceDernier):
    partieAInverser = liste[0:indiceDernier+1]
    partieConstante = liste[indiceDernier+1:len(liste)]

    partieAInverser.reverse()

    return partieAInverser + partieConstante



def trierPileDeCrepe(pileDeCrepe):
    
    cpt = 0
    nbTraite = 0
    # On cherche le max dans la partie du haut non triée 
    while (estTrié(pileDeCrepe) != True):
        indiceMax = 0
        max = pileDeCrepe[0]
        
        for i in range (1,len(pileDeCrepe) - nbTraite):
            
            if pileDeCrepe[i] > max :
                max = pileDeCrepe[i]
                indiceMax = i
        #On retourne la pile pour mettre le max de la partie non triée en haut puis on la retourne pour la triée en dessous
        pileDeCrepe = retournePile(pileDeCrepe,indiceMax)
        pileDeCrepe = retournePile(pileDeCrepe,len(pileDeCrepe) - nbTraite - 1)
        nbTraite = nbTraite + 1
        

    return pileDeCrepe
            
pileDeCrepe = [1,4,7,5,1,2,4,7,4,6,9,8,55,1,47,74,1,2,5,44,22,14,12,11]
pileDeCrepe = trierPileDeCrepe(pileDeCrepe)
print(pileDeCrepe)
