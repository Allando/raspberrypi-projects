import RPi.GPIO as GPIO
from time import sleep

def main():
    GPIO.setmode(GPIO.BOARD)

    # LEDS
    global blueLed
    global yellowLed

    blueLed = 8
    yellowLed = 37

    # BUTTONS
    blueButton = 36
    yellowButton = 40
    whiteButton = 35
    redButton = 31

    # LED State
    blueLedState = False
    yellowLedState = False

    # Button presses
    blueButtonPress = True
    yellowButtonPress = True
    whiteButtonPress = True
    redButtonPress = True

    # Setup the pin the LED is connected to
    GPIO.setup(blueLed, GPIO.OUT)
    GPIO.setup(yellowLed, GPIO.OUT)

    # Setup the button
    GPIO.setup(blueButton, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(yellowButton, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(whiteButton, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(redButton, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    try:
        while True:
            print("Come on man, press the button!")

            blueButtonPress = GPIO.input(blueButton)
            yellowButtonPress = GPIO.input(yellowButton)
            
            whiteButtonPress = GPIO.input(whiteButton)
            redButtonPress = GPIO.input(redButton)

            if not blueButtonPress and not blueLedState and not yellowLedState:
                blueLedState = True
                outputter(blueLedState, yellowLedState)
            elif not yellowButtonPress and not blueLedState and not yellowLedState:
                yellowLedState = True
                outputter(blueLedState, yellowLedState)
            elif not blueButtonPress and not blueLedState and yellowLedState:
                blueLedState = True
                yellowLedState = False
                outputter(blueLedState, yellowLedState)
            elif not yellowButtonPress and blueLedState and not yellowLedState:
                blueLedState = False
                yellowLedState = True
                outputter(blueLedState, yellowLedState)
            elif not whiteButtonPress:
                print('hi')
                blueLedState = False
                yellowLedState = False
                outputter(blueLedState, yellowLedState)
            elif not redButtonPress:
                blueLedState = False
                yellowLedState = False
                outputter(blueLedState, yellowLedState)
                print("Exiting...")
                break
            sleep(.1)
    finally:
        # Reset the GPIO Pins to a safe state
        GPIO.output(blueLed, False)
        GPIO.output(yellowLed, False)
        GPIO.cleanup()
    

def outputter(blueLedState, yellowLedState):
    GPIO.output(blueLed, blueLedState)
    GPIO.output(yellowLed, yellowLedState)
    
    print("Blue State: {} | Yellow State: {}".format(blueLedState, yellowLedState))

main()
