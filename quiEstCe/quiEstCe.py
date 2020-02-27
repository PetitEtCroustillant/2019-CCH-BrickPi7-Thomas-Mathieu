# Appel des fichiers
import character
import question
import chariot
import motors
import tts

import brickpi3
import time
import os
BP = brickpi3.BrickPi3()

def main():
    '''motors.stop(BP.PORT_B)
    motors.resetEncoder(BP.PORT_B)
    chariot.move(8)'''
    
    listePersos = character.createList()
    persoAléatoire = character.getRandom(listePersos)
    print(persoAléatoire)
    #motors.resetEncoder(BP.PORT_A)
    
    '''for personnage in listePersos :
      print(personnage)
      print("\n")'''
    
    listeQuestion = question.createList()
    questionChoisie = question.select(listeQuestion)
    print(questionChoisie)
    #questionChoisie = question.robotSelect(1)
    #réponse = question.answer()
    #if réponse:
    #    print("Vrai")
    #else:
    #    print("Faux")
        
    #questionChoisie = question.robotSelect(2, réponse)
    
    # Le robot pose des questions, on y répond jusqu'à ce qu'il ne reste un personnage.
    passe = 1
    réponse = None
    while True:
        questionChoisie = question.robotSelect(passe, réponse) # le robot choisi une question
        réponse = question.answer() # le joueur y répond
        listePersos = character.eliminate(listePersos, questionChoisie, réponse) # les personnages qui ne correspondent pas sont supprimés
        passe += 1
        if len(listePersos) == 1:
            return False
        #if question.final():
            #return False
    
    # On pose une question au robot, il répond selon les caractéristiques
    # du personnage tiré aléatoirement.
    '''questionChoisie = question.select(listeQuestion)
    réponseRobot = question.robotAnswer(persoAléatoire, questionChoisie)
    if réponseRobot:
        print("Vrai")
    else:
        print("Faux")'''
    
    '''for personnage in listePersos :
        print(personnage)
        print("\n")'''

main()
