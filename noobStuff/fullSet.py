#!/bin/python

import RPi.GPIO as GPIO
from time import sleep

class DefaultState:
    def __init__(self):
        # LED
        blueLed = 8
        yellowLed = 37

        # BUTTONS
        blueButton = 36
        yellowButton = 40
        whiteButton = 35
        redButton = 31
        
        blueLedState = False
        yellowLedState = False
   
        blueButtonPress = True
        yellowButtonPress = True
        whiteButtonPress = True
        redButtonPress = True

    GPIO.setmode(GPIO.BOARD)
 
    # Setup the pin the LED is connected to
    GPIO.setup(blueLed, GPIO.OUT)
    GPIO.setup(yellowLed, GPIO.OUT)

    # Setup the button
    GPIO.setup(blueButton, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(yellowButton, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(whiteButton, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(redButton, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    try:
        print("Status: Ready | Blue State: {} | Yellow State: {}".format(blueLedState, yellowLedState))
        
        while True:
            blueButtonPress = GPIO.input(blueButton)
            yellowButtonPress = GPIO.input(yellowButton) 
            whiteButtonPress = GPIO.input(whiteButton)
            redButtonPress = GPIO.input(redButton)

            if not blueButtonPress and not blueLedState and not yellowLedState:
                blueLedState = True
                outputter()
            elif not yellowButtonPress and not blueLedState and not yellowLedState:
                yellowLedState = True
                outputter()
            elif not blueButtonPress and not blueLedState and yellowLedState:
                blueLedState = True
                yellowLedState = False
                outputter()
            elif not yellowButtonPress and blueLedState and not yellowLedState:
                blueLedState = False
                yellowLedState = True
                outputter()
            elif not whiteButtonPress:
                blueLedState = False
                yellowLedState = False
                outputter()
                if not whiteButtonPress:
                    print("seq")
                    blink() 
                    seq = Sequencer
                    seq.seq()
            elif not redButtonPress:
                blueLedState = False
                yellowLedState = False
                outputter()
                print("Exiting...")
                break
            sleep(.1)
    finally:
        # Reset the GPIO Pins to a safe state
        GPIO.output(blueLed, False)
        GPIO.output(yellowLed, False)
        GPIO.cleanup()

def blink():
    """if blueLedState:
        blueLedState = False
    elif yellowLedState:    
        yellowLedState = False
    """
    print("Blink")
    blueLedState = True
    yellowLedState = True
    blueLedState = False
    yellowLedState = False
    outputter()

def outputter():
    GPIO.output(blueLed, blueLedState)
    GPIO.output(yellowLed, yellowLedState)
    
    print("Blue State: {} | Yellow State: {}".format(blueLedState, yellowLedState))


class Sequencer(DefaultState):
    def seq():
        print("Press the red button to record")
        
        seqList = []

        if not redButtonPress:
            while not redButtonPress:
                if not blueButtonPress:
                    seqList.append('b')
                elif not yellowButtonPress:
                    seqList.append('y')
                elif not whiteButtonPress:
                    break

        if whiteButtonPress:
            for s in seqList:
                if s == 'b':
                    blueLedState = True
                    blueLedState = False
                elif s == 'y':
                    yellowLedState = True
                    yellowLedState = False



main()
