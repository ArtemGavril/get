import RPi.GPIO as gpio

def dec2bin(num: int) -> list:
    return [int(i) for i in bin(num)[2:].zfill(8)]



dac = [26, 19, 13, 6, 5, 11, 9, 10]

gpio.setmode(gpio.BCM)
gpio.setup(dac, gpio.OUT)

try:
    n = input('Введите число от 0 до 255\n')
    while n != 'q':
        if int(n) < 0:
            print('Введённое число меньше нуля')
            break
        elif int(n) > 255:
            print('Число выходит за пределы 8-ми разрядов')
            break
        n = int(n)
        gpio.output(dac, dec2bin(n))
        n = input('Введите число от 0 до 255\n')
except ValueError:
    print('Введено не число или введено не целое число!')

finally:
    gpio.output(dac, 0)
    gpio.cleanup()
