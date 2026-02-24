#Name: Mark Leslie
#Date: 24/02/2026

from tkinter import *

def hello():
    print("Hello from Les")

root = Tk()
root.geometry("600x600")

frame_one= Frame(root)
frame_one.pack()


button_one = Button(frame_one,text="say hello",command = hello)
button_one.pack()

root.mainloop()