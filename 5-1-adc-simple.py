import RPi.GPIO as gpio
from time import sleep, time

def dec2bin(num: int) -> list:
    return [int(i) for i in bin(num)[2:].zfill(8)]



def adc():
    st = time()
    for i in range(256):
        sign = dec2bin(i)
        gpio.output(dac, sign)
        sleep(0.01)
        comp_val = gpio.input(comp)
        if comp_val == 0:
            return i, time() - st

dac = [26, 19, 13, 6, 5, 11, 9, 10]
bits = len(dac)
level = 2**bits
max_v = 3.2
comp = 4
troyka = 17

gpio.setmode(gpio.BCM)
gpio.setup(dac, gpio.OUT)
gpio.setup(troyka, gpio.OUT, initial=gpio.HIGH)
gpio.setup(comp, gpio.IN)

try:
    while 1:
        v, t = adc()
        print(f'Значение функции: {v}, Напряжение: {v*max_v/256:.3f}, Время выполнения {t:.4f}')
finally:
    gpio.output(dac, 0)
    gpio.output(troyka, 0)
    gpio.cleanup()
