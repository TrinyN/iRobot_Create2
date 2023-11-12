"""
Author:             Triny Nguyen and Ethan Scott
Date Created:       10/19/2023
Last Editted:       10/  /2023

Purpose:            This file includes all of the code to create a window that a user
                    will be able to use to control the robot, including driving it,
                    changing its LED light color(s), changing its ASCII LED,
                    and more.

Sample Run:         c:/Users/escot/vscode-workspace/Project4.py

Sample Output:      Connected!
                    "Invalid Input"
"""
import tkinter
from tkinter import *
from functools import partial
import threading
import re
from PIL import Image, ImageTk
import keyboard
from Robot import Robot

W = A = S = D = SPACE = FALSE

######################################### LED Buttons #############################################
def LED(color):
    """Method that handles users choosing one of the different color options
    and will change the robot's central LED accordingly.

    Args:
        color (str):                    Color returned by corresponding button
    """
    if color == "green":
        robot.leds(b"\x04", b"\x00", b"\xFF")
    elif color == "yellow":
        robot.leds(b"\x04", b"\x05", b"\xFF")
    elif color == "orange":
        robot.leds(b"\x04", b"\x30", b"\xFF")
    elif color == "red":
        robot.leds(b"\x04", b"\xFF", b"\xFF")
    else:
        print("error")

############################################## End ################################################

###################################### On-Screen Movement Keys #####################################

def w_button_press():
    """Method that handles the on-screen w key being pressed."""
    robot.driveDirect(b"\x02", b"\x58", b"\x02", b"\x58")
    canvas.delete(canvas.find_closest(770, 440))
    canvas.create_image(770, 440, image=roombaPic_N)


def s_button_press():
    """Method that handles the on-screen s key being pressed."""
    robot.driveDirect(b"\xFF", b"\x38", b"\xFF", b"\x38")
    canvas.delete(canvas.find_closest(770, 440))
    canvas.create_image(770, 440, image=roombaPic_S)


def a_button_press():
    """Method that handles the on-screen a key being pressed."""
    robot.driveDirect(b"\x00", b"\xC8", b"\xFF", b"\x38")
    canvas.delete(canvas.find_closest(770, 440))
    canvas.create_image(770, 440, image=roombaPic_W)


def d_button_press():
    """Method that handles the on-screen d key being pressed."""
    robot.driveDirect(b"\xFF", b"\x38", b"\x00", b"\xC8")
    canvas.delete(canvas.find_closest(770, 440))
    canvas.create_image(770, 440, image=roombaPic_E)


def wa_button_press():
    """Method that handles the on-screen wa key being pressed."""
    robot.driveDirect(b"\x02", b"\x58", b"\x01", b"\x5E")
    canvas.delete(canvas.find_closest(770, 440))
    canvas.create_image(770, 440, image=roombaPic_NW)


def wd_button_press():
    """Method that handles the on-screen wd key being pressed."""
    robot.driveDirect(b"\x01", b"\x5E", b"\x02", b"\x58")
    canvas.delete(canvas.find_closest(770, 440))
    canvas.create_image(770, 440, image=roombaPic_NE)


def sa_button_press():
    """Method that handles the on-screen sa key being pressed."""
    robot.driveDirect(b"\xFE", b"\xA2", b"\xFF", b"\x06")
    canvas.delete(canvas.find_closest(770, 440))
    canvas.create_image(770, 440, image=roombaPic_SW)


def sd_button_press():
    """Method that handles the on-screen sd key being pressed."""
    robot.driveDirect(b"\xFF", b"\x06", b"\xFE", b"\xA2")
    canvas.delete(canvas.find_closest(770, 440))
    canvas.create_image(770, 440, image=roombaPic_SE)


def button_release():
    """Method that handles any on-screen buttons being released."""
    robot.driveDirect(b"\x00", b"\x00", b"\x00", b"\x00")
    canvas.delete(canvas.find_closest(770, 440))
    canvas.create_image(770, 440, image=roombaPic_N)


