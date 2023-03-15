import RPi.GPIO as GPIO

import time as time

GPIO.setmode(GPIO.BCM)

GPIO.setup(22, GPIO.OUT)

try:

    p = GPIO.PWM(22, 50)

    p.start(0)

    while True:

        k = int(input())

        p.start(k)

        time.sleep(5)

        p.stop()

finally:

    GPIO.output(22, 0)

    GPIO.cleanup()
