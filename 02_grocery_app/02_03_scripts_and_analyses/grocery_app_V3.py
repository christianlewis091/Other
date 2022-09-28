# https://www.youtube.com/watch?v=YXPyB4XeYLA&t=2640s&ab_channel=freeCodeCamp.org
from tkinter import *
from tkinter import ttk
import pandas as pd
import numpy as np
from PIL import Image, ImageTk

# The excel file location has been edited so that if turned into an executeable, the file must only be in
# the same location an the executeable, and it will run.
df = pd.read_excel('recipebookV3.xlsx')

# later, I'll need a list of all the unique recipes to loop through, and that is created here.
recipes_un = df.Recipe_Title.unique()

# initialize the widget
root = Tk()
# root.geometry("500x400")

# hello_message = Label(root, text="Hello! Welcome to the grocery list generator")
# hello_message.pack()
#
# version_message = Label(root, text="Created by: Dr. Christian B. Lewis, Version 2, September 27, 2022")
# version_message.pack()

# Initialize string variables where the dropboxes will sit. I'm not sure if this step is really truly
# necessary, but for now, I need it here for the code to work.
e1 = StringVar()
e2 = StringVar()
e3 = StringVar()
e4 = StringVar()
e5 = StringVar()
e6 = StringVar()
e7 = StringVar()
e8 = StringVar()
e9 = StringVar()
e10 = StringVar()
e11 = StringVar()
e12 = StringVar()
e13 = StringVar()
e14 = StringVar()
e15 = StringVar()
e16 = StringVar()
e17 = StringVar()
e18 = StringVar()
e19 = StringVar()
e20 = StringVar()
e21 = StringVar()
e22 = StringVar()
e23 = StringVar()
e24 = StringVar()
e25 = StringVar()
e26 = StringVar()
e27 = StringVar()
e28 = StringVar()


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
extra = Label(root, text="Anything else?")
mon.grid(row=1, column=0)
tues.grid(row=2, column=0)
wed.grid(row=3, column=0)
thurs.grid(row=4, column=0)
fri.grid(row=5, column=0)
sat.grid(row=6, column=0)
sun.grid(row=7, column=00)
breakfast.grid(row=0, column=1)
lunch.grid(row=0, column=2)
dinner.grid(row=0, column=3)
extra.grid(row=0, column=4)

values = ['all'] + list(df.Recipe_Title.unique())  # CREATES THE ITEMS IN DROPDOWN LIST
x = df.loc[df['Meal'] == 'breakfast']
y = df.loc[df['Meal'] == 'lunch']
z = df.loc[df['Meal'] == 'dinner']
x = ['breakfast recipes'] + list(x.Recipe_Title.unique())  # CREATES THE ITEMS IN DROPDOWN LIST
y = ['lunch recipes'] + list(y.Recipe_Title.unique())  # CREATES THE ITEMS IN DROPDOWN LIST
z = ['dinner recipes'] + list(z.Recipe_Title.unique())  # CREATES THE ITEMS IN DROPDOWN LIST

e1_entry = ttk.OptionMenu(root, e1, *x)
e1_entry.grid(row=1, column=1)

e2_entry = ttk.OptionMenu(root, e2, *y)
e2_entry.grid(row=1, column=2)

e3_entry = ttk.OptionMenu(root, e3, *z)
e3_entry.grid(row=1, column=3)

e4_entry = ttk.OptionMenu(root, e4, *x)
e4_entry.grid(row=2, column=1)

e5_entry = ttk.OptionMenu(root, e5, *y)
e5_entry.grid(row=2, column=2)

e6_entry = ttk.OptionMenu(root, e6, *z)
e6_entry.grid(row=2, column=3)

e7_entry = ttk.OptionMenu(root, e7, *x)
e7_entry.grid(row=3, column=1)

e8_entry = ttk.OptionMenu(root, e8, *y)
e8_entry.grid(row=3, column=2)

e9_entry = ttk.OptionMenu(root, e9, *z)
e9_entry.grid(row=3, column=3)

e10_entry = ttk.OptionMenu(root, e10, *x)
e10_entry.grid(row=4, column=1)

e11_entry = ttk.OptionMenu(root, e11, *y)
e11_entry.grid(row=4, column=2)

e12_entry = ttk.OptionMenu(root, e12, *z)
e12_entry.grid(row=4, column=3)

e13_entry = ttk.OptionMenu(root, e13, *x)
e13_entry.grid(row=5, column=1)

e14_entry = ttk.OptionMenu(root, e14, *y)
e14_entry.grid(row=5, column=2)

e15_entry = ttk.OptionMenu(root, e15, *z)
e15_entry.grid(row=5, column=3)

e16_entry = ttk.OptionMenu(root, e16, *x)
e16_entry.grid(row=6, column=1)

e17_entry = ttk.OptionMenu(root, e17, *y)
e17_entry.grid(row=6, column=2)

e18_entry = ttk.OptionMenu(root, e18, *z)
e18_entry.grid(row=6, column=3)

e19_entry = ttk.OptionMenu(root, e19, *x)
e19_entry.grid(row=7, column=1)

e20_entry = ttk.OptionMenu(root, e20, *y)
e20_entry.grid(row=7, column=2)

e21_entry = ttk.OptionMenu(root, e21, *z)
e21_entry.grid(row=7, column=3)

e22_entry = ttk.OptionMenu(root, e22, *values)
e22_entry.grid(row=1, column=4)

e23_entry = ttk.OptionMenu(root, e23, *values)
e23_entry.grid(row=2, column=4)

e24_entry = ttk.OptionMenu(root, e24, *values)
e24_entry.grid(row=3, column=4)

