# https://www.youtube.com/watch?v=YXPyB4XeYLA&t=2640s&ab_channel=freeCodeCamp.org
from tkinter import *
from tkinter import ttk
import pandas as pd
import numpy as np

# TODO fix the format of the window, the user interface essentially is hard to read/ugly at the moment, but it works!
df = pd.read_excel(r'C:\Users\lewis\venv\python310\python-masterclass-remaster-shared\finances\recipebook.xlsx')
# print(df)
recipes = (np.unique(df['Recipe Title']))  # grab each unique recipe from the recipe book and print it so the

root = Tk()
root['bg'] = '#ffbf00'


# df = pd.read_excel(r'C:\Users\lewis\venv\python310\python-masterclass-remaster-shared\finances\recipebook.xlsx')
# recipes = (np.unique(df['Recipe Title']))  # grab each unique recipe from the recipe book and print it so the
# user can see what their options are. This will be superceded by a
# dropdown menu when I get the GUI running.

hello_message = Label(root, text="Hello! Welcome to the grocery list generator")
# hello_message.grid(row=0, column=0)

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

e1 = StringVar()
e1_entry = ttk.Entry(root, width=30, textvariable=e1)
e1_entry.grid(row=3, column=1)

e2 = StringVar()
e2_entry = ttk.Entry(root, width=30, textvariable=e2)
e2_entry.grid(row=3, column=2)

e3 = StringVar()
e3_entry = ttk.Entry(root, width=30, textvariable=e3)
e3_entry.grid(row=3, column=3)

e4 = StringVar()
e4_entry = ttk.Entry(root, width=30, textvariable=e4)
e4_entry.grid(row=3, column=4)

e5 = StringVar()
e5_entry = ttk.Entry(root, width=30, textvariable=e5)
e5_entry.grid(row=3, column=5)

e6 = StringVar()
e6_entry = ttk.Entry(root, width=30, textvariable=e6)
e6_entry.grid(row=3, column=6)

e7 = StringVar()
e7_entry = ttk.Entry(root, width=30, textvariable=e7)
e7_entry.grid(row=3, column=7)

e8 = StringVar()
e8_entry = ttk.Entry(root, width=30, textvariable=e8)
e8_entry.grid(row=4, column=1)

e9 = StringVar()
e9_entry = ttk.Entry(root, width=30, textvariable=e9)
e9_entry.grid(row=4, column=2)

e10 = StringVar()
e10_entry = ttk.Entry(root, width=30, textvariable=e10)
e10_entry.grid(row=4, column=3)

e11 = StringVar()
e11_entry = ttk.Entry(root, width=30, textvariable=e11)
e11_entry.grid(row=4, column=4)

e12 = StringVar()
e12_entry = ttk.Entry(root, width=30, textvariable=e12)
e12_entry.grid(row=4, column=5)

e13 = StringVar()
e13_entry = ttk.Entry(root, width=30, textvariable=e13)
e13_entry.grid(row=4, column=6)

e14 = StringVar()
e14_entry = ttk.Entry(root, width=30, textvariable=e14)
e14_entry.grid(row=4, column=7)

e15 = StringVar()
e15_entry = ttk.Entry(root, width=30, textvariable=e15)
e15_entry.grid(row=5, column=1)

e16 = StringVar()
e16_entry = ttk.Entry(root, width=30, textvariable=e16)
e16_entry.grid(row=5, column=2)

e17 = StringVar()
e17_entry = ttk.Entry(root, width=30, textvariable=e17)
e17_entry.grid(row=5, column=3)

e18 = StringVar()
e18_entry = ttk.Entry(root, width=30, textvariable=e18)
e18_entry.grid(row=5, column=4)

e19 = StringVar()
e19_entry = ttk.Entry(root, width=30, textvariable=e19)
e19_entry.grid(row=5, column=5)

e20 = StringVar()
e20_entry = ttk.Entry(root, width=30, textvariable=e20)
e20_entry.grid(row=5, column=6)

e21 = StringVar()
e21_entry = ttk.Entry(root, width=30, textvariable=e21)
e21_entry.grid(row=5, column=7)


def myClick():
    myLabel = Label(root, text=recipes)
    myLabel.grid(row=2, column=0)

myButton = Button(root, text="Click here to see available recipes", command=myClick, fg='blue')
myButton.grid(row=1, column=0)

