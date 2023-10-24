"""
Author:
Date Created:
Last Editted:

# tkinter
# creating listeners that looks whether a button is pressed; code based on these
...

"""
import tkinter
from tkinter import *
from PIL import Image, ImageTk
from pynput import keyboard
from functools import partial
import keyboard
import threading
from Robot import Robot

robot = Robot("COM11")
robot.start()
robot.safe()

root = Tk()  # create a root widget
root.title("Roomba")
root.configure(background="white")
root.minsize(1920, 1080)  # width, height
root.maxsize(1920, 1080)
root.geometry("1920x1080+0+0")  # width x height + x + y
root.resizable=FALSE
root.state('zoomed') # automatically fullscreen

frame = Frame(root)
frame.pack()

# Canvas must be made and used to prevent background color
canvas = Canvas(frame, bg="purple", width=1920, height=1080)
canvas.pack()

# Creating images at different angles
pil_roombaPic_N = Image.open('create2sm.png')
pil_roombaPic_NE = pil_roombaPic_N.rotate(45)
pil_roombaPic_E = pil_roombaPic_N.rotate(90)
pil_roombaPic_SE = pil_roombaPic_N.rotate(135)
pil_roombaPic_S = pil_roombaPic_N.rotate(180)
pil_roombaPic_SW = pil_roombaPic_N.rotate(225)
pil_roombaPic_W = pil_roombaPic_N.rotate(270)
pil_roombaPic_NW = pil_roombaPic_N.rotate(315)

roombaPic_N = ImageTk.PhotoImage(pil_roombaPic_N)
roombaPic_NE = ImageTk.PhotoImage(pil_roombaPic_NW)
roombaPic_E = ImageTk.PhotoImage(pil_roombaPic_W)
roombaPic_SE = ImageTk.PhotoImage(pil_roombaPic_SW)
roombaPic_S = ImageTk.PhotoImage(pil_roombaPic_S)
roombaPic_SW = ImageTk.PhotoImage(pil_roombaPic_SE)
roombaPic_W = ImageTk.PhotoImage(pil_roombaPic_E)
roombaPic_NW = ImageTk.PhotoImage(pil_roombaPic_NE)

canvas.create_image(770,440,image=roombaPic_N)

#######LED Buttons######
def LED(color):
    if color == "green":
        robot.leds(b'\x04',b'\x00',b'\xFF')
        print("green")
    elif color == "yellow":
        robot.leds(b'\x04',b'\x5F',b'\xFF')
        print("yellow")
    elif color == "orange":
        robot.leds(b'\x04',b'\xBF',b'\xFF')
        print("orange")
    elif color == "red":
        robot.leds(b'\x04',b'\xFF',b'\xFF')
        print("red")
    else:
        print("error")

# Create a frame to surround the color buttons
color_frame = Frame(root, bg="white", width=400, height=100)  # Adjust width and height as needed
color_frame.place(x = 30, y = 30)


text = Label(color_frame, text="Clean/Power LED", pady = 5, bg="white", font=("Georgia", 16))
text.pack()

LED_GREEN = Button(color_frame, bg="green", text="    ", command=partial(LED, "green"))
LED_YELLOW = Button(color_frame, bg="yellow", text="    ", command=partial(LED, "yellow"))
LED_ORANGE = Button(color_frame, bg="orange", text="    ", command=partial(LED, "orange"))
LED_RED = Button(color_frame, bg="red", text="    ", command=partial(LED, "red"))

LED_GREEN.pack(side=LEFT, padx=10)
LED_YELLOW.pack(side=LEFT, padx=10)
LED_ORANGE.pack(side=RIGHT, padx=10)
LED_RED.pack(side=RIGHT, padx=10)

############WASD########
# Create a frame to surround the wasd buttons
wasd_frame = Frame(root, bg="white", width=400, height=100)  # Adjust width and height as needed
wasd_frame.place(x = 30, y = 640)

# Create a frame to surround the wasd buttons
wasd_frame = Frame(root, bg="white", width=400, height=100)  # Adjust width and height as needed
wasd_frame.place(x = 30, y = 640)

W = FALSE
A = FALSE
S = FALSE
D = FALSE

# def handle_w_button_press():
#     global W
#     W = True

# def handle_w_button_release():
#     global W
#     W = False

# w_button = Button(wasd_frame, text="W", command=handle_w_button_press, width=6, height=3)
# w_button.bind('<ButtonRelease-1>', lambda event: handle_w_button_release())
    

# # Create buttons with text labels
# w_button = Button(wasd_frame, text="W", command=lambda: handle_input('W'), width=6, height=3)
# a_button = Button(wasd_frame, text="A", command=lambda: handle_input('A'), width=6, height=3)
# s_button = Button(wasd_frame, text="S", command=lambda: handle_input('S'), width=6, height=3)
# d_button = Button(wasd_frame, text="D", command=lambda: handle_input('D'), width=6, height=3)

# # Position buttons to resemble a keyboard layout
# w_button.grid(row=0, column=1, padx=10)
# a_button.grid(row=1, column=0, pady=10)
# s_button.grid(row=1, column=1, pady=10)
# d_button.grid(row=1, column=2, pady=10)


# def handle_input(key):
#     if key == 'W':
#         print("Driving Forward...")

#     elif key == 'A':
#         print("Driving Left...")

#     elif key == 'S':
#         print("Driving Backwards...")

#     elif key == 'D':
#         print("Driving Right...")

#     else:
#         print("stop!")

