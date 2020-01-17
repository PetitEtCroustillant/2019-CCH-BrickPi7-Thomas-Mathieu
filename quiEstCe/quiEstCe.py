# Appel des fichiers
import character
import question
import chariot
import motors
import tts

import brickpi3
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
    #questionChoisie = question.select(listeQuestion)
    #print(questionChoisie)
    questionChoisie = question.robotSelect(1)
    réponse = question.answer()
    if réponse:
        print("Vrai")
    else:
        print("Faux")
        
    questionChoisie = question.robotSelect(2, réponse)
    
    '''réponseRobot = question.robotAnswer(persoAléatoire, questionChoisie)
    if réponseRobot:
        print("Vrai")
    else:
        print("Faux")'''
    
    
    
    #listePersos = character.eliminate(listePersos, questionChoisie, réponse)
    '''for personnage in listePersos :
        print(personnage)
        print("\n")'''

main()
