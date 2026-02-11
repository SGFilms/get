import RPi.GPIO as GPIO, time as t

GPIO.setmode(GPIO.BCM)

led = 26
GPIO.setup(led, GPIO.OUT)

pwm = GPIO.PWM(led, 200)
duty = 0.0
pwm.start(duty)
    
upwards = True
while True:
    pwm.ChangeDutyCycle(duty)
    t.sleep(1/200)

    if upwards:
        if duty == 100.0:
            upwards = False
        else:
            duty += 1.0
    else:
        if duty == 0.0:
            upwards = True
        else:
            duty -= 1.0