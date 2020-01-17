#from espeak import espeak
import os

def say(text):
    fréquence = 100
    débitParole = 140
    
    os.system ('espeak -a ' + str(fréquence) + ' -v mb-fr1 -s ' + str(débitParole) + ' "' + text + '"')