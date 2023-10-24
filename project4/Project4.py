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

# Create a frame to surround the wasd buttons
wasd_frame = Frame(root, bg="white", width=400, height=100)  # Adjust width and height as needed
wasd_frame.place(x = 30, y = 640)

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
