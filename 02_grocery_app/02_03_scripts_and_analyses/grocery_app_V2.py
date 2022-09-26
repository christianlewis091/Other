# https://www.youtube.com/watch?v=YXPyB4XeYLA&t=2640s&ab_channel=freeCodeCamp.org
from tkinter import *
from tabulate import tabulate
from tkinter import ttk
import pandas as pd
import numpy as np
from PIL import Image, ImageTk

df = pd.read_excel(
    r'C:\Users\lewis\venv\python310\python-masterclass-remaster-shared\personal_projects\02_grocery_app\02_02_prepared_data\recipebook2.xlsx')
# get a list of all the recipes in the database for the "Database click"
recipes_un = (np.unique(df['Recipe Title']))  # grab each unique recipe from the recipe book and print it so the
recipes = pd.DataFrame({"Recipe": recipes_un})
recipe_list = recipes.sort_values(by='Recipe')

"""
Initialize the widget
"""

root = Tk()
root.geometry("500x400")

img1 = ImageTk.PhotoImage(Image.open("snoopy.png"))
hello_message = Label(root, text="Hello! Welcome to the grocery list generator")
hello_message.grid(row=0, rowspan=2, column=0, columnspan=5)

label_image = Label(root, image=img1)
label_image.grid(row=2, column=0, columnspan=5)

version_message = Label(root, text="Created by: Dr. Christian B. Lewis, Version 2, September 27, 2022")
version_message.grid(row=20, rowspan=2, column=0, columnspan=5)

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

"""
This first button just creates the code to update the excel sheet if you add a new recipe
"""

def updating():
    top0 = Toplevel()
    myLabel = Label(top0, text='Updated!', justify=LEFT).pack()
    df_bfast = df.loc[df['Meal'] == 'breakfast']
    df_lunch = df.loc[df['Meal'] == 'lunch']
    df_dinner = df.loc[df['Meal'] == 'dinner']
    df_dessert = df.loc[df['Meal'] == 'dessert']
    df_bfast = np.unique(df_bfast['Recipe Title'])
    df_bfast = pd.DataFrame({"Breakfast": df_bfast})
    df_lunch = np.unique(df_lunch['Recipe Title'])
    df_lunch = pd.DataFrame({"Lunch": df_lunch})
    df_dinner = np.unique(df_dinner['Recipe Title'])
    df_dinner = pd.DataFrame({"Dinner": df_dinner})
    df_dessert = np.unique(df_dessert['Recipe Title'])
    df_dessert = pd.DataFrame({"Dessert": df_dessert})
    recipes_summary = pd.concat([df_bfast, df_lunch, df_dinner, df_dessert], axis=1, join="outer")
    with pd.ExcelWriter(
            r'C:/Users/lewis/venv/python310/python-masterclass-remaster-shared/personal_projects/02_grocery_app/02_02_prepared_data/recipebook2.xlsx') as writer:
        df.to_excel(writer, sheet_name='Database', index=False)
        recipes_summary.to_excel(writer, sheet_name='SummaryList', index=False)


myButton = Button(root, text="Click here to update the summary list (File must be closed!)", command=updating, fg='blue')
myButton.grid(row=30, rowspan=7, column=0, columnspan=5)



