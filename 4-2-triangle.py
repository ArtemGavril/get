import RPi.GPIO as gpio
from time import sleep


def dec2bin(num: int) -> list:
    return [int(i) for i in bin(num)[2:].zfill(8)]


dac = [26, 19, 13, 6, 5, 11, 9, 10]

gpio.setmode(gpio.BCM)
gpio.setup(dac, gpio.OUT)

try:
    T = input()
    y = 0
    k = 1
    while 1:
        for _ in range(255):
            sleep(0.01)
            y += k
            gpio.output(dac, dec2bin(y))
        for _ in range(255, 0, -1):
            sleep(0.01)
            y -= k
            gpio.output(dac, dec2bin(y))

finally:
    gpio.output(dac, 0)
    gpio.cleanup()