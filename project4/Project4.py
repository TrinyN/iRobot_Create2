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

root = Tk()  # create a root widget
root.title("Roomba")
root.configure(background="white")
root.minsize(1920, 1080)  # width, height
root.maxsize(1920, 1080)
root.geometry("1920x1080+0+0")  # width x height + x + y
root.resizable=FALSE

frame = Frame(root)
frame.pack()

# Canvas must be made and used to prevent background color
canvas = Canvas(frame, bg="purple", width=1920, height=1080)
canvas.pack()

imgpath = 'C:/Users/escot/Downloads/create2-removebg-preview.png'
roombaPic = PhotoImage(file=imgpath)
canvas.create_image(500,500,image=roombaPic)

# imgpath = 'C:/Users/escot/Downloads/create2-removebg-preview.png'
# image = PhotoImage(file=imgpath)
# image = image.subsample(25)
# img = Label(root, image=image)
# img.pack()
root.mainloop()
