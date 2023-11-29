"""
Author:             Triny Nguyen and Ethan Scott
Date Created:       11/23/2023
Last Editted:       11/28/2023

Purpose:            This file works to make the robot stay a relatively-close
                    distance to a wall by using a PID controller.

Progress:           We were able to get the Proportional aspect of the PID controller
                    working, including the sensor commands retrieving the ACTUAL DISTANCE
                    away from the wall and comparing it with the REFERENCE and sending the
                    altered drive direct command.

                    We were not able to move past the Proportional part, so the Integral
                    and Derivative aspects are both not included.

Sample Input:       c:/Users/escot/vscode-workspace/PIDProject.py

Sample Output:  	300
                    100
"""
import time
import sys
from Robot import Robot

# Establishing the connection with the robot by instantiation
robot = Robot("COM7")
robot.start()
robot.safe()

# Constants to be used for sensing the wall and driving accordingly
REFERENCE = int(200)

# Initially drive with 200 speed
robot.driveDirect(b"\x00\xC8\x00\xC8")

# Set speed variables to 200
currentLeftSpeed = int(200)
currentRightSpeed = int(200)

while (True):
    # get distance in int form
    distance = int(robot.sense_twoByte(b'\x1B'), 2)
    print(distance)

    # get error
    error = int(.1 * (REFERENCE - distance))
    print(error)

    # change speeds according to error
    currentLeftSpeed -= error
    currentRightSpeed += error

    # convert int speeds to hex
    rightHex = hex(currentRightSpeed & 0xFFFF)
    leftHex = hex(currentLeftSpeed & 0xFFFF)


    # convert hex speeds to bytes, checking whether or not there is a high byte or not

    # if right speed has high byte
    if sys.getsizeof(rightHex) >= 54:
        rightSpeed = bytes([int(rightHex[2:4], 16), int(rightHex[4:], 16)])
    # else make high byte 0
    else:
        rightSpeed = b"\x00" + bytes([int(rightHex, 16)])

    # if left speed has high byte
    if sys.getsizeof(leftHex) >= 54:
        leftSpeed = bytes([int(leftHex[2:4], 16), int(leftHex[4:], 16)])
    # else make high byte 0
    else:
        leftSpeed = b"\x00" + bytes([int(leftHex, 16)])

    robot.driveDirect(rightSpeed + leftSpeed)

    time.sleep(1)

