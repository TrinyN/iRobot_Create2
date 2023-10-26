"""
Author:             Triny Nguyen and Ethan Scott
Date Created:       10/19/2023
Last Editted:       10/  /2023

Purpose:            ...

Sample Run:         ...

Sample Output:      ...

# tkinter
# creating listeners that looks whether a button is pressed; code based on these
...

"""
import tkinter
from tkinter import *
from functools import partial
import threading
from PIL import Image, ImageTk
import keyboard
from Robot import Robot
import re

# Establish connection and prime robot
robot = Robot("COM9")
robot.start()
robot.safe()

# Creating a root widget (i.e. a window)
root = Tk()
root.title("Roomba")
root.configure(background="white")
root.minsize(1920, 1080)                                # Minimum width and height
root.maxsize(1920, 1080)
root.geometry("1920x1080+0+0")                          # Set actual width x height and starting point
root.resizable=FALSE
root.state('zoomed')                                    # Automatically set to fullscreen

# Creating a frame for the canvas
canvas_frame = Frame(root)
canvas_frame.pack()

# Create a canvas for the .png image (allows transparent background)
canvas = Canvas(canvas_frame, bg="purple", width=1920, height=1080)
canvas.pack()

# Creating images at different angles
pil_roombaPic_N = Image.open('create2sm.png')           # Pillow version of original image
pil_roombaPic_NE = pil_roombaPic_N.rotate(45)
pil_roombaPic_E = pil_roombaPic_N.rotate(90)
pil_roombaPic_SE = pil_roombaPic_N.rotate(135)
pil_roombaPic_S = pil_roombaPic_N.rotate(180)
pil_roombaPic_SW = pil_roombaPic_N.rotate(225)
pil_roombaPic_W = pil_roombaPic_N.rotate(270)
pil_roombaPic_NW = pil_roombaPic_N.rotate(315)

roombaPic_N = ImageTk.PhotoImage(pil_roombaPic_N)       # Convert all pillow images to PhotoImage's
roombaPic_NE = ImageTk.PhotoImage(pil_roombaPic_NW)
roombaPic_E = ImageTk.PhotoImage(pil_roombaPic_W)
roombaPic_SE = ImageTk.PhotoImage(pil_roombaPic_SW)
roombaPic_S = ImageTk.PhotoImage(pil_roombaPic_S)
roombaPic_SW = ImageTk.PhotoImage(pil_roombaPic_SE)
roombaPic_W = ImageTk.PhotoImage(pil_roombaPic_E)
roombaPic_NW = ImageTk.PhotoImage(pil_roombaPic_NE)

canvas.create_image(770,440,image=roombaPic_N)          # Placing the default image on the canvas

#######LED Buttons######
def LED(color):
    """Method that handles users choosing one of the different color options
    and will change the robot's central LED accordingly.

    Args:
        color (str):                    Color returned by corresponding button
    """
    if color == "green":
        robot.leds(b'\x04',b'\x00',b'\xFF')
        print("green")
    elif color == "yellow":
        robot.leds(b'\x04',b'\x05',b'\xFF')
        print("yellow")
    elif color == "orange":
        robot.leds(b'\x04',b'\x30',b'\xFF')
        print("orange")
    elif color == "red":
        robot.leds(b'\x04',b'\xFF',b'\xFF')
        print("red")
    else:
        print("error")

# Create a frame to surround the color buttons
color_frame = Frame(root, bg="white", width=400, height=100)  # Adjust parameters as needed
color_frame.place(x = 30, y = 30)

# Create a label to hold all of the color buttons
text = Label(color_frame, text="Clean/Power LED", pady = 5, bg="white", font=("Georgia", 16))
text.pack()

# Color buttons
LED_GREEN = Button(color_frame, bg="green", text="    ", command=partial(LED, "green"))
LED_YELLOW = Button(color_frame, bg="yellow", text="    ", command=partial(LED, "yellow"))
LED_ORANGE = Button(color_frame, bg="orange", text="    ", command=partial(LED, "orange"))
LED_RED = Button(color_frame, bg="red", text="    ", command=partial(LED, "red"))

LED_GREEN.pack(side=LEFT, padx=10)
LED_YELLOW.pack(side=LEFT, padx=10)
LED_ORANGE.pack(side=LEFT, padx=10)
LED_RED.pack(side=RIGHT, padx=10)

############WASD########
# Create a frame to surround the wasd buttons
wasd_frame = Frame(root, bg="white", width=400, height=100)  # Adjust parameters as needed
wasd_frame.place(x = 30, y = 640)

# Create a frame to surround the wasd buttons
wasd_frame = Frame(root, bg="white", width=400, height=100)  # Adjust parameters as needed
wasd_frame.place(x = 30, y = 640)

# Create buttons with text labels
w_button = Button(wasd_frame, text="W", command=lambda: handle_input('W'), width=6, height=3)
a_button = Button(wasd_frame, text="A", command=lambda: handle_input('A'), width=6, height=3)
s_button = Button(wasd_frame, text="S", command=lambda: handle_input('S'), width=6, height=3)
d_button = Button(wasd_frame, text="D", command=lambda: handle_input('D'), width=6, height=3)

