# https://www.youtube.com/watch?v=YXPyB4XeYLA&t=2640s&ab_channel=freeCodeCamp.org
from tkinter import *
from tkinter import ttk
import pandas as pd
import numpy as np
from PIL import Image, ImageTk

df = pd.read_excel(r'C:\Users\lewis\venv\python310\python-masterclass-remaster-shared\personal_projects\02_grocery_app\02_02_prepared_data\recipebook.xlsx')

"""
Initialize the widget
"""
root = Tk()
root.geometry("500x400")
img1 = ImageTk.PhotoImage(Image.open("snoopy.png"))

hello_message = Label(root, text="Hello! Welcome to the grocery list generator").grid(row=0, rowspan=2, column=0, columnspan=5)
label_image = Label(root, image=img1).grid(row=2, column=0, columnspan=5)
next_message = Label(root, text='nextline').grid(row=3, column=0, columnspan=5)

root.mainloop()
