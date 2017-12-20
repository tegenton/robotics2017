import radio
from microbit import *

# The radio won't work unless it's switched on.
radio.on()

# define directional signals
forward = "forward"
backward = "backward"
left = "left"
right = "right"

while True:
  if button_a.was_pressed():
    radio.send(forward)
  if button_b.was_pressed():
    radio.send(backward)
  # if left
    # radio.send(left)
  # if forward
    # radio.send(right)
