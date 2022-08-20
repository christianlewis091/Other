# https://www.youtube.com/watch?v=YXPyB4XeYLA&t=2640s&ab_channel=freeCodeCamp.org

from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="Look, I clicked!")
    myLabel.pack()

myButton = Button(root, text="Click Me!", command=myClick, fg='blue')
myButton.pack()

root.mainloop()