def boost_button_press():
    """Method that handles the user clicking on the on-screen boost buttons."""
    # robot.driveDirect(b'\x01',b'\xF4',b'\x01',b'\xF4')
    robot.driveDirect(b"xFF", b"xC0", b"xFF", b"x51")
    canvas.delete(canvas.find_closest(770, 440))
    canvas.create_image(770, 440, image=roombaPic_N)

############################################### End ################################################

################################# Physical Keyboard Movement Keys ##################################
def get_command():
    w_pressed = keyboard.is_pressed("w") or keyboard.is_pressed("up arrow")
    a_pressed = keyboard.is_pressed("a") or keyboard.is_pressed("left arrow")
    s_pressed = keyboard.is_pressed("s") or keyboard.is_pressed("down arrow")
    d_pressed = keyboard.is_pressed("d") or keyboard.is_pressed("right arrow")

    if w_pressed and a_pressed:
        print("diagonal")
        canvas.delete(canvas.find_closest(770, 440))
        canvas.create_image(770, 440, image=roombaPic_NW)
        return b"\x02", b"\x58", b"\x01", b"\x5E"
        # return "wa"  # Driving diagonally forward-left
    elif w_pressed and d_pressed:
        print("diagonal")
        canvas.delete(canvas.find_closest(770, 440))
        canvas.create_image(770, 440, image=roombaPic_NE)
        return b"\x01", b"\x5E", b"\x02", b"\x58"
        # return "wd"  # Driving diagonally forward-right
    elif s_pressed and a_pressed:
        print("diagonal")
        canvas.delete(canvas.find_closest(770, 440))
        canvas.create_image(770, 440, image=roombaPic_SW)
        return b"\xFE", b"\xA2", b"\xFF", b"\x06"
        # return "sa"  # Driving diagonally backward-left
    elif s_pressed and d_pressed:
        print("diagonal")
        canvas.delete(canvas.find_closest(770, 440))
        canvas.create_image(770, 440, image=roombaPic_SE)
        return b"\xFF", b"\x06", b"\xFE", b"\xA2"
        # return "sd"  # Driving diagonally backward-right
    elif w_pressed:
        canvas.delete(canvas.find_closest(770, 440))
        canvas.create_image(770, 440, image=roombaPic_N)
        # return b"\x02", b"\x58", b"\x02", b"\x58"
        return "w"  # Driving forwards
    elif a_pressed:
        canvas.delete(canvas.find_closest(770, 440))
        canvas.create_image(770, 440, image=roombaPic_W)
        # return b"\x00", b"\xC8", b"\xFF", b"\x38"
        return "a"  # Driving left
    elif s_pressed:
        canvas.delete(canvas.find_closest(770, 440))
        canvas.create_image(770, 440, image=roombaPic_S)
        # return b"\xFF", b"\x38", b"\xFF", b"\x38"
        return "s"  # Driving backward
    elif d_pressed:
        canvas.delete(canvas.find_closest(770, 440))
        canvas.create_image(770, 440, image=roombaPic_E)
        # return b"\xFF", b"\x38", b"\x00", b"\xC8"
        return "d"  # Driving right
    else:
        canvas.delete(canvas.find_closest(770, 440))
        canvas.create_image(770, 440, image=roombaPic_N)
        # return b"\x00", b"\x00", b"\x00", b"\x00"  # Default stop command

def on_press(event):
    command = get_command()
    robot.driveDirect(command)     # POSSIBLE PROBLEM: format of command. if issue: try one b"\..\....""
    print("Key pressed:", event.name)

def on_release(event):
    command = get_command()
    robot.driveDirect(command)
    print("Key released:", event.name)

############################################### End ################################################

########################################### ASCII Digits ###########################################

def handle_enter_key_press(event):
    """Method to track when the user presses enter to choose
        the AASCII LED digits they want. It uses the first four.

    Args:
        event (str):                    The enter key
    """
    input_text = four_digit_input.get()[:4]  # Gets first 4 characters

    # If the first 4 characters are all numbers, display LED
    if re.search(r"\d{4}", input_text):
        # Convert the digits to integers
        digit1 = int(input_text[0])
        digit2 = int(input_text[1])
        digit3 = int(input_text[2])
        digit4 = int(input_text[3])

        # Convert the integers to ASCII and then to hexadecimal
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