def executeList():
    myLabel2 = Label(root, text="List has been created...I think")
    myLabel2.grid(row=8, column=0)
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

    pd.options.mode.chained_assignment = None  # this supresses an annoying error
    df = pd.read_excel(r'C:\Users\lewis\venv\python310\python-masterclass-remaster-shared\finances\recipebook.xlsx')
    # print(df)
    recipes = (np.unique(df['Recipe Title']))  # grab each unique recipe from the recipe book and print it so the
    print(recipes)
    x = pd.DataFrame()
    for i in range(0, len(recipes)):
        item = recipes[i]
        if value1 == item:  # if the input is equal to a specific item,
            df_new = df.loc[(df['Recipe Title'] == item)]  # take the first input from the user, and find where in the
            x = pd.concat([x, df_new])  # then add it to the DataFrame that we're building for the grocery list
        if value2 == item:  # if the input is equal to a specific item,
            df_new = df.loc[(df['Recipe Title'] == item)]  # take the first input from the user, and find where in the
            x = pd.concat([x, df_new])  # then add it to the DataFrame that we're building for the grocery list
        if value3 == item:  # if the input is equal to a specific item,
            df_new = df.loc[(df['Recipe Title'] == item)]  # take the first input from the user, and find where in the
            x = pd.concat([x, df_new])  # then add it to the DataFrame that we're building for the grocery list
        if value4 == item:  # if the input is equal to a specific item,
            df_new = df.loc[(df['Recipe Title'] == item)]  # take the first input from the user, and find where in the
            x = pd.concat([x, df_new])  # then add it to the DataFrame that we're building for the grocery list
        if value5 == item:  # if the input is equal to a specific item,
            df_new = df.loc[(df['Recipe Title'] == item)]  # take the first input from the user, and find where in the
            x = pd.concat([x, df_new])  # then add it to the DataFrame that we're building for the grocery list
        if value6 == item:  # if the input is equal to a specific item,
            df_new = df.loc[(df['Recipe Title'] == item)]  # take the first input from the user, and find where in the
            x = pd.concat([x, df_new])  # then add it to the DataFrame that we're building for the grocery list
        if value7 == item:  # if the input is equal to a specific item,
            df_new = df.loc[(df['Recipe Title'] == item)]  # take the first input from the user, and find where in the
            x = pd.concat([x, df_new])  # then add it to the DataFrame that we're building for the grocery list
        if value8 == item:  # if the input is equal to a specific item,
            df_new = df.loc[(df['Recipe Title'] == item)]  # take the first input from the user, and find where in the
            x = pd.concat([x, df_new])  # then add it to the DataFrame that we're building for the grocery list
        if value9 == item:  # if the input is equal to a specific item,
            df_new = df.loc[(df['Recipe Title'] == item)]  # take the first input from the user, and find where in the
            x = pd.concat([x, df_new])  # then add it to the DataFrame that we're building for the grocery list
        if value10 == item:  # if the input is equal to a specific item,
            df_new = df.loc[(df['Recipe Title'] == item)]  # take the first input from the user, and find where in the
            x = pd.concat([x, df_new])  # then add it to the DataFrame that we're building for the grocery list
        if value11 == item:  # if the input is equal to a specific item,
            df_new = df.loc[(df['Recipe Title'] == item)]  # take the first input from the user, and find where in the
            x = pd.concat([x, df_new])  # then add it to the DataFrame that we're building for the grocery list
        if value12 == item:  # if the input is equal to a specific item,
            df_new = df.loc[(df['Recipe Title'] == item)]  # take the first input from the user, and find where in the
            x = pd.concat([x, df_new])  # then add it to the DataFrame that we're building for the grocery list
        if value13 == item:  # if the input is equal to a specific item,
            df_new = df.loc[(df['Recipe Title'] == item)]  # take the first input from the user, and find where in the
            x = pd.concat([x, df_new])  # then add it to the DataFrame that we're building for the grocery list
        if value14 == item:  # if the input is equal to a specific item,
            df_new = df.loc[(df['Recipe Title'] == item)]  # take the first input from the user, and find where in the
            x = pd.concat([x, df_new])  # then add it to the DataFrame that we're building for the grocery list
        if value15 == item:  # if the input is equal to a specific item,
            df_new = df.loc[(df['Recipe Title'] == item)]  # take the first input from the user, and find where in the
            x = pd.concat([x, df_new])  # then add it to the DataFrame that we're building for the grocery list
        if value16 == item:  # if the input is equal to a specific item,
            df_new = df.loc[(df['Recipe Title'] == item)]  # take the first input from the user, and find where in the
            x = pd.concat([x, df_new])  # then add it to the DataFrame that we're building for the grocery list
        if value17 == item:  # if the input is equal to a specific item,
            df_new = df.loc[(df['Recipe Title'] == item)]  # take the first input from the user, and find where in the
            x = pd.concat([x, df_new])  # then add it to the DataFrame that we're building for the grocery list
        if value18 == item:  # if the input is equal to a specific item,
            df_new = df.loc[(df['Recipe Title'] == item)]  # take the first input from the user, and find where in the
            x = pd.concat([x, df_new])  # then add it to the DataFrame that we're building for the grocery list
        if value19 == item:  # if the input is equal to a specific item,
            df_new = df.loc[(df['Recipe Title'] == item)]  # take the first input from the user, and find where in the
            x = pd.concat([x, df_new])  # then add it to the DataFrame that we're building for the grocery list
        if value20 == item:  # if the input is equal to a specific item,
            df_new = df.loc[(df['Recipe Title'] == item)]  # take the first input from the user, and find where in the
            x = pd.concat([x, df_new])  # then add it to the DataFrame that we're building for the grocery list
        if value21 == item:  # if the input is equal to a specific item,
            df_new = df.loc[(df['Recipe Title'] == item)]  # take the first input from the user, and find where in the
            x = pd.concat([x, df_new])  # then add it to the DataFrame that we're building for the grocery list
    if len(x) != 0:
        x['Duplicate_search'] = x.duplicated(subset='Ingredient', keep=False)  # This function identifies duplicates, by adding a new column and setting all dups to True.
        # by setting keep = False, all dups are True

        nondups = x.loc[(x['Duplicate_search'] == False)]                   # locate a list of all NON duplicates, and save for later use
        dups = x.loc[(x['Duplicate_search'] == True)]                       # locate a lost of ALL duplicates, to work with now
        dups = np.unique(dups['Ingredient'])                                # Create a list of all the unique ingredients that are duplicated
        for item in dups:                                                   # iterate through the list of duplicates
            current_ingredient = x.loc[(x['Ingredient'] == item)]           # find all those items in the whole list
            if len(np.unique(current_ingredient['Unit of Measure'])) == 1:  # if there is only one type of unit measure,
                sum = np.sum(current_ingredient['Quantity'])                # add the quantities together
                current_ingredient['Quantity'] = sum                        # change the "quantity" to the sum:
                # currently, there will be dups on the main sheet, but they'll all have the total quantity, and I'll just drop the dups later

                recipes = np.unique(current_ingredient['Recipe Title'])     # this next block of code will string all the recipes together that call for the duplicate items
                strings = ""                                                # so that the user can see at a glance when looking at the grocery list
                for k in range(0, len(recipes)):
                    name = recipes[k]
                    strings = strings + str(name) + str("\u007e")
                current_ingredient['Recipe Title'] = strings
                nondups = pd.concat([nondups, current_ingredient])          # concat this duplicated ingredient onto the list of nondups

            elif len(np.unique(current_ingredient[
                                   'Unit of Measure'])) != 1:               # if there are duplicate ingredients but they have different units of measure,
                nondups = pd.concat([nondups, current_ingredient])          # make sure that's back on the main list as well.

        """
        Now, at this point, we're just trying to get a grocery list, so I'm going to drop the recipe title, and then
        drop the duplicates.
        """
        nondups = nondups[['Ingredient', 'Quantity', 'Unit of Measure', 'Recipe Title']].reset_index(drop=True)
        nondups['Dups to Drop'] = nondups.duplicated()
        final_list = nondups.loc[(nondups[
                                      'Dups to Drop'] == False)]  # grab only the items that the above function sets to false. (All duplicates are set to true, so keep all the false ones)
        final_list.to_excel('recipetest.xlsx')





myButton = Button(root, text="Execute list creation", command=executeList, fg='blue')
myButton.grid(row=7, column=0)

root.mainloop()