# Position buttons to resemble a keyboard layout
w_button.grid(row=0, column=1, padx=10)
a_button.grid(row=1, column=0, pady=10)
s_button.grid(row=1, column=1, pady=10)
d_button.grid(row=1, column=2, pady=10)

def handle_input(key):
    """Method that handles the user clicking on the on-screen WASD buttons.
        NOTE: This does not allow the robot as many degrees of movement as the keyboard.

    Args:
        key (str):                      Key chosen on-screen
    """
    if key == 'W':
        robot.driveDirect(b'\x00', b'\x64', b'\x00', b'\x64')
        canvas.delete(canvas.find_closest(770,440))
        canvas.create_image(770,440,image=roombaPic_N)
        print("Driving Forward...")
    elif key == 'S':
        robot.driveDirect(b'\xFF', b'\xC0', b'\xFF', b'\xC0')
        canvas.delete(canvas.find_closest(770,440))
        canvas.create_image(770,440,image=roombaPic_S)
        print("Driving Backwards...")
    elif key == 'A':
        robot.driveDirect(b'\x00', b'\x64', b'\xFF', b'\x9C') # rotate counter-clockwise
        canvas.delete(canvas.find_closest(770,440))
        canvas.create_image(770,440,image=roombaPic_W)

        print("Driving Left...")
    elif key == 'D':
        robot.driveDirect(b'\xFF', b'\x9C', b'\x00', b'\x64') # rotate clockwise
        canvas.delete(canvas.find_closest(770,440))
        canvas.create_image(770,440,image=roombaPic_E)

    elif key == " ":
        print("Stop!")

W = FALSE
A = FALSE
S = FALSE
D = FALSE
SPACE = FALSE

def handle_keyboard_input():
    """Method that handles user's inputs of movement through the keyboard. The imported
        keyboard module is used to track the user's inputs.
        NOTE: There is more freedom of movement in using the keyboard. Specifically,
            the user may now choose to move two directions at once, if they allow.
    """
    global W, A, S, D, SPACE
    # ADD ARROWS
    # add caps version?
    # add buttons pressed
    while True:
        # Driving forwards
        if (
            (keyboard.is_pressed("w") or keyboard.is_pressed("up arrow")) and not \
            (keyboard.is_pressed("a") or keyboard.is_pressed("left arrow")) and not \
            (keyboard.is_pressed("d") or keyboard.is_pressed("right arrow")) and not \
            (keyboard.is_pressed("s") or keyboard.is_pressed("down arrow"))
        ):
            if not W:
                W = True
                robot.driveDirect(b'\x00', b'\x64', b'\x00', b'\x64')
                canvas.delete(canvas.find_closest(770,440))
                canvas.create_image(770,440,image=roombaPic_N)
                print("Driving Forward...")

        # Driving backwards
        elif (
            (keyboard.is_pressed("s") or keyboard.is_pressed("down arrow")) and not \
            (keyboard.is_pressed("a") or keyboard.is_pressed("left arrow")) and not \
            (keyboard.is_pressed("d") or keyboard.is_pressed("right arrow")) and not \
            (keyboard.is_pressed("w") or keyboard.is_pressed("up arrow"))
        ):
            if not S:
                S = True
                robot.driveDirect(b'\xFF', b'\xC0', b'\xFF', b'\xC0')
                canvas.delete(canvas.find_closest(770,440))
                canvas.create_image(770,440,image=roombaPic_S)
                print("Driving Backwards...")

        # Turning left
        elif (
            (keyboard.is_pressed("a") or keyboard.is_pressed("left arrow")) and not \
            (keyboard.is_pressed("w") or keyboard.is_pressed("up arrow")) and not \
            (keyboard.is_pressed("s") or keyboard.is_pressed("down arrow")) and not \
            (keyboard.is_pressed("d") or keyboard.is_pressed("right arrow"))
        ):
            if not A:
                A = True
                robot.driveDirect(b'\x00', b'\x64', b'\xFF', b'\x9C')
                canvas.delete(canvas.find_closest(770,440))
                canvas.create_image(770,440,image=roombaPic_W)
                print("Driving Left...")

        # Turning right
        elif (
            (keyboard.is_pressed("d") or keyboard.is_pressed("right arrow")) and not \
            (keyboard.is_pressed("w") or keyboard.is_pressed("up arrow")) and not \
            (keyboard.is_pressed("s") or keyboard.is_pressed("down arrow")) and not \
            (keyboard.is_pressed("a") or keyboard.is_pressed("left arrow"))
        ):
            if not D:
                D = True
                robot.driveDirect(b'\xFF', b'\x9C', b'\x00', b'\x64')
                canvas.delete(canvas.find_closest(770,440))
                canvas.create_image(770,440,image=roombaPic_E)
                print("Driving Right...")

        # Moving forward and left
        elif (keyboard.is_pressed("w") or keyboard.is_pressed("up arrow")) and \
            (keyboard.is_pressed("a") or keyboard.is_pressed("left arrow")):
            if not W or not A:
                W = True
                A = True
                robot.driveDirect(b'\x00', b'\xA4', b'\x00', b'\x64')
                canvas.delete(canvas.find_closest(770,440))
                canvas.create_image(770,440,image=roombaPic_NW)
                print("W and A Driving...")

        # Mving forward and right
        elif (keyboard.is_pressed("w") or keyboard.is_pressed("up arrow")) and \
            (keyboard.is_pressed("d") or keyboard.is_pressed("right arrow")):
            if not W or not D:
                W = True
                D = True
                robot.driveDirect(b'\x00', b'\x64', b'\x00', b'\xA4')
                canvas.delete(canvas.find_closest(770,440))
                canvas.create_image(770,440,image=roombaPic_NE)
                print("W and D Driving...")

        # Moving backwards and left
        elif (keyboard.is_pressed("s") or keyboard.is_pressed("down arrow")) and \
            (keyboard.is_pressed("a") or keyboard.is_pressed("left arrow")):
            if not S or not A:
                S = True
                A = True
                robot.driveDirect(b'\xFF', b'\x51', b'\xFF', b'\xC0')
                canvas.delete(canvas.find_closest(770,440))
                canvas.create_image(770,440,image=roombaPic_SW)
                print("S and A Driving...")

        # Moving backwards and right
        elif (keyboard.is_pressed("s") or keyboard.is_pressed("down arrow")) and \
            (keyboard.is_pressed("d") or keyboard.is_pressed("right arrow")):
            if not S or not D:
                S = True
                D = True
                robot.driveDirect(b'\xFF', b'\xC0', b'\xFF', b'\x51')
                canvas.delete(canvas.find_closest(770,440))
                canvas.create_image(770,440,image=roombaPic_SE)
                print("S and D Driving...")

        # 
        elif keyboard.is_pressed(" "):
                    if not SPACE:
                        SPACE = True
                        robot.driveDirect(b'xFF', b'xC0', b'xFF', b'x51')
                        canvas.delete(canvas.find_closest(770,440))
                        canvas.create_image(770,440,image=roombaPic_N)
                        print("Boost Driving...")
        # Finished with keyboard inputs
        elif keyboard.is_pressed("esc"):
            break

        else:
            if W or A or S or D:
                W = False
                A = False
                S = False
                D = False
                robot.driveDirect(b'\x00', b'\x00', b'\x00', b'\x00')
                canvas.delete(canvas.find_closest(770,440))
                canvas.create_image(770,440,image=roombaPic_N)
                print("Stop!")

