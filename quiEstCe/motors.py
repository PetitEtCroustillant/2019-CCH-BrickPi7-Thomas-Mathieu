import brickpi3

def zero():
    BP = brickpi3.BrickPi3()
    while True:
        valEncoder = BP.get_motor_encoder(BP.PORT_A)
        speed = 20
        
        if valEncoder == 0:
            BP.set_motor_power(BP.PORT_A, 0)
            break
        elif valEncoder > 0:
            speed *= -1
        
        BP.set_motor_power(BP.PORT_A, speed)