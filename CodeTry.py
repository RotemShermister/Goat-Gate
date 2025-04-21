from gpiozero import Button
import time
import my_email as email

# Set up the GPIO pin (GPIO pin 4)
sensor = Button(4, pull_up=False)

# Initialize email
email.initialize()

previous_state = False

try:
    while True:
        if sensor.is_pressed:
            if previous_state == False:
                print("Sending email...")
                email.send_open()
            time.sleep(0.75)  # Prevent multiple triggers in rapid succession
            previous_state = True
        else:
            print("Button not pressed.")
            previous_state = False
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Exiting program.")