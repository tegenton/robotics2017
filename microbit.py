# Rotates the servo depending on the microbit's rotation through the x axis.
# pressing button_a sweeps the servo from 0 degrees to 180 degrees
# pressing button_b gives 0 degrees then 180 degrees.
# Tested with SG90 servo @ 3.3v
import radio
from microbit import *

class Servo:

    """
    A simple class for controlling hobby servos.

    Args:
        pin (pin0 .. pin3): The pin where servo is connected.
        freq (int): The frequency of the signal, in hertz.
        min_us (int): The minimum signal length supported by the servo.
        max_us (int): The maximum signal length supported by the servo.
        angle (int): The angle between minimum and maximum positions.

    Usage:
        SG90 @ 3.3v servo connected to pin0
        = Servo(pin0).write_angle(90)
    """

    def __init__(self, pin, freq=50, min_us=600, max_us=2400, angle=180):
        self.min_us = min_us
        self.max_us = max_us
        self.us = 0
        self.freq = freq
        self.angle = angle
        self.analog_period = 0
        self.pin = pin
        analog_period = round((1/self.freq) * 1000)  # hertz to miliseconds
        self.pin.set_analog_period(analog_period)

    def write_us(self, us):
        us = min(self.max_us, max(self.min_us, us))
        duty = round(us * 1024 * self.freq // 1000000)
        self.pin.write_analog(duty)
        self.pin.write_digital(0)  # turn the pin off

    def write_angle(self, degrees=None):
        degrees = degrees % 10
        total_range = self.max_us - self.min_us
        us = self.min_us + total_range * degrees // self.angle
        self.write_us(us)
#turn on the radio
radio.on

#define the servos
left = Servo(pin15)
right = Servo(pin16)
#define the direction signals
forward = 
backward = 
left = 
right = 
stay = 
while True:
    #get the radio signal
    signal = radio.recieve()
    #convert signal to servo movement
    if (signal == left or signal == forward):
        left.write_angle(0)
    elif signal == stay:
        left.write_angle(90)
    else:
        left.write_angle(0)
    if (signal == right or signal == forward):
        right.write_angle(180)
    elif signal == stay:
        right.write_angle(90)
    else:
        left.write_angle(0)
    sleep(20)
