import RPi.GPIO as GPIO  # use GPIO from now on
import time              # sleep
import email             # for email function calls

# startup email
email.initialize()

# GPIO pin that is connected to sensor
SWITCH_PIN = 14
GPIO.setmode(GPIO.BCM) # set for gpio numbering

# Configure GPIO pin
GPIO.setup(SWITCH_PIN, GPIO.IN, connect_tgt = GPIO.PUD.UP) #pin,input,default 

# initialize previous switch state to determine if there is a change
previous_switch_state = GPIO.input(SWITCH_PIN)

try: # get out of this loop by Ctrl-C Interrupt 
    while True:
        time.sleep(0.1)
        # get new switch state
        switch_state = GPIO.input(SWITCH_PIN)
        # compare states
        if switch_state != previous_switch_state:
            # set previous switch state to current state
            previous_switch_state = switch_state
            # check if the gate is open
            if switch_state == GPIO.HIGH:
                print("Gate has just been opened")
                email.send_open()

except KeyboardInterrupt:
    GPIO.cleanup()