############################################### End ################################################

############################################## Music ###############################################

def play_music():
    """Method to play the music used within in the Robot class. In our case that
    is the Happy Birthday song.
    """
    robot.playHappyBirthday()

############################################### End ################################################

################################## Setting up the main window ######################################

# Establish connection and prime robot
robot = Robot("COM9")
robot.start()
robot.safe()

# Creating a root widget (i.e. a window)
root = Tk()
root.title("Roomba")
root.configure(background="white")
root.geometry("1920x1080+0+0")
root.resizable = FALSE
root.state("zoomed")                               # Automatically set to fullscreen

# Creating a frame for the canvas
canvas_frame = Frame(root)
canvas_frame.pack()

# Create a canvas for the .png image (allows transparent background)
canvas = Canvas(canvas_frame, bg="white", width=1920, height=1080)
canvas.pack()

# Creating images at different angles
pil_roombaPic_N = Image.open("create2sm.png")      # Pillow version of original image
pil_roombaPic_NE = pil_roombaPic_N.rotate(45)
pil_roombaPic_E = pil_roombaPic_N.rotate(90)
pil_roombaPic_SE = pil_roombaPic_N.rotate(135)
pil_roombaPic_S = pil_roombaPic_N.rotate(180)
pil_roombaPic_SW = pil_roombaPic_N.rotate(225)
pil_roombaPic_W = pil_roombaPic_N.rotate(270)
pil_roombaPic_NW = pil_roombaPic_N.rotate(315)

roombaPic_N = ImageTk.PhotoImage(pil_roombaPic_N)  # Pillow images conv. to PhotoImages
roombaPic_NE = ImageTk.PhotoImage(pil_roombaPic_NW)
roombaPic_E = ImageTk.PhotoImage(pil_roombaPic_W)
roombaPic_SE = ImageTk.PhotoImage(pil_roombaPic_SW)
roombaPic_S = ImageTk.PhotoImage(pil_roombaPic_S)
roombaPic_SW = ImageTk.PhotoImage(pil_roombaPic_SE)
roombaPic_W = ImageTk.PhotoImage(pil_roombaPic_E)
roombaPic_NW = ImageTk.PhotoImage(pil_roombaPic_NE)

canvas.create_image(770, 440, image=roombaPic_N)   # Placing default image on canvas

# Create a frame to surround the color buttons, adjust sizes as needed
color_frame = Frame(root, bg="white", width=400, height=100)
color_frame.place(x=30, y=30)

# Create a label to hold all of the color buttons
text = Label(
    color_frame, text="Clean/Power LED", pady=5, bg="white", font=("Georgia", 16)
)
text.pack()

# Color buttons
LED_GREEN = Button(color_frame, bg="green", text="    ", command=partial(LED, "green"))
LED_YELLOW = Button(
    color_frame, bg="yellow", text="    ", command=partial(LED, "yellow")
)
LED_ORANGE = Button(
    color_frame, bg="orange", text="    ", command=partial(LED, "orange")
)
LED_RED = Button(color_frame, bg="red", text="    ", command=partial(LED, "red"))

LED_GREEN.pack(side=LEFT, padx=10)
LED_YELLOW.pack(side=LEFT, padx=10)
LED_ORANGE.pack(side=LEFT, padx=10)
LED_RED.pack(side=RIGHT, padx=10)

# Create a frame to surround the wasd buttons, adjust sizes as needed
wasd_frame = Frame(root, bg="white", width=400, height=400)
wasd_frame.place(x=30, y=600)

# Create a frame to hold the boost button
boost_button_frame = Frame(root, bg="white", width=400, height=100)
boost_button_frame.place(x=1430, y=730)

# Load the boost button icon image
boost_icon_image = PhotoImage(file="boostIcon.png")

