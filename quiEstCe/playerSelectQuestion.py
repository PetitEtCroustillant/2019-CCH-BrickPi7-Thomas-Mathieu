import time
import brickpi3
import tts
import motors
import buttonAnswerQuestion as BAQ

BP = brickpi3.BrickPi3()

BP.set_sensor_type(BP.PORT_1, BP.SENSOR_TYPE.TOUCH)

def selectQuestion(listeQuestion):
    try:
        value = 0
        motors.zero()
        while True:
            BP.set_motor_power(BP.PORT_A, 0)
        
            valEncoder = BP.get_motor_encoder(BP.PORT_A) / 25.7
            print(valEncoder)
            print("Encoder A: %6d" % BP.get_motor_encoder(BP.PORT_A))
            time.sleep(0.02)
            questionChoisie = ""
            
            if (valEncoder < 14):
                questionChoisie = listeQuestion[int(valEncoder)]
            
            if BAQ.answerQuestion():
                break
        
        print("Fin de la boucle")
        tts.say("La question choisie est: " + questionChoisie + ". Est-ce que vous confirmez ?")
        if BAQ.answerQuestion():
            motors.zero()
            return questionChoisie
        
    except KeyboardInterrupt:
        BP.reset_all()
    
