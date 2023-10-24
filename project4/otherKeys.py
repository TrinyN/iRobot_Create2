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
canvas = Canvas(frame, bg="white", width=1920, height=1080)
canvas.pack()

pil_roombaPic = Image.open('create2sm.png')
pil_roombaPic_west = pil_roombaPic.rotate(90)
roombaPic = ImageTk.PhotoImage(pil_roombaPic)
roombaPic_west = ImageTk.PhotoImage(pil_roombaPic_west)
canvas.create_image(770,440,image=roombaPic)
canvas.create_image(770,440,image=roombaPic_west)




# imgpath = 'C:/Users/escot/Downloads/create2sm.png'
# roombaPic = PhotoImage(file=imgpath)
# canvas.create_image(770,440,image=roombaPic)

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
