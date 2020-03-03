# Appel des fichiers
import character
import question
import chariot
import motors
import tts

from enum import Enum
import brickpi3
import time
BP = brickpi3.BrickPi3()

BP.set_sensor_type(BP.PORT_2, BP.SENSOR_TYPE.TOUCH) # Bouton Droite
BP.set_sensor_type(BP.PORT_1, BP.SENSOR_TYPE.TOUCH) # Bouton Gauche

class ModeJeu(Enum):
    MODE_SIMPLE = 1
    MODE_DUR = 2

def main():
    modeJeu = débutJeu()
    
    while True:
        '''motors.stop(BP.PORT_B)
        motors.resetEncoder(BP.PORT_B)
        motors.resetEncoder(BP.PORT_A)'''
        motors.goToZero(BP.PORT_A)
    
        if modeJeu == ModeJeu.MODE_SIMPLE:
            listeQuestionsRobot = question.createList()
        else:
            listeRéponse: [bool] = []
        
        # Création des deux listes de personnages
        listePersosRobot = character.createList()
        listePersosJoueur = character.createList()
        
        # Création de la liste de questions
        listeQuestion = question.createList()
        
        # Le robot choisi un personnage
        persoSecretRobot = character.getRandom(listePersosRobot)
        print(persoSecretRobot)
        
        # Le robot pose des questions, on y répond jusqu'à ce qu'il ne reste un personnage.
        while True:
            # Tour du joueur
            # On pose une question au robot, il répond selon les caractéristiques du personnage tiré aléatoirement.
            tts.say("C'est à votre tour !")
            print("\nTour joueur\n")
            time.sleep(0.2)
            questionChoisieJoueur = question.selectOrGuess(listeQuestion, listePersosJoueur)
            if type(questionChoisieJoueur) is character.Personnage:
                if character.checkSelected(persoSecretRobot, questionChoisieJoueur):
                    print("Vous avez gagné !")
                    tts.say("Vous avez gagné !")
                    break
                else:
                    listePersosJoueur.remove(questionChoisieJoueur)
                    print("Désolé " + questionChoisieJoueur.nom + " n'est pas mon personnage")
                    tts.say("Désolé " + tts.getPhonétiquePersonnage(questionChoisieJoueur) + " n'est pas mon personnage")
            else:
                réponseRobot = question.robotAnswer(persoSecretRobot, questionChoisieJoueur)
                if réponseRobot:
                    print("La réponse a votre question est : Vrai")
                    tts.say("La réponse a votre question est : Vrai")
                else:
                    print("La réponse a votre question est : Faux")
                    tts.say("La réponse a votre question est : Faux")
                listePersosJoueur = character.eliminate(listePersosJoueur, questionChoisieJoueur, réponseRobot) 
            if len(listePersosJoueur) == 1:
                print("Mon personnage est : " + listePersosJoueur[0].nom + ", vous avez gagné !")
                tts.say("Mon personnage est : " + tts.getPhonétiquePersonnage(listePersosJoueur[0]) + ", vous avez gagné !")
                break
            
            time.sleep(len(listePersosJoueur) / 6)
            
            # Tour du robot
            tts.say("C'est à mon tour !")
            print("\nTour Robot\n")
            time.sleep(0.2)
            
            # le robot choisi une question en fonction du mode de difficulté
            if modeJeu == ModeJeu.MODE_SIMPLE:
                questionChoisieRobot = question.robotSelectEasy(listeQuestionsRobot)
            else:
                questionChoisieRobot = question.robotSelectHard(listeRéponse)
            
            # le joueur y répond
            réponse = question.answer()
            
            if modeJeu == ModeJeu.MODE_DUR:
                listeRéponse.append(réponse)
                
            listePersosRobot = character.eliminate(listePersosRobot, questionChoisieRobot, réponse) # les personnages qui ne correspondent pas sont supprimés
            if len(listePersosRobot) == 1:
                print("Votre personnage est : " + listePersosRobot[0].nom + ", j'ai gagné !")
                tts.say("Votre personnage est : " + tts.getPhonétiquePersonnage(listePersosRobot[0]) + ", j'ai gagné !")
                break
        
        # Choix de rejouer (m]ême paramètres) ou d'aller au menu
        tts.say("Voulez-vous rejouer ?")
        if choixFinPartie():
            continue
        else:
            main()
    
def choixModeJeu():
    try:
        while True:
            try:
                # Bouton Difficile
                if (BP.get_sensor(BP.PORT_2) == 1):
                    while (BP.get_sensor(BP.PORT_2) == 1):
                        time.sleep(0.02)
                    tts.say("Mode dur sélectionné")
                    return ModeJeu.MODE_DUR
                # Bouton Facile
                elif (BP.get_sensor(BP.PORT_1) == 1):
                    while (BP.get_sensor(BP.PORT_1) == 1):
                        time.sleep(0.02)
                    tts.say("Mode facile sélectionné")
                    return ModeJeu.MODE_SIMPLE
                
            except brickpi3.SensorError as error:
                print(error)
            
            time.sleep(0.02)

    except KeyboardInterrupt:
        BP.reset_all()

def choixFinPartie():
    try:
        while True:
            try:
                # Bouton Arrêter
                if (BP.get_sensor(BP.PORT_2) == 1):
                    while (BP.get_sensor(BP.PORT_2) == 1):
                        time.sleep(0.02)
                    return False
                # Bouton Rejouer
                elif (BP.get_sensor(BP.PORT_1) == 1):
                    while (BP.get_sensor(BP.PORT_1) == 1):
                        time.sleep(0.02)
                    return True
                
            except brickpi3.SensorError as error:
                print(error)
            
            time.sleep(0.02)

    except KeyboardInterrupt:
        BP.reset_all()

def débutJeu():
    tts.say("Bienvenu dans Qui est-ce ? choisissez votre mode de jeu.")
    modeJeu = choixModeJeu()
    return modeJeu

def test():
    '''listeQuestion = question.createList()
    for questions in listeQuestion:
        tts.sayQuestion(questions)
        time.sleep(1)'''
    #tts.say("bip bloup je suis le robot")
    
while True:
    tts.say("nigga nigga nigga nigga nigga nigga nigga nigga nigga nigga nigga nigga nigga nigga nigga nigga ")
#main()
#test()