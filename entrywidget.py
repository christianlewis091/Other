# https://www.youtube.com/watch?v=YXPyB4XeYLA&t=2640s&ab_channel=freeCodeCamp.org
from tkinter import *

root = Tk()

e = Entry(root, width = 50)                   # bg = 'blue', fg = 'white'
e.pack()
e.get()     # gets whatever you typed into this entry
e.insert(0, "Enter your name: ")  # this puts default text inside the text box


def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)  # label is set to the Entry field
    myLabel.pack()

myButton = Button(root, text="Click Me!", command=myClick, fg='blue')
myButton.pack()

root.mainloop()