# Create buttons with text labels
w_button = Button(wasd_frame, text="W", width=8, height=4)
a_button = Button(wasd_frame, text="A", width=8, height=4)
s_button = Button(wasd_frame, text="S", width=8, height=4)
d_button = Button(wasd_frame, text="D", width=8, height=4)
wa_button = Button(wasd_frame, text=" ", width=8, height=4)
wd_button = Button(wasd_frame, text=" ", width=8, height=4)
sa_button = Button(wasd_frame, text=" ", width=8, height=4)
sd_button = Button(wasd_frame, text=" ", width=8, height=4)
boost_button = Button(
    boost_button_frame, image=boost_icon_image, command=boost_button_press
)

w_button.bind("<ButtonPress>", lambda event: w_button_press())
w_button.bind("<ButtonRelease>", lambda event: button_release())

s_button.bind("<ButtonPress>", lambda event: s_button_press())
s_button.bind("<ButtonRelease>", lambda event: button_release())

a_button.bind("<ButtonPress>", lambda event: a_button_press())
a_button.bind("<ButtonRelease>", lambda event: button_release())

d_button.bind("<ButtonPress>", lambda event: d_button_press())
d_button.bind("<ButtonRelease>", lambda event: button_release())

wa_button.bind("<ButtonPress>", lambda event: wa_button_press())
wa_button.bind("<ButtonRelease>", lambda event: button_release())

wd_button.bind("<ButtonPress>", lambda event: wd_button_press())
wd_button.bind("<ButtonRelease>", lambda event: button_release())

sa_button.bind("<ButtonPress>", lambda event: sa_button_press())
sa_button.bind("<ButtonRelease>", lambda event: button_release())

sd_button.bind("<ButtonPress>", lambda event: sd_button_press())
sd_button.bind("<ButtonRelease>", lambda event: button_release())

# Create the boost button using the image
boost_button.pack()

# Position buttons to resemble a keyboard layout
w_button.grid(row=0, column=1, padx=5)
s_button.grid(row=2, column=1, pady=0)
a_button.grid(row=1, column=0, pady=5)
d_button.grid(row=1, column=2, pady=5)
wa_button.grid(row=0, column=0, pady=0)
wd_button.grid(row=0, column=2, pady=0)
sa_button.grid(row=2, column=0, pady=0)
sd_button.grid(row=2, column=2, pady=0)

# keyboard_thread = threading.Thread(target=handle_keyboard_input)
# keyboard_thread.start()

keyboard.on_press_key("w", on_press)
keyboard.on_release_key("w", on_release)
keyboard.on_press_key("a", on_press)
keyboard.on_release_key("a", on_release)
keyboard.on_press_key("d", on_press)
keyboard.on_release_key("d", on_release)
keyboard.on_press_key("s", on_press)
keyboard.on_release_key("s", on_release)
# keyboard.on_press_key("wa", on_press)       # Can't be used?
# keyboard.on_release_key("wa", on_release)
# keyboard.on_press_key("wd", on_press)
# keyboard.on_release_key("wd", on_release)
# keyboard.on_press_key("sa", on_press)
# keyboard.on_release_key("sa", on_release)
# keyboard.on_press_key("sd", on_press)
# keyboard.on_release_key("sd", on_release)

# Create a frame to surround the 4 digit input; Adj parameters as needed
four_digit_frame = Frame(root, bg="white", width=400, height=100)
four_digit_frame.place(x=30, y=150)

# Create a label to hold all of the color buttons
entry_label = Label(
    four_digit_frame, text="4 Digit ASCII LED", pady=5, bg="white", font=("Georgia", 16))
entry_label.pack()

# Create an entry box to take in input
four_digit_input = Entry(
    four_digit_frame,
    width=11,
    font=("Georgia", 17),
    bg="black",
    fg="white",
    insertbackground="white",
)
four_digit_input.pack(side=LEFT, padx=10)

four_digit_input.bind("<Return>", handle_enter_key_press)

# Create a frame to hold the play button
play_button_frame = Frame(root, bg="white", width=400, height=100)
play_button_frame.place(x=1430, y=20)

# Load the play button icon image
play_icon_image = PhotoImage(file="playButton.png")

# Create the play button using the image
play_button = Button(
    play_button_frame, image=play_icon_image, bg="white", command=play_music
)
play_button.pack()

root.mainloop()

############################################### End ################################################

############################################ End Class #############################################
