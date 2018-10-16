# Human-Assistant-Robot
HACKADAY PRIZE 2017 

i built allgpio python code, but for the fan, thanks to Zainoz Zaini who create that, you can download all of these code but make sure you've installed jasper and pigpio properly.

Guide to install the necessary software components:

-------------------------------------------------------------------------------------------------------------------------------------------
Install webiopi:
$ sudo wget http://sourceforge.net/projects/webiopi/files/WebIOPi-0.7.1.tar.gz
$ sudo tar xvzf WebIOPi-0.7.1.tar.gz
$ cd WebIOPi-0.7.1
$ sudo wget https://raw.githubusercontent.com/doublebind/raspi/master/webiopi-pi2bplus.patch
$ sudo patch -p1 -i webiopi-pi2bplus.patch
$ sudo ./setup.sh
$ sudo reboot

-------------------------------------------------------------------------------------------------------------------------------------------
Install PIGPIO for the raspberry pi:
$ sudo apt-get update
$ sudo apt-get install pigpio python-pigpio python3-pigpio

-------------------------------------------------------------------------------------------------------------------------------------------
