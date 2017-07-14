# Import modul webiopi
import webiopi
import os
import sys
import time
import RPi.GPIO as GPIO
# Memanggil library GPIO
#GPIO = RPiGPIO.GPIO

# -------------------------------------------------- #
# Mendefinisikan GPIO                                #
# -------------------------------------------------- #
GPIO.setmode(GPIO.BCM)

# GPIO untuk Motor Kiri
L1=22 # H-Bridge Input Pin 1
L2=23 # H-Bridge Input Pin 2

R1=24 # H-Bridge Input Pin 3
R2=25 # H-Bridge Input Pin 4

#SERVO GPIO
S1=18 #CAMERA USE
S2=02 #GRIPPER BESAR
S3=03 #GRIPPER KECIL
S4=17 #ANGKAT TURUN ARM
S5=04 #MAJU MUNDUR ARM
S6=15 #KIRI KANAN ARM


# -------------------------------------------------- #
# Membuat Fungsi Motor Kiri                          #
# -------------------------------------------------- #

def left_stop():
    GPIO.output(L1, GPIO.LOW)

def left_forward():
    GPIO.output(L1, GPIO.HIGH)
    GPIO.output(L2, GPIO.LOW)

def left_backward():
    GPIO.output(L1, GPIO.LOW)
    GPIO.output(L2, GPIO.HIGH)

def right_stop():
    GPIO.output(R1, GPIO.LOW)
    GPIO.output(R2, GPIO.LOW)

def right_forward():
    GPIO.output(R1, GPIO.HIGH)
    GPIO.output(R2, GPIO.LOW)

def right_backward():
    GPIO.output(R1, GPIO.LOW)
    GPIO.output(R2, GPIO.HIGH)

def servo_left():
    p.ChangeDutyCycle(12.5)
#time.sleep(0.3)

def servo_right():
    p.ChangeDutyCycle(2.5)
#time.sleep(0.3)

def servo_normal():
    #p.normal(7.5)
    #time.sleep(0.3)
    p.ChangeDutyCycle(6.7)
    time.sleep(0.3)

def servo_take1():
    p1.ChangeDutyCycle(6.7)

def servo_release1():
    p1.ChangeDutyCycle(2.5)

def servo_take2():
    p2.ChangeDutyCycle(6.7)

def servo_release2():

def servo_take2():
    p2.ChangeDutyCycle(6.7)

def servo_release2():
    p2.ChangeDutyCycle(2.5)

def servo_up():
    p3.ChangeDutyCycle(12.5)

def servo_down():
    p3.ChangeDutyCycle(6.7)

def servo_forwards():
    p4.ChangeDutyCycle(2.5)

def servo_backs():
    p4.ChangeDutyCycle(12.5)

def servo_lefts():
    p5.ChangeDutyCycle(12.5)

def servo_center():
    p5.ChangeDutyCycle(6.7)

def servo_rights():
    p5.ChangeDutyCycle(2.5)

# -------------------------------------------------- #
# Definisi Macro untuk JavaScript                    #
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
# Setup GPIO
GPIO.setup(L1, GPIO.OUT)
GPIO.setup(L2, GPIO.OUT)

GPIO.setup(R1, GPIO.OUT)
GPIO.setup(R2, GPIO.OUT)

GPIO.setup(S1, GPIO.OUT)
p = GPIO.PWM(S1,50)
p.start(7.5)

GPIO.setup(S2, GPIO.OUT)
p1 = GPIO.PWM(S2,50)
p1.start(12.5)

GPIO.setup(S3, GPIO.OUT)
p2 = GPIO.PWM(S3,50)
p2.start(12.5)

GPIO.setup(S4, GPIO.OUT)
p3 = GPIO.PWM(S4,50)
p3.start(12.5)

GPIO.setup(S5, GPIO.OUT)
p4 = GPIO.PWM(S5,50)
p4.start(12.5)

GPIO.setup(S6, GPIO.OUT)
p5 = GPIO.PWM(S6,50)
p5.start(7.5)

# Menempatkan web server pada port 8000, dan membuat ID dan password
server = webiopi.Server(port=9000, login="jasper", password="rishaldy")

# Mendaftarkan Macro untuk dipanggil pada javascript di HTML

server.addMacro(go_forward)
server.addMacro(go_backward)
server.addMacro(turn_left)
server.addMacro(turn_right)
server.addMacro(stop)

server.addMacro(left_s)
server.addMacro(right_s)

server.addMacro(take1)
server.addMacro(release1)

server.addMacro(take2)
server.addMacro(rights)
server.addMacro(center)
# -------------------------------------------------- #
# Me-Loop Program Web Server                         #
# -------------------------------------------------- #

# Menjalankan Loop sampai CTRL+C ditekan atau Raspberry direstart
webiopi.runLoop()

# -------------------------------------------------- #
# Mematikan Program Web Server                                   #
# -------------------------------------------------- #

# Stop Web server
server.stop()

# Reset GPIO Pins
GPIO.setup(L1, GPIO.IN)
GPIO.setup(L2, GPIO.IN)

GPIO.setup(R1, GPIO.IN)
GPIO.setup(R2, GPIO.IN)

GPIO.setup(S1, GPIO.IN)
GPIO.setup(S2, GPIO.IN)
GPIO.setup(S3, GPIO.IN)
GPIO.setup(S4, GPIO.IN)
GPIO.setup(S5, GPIO.IN)
GPIO.setup(S6, GPIO.IN)
