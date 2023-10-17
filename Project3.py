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




































# connection = serial.Serial("COM8", baudrate=115200, timeout=1)

# # start and turns roomba to safe mode
# connection.write(b"\x80\x83")
# time.sleep(0.5)

# # drive forward [137 0 100 7F FF] 100 speed straight

# DRIVE_DIRECT_SAME = b'\x91\x01\x90\x01\x90'


# DRIVE_WHEEL_OPPOSITE_200 = b'\x91\xFF\x38\x00\xC8'


# connection.write(DRIVE_DIRECT_SAME)

# time.sleep(3.7)

# connection.write(b"\xAD")

# connection.write(b"\x80\x83")
# time.sleep(0.5)

# connection.write(DRIVE_WHEEL_OPPOSITE_200)

# time.sleep(.7)

# connection.write(b"\xAD")
# connection.write(b"\x80\x83")
# time.sleep(0.5)
# connection.write(DRIVE_DIRECT_SAME)

# time.sleep(3.2)

# connection.write(b"\xAD")

# connection.write(b"\x80\x83")
# time.sleep(0.5)

# connection.write(DRIVE_WHEEL_OPPOSITE_200)

# time.sleep(.9)

# connection.write(b"\xAD")

# connection.write(b"\x80\x83")
# time.sleep(0.5)
# connection.write(DRIVE_DIRECT_SAME)

# time.sleep(3.2)

# connection.write(b"\xAD")

# connection.write(b"\x80\x83")
# time.sleep(0.5)

# connection.write(DRIVE_WHEEL_OPPOSITE_200)

# time.sleep(.75)

# connection.write(b"\xAD")

# connection.write(b"\x80\x83")
# time.sleep(0.5)
# connection.write(DRIVE_DIRECT_SAME)

# time.sleep(2.8)

# connection.write(b"\xAD")
