'''
Author:             Ethan Scott
Date Created:       9/26/2023
Last Editted:       10/22/2023

Purpose:            This code works to allow the robot to play a song, specifically through 
                    the use of multiple variables that correspond to the different notes. 
                    Displayed is a notification telling the user that the song has began
                    and ended. PSY's "Gangnam Style" is the song that I chose to play through
                    this code.

Sample Run:         c:/Users/escot/create2Project2.py

Sample Output:      Playing Gangnam Style...
                    (sound)
                    Fin.
'''
import time
import serial

# Establish connection to the iCreate 2; note that COM number often changes
connection = serial.Serial("COM13", baudrate=115200, timeout=1)

# Notes, the number signifies the octave and "S" if the note is sharp
D5 = b'\x4A'
D5S = b'\x4B'
B4 = b'\x47'
F5S = b'\x4E'
E5 = b'\x4C'
E5S = b'\x4D'
C5S = b'\x49'
A4S = b'\x45'
G4S = b'\x43'
B4S = b'\x48'

# Note Durations, adjusted for higher tempo
FULL =  b'\x40'                                        # Full note
HALF = b'\x1A'                                         # Half note
QTR = b'\x0C'                                          # Quarter note
EHT = b'\x09'                                          # Eighth note
SXTTH = b'\x04'                                        # Sixteenth note

# OPCODE Commands
START = b'\x80'
SAFE = b'\x83'

LOAD_PART_1 = b'\x8C\x00\x10'                          # Load song (part) 1
LOAD_PART_2 = b'\x8C\x01\x10'                          # Load song (part) 2
LOAD_PART_3 = b'\x8C\x02\x10'                          # Load song (part) 3
LOAD_PART_4 = b'\x8C\x03\x10'                          # Load song (part) 4
LOAD_PART_5 = b'\x8C\x03\x10'                          # Load song (part) 5

PLAY_PART_1 = b'\x8D\x00'                              # Play song (part) 1
PLAY_PART_2 = b'\x8D\x01'                              # Play song (part) 2
PLAY_PART_3 = b'\x8D\x02'                              # Play song (part) 3
PLAY_PART_4 = b'\x8D\x03'                              # Play song (part) 4
PLAY_PART_5 = b'\x8D\x03'                              # Play song (part) 5


print("Playing Gangnam Style...")
connection.write(START)
time.sleep(1)

connection.write(LOAD_PART_1 +D5+EHT +C5S+HALF +B4+EHT +B4+EHT +F5S+EHT + \
               F5S+EHT +F5S+HALF +F5S+EHT +E5+EHT +E5+HALF +D5S+HALF + \
               E5S+EHT +D5S+EHT +D5S+EHT +D5S+HALF +B4+EHT)
time.sleep(1)
connection.write(START + SAFE + PLAY_PART_1)
time.sleep(3.5)

connection.write(LOAD_PART_2 +B4+EHT +B4+HALF +A4S+HALF +B4+EHT +B4+HALF + \
               B4+QTR +B4+QTR +D5+EHT +C5S+HALF +B4+EHT +B4+HALF +F5S+EHT + \
               F5S+EHT +F5S+EHT +F5S+HALF +E5+HALF)
time.sleep(1)
connection.write(START + SAFE + PLAY_PART_2)
time.sleep(4)

connection.write(LOAD_PART_3 +E5+HALF +E5S+HALF +E5S+HALF +E5S+HALF + \
               F5S+HALF +F5S+HALF +F5S+EHT +F5S+EHT +F5S+EHT +F5S+HALF + \
               F5S+HALF +F5S+HALF +F5S+EHT +F5S+EHT +F5S+EHT +F5S+EHT)
time.sleep(1)
connection.write(START + SAFE + PLAY_PART_3)
time.sleep(4)

connection.write(LOAD_PART_4 +F5S+HALF +F5S+HALF +F5S+HALF +F5S+HALF + \
               F5S+SXTTH +F5S+SXTTH +F5S+SXTTH +F5S+SXTTH +F5S+SXTTH +F5S+SXTTH + \
               F5S+SXTTH +F5S+SXTTH +F5S+SXTTH +F5S+SXTTH +F5S+SXTTH +F5S+SXTTH)
time.sleep(1)
connection.write(START + SAFE + PLAY_PART_4)
time.sleep(3.5)

connection.write(LOAD_PART_5 +F5S+EHT +F5S+EHT +F5S+EHT +F5S+EHT +F5S+EHT + \
               F5S+EHT +E5S+EHT +D5S+EHT +C5S+EHT +B4+EHT +A4S+FULL +B4+QTR + \
               B4+QTR +D5+QTR +B4S+QTR +A4S+HALF)
time.sleep(1)
connection.write(START + SAFE + PLAY_PART_5)
time.sleep(4)

print("Fin.")
