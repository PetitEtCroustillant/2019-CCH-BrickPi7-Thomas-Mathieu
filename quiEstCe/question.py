import time
import brickpi3
import tts
import motors


BP = brickpi3.BrickPi3()

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


