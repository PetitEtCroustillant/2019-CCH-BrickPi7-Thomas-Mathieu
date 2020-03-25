#from espeak import espeak
import os

# Dit une chaine de caractères à haute voix
def say(text):
    fréquence = 100
    débitParole = 140
    
    os.system ('espeak -a ' + str(fréquence) + ' -v mb-fr1 -s ' + str(débitParole) + ' "' + text + '"')

# Pose des questions au joueur à haute voix
def sayQuestion(question):
    switcher = {
        "homme": "Est-ce que votre personnage est un homme ?",
        "grande bouche": "Votre personnage a t'il une grande bouche ?",
        "yeux brun": "Votre personnage a t'il des yeux brun ?",
        "moustache": "A t'il une moustache ?",
        "barbe": "A t'il une barbe ?",
        "chauve": "Est-ce que votre personnage est chauve ?",
        "cheveux noirs": "Ses cheveux sont-ils noirs ?",
        "cheveux blonds": "Ses cheveux sont-ils blonds ?",
        "cheveux brun": "Ses cheveux sont-ils brun ?",
        "peau noir": "Est-ce que votre personnage est noir ?",
        "lunettes": "Votre personnage a-t'il des lunettes ?",
        "couvre-chef": "Porte t'il un couvre-chef ?",
        "gros nez": "A-t'il un gros nez ?"
        }
        
    prononciationQuestion = switcher.get(question, "")
    
    say(prononciationQuestion)
    print(prononciationQuestion)

# Retourne un nom prononçable par le robot
def getPhonétiquePersonnage(personnage):
    switcher = {
        "Roger": "Roger",
        "Joe": "Djoe",
        "Hans": "Hantse",
        "Daniel": "Daniel",
        "Sarah": "Sarah",
        "Katrin": "Katrine",
        "Théo": "Théo",
        "Max": "Max",
        "Anne": "Anne",
        "Charles": "Charles",
        "Carmen": "Carmen",
        "Herman": "Hermanne",
        "Sophie": "Sophie",
        "Maria": "Maria",
        "Eric": "Eric",
        "Anita": "Anita",
        "Philippe": "Philippe",
        "Stephen": "Stephen",
        "Lucas": "Lucas",
        "Bernard": "Bernard",
        "Isabelle": "Isabelle",
        "Victor": "Victor",
        "Frank": "Franque",
        "Paul": "Paul"
        }
    
    return switcher.get(personnage.nom, "")
