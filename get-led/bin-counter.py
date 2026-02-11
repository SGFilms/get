import RPi.GPIO as GPIO, time as t

GPIO.setmode(GPIO.BCM)

leds = [24, 22, 23, 27, 17, 25, 12, 16]

GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, 0)

up = 9
down = 10
GPIO.setup([up, down], GPIO.IN)

num = 0

def dec2bin(val) -> list:
    return [int(el) for el in bin(val)[2:].zfill(8)]

sleep_time = 0.2

while True:
    if GPIO.input(up):
        num += 1
        if num < 0 or num > 255:
            num = 0
        print(num, dec2bin(num))
        t.sleep(sleep_time)
    if GPIO.input(down):
        num -= 1
        if num < 0 or num > 255:
            num = 0
        print(num, dec2bin(num))
        t.sleep(sleep_time)
    GPIO.output(leds, dec2bin(num))