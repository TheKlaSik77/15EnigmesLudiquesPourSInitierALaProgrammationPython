# Code Enigme 1


def asciiToCaracter():
    
    fichier = open('Enigme1.txt','r')
    
    finalSentence = []
    for line in fichier:
        for word in line.split(' '):
            if (word != "\n"):
                finalSentence.append(chr(int(word)))
    
    return finalSentence



liste = asciiToCaracter()

for car in liste:
    print(car,end='')
    

"""
Chaque génération a son philosophe, écrivain ou artiste qui saisit et
incarne l'imaginaire du moment. Il arrive que ces philosophes soient
reconnus de leur vivant, mais le plus souvent il faut attendre que la
patine du temps fasse son effet. Que cette reconnaissance soit
immédiate ou différée, une époque est marquée par ces hommes qui
expriment leurs idéaux, dans les murmures d'un poème ou dans le
grondement d'un mouvement politique. Notre génération a un
philosophe. Ce n'est ni un artiste ni un écrivain. C'est un
informaticien.
"""
        