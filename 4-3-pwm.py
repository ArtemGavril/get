import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)
gpio.setup([22, 20], gpio.OUT)

p = gpio.PWM(22, 1000)
p.start(0)

led = gpio.PWM(20, 1000)
led.start(0)
try:
    while 1:
        power = int(input('Введите коэффициент заполнения \n'))
        p.ChangeDutyCycle(power)
        led.ChangeDutyCycle(power)

    
finally:
    gpio.output([22, 20], 0)
    gpio.cleanup()