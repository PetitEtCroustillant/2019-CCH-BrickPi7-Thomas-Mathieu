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
def select(listeQuestion, listePersonnages):
    try:
        cycleCount = 0
        oldValEncoder = -1
        time.sleep(0.02)
        valDépartEncoder = int(BP.get_motor_encoder(BP.PORT_A))
        while True:
            try:
                valEncoderRéelle = int(BP.get_motor_encoder(BP.PORT_A))
                
                while valDépartEncoder == valEncoderRéelle:
                    valEncoderRéelle = int(BP.get_motor_encoder(BP.PORT_A))
                    time.sleep(0.2)
                    if (BP.get_sensor(BP.PORT_4) == 1):
                        while (BP.get_sensor(BP.PORT_4) == 1):
                            time.sleep(0.02)
                        return final(listePersonnages)
                       
                    
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
                if cycleCount == 2:
                    tts.say("La question choisie est : " + questionChoisie)
                    print("La question choisie est : " + questionChoisie)
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
                    while (BP.get_sensor(BP.PORT_2) == 1):
                        time.sleep(0.02)
                    return False
                # Bouton Vrai
                elif (BP.get_sensor(BP.PORT_1) == 1):
                    while (BP.get_sensor(BP.PORT_1) == 1):
                        time.sleep(0.02)
                    return True
                
            except brickpi3.SensorError as error:
                print(error)
            
            time.sleep(0.02)

    except KeyboardInterrupt:
        BP.reset_all()

# Le robot pose des questions au joueur en fonction des réponses précédentes
def robotSelect(listeRéponse):
    try:
        questionChoisie = "Non fonctionnel"
        if not listeRéponse:
            questionChoisie = "homme"
        else:
            if listeRéponse[0]:
                # Hommes
                questionChoisie = "grande bouche"
                if 1 < len(listeRéponse):
                    if listeRéponse[1]:
                        questionChoisie = "gros nez"
                        if 2 < len(listeRéponse):
                            if listeRéponse[2]:
                                questionChoisie = "cheveux noirs"
                                if 3 < len(listeRéponse):
                                    if listeRéponse[3]:
                                        questionChoisie = "couvre-chef"
                            else:
                                questionChoisie = "moustache"
                                if 2 < len(listeRéponse):
                                    if not listeRéponse[2]:
                                        questionChoisie = "yeux brun"
                                        if 3 < len(listeRéponse):
                                            if listeRéponse[3]:
                                                questionChoisie = "couvre-chef"
                    else:
                        questionChoisie = "moustache"
                        if 2 < len(listeRéponse):
                            if listeRéponse[2]:
                                questionChoisie = "chauve"
                                if 3 < len(listeRéponse):
                                    if listeRéponse[3]:
                                        questionChoisie = "lunettes"
                                    else:
                                        questionChoisie = "yeux brun"
                            else:
                                questionChoisie = "chauve"
                                if 3 < len(listeRéponse):
                                    if listeRéponse[3]:
                                        questionChoisie = "yeux brun"
                                        if 4 < len(listeRéponse):
                                            if not listeRéponse[4]:
                                                questionChoisie = "barbe"
                                    else:
                                        questionChoisie = "lunettes"
                    
            else:
                # Femmes
                questionChoisie = "cheveux bruns"
                if 1 < len(listeRéponse):
                    if listeRéponse[1]:
                        questionChoisie = "couvre-chef"
                        if 2 < len(listeRéponse):
                            if not listeRéponse[2]:
                                questionChoisie = "peau noir"
                    else:
                        questionChoisie = "lunettes"
                        if 2 < len(listeRéponse):
                            if listeRéponse[2]:
                                questionChoisie = "grande bouche"
                                if 3 < len(listeRéponse):
                                    if not listeRéponse[3]:
                                        questionChoisie = "couvre-chef"
                            else:
                                questionChoisie = "yeux brun"
        
        switcher = {
        "homme": "Est-ce que votre personnage est un homme ?",
        "grande bouche": "Votre personnage a t'il une grande bouche ?",
        "yeux brun": "Votre personnage a t'il des yeux bruns ?",
        "moustache": "A t'il une moustache ?",
        "barbe": "A t'il une barbe ?",
        "chauve": "Est-ce que votre personnage est chauve ?",
        "cheveux noirs": "Ses cheveux sont-ils noirs ?",
        "cheveux blonds": "Ses cheveux sont-ils blonds ?",
        "cheveux bruns": "Ses cheveux sont-ils bruns ?",
        "peau noir": "Kanyé West ?",
        "lunettes": "Votre personnage a-t'il des lunettes ?",
        "couvre-chef": "Porte t'il un couvre-chef ?",
        "gros nez": "A-t'il un gros nez ?"
        }
        
        question = switcher.get(questionChoisie, "")
        
        tts.say(question)
        print(question)
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
            if valeurPerso == "Homme":
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

def final(listePersonnages):
    try:
        indexEnCours = 0
        tts.say(listePersonnages[indexEnCours].nom)
        while True:
            try:
                if (BP.get_sensor(BP.PORT_2) == 1):
                    while (BP.get_sensor(BP.PORT_2) == 1):
                        time.sleep(0.02)
                    if indexEnCours == len(listePersonnages) - 1:
                        indexEnCours = 0
                    else:
                        indexEnCours += 1
                    
                    tts.say(listePersonnages[indexEnCours].nom)
                    
                elif (BP.get_sensor(BP.PORT_1) == 1):
                    while (BP.get_sensor(BP.PORT_1) == 1):
                        time.sleep(0.02)
                    if indexEnCours == 0:
                        indexEnCours = len(listePersonnages) - 1
                    else:
                        indexEnCours -= 1
                    
                    tts.say(listePersonnages[indexEnCours].nom)
                
                if (BP.get_sensor(BP.PORT_4) == 1):
                    while (BP.get_sensor(BP.PORT_4) == 1):
                        time.sleep(0.02)
                    return listePersonnages[indexEnCours]
                
            except brickpi3.SensorError as error:
                print(error)
            
            time.sleep(0.02)

    except KeyboardInterrupt:
        BP.reset_all()