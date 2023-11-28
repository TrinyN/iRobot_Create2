# tell whats working whats not

import struct
import time
import serial
from Robot import Robot
import sys

robot = Robot("COM7")
robot.start()
robot.safe()

reference = int(200)
distance = int(300)

# initially drive with 200 speed
robot.driveDirect(b"\x00\xC8\x00\xC8")

# set speed variables to 200
currentLeftSpeed = int(200)
currentRightSpeed = int(200)


while (True):
    # get distance in int form
    distance = int(robot.sense_twoByte(b'\x1B'), 2)
    print(distance)

    # change speed accordingly
    error = int(.1 * (reference - distance))
    print(error)

    # change speeds according to error
    currentLeftSpeed -= error
    currentRightSpeed += error

    # convert int speeds to hex
    rightHex = hex(currentRightSpeed & 0xFFFF)
    leftHex = hex(currentLeftSpeed & 0xFFFF)


    # convert hex speeds to bytes, checking whether or not there is a high byte or not

    # if right and left speeds need two bytes
    if sys.getsizeof(rightHex) >= 55 and sys.getsizeof(leftHex) >= 55 :
        rightSpeed = bytes([int(rightHex[2:4], 16), int(rightHex[4:], 16)])
        leftSpeed = bytes([int(leftHex[2:4], 16), int(leftHex[4:], 16)])
        robot.driveDirect(rightSpeed + leftSpeed)

    # if only right speed needs two bytes
    elif sys.getsizeof(rightHex) >= 55 and sys.getsizeof(leftHex) < 55 :
        rightSpeed = bytes([int(rightHex[2:4], 16), int(rightHex[4:], 16)])
        leftSpeed = bytes([int(leftHex, 16)])
        robot.driveDirect(rightSpeed + b"\x00" + leftSpeed)

    # if only left speed needs two bytes
    elif sys.getsizeof(rightHex) < 55 and sys.getsizeof(leftHex) >= 55 :
        rightSpeed = bytes([int(rightHex, 16)])
        leftSpeed = bytes([int(leftHex[2:4], 16), int(leftHex[4:], 16)])
        robot.driveDirect(b"\x00" + rightSpeed + leftSpeed)

    # if right and left speeds need only one byte
    else:
        rightSpeed = bytes([int(rightHex, 16)])
        leftSpeed = bytes([int(leftHex, 16)])
        robot.driveDirect(b"\x00" + rightSpeed + b"\x00" + leftSpeed)

    time.sleep(5)
