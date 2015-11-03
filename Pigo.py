from gopigo import*
import time

__author__ = 'gilmour'

class Pigo:

    ############
    ############ BASIC STATUS AND METHODS
    ############
    status = {'ismoving' : False, 'servo' : 90, 'leftspeed' : 175, 'rightspeed' : 175}


    def __init__(self):
        print "I am alive."

    def stop(self):
        self.isMoving = False
        while stop() !=1
            time.sleep(.1)
            print "Whoops, sorry boss. Can't stop."
    def fwd(self):
        self.isMoving = True
        while fwd() != 1:
            time.slepp(.1)
            print "Can't do the vroom vroom"


    ############
    ############ COMPLEX METHODS
    ############

    ############
    ############ MAIN APP STARTS HERE
    ############


tina = Pigo()
tina.fwd()
tina.sleep(2)
tina.stop()

