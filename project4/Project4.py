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
        print("green")
    elif color == "yellow":
        print("yellow")
    elif color == "orange":
        print("orange")
    elif color == "red":
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

def handle_keyboard_input():
    global W, A, S, D
    
    # add caps version?
    # add buttons pressed
    while True:
        if (
            keyboard.is_pressed("w")
            and not keyboard.is_pressed("a")
            and not keyboard.is_pressed("d")
            and not keyboard.is_pressed("s")

        ):
            if not W:
                W = True
                # handle_input('W')
                # robot.driveDirect(b'x00', b'xC8', b'x00', b'xC8')
                robot.driveDirect(b'\x00', b'\x64', b'\x00', b'\x64')

                # connection.write(b'\x80\x83')
                # time.sleep(0.5)
                # connection.write(DRIVE_FORWARD_200)
                canvas.create_image(770,440,image=roombaPic_N)
                print("Driving Forward...")

        elif (
            keyboard.is_pressed("s")
            and not keyboard.is_pressed("a")
            and not keyboard.is_pressed("d")
            and not keyboard.is_pressed("w")
        ):
            if not S:
                S = True
                # handle_input('S')
                canvas.create_image(770,440,image=roombaPic_S)
                print("Driving Backwards...")
                # robot.drive(b'xFF', b'x38', b'x7F', b'xFF')
                # robot.driveDirect(b'xFF', b'x38', b'xFF', b'x38')
                robot.driveDirect(b'\xFF', b'\xC0', b'\xFF', b'\xC0')
                # connection.write(b'\x80\x83')
                # time.sleep(0.5)
                # connection.write(DRIVE_BACKWARDS_200)



        elif (
            keyboard.is_pressed("a")
            and not keyboard.is_pressed("w")
            and not keyboard.is_pressed("s")
            and not keyboard.is_pressed("d")
        ):
            if not A:
                A = True
                # handle_input('A')
                canvas.create_image(770,440,image=roombaPic_W)

                print("Driving Left...")

        elif (
            keyboard.is_pressed("d")
            and not keyboard.is_pressed("w")
            and not keyboard.is_pressed("s")
            and not keyboard.is_pressed("a")
        ):
            if not D:
                D = True
                # handle_input('D')
                canvas.create_image(770,440,image=roombaPic_E)
                print("Driving Right...")

        elif keyboard.is_pressed("w") and keyboard.is_pressed("a"):
            if not W or not A:
                W = True
                A = True
                canvas.create_image(770,440,image=roombaPic_NW)
                print("W and A Driving...")

        elif keyboard.is_pressed("w") and keyboard.is_pressed("d"):
            if not W or not D:
                W = True
                D = True
                canvas.create_image(770,440,image=roombaPic_NE)
                print("W and D Driving...")

        elif keyboard.is_pressed("s") and keyboard.is_pressed("a"):
            if not S or not A:
                S = True
                A = True
                canvas.create_image(770,440,image=roombaPic_SW)
                print("S and A Driving...")

        elif keyboard.is_pressed("s") and keyboard.is_pressed("d"):
            if not S or not D:
                S = True
                D = True
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

                # handle_input("null")
                robot.driveDirect(b'\x00', b'\x00', b'\x00', b'\x00')
                # DRIVE_ONE_WHEEL_200 = b'\x86'
                # robot.stop()
                # connection.write(b'\xAD')
                print("Stop!")


keyboard_thread = threading.Thread(target=handle_keyboard_input)
keyboard_thread.start()

root.mainloop()
