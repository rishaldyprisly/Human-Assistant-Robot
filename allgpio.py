#                  MANUAL CONTROL                   #
#      AUTHOR : MOCHAMAD RISHALDY PRISLIYANTO       #
#                      2017                         #
#             LICENSE : PUBLIC DOMAIN               #
#               www.sparkintech.com                 #
#           www.rishaldy.sparkintech.com            #
#   PLEASE READ THE README FOR FURTHER INFORMATION  #

from __future__ import division
import webiopi
import os
import sys
import time
import pigpio
import Adafruit_PCA9685
pi = pigpio.pi()
pwm = Adafruit_PCA9685.PCA9685()

L1=22 # H-Bridge Input Pin 1
L2=23 # H-Bridge Input Pin 2

R1=24 # H-Bridge Input Pin 3
R2=25 # H-Bridge Input Pin 4

pi.set_mode(L1, pigpio.OUTPUT)
pi.set_mode(L2, pigpio.OUTPUT)
pi.set_mode(R1, pigpio.OUTPUT)
pi.set_mode(R2, pigpio.OUTPUT)


# -------------------------------------------------- #
#                    PWM SETUP                       #
# -------------------------------------------------- #
servo_min = 150  # Min pulse length out of 4096
servo_max = 600  # Max pulse length out of 4096
servo_mid = 375
servo_take = 50
servo_max1 = 550
servo_min1 = 200
# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

pwm.set_pwm_freq(60)
# -------------------------------------------------- #
#                  MOTOR FUNCTION                    #
# -------------------------------------------------- #

def left_stop():
    pi.write(L1, 0)
    pi.write(L2, 0)
def left_forward():
    pi.write(L1, 1)
    pi.write(L2, 0)

def left_backward():
    pi.write(L1, 0)
    pi.write(L2, 1)

def right_stop():
    pi.write(R1, 0)
    pi.write(R2, 0)

def right_forward():
    pi.write(R1, 1)
    pi.write(R2, 0)

def right_backward():
    pi.write(R1, 0)
    pi.write(R2, 1)

# -------------------------------------------------- #
#                 SERVOS FUNCTION                    #
# -------------------------------------------------- #
def servo_left():
    pwm.set_pwm(0, 0, servo_min)
    time.sleep(1)
def servo_right():
    pwm.set_pwm(0, 0, servo_max)
#pi.set_servo_pulsewidth(S1, 2000)

def servo_normal():
    pwm.set_pwm(0, 0, servo_mid)
#pi.set_servo_pulsewidth(S1, 1500)

def servo_take1():
    pwm.set_pwm(1, 0, servo_min)

def servo_release1():
    pwm.set_pwm(1, 0, servo_max)

def servo_take2():
    pwm.set_pwm(2, 0, servo_max)

def servo_release2():
    pwm.set_pwm(2, 0, servo_min)

def servo_up():
    pwm.set_pwm(3, 0, servo_max)

def servo_down():
    pwm.set_pwm(3, 0, servo_down)

def servo_forwards():
    pwm.set_pwm(4, 0, servo_max1)

def servo_backs():
    pwm.set_pwm(4, 0, servo_min1)

def servo_lefts():
    pwm.set_pwm(5, 0, min)

def servo_center():
    pwm.set_pwm(5, 0, servo_mid)

def servo_rights():
    pwm.set_pwm(5, 0, servo_max)
    time.sleep(1)

# -------------------------------------------------- #
#                JAVASCRIPT FUNCTION                 #
# -------------------------------------------------- #
def go_forward():
    left_forward()
    right_forward()

def go_backward():
    left_backward()
    right_backward()
def turn_left():
    left_forward()
    right_backward()

def turn_right():
    left_backward()
    right_forward()

def stop():
    left_stop()
    right_stop()

def left_s():
    servo_left()

def right_s():
    servo_right()

def normal_s():
    servo_normal()

def take1():
    servo_take1()

def release1():
    servo_release1()

def take2():
    servo_take2()

def release2():
    servo_release2()

def up():
    servo_up()

def down():
    servo_down()

def forwards():
    servo_forwards()

def backs():
    servo_backs()

def lefts():
    servo_lefts()

def rights():
    servo_rights()

def center():
    servo_center()

def s_stop():
    servo_stop()
    
# -------------------------------------------------- #
#            WEBSERVER AND USER AUTH SETUP           #
# -------------------------------------------------- #
server = webiopi.Server(port=9000, login="jasper", password="rishaldy")

# -------------------------------------------------- #
#              JAVASCRIPT TO HTML MACROS             #
# -------------------------------------------------- #

server.addMacro(go_forward)
server.addMacro(go_backward)
server.addMacro(turn_left)
server.addMacro(turn_right)
server.addMacro(stop)

server.addMacro(left_s)
server.addMacro(right_s)
server.addMacro(normal_s)

server.addMacro(take1)
server.addMacro(release1)

server.addMacro(take2)
server.addMacro(release2)

server.addMacro(up)
server.addMacro(down)

server.addMacro(forwards)
server.addMacro(backs)
server.addMacro(s_stop)
server.addMacro(lefts)
server.addMacro(rights)
server.addMacro(center)
# -------------------------------------------------- #
#               LOOP THE WEBSERVER                   #
# -------------------------------------------------- #

# Menjalankan Loop sampai CTRL+C ditekan atau Raspberry direstart
webiopi.runLoop()

# -------------------------------------------------- #
#             SHUTDOWN THE WEB SERVER                #
# -------------------------------------------------- #

# Stop Web server
server.stop()


