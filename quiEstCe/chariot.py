# Déplace le chariot entre les emplacements 0 et 8
import time     # import the time library for the sleep function
import brickpi3 # import the BrickPi3 drivers

BP = brickpi3.BrickPi3() # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.

BP.set_sensor_type(BP.PORT_1, BP.SENSOR_TYPE.TOUCH)

def move(nColonne): # nColonne
    while True:
        valEncoder = int((BP.get_motor_encoder(BP.PORT_B) / 440))
        speed = 50
        
        if valEncoder == nColonne:
            BP.set_motor_power(BP.PORT_B, 0)
            break
        #elif valEncoder > nColonne:
            #speed *= -1
      
        BP.set_motor_power(BP.PORT_B, speed)

