import time
import brickpi3
import tts
import motors
import random

BP = brickpi3.BrickPi3()

BP.set_sensor_type(BP.PORT_4, BP.SENSOR_TYPE.TOUCH) # Bouton Stop
BP.set_sensor_type(BP.PORT_2, BP.SENSOR_TYPE.TOUCH) # Bouton Faux
BP.set_sensor_type(BP.PORT_1, BP.SENSOR_TYPE.TOUCH) # Bouton Vrai

# Génère une liste de questions
def createList():
    départ = ""
    homme = "homme"
    grandeBouche = "grande bouche"
    yeuxBruns = "yeux brun"
    moustache = "moustache"
    barbe = "barbe"
    chauve = "chauve"
    cheveuxNoirs = "cheveux noirs"
    cheveuxBlonds = "cheveux blonds"
    cheveuxBruns = "cheveux bruns"
    peauNoir = "peau noir"
    lunettes = "lunettes"
    couvreChef = "couvre-chef"
    grosNez = "gros nez"
    
    
    liste_questions = [homme, grandeBouche, yeuxBruns, moustache, barbe, chauve, cheveuxNoirs,
                       cheveuxBlonds, cheveuxBruns, peauNoir, lunettes, couvreChef, grosNez, départ]
    
    return liste_questions

# Utilise la valeur de l'encoder pour sélectionner une question dans la liste
def select(listeQuestion):
    try:
        cycleCount = 0
        oldValEncoder = -1
        motors.zero(BP.PORT_A)
        while True:
            try:
                # Valeur entre 1 et 14
                valEncoder = int(BP.get_motor_encoder(BP.PORT_A) / (360 / len(listeQuestion)))
                
                # Prend une questions dans la liste
                if valEncoder < 14.0:
                    questionChoisie = listeQuestion[int(valEncoder)]
                
                time.sleep(0.5)
                
                if oldValEncoder == valEncoder:
                    cycleCount += 1
                else:
                    cycleCount = 0
                    oldValEncoder = valEncoder
                
                # Retourne la question au bout de 3 sec d'inactivité
                if cycleCount == 6:
                    tts.say("La question choisie est: " + questionChoisie)
                    #print("La question choisie est: " + questionChoisie)
                    motors.zero(BP.PORT_A)
                    return questionChoisie
        
            except IOError as error:
                print(error)
        
    except KeyboardInterrupt:
        BP.reset_all()


# Retourne true ou false selon le bouton appuyé
def answer():
    try:
        while True:
            try:
                # Bouton Faux
                if (BP.get_sensor(BP.PORT_2) == 1):
                    return False
                # Bouton Vrai
                elif (BP.get_sensor(BP.PORT_1) == 1):
                    return True
                
            except brickpi3.SensorError as error:
                print(error)
            
            time.sleep(0.02)

    except KeyboardInterrupt:
        BP.reset_all()

#
def robotSelect(passe, réponse = True):
    try:
        questionChoisie = "Non fonctionnel"
        if réponse == None:
            questionChoisie = "homme"
        elif passe >= 2:
            if réponse:
                # Hommes
                questionChoisie = "grande bouche"
                if passe >= 3:
                    if réponse:
                        questionChoisie = "gros nez"
                    else:
                        questionChoisie = "moustache"
            else:
                # Femmes
                questionChoisie = "cheveux bruns"
        # 5 passes max pour les femmes
        # 6 passes maxpour les hommes
        
        
        #tts.say("La question choisie est: " + questionChoisie)
        print("Je choisi la question : " + questionChoisie)
        return questionChoisie
        
    except KeyboardInterrupt:
        BP.reset_all()


# Le robot compare les charactéristiques du personnage choisi
# et la question sélectionnée pour répondre à la question,
def robotAnswer(personnage, question):
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
    if not caractéristique == "":
        valeurPerso = getattr(personnage, caractéristique)
        if type(valeurPerso) == bool:
            if valeurPerso:
                return True
            else:
                return False
    
        if caractéristique == "sexe":
            if valeurPerso == "homme":
                return True
            else:
                return False
        
        if caractéristique == "cheveux":
            if question == "cheveux noirs":
                if valeurPerso == "Noir":
                    return True
                else:
                    return False
            
            if question == "cheveux bruns":
                if valeurPerso == "Brun":
                    return True
                else:
                    return False
            
            if question == "cheveux blonds":
                if valeurPerso == "Blond":
                    return True
                else:
                    return False
        '''if caractéristique == "cheveux":
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
                        listePersoSupprimés.append(personnage)'''

def final():
    try:
        while True:
            try:
                # Bouton Stop
                if (BP.get_sensor(BP.PORT_4) == 1):
                    return True
                
            except brickpi3.SensorError as error:
                print(error)
            
            time.sleep(0.02)

    except KeyboardInterrupt:
        BP.reset_all()