import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)
gpio.setup(14, gpio.OUT)
gpio.setup(27, gpio.IN)
gpio.output(14, 0)

if gpio.input(27):
    gpio.output(14, 1)