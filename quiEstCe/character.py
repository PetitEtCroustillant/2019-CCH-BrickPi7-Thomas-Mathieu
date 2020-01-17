from dataclasses import dataclass
from random import randrange
from enum import Enum

class Sexe(Enum):
    Homme = 1
    Femme = 2
     
class Cheveux(Enum):
    Brun = 1
    Noir = 2
    Blond = 3
    Autre = 4

@dataclass
class Coordonnées:
    x: float
    y: float

@dataclass
class Personnage:
    nom: str
    sexe: Sexe
    cheveux: Cheveux
    yeuxBruns: bool
    grandeBouche: bool
    chauve: bool
    moustache: bool
    barbe: bool
    peauNoire: bool
    couvreChef: bool
    lunettes: bool
    grosNez: bool
    coordonnées: Coordonnées

# Crée une liste de personnages
def createList():
    # Nom, Sexe, Cheveux, Yeux bruns, Grande bouche, chauve, moustache, barbe, peau noir, couvre chef, lunettes, gros nez

    #personnages première ligne
    roger = Personnage("Roger", "Homme", "Brun", True, False, True, True, True, True, False, False, False, Coordonnées(1,1))
    joe = Personnage("Joe", "Homme", "Blond", False, True, False, False, False, False, False, False, False, Coordonnées(1,2))
    hans = Personnage("Hans", "Homme", "Blond", True, True, False, True, False, False, False, False, False, Coordonnées(1,3))
    daniel = Personnage("Daniel", "Homme", "Noir", False, False, True, False, False, False, False, True, False, Coordonnées(1,4))
    sarah = Personnage("Sarah", "Femme", "Blond", True, False, False, False, False, False, True, True, False, Coordonnées(1,5))
    katrin = Personnage("Katrin", "Femme", "Brun", True, False, False, False, False, False, False, False, False, Coordonnées(1,6))
    théo = Personnage("Théo", "Homme", "Noir", True, True, False, True, False, False, False, False, True, Coordonnées(1,7))
    max = Personnage("Max", "Homme", "Noir", True, True, False, False, True, True, False, False, False, Coordonnées(1,8))

    #personnages deuxième ligne
    anne = Personnage("Anne", "Femme", "Autre", False, False, False, False, False, False, False, True, False, Coordonnées(2,1))
    charles = Personnage("Charles", "Homme", "Autre", True, False, True, True, False, False, False, True, True, Coordonnées(2,2))
    carmen = Personnage("Carmen", "Femme", "Brun", True, False, False, False, False, True, False, False, False, Coordonnées(2,3))
    herman = Personnage("Herman", "Homme", "Autre", True, False, True, False, False, False, False, False, True, Coordonnées(2,4))
    sophie = Personnage("Sophie", "Femme", "Noir", True, True, False, False, False, True, False, True, True, Coordonnées(2,5))
    maria = Personnage("Maria", "Femme", "Brun", True, False, False, False, False, False, True, False, False, Coordonnées(2,6))
    eric = Personnage("Eric", "Homme", "Blond", True, True, False, False, False, False, True, False, False, Coordonnées(2,7))
    anita = Personnage("Anita", "Femme", "Blond", False, False, False, False, False, False, False, False, False, Coordonnées(2,8))

    #personnages troisième ligne
    philippe = Personnage("Philippe", "Homme", "Autre", True, False, True, False, True, False, False, False, False, Coordonnées(3,1))
    stephen = Personnage("Stephen", "Homme", "Autre", False, False, False, True, False, False, False, False, False, Coordonnées(3,2))
    lucas = Personnage("Lucas", "Homme", "Blond", True, False, False, True, True, False, False, False, False, Coordonnées(3,3))
    bernard = Personnage("Bernard", "Homme", "Brun", True, False, False, False, False, True, True, False, True, Coordonnées(3,4))
    isabelle = Personnage("Isabelle", "Femme", "Autre", True, False, False, False, False, False, False, False, False, Coordonnées(3,5))
    victor = Personnage("Victor", "Homme", "Autre", True, True, False, False, False, False, False, False, True, Coordonnées(3,6))
    frank = Personnage("Frank", "Homme", "Noir", True, True, False, False, False, False, True, False, True, Coordonnées(3,7))
    paul = Personnage("Paul", "Homme", "Autre", True, False, False, False, True, False, False, True, False, Coordonnées(3,8))

    liste_personnage = [roger, joe, hans, daniel, sarah, katrin, théo, max, anne, charles, carmen, herman, sophie, maria, eric, anita, philippe,
                        stephen, lucas, bernard, isabelle, victor, frank, paul]
    return liste_personnage


# Tire un personnage au sort dans une liste passé en paramètre
# Retourne le personnage tiré
def getRandom(listePersonnages):
    characterIndex = randrange(len(listePersonnages))
    return listePersonnages[characterIndex]


# Supprime des personnages de la liste
def eliminate(listePersonnage, question, réponse):
    switcher = {
        "homme": "sexe",
        "grande bouche": "grandeBouche",
        "yeux brun": "yeuxBruns",
        "moustache": "moustache",
        "barbe": "barbe",
        "chauve": "chauve",
        "cheveux noirs": "cheveux",
        "cheveux blonds": "cheveux",
        "cheveux bruns": "cheveux",
        "peau noir": "peauNoire",
        "lunettes": "lunettes",
        "couvre-chef": "couvreChef",
        "gros nez": "grosNez"
    }
    
    caractéristique = switcher.get(question, "")
    listePersoSupprimés = []
    if not caractéristique == "":
        for personnage in listePersonnage:
            valeurPerso = getattr(personnage, caractéristique)
            
            if type(valeurPerso) == bool:
                if valeurPerso != réponse:
                    print(personnage.nom + " supprimé")
                    listePersoSupprimés.append(personnage)
            if type(valeurPerso) == str:
                if caractéristique == "sexe":
                    réponseSexe = ""
                    if réponse:
                        réponseSexe = "Homme"
                    else:
                        réponseSexe = "Femme"
                        
                    if valeurPerso != réponseSexe:
                        print(personnage.nom + " supprimé")
                        listePersoSupprimés.append(personnage)
                        
                if caractéristique == "cheveux":
                    réponseCheveux = ""
                    supprimerPerso = False
                    if question == "cheveux noirs":
                        réponseCheveux = "Noir"
                        if not réponse:
                            supprimerPerso = True
                    elif question == "cheveux blonds":
                        réponseCheveux = "Blond"
                        if not réponse:
                            supprimerPerso = True
                    elif question == "cheveux bruns":
                        réponseCheveux = "Brun"
                        if not réponse:
                            supprimerPerso = True
                    else:
                        réponseCheveux = "Autre"
                    
                    if supprimerPerso:
                        if valeurPerso == réponseCheveux:
                            print(personnage.nom + " supprimé")
                            listePersoSupprimés.append(personnage)
                    else:
                        if valeurPerso != réponseCheveux:
                            print(personnage.nom + " supprimé")
                            listePersoSupprimés.append(personnage)
                
        for personnage in listePersoSupprimés:
            listePersonnage.remove(personnage)
    return listePersonnage
    #return None
