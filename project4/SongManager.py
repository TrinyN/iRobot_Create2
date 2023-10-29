"""
Author:             Ethan Scott (Values from Triny Nguyen)
Written:            10/29/2023
Last Updated:       10/29/2023

Purpose:            This file contains data and getters related to Triny Nguyen's 
                    Happy Birthday song originally designed to play on the 
                    iRobot Create 2.

Sample Run:         c:/Users/escot/vscode-workspace/Song_Manager.py

Sample Output:      none

"""
import struct
import time
import serial
from Robot import Robot

class SongManager:
    """Class that contains song data to play Happy Birthday
    """
    # Note pitches
    C_LOW = b"\x48"
    A = b"\x51"
    A_SHARP = b"\x52"
    B = b"\x53"
    C = b"\x54"
    D = b"\x4A"
    E = b"\x4C"
    F = b"\x4D"
    G = b"\x4F"
    
    # Note durations
    QUARTER_NOTE = b"\x30"          # 48
    HALF_NOTE = b"\x60"             # 96
    QUARTER_BEAM = b"\x18"          # 24

    # First verse data
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
    
    # Second verse data
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

    def get_verse_one(self):
        """Method to allow accessing of the first verse outside this class.

        Returns:
            str: A string including the full command to load verse 1
        """
        print("verse 1 retrieved")
        return self.VERSE_ONE
    
    def get_verse_two(self):
        """Method to allow accessing of the second verse outside this class.

        Returns:
            str: A string including the full command to load verse 2
        """
        print("verse 2 retrieved")
        return self.VERSE_TWO
