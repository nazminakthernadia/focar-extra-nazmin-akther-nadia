import focar
from time import sleep

LONG_TIME = 2.0    # seconds for the long side, calibrate
SHORT_TIME = 1.2   # seconds for the short side, calibrate
TURN_TIME = 0.6    # seconds for a 90 degree turn, calibrate

for side in (LONG_TIME, SHORT_TIME, LONG_TIME, SHORT_TIME):
    focar.forward(side)
    focar.stop()
    sleep(0.5)                  # stop at the corner
    focar.turn_right(TURN_TIME)
    sleep(0.5)