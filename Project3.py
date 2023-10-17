"""
Author: Triny Nguyen
Written: 10/5/23
Last Updated: 10/17/23

Description: creates a Robot object and uses the methods in the Robot 
class to get the roomba to travel in a "square" 

Sample Run: C:\\Users\\User>python Project3.py

Sample Output: Connected!
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