def listcreation():
    top = Toplevel()
    mon = Label(top, text="M")
    tues = Label(top, text="Tu")
    wed = Label(top, text="W")
    thurs = Label(top, text="Th")
    fri = Label(top, text="F")
    sat = Label(top, text="Sat")
    sun = Label(top, text="Sun")
    breakfast = Label(top, text="Breakfast")
    lunch = Label(top, text="Lunch")
    dinner = Label(top, text="Dinner")
    mon.grid(row=1, column=6)
    tues.grid(row=2, column=6)
    wed.grid(row=3, column=6)
    thurs.grid(row=4, column=6)
    fri.grid(row=5, column=6)
    sat.grid(row=6, column=6)
    sun.grid(row=7, column=6)
    breakfast.grid(row=0, column=7)
    lunch.grid(row=0, column=8)
    dinner.grid(row=0, column=9)

    values = ['all'] + list(recipes['Recipe'].unique())  # CREATES THE ITEMS IN DROPDOWN LIST

    e1_entry = ttk.OptionMenu(top, e1, *values)
    e1_entry.grid(row=1, column=7)

    e2_entry = ttk.OptionMenu(top, e2, *values)
    e2_entry.grid(row=1, column=8)

    e3_entry = ttk.OptionMenu(top, e3, *values)
    e3_entry.grid(row=1, column=9)

    e4_entry = ttk.OptionMenu(top, e4, *values)
    e4_entry.grid(row=2, column=7)

    e5_entry = ttk.OptionMenu(top, e5, *values)
    e5_entry.grid(row=2, column=8)

    e6_entry = ttk.OptionMenu(top, e6, *values)
    e6_entry.grid(row=2, column=9)

    e7_entry = ttk.OptionMenu(top, e7, *values)
    e7_entry.grid(row=3, column=7)

    e8_entry = ttk.OptionMenu(top, e8, *values)
    e8_entry.grid(row=3, column=8)

    e9_entry = ttk.OptionMenu(top, e9, *values)
    e9_entry.grid(row=3, column=9)

    e10_entry = ttk.OptionMenu(top, e10, *values)
    e10_entry.grid(row=4, column=7)

    e11_entry = ttk.OptionMenu(top, e11, *values)
    e11_entry.grid(row=4, column=8)

    e12_entry = ttk.OptionMenu(top, e12, *values)
    e12_entry.grid(row=4, column=9)

    e13_entry = ttk.OptionMenu(top, e13, *values)
    e13_entry.grid(row=5, column=7)

    e14_entry = ttk.OptionMenu(top, e14, *values)
    e14_entry.grid(row=5, column=8)

    e15_entry = ttk.OptionMenu(top, e15, *values)
    e15_entry.grid(row=5, column=9)

    e16_entry = ttk.OptionMenu(top, e16, *values)
    e16_entry.grid(row=6, column=7)

    e17_entry = ttk.OptionMenu(top, e17, *values)
    e17_entry.grid(row=6, column=8)

    e18_entry = ttk.OptionMenu(top, e18, *values)
    e18_entry.grid(row=6, column=9)

    e19_entry = ttk.OptionMenu(top, e19, *values)
    e19_entry.grid(row=7, column=7)

    e20_entry = ttk.OptionMenu(top, e20, *values)
    e20_entry.grid(row=7, column=8)

    e21_entry = ttk.OptionMenu(top, e21, *values)
    e21_entry.grid(row=7, column=9)


    def executeList():
        myLabel2 = Label(top, text="List has been created.")
        myLabel2.grid(row=10, column=6, columnspan=5)
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

        pd.options.mode.chained_assignment = None  # this supresses an annoying error
        # df = pd.read_excel(r'C:\Users\lewis\venv\python310\python-masterclass-remaster-shared\personal_projects\02_grocery_app\02_02_prepared_data\recipebook.xlsx')
        # recipes = (np.unique(df['Recipe Title']))  # grab each unique recipe from the recipe book and print it so the
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
        x = pd.DataFrame()
        for i in range(0, len(recipes_un)):  # for the length of the range of the unique recipe names:
            item = recipes_un[i]                # grab the first recipe of the unique list...
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

        x['Duplicate_search'] = x.duplicated(subset='Ingredient', keep=False)  # This function identifies duplicates, by adding a new column and setting all dups to True.
        duplicates = x.loc[(x['Duplicate_search'] == True)]                    # dump all the duplicates into one DataFrame (here, there are still multiples of the same things in the dataframe)
        duplicates_list = np.unique(duplicates['Ingredient'])                  # extract a list of all the duplicate ingredients
        array1 = []
        array2 = []
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
                string1 = string1 + str(row['Recipe Title']) + str('_') + str('+') + str('_')  # create a longer string of all the recipes where its used
            array1.append(string1)
            type_new.append(row['Type'])

        cleaned_data = pd.DataFrame(
            {"Recipe Title": array1, "Ingredient": duplicates_list, "Type": type_new, "Quantity": array2})
        # cleaned_data.to_excel('cleaned.xlsx')

        others = x.loc[(x['Duplicate_search'] == False)]  # all the ones where the original dup search was false.
        final_list = pd.concat([cleaned_data, others])
        final_list = final_list[['Ingredient', 'Quantity', 'Unit of Measure', 'Type', 'Recipe Title']]
        final_list = final_list.sort_values(by='Type', ascending=False).reset_index(drop=True)
        final_list.to_excel(
            r'C:/Users/lewis/venv/python310/python-masterclass-remaster-shared/personal_projects'
            r'/02_grocery_app/02_04_output_data/list.xlsx')


    myButton = Button(top, text="Execute list creation", command=executeList, fg='blue')
    myButton.grid(row=30, rowspan=7, column=0, columnspan=5)


myButton = Button(root, text="Click here to get started making your list", command=listcreation, fg='blue')
myButton.grid(row=40, rowspan=7, column=0, columnspan=5)

root.mainloop()
