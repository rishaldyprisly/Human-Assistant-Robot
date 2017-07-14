import re
import os

WORDS = ["LETS", "WORKING"]


def handle(text, mic, profile):
    """
        Responds to user-input, typically speech text, by relaying the
        meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """
    mic.say("I am ready. sir. What kind of car. sir?")
    mic.say("I will check my library")
    file = open ('/home/pi/jasper/library/carlist.txt', 'r')
    message = file.read
    mic.say(message)


def isValid(text):
    """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\blets working\b', text, re.IGNORECASE))


