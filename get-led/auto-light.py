import RPi.GPIO as GPIO, time as t

GPIO.setmode(GPIO.BCM)

led = 26
GPIO.setup(led, GPIO.OUT)

luminance = 6
GPIO.setup(luminance, GPIO.IN)

while True:
    if GPIO.input(luminance):
        GPIO.output(led, 1)
        t.sleep(0.1)
    else:
        GPIO.output(led, 0)
        t.sleep(0.1)