########## digits W.I.P. #############
def handle_enter_key_press(event):
    """_summary_

    Args:
        event (_type_): _description_
    """
    input_text = four_digit_input.get()[:4]                 # Gets the first 4 characters
    print("Enter key pressed. Input:", input_text)


# If the first 4 characters are all numbers, display LED
    if re.search(r'\d{4}', input_text):
        # Convert the digits to integers
        digit1 = int(input_text[0])
        digit2 = int(input_text[1])
        digit3 = int(input_text[2])
        digit4 = int(input_text[3])


        # Convert the integers to hexadecimal
        hex1 = hex(digit1 + 48)
        hex2 = hex(digit2 + 48)
        hex3 = hex(digit3 + 48)
        hex4 = hex(digit4 + 48)

        # Convert the hexadecimal to bytes
        num1 = bytes([int(hex1, 16)])
        num2 = bytes([int(hex2, 16)])
        num3 = bytes([int(hex3, 16)])
        num4 = bytes([int(hex4, 16)])

        robot.digitLEDsASCII(num1, num2, num3, num4)
    else:
        print("Invalid Input")

# Create a frame to surround the 4 digit input; Adj parameters as needed
four_digit_frame = Frame(root, bg="white", width=400, height=100)
four_digit_frame.place(x = 30, y = 250)

# Create an entry box to take in input
four_digit_input = Entry(four_digit_frame, width=4, font=("Georgia", 30), \
                         bg="black", fg="white", insertbackground="white")
four_digit_input.pack(side=LEFT, padx=10)

four_digit_input.bind("<Return>", handle_enter_key_press)
######################################

keyboard_thread = threading.Thread(target=handle_keyboard_input)
keyboard_thread.start()

################MUSIC##################
def play_music():
    robot.playHappyBirthday()

# Create a frame to hold the play button
play_button_frame = Frame(root, bg="white", width=400, height=100)
play_button_frame.place(x=1430, y=20)

# Load the play button icon image
play_icon_image = PhotoImage(file="playButton.png")

# Create the play button using the image
play_button = Button(play_button_frame, image=play_icon_image, bg="white", command=play_music)
play_button.pack()

################BOOST BUTTON###############

# Create a frame to hold the play button
boost_button_frame = Frame(root, bg="white", width=400, height=100)
boost_button_frame.place(x=1430, y=670)

# Load the play button icon image
boost_icon_image = PhotoImage(file="boostIcon.png")

# Create the play button using the image
boost_button = Button(boost_button_frame, image=boost_icon_image, bg="white", command=play_music)
boost_button.pack()

root.mainloop()
