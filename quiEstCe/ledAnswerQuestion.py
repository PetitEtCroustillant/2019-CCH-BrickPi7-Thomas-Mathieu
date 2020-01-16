# ALlume une led rouge si la réponse à une question est fausse,
# allume une led bleue si la réponse est vrai
from grovepi import *

ledRouge = 7
ledBleue = 8

pinMode(ledRouge,"OUTPUT")
pinMode(ledBleue,"OUTPUT")

def answerQuestion(réponse):
    
    if réponse == True:
        digitalWrite(ledBleue, 1)
    else:
        digitalWrite(ledRouge, 1)
        
    time.sleep(5)
    digitalWrite(ledBleue, 0)
    digitalWrite(ledRouge, 0)
        
        
