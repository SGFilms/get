import RPi.GPIO as GPIO, time as t

GPIO.setmode(GPIO.BCM)

led = 26

GPIO.setup(led, GPIO.OUT)

state = 0
period = 1.0

while True:
    GPIO.output(led, state)
    state = not state
    t.sleep(period)

