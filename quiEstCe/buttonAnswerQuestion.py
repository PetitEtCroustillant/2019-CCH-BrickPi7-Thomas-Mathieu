import time
import brickpi3

BP = brickpi3.BrickPi3()
BP.set_sensor_type(BP.PORT_3, BP.SENSOR_TYPE.TOUCH) # Bouton Faux
BP.set_sensor_type(BP.PORT_4, BP.SENSOR_TYPE.TOUCH) # Bouton Vrai

def answerQuestion():
    try:
        while True:
            try:
                if (BP.get_sensor(BP.PORT_3) == 1):
                    return False
                elif (BP.get_sensor(BP.PORT_4) == 1):
                    return True
                
            except brickpi3.SensorError as error:
                print(error)
            
            time.sleep(0.02)

    except KeyboardInterrupt:
        BP.reset_all()

