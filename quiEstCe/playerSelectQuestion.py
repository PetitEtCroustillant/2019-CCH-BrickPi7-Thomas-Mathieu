import time
import brickpi3
import tts
import motors

BP = brickpi3.BrickPi3()

BP.set_sensor_type(BP.PORT_1, BP.SENSOR_TYPE.TOUCH)

## Utilise la valeur de l'encoder pour sélectionner une question dans la liste
def selectQuestion(listeQuestion):
    try:
        cycleCount = 0
        oldValEncoder = -1
        motors.zero()
        while True:
            try:
                # Valeur entre 1 et 14
                valEncoder = int(BP.get_motor_encoder(BP.PORT_A) / 25.7)
                
                #print(valEncoder)
                
                # Prend une questions dans la liste
                if valEncoder < 14.0:
                    questionChoisie = listeQuestion[int(valEncoder)]
                
                time.sleep(0.5)
                
                if oldValEncoder == valEncoder:
                    cycleCount += 1
                else:
                    cycleCount = 0
                    oldValEncoder = valEncoder
                
                # Choisi une question au bout de 3 sec d'inactivité
                if cycleCount == 6:
                    tts.say("La question choisie est: " + questionChoisie)
                    print("La question choisie est: " + questionChoisie)
                    motors.zero()
                    return questionChoisie
        
            except IOError as error:
                print(error)
        
    except KeyboardInterrupt:
        BP.reset_all()
    
