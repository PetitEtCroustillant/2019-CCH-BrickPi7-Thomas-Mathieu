from dataclasses import dataclass
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

def createList():
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

