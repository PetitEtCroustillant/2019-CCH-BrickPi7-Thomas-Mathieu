# Appel des fichiers
import createCharacterList as CCL
import createQuestionList as Questions
import eliminateCharacter as EC
import getRandomCharacter as GRC
import ledAnswerQuestion as LAQ
import buttonAnswerQuestion as BAQ
import playerSelectQuestion as PSQ
import motors
import tts

def main():    

    #listePerso = CCL.createList()

    #perso = GRC.getCharacter(listePerso)
    #print(perso)

    #if (BAQ.answerQuestion() == True):
     #   LAQ.answerQuestion(True)
    #elif (BAQ.answerQuestion() == False):
     #   LAQ.answerQuestion(False)
    #for personnage in liste :
      #print(personnage)
      #print("\n")
    
    listeQuestion = Questions.createList()
    questionChoisie = PSQ.selectQuestion(listeQuestion)
    print(questionChoisie)

main()
