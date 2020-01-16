from random import randrange

# Tire un personnage au sort dans une liste passé en paramètre
# Retourne le personnage tiré
def getCharacter(listePersonnages):
    characterIndex = randrange(24)
    return listePersonnages[characterIndex]