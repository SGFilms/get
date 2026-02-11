import RPi.GPIO as GPIO, time as t

GPIO.setmode(GPIO.BCM)

leds = [24, 22, 23, 27, 17, 25, 12, 16]

GPIO.setup(leds, GPIO.OUT)

GPIO.output(leds, 0)

light_time = 0.02

while True:
    for led in leds:
        GPIO.output(led, 1)
        t.sleep(light_time)
        GPIO.output(led, 0)

    for led in reversed(leds):
        GPIO.output(led, 1)
        t.sleep(light_time)
        GPIO.output(led, 0)