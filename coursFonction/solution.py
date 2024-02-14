def trouvePomme(fruits):
    for i in range(len(fruits)):
        if fruits[i] == 'pomme':
            print(fruits[i])
            return i
    return 'pas de pomme'

#TODO compte les pommes
def compteLesPommes(fruits):
    compteur = 0
    for i in range(len(fruits)):
        if fruits[i] == 'pomme':
            compteur += 1
    return compteur

def remplacePommeParPoire(liste):
    for i in range(len(liste)):
        if liste[i] == "pomme":
            liste[i] = "poire"

liste = [ "cerise", "olive", 'pomme', "tomate", "pomme"]
print(trouvePomme(liste))
remplacePommeParPoire(liste)
print(liste)

    