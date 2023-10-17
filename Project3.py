"""
Author:             Triny Nguyen and Ethan Scott
Date Created:       10/5/2023
Last Editted:       10/17/2023

Purpose:            This code works to make the robot move around a 4ft x 4ft square 
                    on the class floor, marked by tape. The code uses the Robot.py class
                    to import all of the necessary methods related to passing
                    commands (and possible packet IDs) to the 

Sample Input:       C:\\Users\\User>python Project3.py

Sample Output:      Connected!
                    Then followed by the movement of the Create 2.
"""

import sys
import time

sys.path.append(r"C:\Users\User")
from Robot import Robot


instance = Robot("COM7")

# start and turn to safe mode
instance.start()
instance.safe()

# drive straight 400 speed
instance.driveDirect(b"\x01", b"\x90", b"\x01", b"\x92")

time.sleep(3.7)

# stop driving
instance.stop()

# start and turn to safe mode
instance.start()
instance.safe()

# turn with wheels opposite 200 and -200 speed
instance.driveDirect(b"\xFF", b"\x38", b"\x00", b"\xC8")

time.sleep(.9)

# stop turning
instance.stop()

# start and turn to safe mode
instance.start()
instance.safe()

# drive straight 400 speed
instance.driveDirect(b"\x01", b"\x90", b"\x01", b"\x90")

time.sleep(3.5)

# stop driving
instance.stop()

# start and turn to safe mode
instance.start()
instance.safe()

# turn with wheels opposite 200 and -200 speed
instance.driveDirect(b"\xFF", b"\x38", b"\x00", b"\xC8")

time.sleep(0.9)

# stop turning
instance.stop()

# start and turn to safe mode
instance.start()
instance.safe()

# drive straight 400 speed
instance.driveDirect(b"\x01", b"\x90", b"\x01", b"\x90")

time.sleep(3.2)

# stop driving
instance.stop()

# start and turn to safe mode
instance.start()
instance.safe()

# turn with wheels opposite 200 and -200 speed
instance.driveDirect(b"\xFF", b"\x38", b"\x00", b"\xC8")

time.sleep(0.93)

# stop turning
instance.stop()

# start and turn to safe mode
instance.start()
instance.safe()

# drive straight 400 speed
instance.driveDirect(b"\x01", b"\x90", b"\x01", b"\x90")

time.sleep(2.8)

# stop driving
instance.stop()
