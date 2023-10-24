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
import keyboard
import threading

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

imgpath = 'C:/Users/escot/Downloads/create2sm.png'
roombaPic = PhotoImage(file=imgpath)
canvas.create_image(770,440,image=roombaPic)

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
    if key == 'W':
        print("Driving Forward...")

    elif key == 'A':
        print("Driving Left...")

    elif key == 'S':
        print("Driving Backwards...")

    elif key == 'D':
        print("Driving Right...")

    else:
        print("stop!")

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
                print("Driving Backwards...")

        elif (
            keyboard.is_pressed("a")
            and not keyboard.is_pressed("w")
            and not keyboard.is_pressed("s")
            and not keyboard.is_pressed("d")
        ):
            if not A:
                A = True
                # handle_input('A')
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
                print("Driving Right...")

        elif keyboard.is_pressed("w") and keyboard.is_pressed("a"):
            if not W or not A:
                W = True
                A = True
                print("W and A Driving...")

        elif keyboard.is_pressed("w") and keyboard.is_pressed("d"):
            if not W or not D:
                W = True
                D = True
                print("W and D Driving...")

        elif keyboard.is_pressed("s") and keyboard.is_pressed("a"):
            if not S or not A:
                S = True
                A = True
                print("S and A Driving...")

        elif keyboard.is_pressed("s") and keyboard.is_pressed("d"):
            if not S or not D:
                S = True
                D = True
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
                print("Stop!")


keyboard_thread = threading.Thread(target=handle_keyboard_input)
keyboard_thread.start()

################################## keys ###################

def on_press(key):
    if key == keyboard.Key.esc:
        return False #stops listener
    try:
        k = key.char #single-char-keys
    except:
        k = key.name #other keys
        print(k + " not allowed")
    if k in ['w','a','s','d']:          #keys of interest
        if k == 'w':
            print('moving forward')
        if k == 'a':
            print('moving left')
        if k == 's':
            print('moving right')
        if k == 'd':
            print('moving backward')
        print('Key pressed: ' + k)

    
listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()

root.mainloop()
