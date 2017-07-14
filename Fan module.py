import random
import re
import os

WORDS = ["SPIN", "ON","OFF","BLINKING"]
PRIORITY = 20

def handle(text, mic, profile):
   try:


        cmd = 'sudo python /home/pi/FAN_pi/fan.py -i '
        if bool(re.search(r'\b(spin on|\son\s.*fan)\b', text, re.IGNORECASE)):
                mic.say('fan now is on. sir')
                os.system(cmd+"switch on")
        elif bool(re.search(r'\b(spin off?|\soff?\s.*fan)\b', text, re.IGNORECASE)):
                mic.say('fan now is off. sir')
                os.system(cmd+"switch off")
        else:
                mic.say('light now is blinking 5 times')
                os.system(cmd+"blink 5 1")

        mic.say('DONE SIR... ANYTHING ELSE? ')

   except:
        print "Lighting Error"
        mic.say('Sorry... something wrong on lighting configuration')


def isValid(text):
    """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
    """

    if bool(re.search(r'\b(spin on|spin off?|\soff?\s.*spin|\son\s.*spin|blinking|spin blinking|blinking\s.*spin)\b', text, re.IGNORECASE)):
        return True

    return False
