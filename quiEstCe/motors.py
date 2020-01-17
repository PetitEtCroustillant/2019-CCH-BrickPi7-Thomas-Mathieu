import brickpi3

BP = brickpi3.BrickPi3()

# Fais revenir le moteur au point zéro
def zero(portBP):
    while True:
        valEncoder = BP.get_motor_encoder(portBP)
        speed = 20
        
        if valEncoder == 0.0:
            BP.set_motor_power(portBP, 0)
            break
        elif valEncoder > 0:
            speed *= -1
        
        BP.set_motor_power(portBP, speed)

# Réinitialise l'encoder du moteur
def resetEncoder(portBP):
    BP.offset_motor_encoder(portBP, BP.get_motor_encoder(portBP))

# Arrête un moteur
def stop(portBP):
    BP.set_motor_power(portBP, 0)
zero(BP.PORT_B)