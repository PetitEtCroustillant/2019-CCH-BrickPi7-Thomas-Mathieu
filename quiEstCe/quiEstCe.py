# Appel des fichiers
import character
import question
import chariot
import motors
import tts

import brickpi3
from grove_rgb_lcd import *
import time
BP = brickpi3.BrickPi3()

def main():
    '''motors.stop(BP.PORT_B)
    motors.resetEncoder(BP.PORT_B)
    motors.resetEncoder(BP.PORT_A)'''
    motors.zero(BP.PORT_A)
    
    # Création des deux listes de personnages
    listePersosRobot = character.createList()
    listePersosJoueur = character.createList()
    
    # Création de la liste de questions
    listeQuestion = question.createList()
    
    # Le robot choisi un personnage
    persoAléatoire = character.getRandom(listePersosRobot)
    setText("Mon personnage\nest : " + persoAléatoire.nom)
    setRGB(0,64,128)
    print(persoAléatoire)
    
    # Le robot pose des questions, on y répond jusqu'à ce qu'il ne reste un personnage.
    listeRéponse: List[bool] = []
    while True:
        # Tour du joueur
        # On pose une question au robot, il répond selon les caractéristiques du personnage tiré aléatoirement.
        tts.say("C'est à votre tour !")
        print("\nTour joueur\n")
        time.sleep(0.2)
        questionChoisieJoueur = question.select(listeQuestion, listePersosJoueur)
        if type(questionChoisieJoueur) is character.Personnage:
            if character.checkSelected(persoAléatoire, questionChoisieJoueur):
                print("Vous avez gagné !")
                tts.say("Vous avez gagné !")
                break
            else:
                listePersosJoueur.remove(questionChoisieJoueur)
                print("Désolé " + questionChoisieJoueur.nom + " n'est pas mon personnage")
                tts.say("Désolé " + questionChoisieJoueur.nom + " n'est pas mon personnage")
        else:
            réponseRobot = question.robotAnswer(persoAléatoire, questionChoisieJoueur)
            if réponseRobot:
                print("La réponse a votre question est : Vrai")
                tts.say("La réponse a votre question est : Vrai")
            else:
                print("La réponse a votre question est : Faux")
                tts.say("La réponse a votre question est : Faux")
            listePersosJoueur = character.eliminate(listePersosJoueur, questionChoisieJoueur, réponseRobot) 
        if len(listePersosJoueur) == 1:
            print("Mon personnage est : " + listePersosJoueur[0].nom + ", vous avez gagné !")
            tts.say("Mon personnage est : " + listePersosJoueur[0].nom + ", vous avez gagné !")
            break
        
        time.sleep(len(listePersosJoueur) / 6)
        
        # Tour du robot
        tts.say("C'est à mon tour !")
        print("\nTour Robot\n")
        time.sleep(0.2)
        questionChoisieRobot = question.robotSelect(listeRéponse) # le robot choisi une question
        listeRéponse.append(question.answer()) # le joueur y répond
        listePersosRobot = character.eliminate(listePersosRobot, questionChoisieRobot, listeRéponse[-1]) # les personnages qui ne correspondent pas sont supprimés
        if len(listePersosRobot) == 1:
            print("Votre personnage est : " + listePersosRobot[0].nom + ", j'ai gagné !")
            tts.say("Votre personnage est : " + listePersosRobot[0].nom + ", j'ai gagné !")
            break
    
main()
