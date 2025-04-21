from gpiozero import Button
from signal import pause

# Create a Button object for GPIO 14. Setting pull_up=False enables the internal pull-down resistor.
sensor = Button(4, pull_up=False)

# Define what happens when the sensor is activated (pressed) or deactivated (released)
def on_pressed():
    print("GPIO4 is now HIGH (activated)")

def on_released():
    print("GPIO4 is now LOW (deactivated)")

sensor.when_pressed = on_pressed
sensor.when_released = on_released

print("Monitoring GPIO4. Press CTRL+C to exit.")
pause()