e25_entry = ttk.OptionMenu(root, e25, *values)
e25_entry.grid(row=4, column=4)

e26_entry = ttk.OptionMenu(root, e26, *values)
e26_entry.grid(row=5, column=4)

e27_entry = ttk.OptionMenu(root, e27, *values)
e27_entry.grid(row=6, column=4)

e28_entry = ttk.OptionMenu(root, e28, *values)
e28_entry.grid(row=7, column=4)

# hello_message = Label(root, text="Hello! Welcome to the grocery list generator")
# hello_message.grid(row=7, column=4)

version_message = Label(root, text="Created by: Dr. Christian B. Lewis, Version 3.0, September 28, 2022")
version_message.grid(row=11, column=0, columnspan=5)
version_message = Label(root, text="For issues reach out to christian.lewis091@gmail.com")
version_message.grid(row=12, column=0, columnspan=5)

def executeList():
    myLabel2 = Label(root, text="List has been created.")
    myLabel2.grid(row=8, column=0, columnspan=4)
    """
    The next block of code grabs all of the inputs from all of the dropdown
    boxes that we created before
    """
    value1 = str(e1.get())
    value2 = str(e2.get())
    value3 = str(e3.get())
    value4 = str(e4.get())
    value5 = str(e5.get())
    value6 = str(e6.get())
    value7 = str(e7.get())
    value8 = str(e8.get())
    value9 = str(e9.get())
    value10 = str(e10.get())
    value11 = str(e11.get())
    value12 = str(e12.get())
    value13 = str(e13.get())
    value14 = str(e14.get())
    value15 = str(e15.get())
    value16 = str(e16.get())
    value17 = str(e17.get())
    value18 = str(e18.get())
    value19 = str(e19.get())
    value20 = str(e20.get())
    value21 = str(e21.get())
    value22 = str(e22.get())
    value23 = str(e23.get())
    value24 = str(e24.get())
    value25 = str(e25.get())
    value26 = str(e26.get())
    value27 = str(e27.get())
    value28 = str(e28.get())

    pd.options.mode.chained_assignment = None  # this supresses an annoying error

    """
    The following block of code does the following:
    Loop through each unique recipe in the list, based on the unique list created above (see "recipes_un", "un" for unique")
    For each of the unique recipe names, find if any of the entries in "value1-value21", for each meal of the week, matches
    any of the recipes.
    Once a match is found, this recipe's ingredients will be tacked onto the initialized dataframe, called 'x', and therefore
    will build up a database.
    Since there are 21 meals in which we can input choices, its possible to put the same recipe in all boxes, in this case,
    it will invoke the duplicates region of the code later.

    """
    varlist = [value1, value2, value3, value4, value5, value6, value7,
               value8, value9, value10, value11, value12, value13, value14,
               value15, value16, value17, value18, value19, value20, value21,
               value22, value23, value24, value25, value26, value27, value28]

    x = pd.DataFrame()
    for i in range(0, len(recipes_un)):        # for the length of the range of the unique recipe names:
        item = recipes_un[i]                   # grab the first recipe of the unique list...
        for j in range(0, len(varlist)):               # now run through the variables (each of the dropdown boxes)
            if varlist[j] == item:                 # if the input is equal to a specific item (if you find a match)
                df_new = df.loc[(df['Recipe_Title'] == item)]  # locate this item from the database,
                x = pd.concat([x, df_new])                     # concat it to our growing database

        x['Duplicate_search'] = x.duplicated(subset='Ingredient', keep=False)  # This function identifies duplicates, by adding a new column and setting all dups to True.
        duplicates = x.loc[(x['Duplicate_search'] == True)]                    # dump all the duplicates into one DataFrame (here, there are still multiples of the same things in the dataframe)
        duplicates_list = np.unique(duplicates['Ingredient'])                  # extract a list of all the duplicate ingredients
        array1 = []
        array2 = []
        array3 = []
        type_new = []
        for i in range(0, len(duplicates_list)):
            current = duplicates_list[i]                                     # focus on the first duplicate of all of the duplicates
            current = duplicates.loc[(duplicates['Ingredient'] == current)]  # extract a quick mini dataFrame of only the current ingredient
            quant = np.sum(current['Quantity'])
            array2.append(quant)
            string1 = ""
            string2 = ""
            for k in range(0, len(current)):
                row = current.iloc[k]  # access the first row of the mini-dataframe for the first duplicate
                string1 = string1 + str(row['Recipe_Title']) + str('_') + str('+') + str('_')  # create a longer string of all the recipes where its used
                string2 = string2 + str(row['Unit_of_Measure']) + str('_') + str('+') + str('_')  # create a longer string of all the recipes where its used
            array1.append(string1)
            array3.append(string2)

            type_new.append(row['Type'])

        cleaned_data = pd.DataFrame(
            {"Recipe_Title": array1, "Ingredient": duplicates_list, "Type": type_new, "Quantity": array2, "Unit_of_Measure": array3})
        # cleaned_data.to_excel('cleaned.xlsx')

        others = x.loc[(x['Duplicate_search'] == False)]  # all the ones where the original dup search was false.
        final_list = pd.concat([cleaned_data, others])
        final_list = final_list[['Ingredient', 'Quantity', 'Unit_of_Measure', 'Type', 'Recipe_Title']]
        final_list = final_list.sort_values(by='Type', ascending=False).reset_index(drop=True)
        final_list.to_excel('list.xlsx')

myButton = Button(root, text="Run", command=executeList, fg='blue')
myButton.grid(row=10, column=0)


root.mainloop()
