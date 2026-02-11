import RPi.GPIO as GPIO, time as t

GPIO.setmode(GPIO.BCM)

led = 26
GPIO.setup(led, GPIO.OUT)

button = 13
GPIO.setup(button, GPIO.IN)

state = True

while True:
    if GPIO.input(button) == 1:
        state = not state
        GPIO.output(led, state)
        t.sleep(0.2)

        while GPIO.input(button) == 1:
            t.sleep(0.01)
        t.sleep(0.01)
    


        


