"""
Author:             Ethan Scott and Triny Nguyen
Date Created:       10/5/2023
Last Editted:       10/17/2023

Purpose:            

Sample Input:       c:/Users/escot/vscode-workspace/Robot.py

Sample Output:  	Connected!
					No output is provided unless the class is instantiated.
"""
import struct
import serial
import time

class Robot:
	"""Class of Robot that includes all related and relevant methods
		and variables required to send commands (and possibly
		packet IDs) to the robot through a serial connection.

	Returns:
		Print statements and actions related to the commands sent
			through the use of the methods.
	"""
	# Command HEX byte definitions
	start_cmd					=  b'\x80'
	safe_cmd					=  b'\x83'
	sensors_cmd					=  b'\x8E'
	reset_cmd					=  b'\x07'
	stop_cmd					=  b'\xAD'
	buttons_cmd					=  b'\xA5'
	drive_direct_cmd			=  b'\x91'
	drive_cmd					=  b'\x89'
	leds_ascii_cmd				=  b'\xA4'
	leds_cmd					=  b'\x8B'
	seek_dock_cmd				=  b'\x8F'

	# Packet ID HEX byte definitions
	wall_id						=  b'\x08'
	bumpsAndWheels_id			=  b'\x07'
	cliffLeft_id				=  b'\x09'
	cliffFrontLeft_id			=  b'\x0A'
	cliffFrontRight_id			=  b'\x0B'
	cliffRight_id				=  b'\x0C'
	virtualWall_id				=  b'\x0D'
	buttons_id					=  b'\x12'
	distance_id					=  b'\x13'
	angle_id					=  b'\x14'
	chargingState_id			=  b'\x15'
	voltage_id					=  b'\x16'
	temperature_id				=  b'\x18'
	batteryCharge_id			=  b'\x19'
	wallSignal_id				=  b'\x1B'
	cliffLeftSignal_id			=  b'\x1C'
	cliffFrontLeftSignal_id		=  b'\x1D'
	cliffFrontRightSignal_id	=  b'\x1E'
	cliffRightSignal_id			=  b'\x1F'
	
	
	def __init__(self, port):
		"""This is a constructor that creates an instance of Robot by
			creating a serial connection betwen the robot and users machine.
			NOTE: COM port often changes.

		Args:
			port (str): COM port establishing serial connection between the 
				robot and machine.
		"""
		try:
			self.serial_connection = serial.Serial(port, baudrate=115200,timeout =1)
			print ("Connected!")
		except serial.SerialException:
			print ("Connection failure!")
		time.sleep(1)
		self.serial_connection.close()
		time.sleep(1)
		self.serial_connection.open()

	def sendCommand(self, input):
		"""Method used to format sending a command to the robot using
			.write to write a command through the serial connection.

		Args:
			input (bytes): Variable containing the byte of the HEX OPCODE value.
		"""
		self.serial_connection.write(input)

	def read(self, howManyBytes : int = 1) -> str:
		"""Method used to return and print the binary sent from the robot to
			the user's machine.

		Args:
			howManyBytes (int, optional): Number of expected bytes. Defaults to 1.

		Returns:
			str: Binary representation of information outputted by the robot.
		"""
		if howManyBytes == 1:
			buttonState = self.serial_connection.read(1)
			time.sleep(0.5)
			byte = struct.unpack("B", buttonState)[0]
			binary = "{0:08b}".format(byte)

			return "Binary: "+ binary

		if howManyBytes == 2:
			buttonState = self.serial_connection.read(1)
			time.sleep(0.5)
			buttonState2 = self.serial_connection.read(1)
			time.sleep(0.5)
			byte = struct.unpack("B", buttonState)[0]
			highByte = "{0:08b}".format(byte)
			byte2 = struct.unpack("B", buttonState)[0]
			lowByte = "{0:08b}".format(byte2)

			return "Binary "+ highByte + "" + lowByte

	def start(self):
		"""Start command to prime the robot for actions.
		"""
		self.sendCommand(self.start_cmd)

	def stop(self):
		"""Stop command to halt current communication with the robot.
		"""
		self.sendCommand(self.stop_cmd)

	def reset(self):
		"""Reset command to reset the robot.
		"""
		self.sendCommand(self.reset_cmd)
		time.sleep(1)

	def safe(self):
		"""Safe command to put the robot into safe mode.
			Specifically, the robot will act until a sensor is triggered.
		"""
		self.sendCommand(self.safe_cmd)
		time.sleep(0.5)

	def seekDock(self):
		"""Seek dock command to have the robot find its dock.
		"""
		self.sendCommand(self.seek_dock_cmd)

	def drive(self, velocityHighByte, velocityLowByte, radiusHighByte, radiushLowByte):
		"""Drive command that moves the robot with both wheels at the same velocity
			and allows the choice of turning depending on the provided radius bytes.
			NOTE: This includes negative values of each input, using 2's complement.

		Args:
			velocityHighByte (bytes): 		Second velocity byte to be inputted.
			velocityLowByte (bytes): 		First velocity byte to be inputted. 
			radiusHighByte (bytes): 		Second radius byte to be inputted.
			radiushLowByte (bytes): 		First radius byte to be inputted.
		"""
		self.sendCommand(self.drive_cmd + \
			velocityHighByte + velocityLowByte + \
			radiusHighByte + radiushLowByte)

	def driveDirect(self, rightWheelHighByte, rightWheelLowByte, leftWheelHighByte, leftWheelLowByte):
		"""Drive direct command that allows the user to control each of the robot's
			wheels individually.
			NOTE: This includes negative values of each input, using 2's complement.

		Args:
			rightWheelHighByte (bytes): 	Second right-wheel byte to be inputted.
			rightWheelLowByte (bytes): 		First right-wheel byte to be inputted.
			leftWheelHighByte (bytes): 		Second left-wheel byte to be inputted.
			leftWheelLowByte (bytes): 		First left-wheel byte to be inputted.
		"""
		self.sendCommand(self.drive_direct_cmd + \
			rightWheelHighByte + rightWheelLowByte + \
			leftWheelHighByte + leftWheelLowByte)

	def leds(self, ledBits, powerColor, powerIntensity):
		"""LEDs command that allows the user to control the LED light found in
			the center of the robot.

		Args:
			ledBits (bytes): 				Situation of light.
			powerColor (bytes): 			Color of the light.
			powerIntensity (bytes): 		Intensity of light.
		"""
		self.sendCommand(self.leds_cmd + \
			ledBits + powerColor + powerIntensity)

	def digitLEDsASCII(self, digit3, digit2, digit1, digit0):
		"""ASCII LEDs command that allows the user to control the four
			seven-segment digit LEDs found on the top of the robot.

		Args:
			digit3 (bytes): 				Fourth digit LED.
			digit2 (bytes): 				Third digit LED.
			digit1 (bytes): 				Second digit LED.
			digit0 (bytes): 				First digit LED.
		"""
		self.sendCommand(self.leds_ascii_cmd + \
			digit3 + digit2 + digit1 + digit0)