def handle_input(key):
    if key == 'W':
        print("Driving Forward...")
    elif key == 'A':
        print("Driving Left...")

    elif key == 'S':
        print("Driving Backwards...")

    elif key == 'D':
        print("Driving Right...")

    elif key == " ":
        print("Stop!")

W = FALSE
A = FALSE
S = FALSE
D = FALSE

def handle_keyboard_input():
    global W, A, S, D
    # ADD ARROWS
    # add caps version?
    # add buttons pressed
    while True:
        if (
            keyboard.is_pressed("w") or keyboard.is_pressed("up arrow")
            and not (keyboard.is_pressed("a") or keyboard.is_pressed("left arrow"))
            and not (keyboard.is_pressed("d") or keyboard.is_pressed("right arrow"))
            and not (keyboard.is_pressed("s") or keyboard.is_pressed("down arrow"))

        ):
            if not W:
                W = True
                robot.driveDirect(b'\x00', b'\x64', b'\x00', b'\x64')
                canvas.delete(canvas.find_closest(770,440))
                canvas.create_image(770,440,image=roombaPic_N)
                print("Driving Forward...")

        elif (
            keyboard.is_pressed("s") or keyboard.is_pressed("down arrow")
            and not (keyboard.is_pressed("a") or keyboard.is_pressed("left arrow"))
            and not (keyboard.is_pressed("d") or keyboard.is_pressed("right arrow"))
            and not (keyboard.is_pressed("w") or keyboard.is_pressed("up arrow"))
        ):
            if not S:
                S = True
                robot.driveDirect(b'\xFF', b'\xC0', b'\xFF', b'\xC0')
                canvas.delete(canvas.find_closest(770,440))
                canvas.create_image(770,440,image=roombaPic_S)
                print("Driving Backwards...")

        elif (
            keyboard.is_pressed("a") or keyboard.is_pressed("left arrow")
            and not (keyboard.is_pressed("w") or keyboard.is_pressed("up arrow"))
            and not (keyboard.is_pressed("s") or keyboard.is_pressed("down arrow"))
            and not (keyboard.is_pressed("d") or keyboard.is_pressed("right arrow"))
        ):
            if not A:
                A = True
                canvas.delete(canvas.find_closest(770,440))
                canvas.create_image(770,440,image=roombaPic_W)
                print("Driving Left...")

        elif (
            keyboard.is_pressed("d") or keyboard.is_pressed("right arrow")
            and not (keyboard.is_pressed("w") or keyboard.is_pressed("up arrow"))
            and not (keyboard.is_pressed("s") or keyboard.is_pressed("down arrow"))
            and not (keyboard.is_pressed("a") or keyboard.is_pressed("left arrow"))
        ):
            if not D:
                D = True
                canvas.delete(canvas.find_closest(770,440))
                canvas.create_image(770,440,image=roombaPic_E)
                print("Driving Right...")

        elif (keyboard.is_pressed("w") or keyboard.is_pressed("up arrow")) and (keyboard.is_pressed("a") or keyboard.is_pressed("left arrow")):
            if not W or not A:
                W = True
                A = True
                canvas.delete(canvas.find_closest(770,440))
                canvas.create_image(770,440,image=roombaPic_NW)
                print("W and A Driving...")

        elif (keyboard.is_pressed("w") or keyboard.is_pressed("up arrow")) and (keyboard.is_pressed("d") or keyboard.is_pressed("right arrow")):
            if not W or not D:
                W = True
                D = True
                canvas.delete(canvas.find_closest(770,440))
                canvas.create_image(770,440,image=roombaPic_NE)
                print("W and D Driving...")

        elif (keyboard.is_pressed("s") or keyboard.is_pressed("down arrow")) and (keyboard.is_pressed("a") or keyboard.is_pressed("left arrow")):
            if not S or not A:
                S = True
                A = True
                canvas.delete(canvas.find_closest(770,440))
                canvas.create_image(770,440,image=roombaPic_SW)
                print("S and A Driving...")

        elif (keyboard.is_pressed("s") or keyboard.is_pressed("down arrow")) and (keyboard.is_pressed("d") or keyboard.is_pressed("right arrow")):
            if not S or not D:
                S = True
                D = True
                canvas.delete(canvas.find_closest(770,440))
                canvas.create_image(770,440,image=roombaPic_SE)
                print("S and D Driving...")

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
    input_text = four_digit_input.get()[:4]  # gets the first 4 characters
    print("Enter key pressed. Input:", input_text) 


# if first 4 characters are all numbers, display LED
    if re.search(r'\d{4}', input_text):

        # Convert the digits to integers
        digit1 = int(digit1)
        digit2 = int(digit2)
        digit3 = int(digit3)
        digit4 = int(digit4)

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

        robot.digitLEDsASCII(num4, num3, num2, num1)
    else:
        print("Invalid Input")

# Create a frame to surround the 4 digit input
four_digit_frame = Frame(root, bg="white", width=400, height=100)  # Adjust width and height as needed
four_digit_frame.place(x = 30, y = 250)

# Create an entry box to take in input
four_digit_input = Entry(four_digit_frame, width=4, font=("Georgia", 30), bg="black", fg="white", insertbackground="white")
four_digit_input.pack(side=LEFT, padx=10)

four_digit_input.bind("<Return>", handle_enter_key_press)
######################################

keyboard_thread = threading.Thread(target=handle_keyboard_input)
keyboard_thread.start()

root.mainloop()
