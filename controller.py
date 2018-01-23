from microbit import *
import radio

radio.on()

# Event Loop
while True:
    y_orientation = accelerometer.get_y()

    # Determine direction (either forwards or backwards)
    if y_orientation < 300:
        display.show(Image.ARROW_N)
        direction = "f"
    else:
        display.show(Image.ARROW_S)
        direction = "t"
    
    # Determine which wheels should turn
    if button_a.is_pressed():
        leftSpeed = "t"
    else:
        leftSpeed = "f"

    if button_b.is_pressed():
        rightSpeed = "t"
    else:
        rightSpeed = "f"
    
    radio.send(direction + leftSpeed + rightSpeed)

    sleep(10)
    
