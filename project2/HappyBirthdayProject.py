"""
Author: Triny Nguyen
Written: 9/26/23
Last Updated: 10/3/23

Description: connects to iRobot Create 2. Saves the happy birthday song into the roomba 
and asks the user if they want to play the song. If yes, the song will play and the user
will be asked if they would like the song to play again.

Sample Run: C:\\Users\\User>python HappyBirthdayProject.py

Sample Output: Would you like to play Happy Birthday? If yes enter 1, if no enter 0. 
"""

import struct
import time
import serial

# gets user input
userInput = int(
    input("Would you like to play Happy Birthday? If yes enter 1, if no enter 0. ")
)

# connects to roomba
connection = serial.Serial("COM7", baudrate=115200, timeout=1)

# start and turns roomba to safe mode
connection.write(b"\x80\x83")
time.sleep(0.5)

# notes of song
C_LOW = b"\x48"
A = b"\x51"
A_SHARP = b"\x52"
B = b"\x53"
C = b"\x54"
D = b"\x4A"
E = b"\x4C"
F = b"\x4D"
G = b"\x4F"

# 48
QUARTER_NOTE = b"\x30"

# 96
HALF_NOTE = b"\x60"

# 24
QUARTER_BEAM = b"\x18"

# Happy Birthday to you. Happy Birthday to you.
VERSE_ONE = (
    b"\x8C\x01\x0C"
    + C_LOW
    + QUARTER_BEAM
    + C_LOW
    + QUARTER_BEAM
    + D
    + QUARTER_NOTE
    + C_LOW
    + QUARTER_NOTE
    + F
    + QUARTER_NOTE
    + E
    + HALF_NOTE
    + C_LOW
    + QUARTER_BEAM
    + C_LOW
    + QUARTER_BEAM
    + D
    + QUARTER_NOTE
    + C_LOW
    + QUARTER_NOTE
    + G
    + QUARTER_NOTE
    + F
    + HALF_NOTE
)

# Happy Birthday dear --- ---. Happy Birthday to you!
VERSE_TWO = (
    b"\x8C\x02\x0D"
    + C_LOW
    + QUARTER_BEAM
    + C_LOW
    + QUARTER_BEAM
    + C
    + QUARTER_NOTE
    + A
    + QUARTER_NOTE
    + F
    + QUARTER_NOTE
    + E
    + QUARTER_NOTE
    + D
    + HALF_NOTE
    + A_SHARP
    + QUARTER_BEAM
    + A_SHARP
    + QUARTER_BEAM
    + A
    + QUARTER_NOTE
    + F
    + QUARTER_NOTE
    + G
    + QUARTER_NOTE
    + F
    + HALF_NOTE
)

# saves the song into the roomba, splitting it into 2 parts
connection.write(VERSE_ONE)
time.sleep(1.0)
connection.write(VERSE_TWO)

# if user input is 1, play song
while userInput == 1:
    # plays song
    connection.write(b"\x8D\x01")
    time.sleep(9.5)
    connection.write(b"\x8D\x02")

    # asks user if they want the song to repeat
    userInput = int(
        input("Would you like the song to play again? 1 for yes, 0 for no. ")
    )
