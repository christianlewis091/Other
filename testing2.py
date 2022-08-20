# https://www.youtube.com/watch?v=YXPyB4XeYLA&t=2640s&ab_channel=freeCodeCamp.org

from tkinter import *
import pandas as pd
import numpy as np

root = Tk()
root['bg'] = '#ffbf00'
df = pd.read_excel(r'C:\Users\lewis\venv\python310\python-masterclass-remaster-shared\finances\recipebook.xlsx')
recipes = (np.unique(df['Recipe Title']))  # grab each unique recipe from the recipe book and print it so the
# user can see what their options are. This will be superceded by a
# dropdown menu when I get the GUI running.

hello_message = Label(root, text="Hello! Welcome to the grocery list generator")
hello_message.grid(row=0, column=0)

mon = Label(root, text="M")
tues = Label(root, text="Tu")
wed = Label(root, text="W")
thurs = Label(root, text="Th")
fri = Label(root, text="F")
sat = Label(root, text="Sat")
sun = Label(root, text="Sun")
breakfast = Label(root, text="Breakfast")
lunch = Label(root, text="Lunch")
dinner = Label(root, text="Dinner")

mon.grid(row=2, column=1)
tues.grid(row=2, column=2)
wed.grid(row=2, column=3)
thurs.grid(row=2, column=4)
fri.grid(row=2, column=5)
sat.grid(row=2, column=6)
sun.grid(row=2, column=7)
breakfast.grid(row=3, column=0)
lunch.grid(row=4, column=0)
dinner.grid(row=5, column=0)

e1 = Entry(root, width=30)
e1.get()  # gets whatever you typed into this entry
e1.grid(row=3, column=1)

e2 = Entry(root, width=30)
e2.get()  # gets whatever you typed into this entry
e2.grid(row=3, column=2)

e3 = Entry(root, width=30)
e3.get()  # gets whatever you typed into this entry
e3.grid(row=3, column=3)


def myClick():
    myLabel = Label(root, text=recipes)
    myLabel.grid(row=2, column=0)


myButton = Button(root, text="Click here to see available recipes", command=myClick, fg='blue')
myButton.grid(row=1, column=0)


def executeList():
    myLabel2 = Label(root, text="List has been created...I think")
    myLabel2.grid(row=8, column=0)





myButton = Button(root, text="Execute list creation", command=executeList, fg='blue')
myButton.grid(row=7, column=0)


# e4 = Entry(root, width=30)
# e4.get()  # gets whatever you typed into this entry
# e4.grid(row=3, column=4)
#
# e5 = Entry(root, width=30)
# e5.get()  # gets whatever you typed into this entry
# e5.grid(row=3, column=5)
#
# e6 = Entry(root, width=30)
# e6.get()  # gets whatever you typed into this entry
# e6.grid(row=3, column=6)
#
# e7 = Entry(root, width=30)
# e7.get()  # gets whatever you typed into this entry
# e7.grid(row=3, column=7)
#
# e8 = Entry(root, width=30)
# e8.get()  # gets whatever you typed into this entry
# e8.grid(row=4, column=1)
#
# e9 = Entry(root, width=30)
# e9.get()  # gets whatever you typed into this entry
# e9.grid(row=4, column=2)
#
# e10 = Entry(root, width=30)
# e10.get()  # gets whatever you typed into this entry
# e10.grid(row=4, column=3)
#
# e11 = Entry(root, width=30)
# e11.get()  # gets whatever you typed into this entry
# e11.grid(row=4, column=4)
#
# e12 = Entry(root, width=30)
# e12.get()  # gets whatever you typed into this entry
# e12.grid(row=4, column=5)
#
# e13 = Entry(root, width=30)
# e13.get()  # gets whatever you typed into this entry
# e13.grid(row=4, column=6)
#
# e14 = Entry(root, width=30)
# e14.get()  # gets whatever you typed into this entry
# e14.grid(row=4, column=7)
#
# e15 = Entry(root, width=30)
# e15.get()  # gets whatever you typed into this entry
# e15.grid(row=5, column=1)
#
# e16 = Entry(root, width=30)
# e16.get()  # gets whatever you typed into this entry
# e16.grid(row=5, column=2)
#
# e17 = Entry(root, width=30)
# e17.get()  # gets whatever you typed into this entry
# e17.grid(row=5, column=3)
#
# e18 = Entry(root, width=30)
# e18.get()  # gets whatever you typed into this entry
# e18.grid(row=5, column=4)
#
# e19 = Entry(root, width=30)
# e19.get()  # gets whatever you typed into this entry
# e19.grid(row=5, column=5)
#
# e20 = Entry(root, width=30)
# e20.get()  # gets whatever you typed into this entry
# e20.grid(row=5, column=6)
#
# e21 = Entry(root, width=30)
# e21.get()  # gets whatever you typed into this entry
# e21.grid(row=5, column=7)

root.mainloop()