import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(True)


GPIO.setup(14, GPIO.OUT)
GPIO.setup(2, GPIO.OUT)


while True:
    print "Blue ON | Yellow OFF"
    GPIO.output(2, GPIO.HIGH)
    GPIO.output(14, GPIO.LOW)
    time.sleep(0.5)
    print "Blue OFF | Yellow ON"
    GPIO.output(2, GPIO.LOW)
    GPIO.output(14, GPIO.HIGH)
    time.sleep(0.5)

