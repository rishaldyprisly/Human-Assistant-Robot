# Import modul webiopi
import webiopi
import os
import sys
import time
import pigpio

pi = pigpio.pi()

S1=18 #CAMERA USE
S2=10 #GRIPPER BESAR
S3=9 #GRIPPER KECIL
S4=15 #ANGKAT TURUN ARM
S5=04 #MAJU MUNDUR ARM
S6=17 #KIRI KANAN ARM

L1=22 # H-Bridge Input Pin 1
L2=23 # H-Bridge Input Pin 2

R1=24 # H-Bridge Input Pin 3
R2=25 # H-Bridge Input Pin 4

pi.set_mode(S1, pigpio.OUTPUT)
pi.set_mode(S2, pigpio.OUTPUT)
pi.set_mode(S3, pigpio.OUTPUT)
pi.set_mode(S4, pigpio.OUTPUT)
pi.set_mode(S5, pigpio.OUTPUT)
pi.set_mode(S6, pigpio.OUTPUT)
pi.set_mode(L1, pigpio.OUTPUT)
pi.set_mode(L2, pigpio.OUTPUT)
pi.set_mode(R1, pigpio.OUTPUT)
pi.set_mode(R2, pigpio.OUTPUT)


# -------------------------------------------------- #
# Mendefinisikan GPIO                                #
# -------------------------------------------------- #

# -------------------------------------------------- #
# Membuat Fungsi Motor Kiri                          #
# -------------------------------------------------- #

def left_stop():
    pi.write(L1, 0)
    pi.write(L2, 0)

def left_forward():
    pi.write(L1, 1)
    pi.write(L2, 0)

def left_backward():
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
    # Setup GPIO

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
# Me-Loop Program Web Server                         #
# -------------------------------------------------- #

# Menjalankan Loop sampai CTRL+C ditekan atau Raspberry direstart
webiopi.runLoop()

# -------------------------------------------------- #
# Mematikan Program Web Server                                   #
# -------------------------------------------------- #

# Stop Web server
server.stop()

# Mengatur Ulang fungsi GPIO
pi.set_mode(L1, pigpio.INPUT)
pi.set_mode(L2, pigpio.INPUT)
pi.set_mode(R1, pigpio.INPUT)
pi.set_mode(R2, pigpio.INPUT)
pi.set_mode(S1, pigpio.INPUT)
pi.set_mode(S2, pigpio.INPUT)
pi.set_mode(S3, pigpio.INPUT)
pi.set_mode(S4, pigpio.INPUT)
pi.set_mode(S5, pigpio.INPUT)
pi.set_mode(S6, pigpio.INPUT)


