import RPi.GPIO as gpio
from time import sleep

gpio.setmode(gpio.BCM)
gpio.setup(14, gpio.OUT)

for _ in range(3):
    for _ in range(3):
        gpio.output(14, 1)
        sleep(0.2)
        gpio.output(14, 0)
        sleep(0.2)
    sleep(1)
    for _ in range(3):
        gpio.output(14, 1)
        sleep(0.5)
        gpio.output(14, 0)
        sleep(0.2)
    sleep(1)
    for _ in range(3):
        gpio.output(14, 1)
        sleep(0.2)
        gpio.output(14, 0)
        sleep(0.2)
    sleep(2)
