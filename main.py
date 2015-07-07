import mraa
import time

#setup
x = mraa.Gpio(33)
x.dir(mraa.DIR_IN)

#loop
while True:
    if x.read():
        print ("Apertou")
