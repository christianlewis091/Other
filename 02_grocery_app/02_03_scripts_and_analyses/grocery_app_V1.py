# https://www.youtube.com/watch?v=YXPyB4XeYLA&t=2640s&ab_channel=freeCodeCamp.org
from tkinter import *
from tkinter import ttk
import pandas as pd
import numpy as np
from PIL import Image, ImageTk

# TODO fix the format of the window, the user interface essentially is hard to read/ugly at the moment, but it works!
df = pd.read_excel(r'C:\Users\lewis\venv\python310\python-masterclass-remaster-shared\personal_projects\02_grocery_app\02_02_prepared_data\recipebook.xlsx')
recipes = (np.unique(df['Recipe Title']))  # grab each unique recipe from the recipe book and print it so the
recipes = pd.DataFrame({"Recipe": recipes})
recipes = recipes.sort_values(by='Recipe')

"""
Initialize the widget
"""
root = Tk()
# root['bg'] = '#ffbf00'
# root.geometry("700x500")
hello_message = Label(root, text=
"Hello! Welcome to the grocery list generator")
hello_message.grid(row=0, rowspan=2, column=0, columnspan=5)
img1 = ImageTk.PhotoImage(Image.open("snoopy.png"))
label_image = Label(root, image=img1)
label_image.grid(row=10, column=0)

"""
Create Labels and Tell them where to live
"""
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

"""
This next annoyingly long block of code creates 21 new variables (7 days of the week, 3 meals
per day).
The sequence of three lines does as follows:
e1 = StringVar()                              # INITIALIZE A VARIABLE
e1_entry = ttk.OptionMenu(root, e1, *values)  # INITIALIZE A DROPDOWN LIST OF ALL ITEMS IN "VALUES"
e1_entry.grid(row=1, column=7)                # TELL THE BOX WHERE TO LIVE
"""

values = ['all'] + list(recipes['Recipe'].unique())  # CREATES THE ITEMS IN DROPDOWN LIST

e1 = StringVar()
e1_entry = ttk.OptionMenu(root, e1, *values)
e1_entry.grid(row=1, column=7)

e2 = StringVar()
e2_entry = ttk.OptionMenu(root, e2, *values)
e2_entry.grid(row=1, column=8)

e3 = StringVar()
e3_entry = ttk.OptionMenu(root, e3, *values)
e3_entry.grid(row=1, column=9)

e4 = StringVar()
e4_entry = ttk.OptionMenu(root, e4, *values)
e4_entry.grid(row=2, column=7)

e5 = StringVar()
e5_entry = ttk.OptionMenu(root, e5, *values)
e5_entry.grid(row=2, column=8)

e6 = StringVar()
e6_entry = ttk.OptionMenu(root, e6, *values)
e6_entry.grid(row=2, column=9)

e7 = StringVar()
e7_entry = ttk.OptionMenu(root, e7, *values)
e7_entry.grid(row=3, column=7)

e8 = StringVar()
e8_entry = ttk.OptionMenu(root, e8, *values)
e8_entry.grid(row=3, column=8)

e9 = StringVar()
e9_entry = ttk.OptionMenu(root, e9, *values)
e9_entry.grid(row=3, column=9)

e10 = StringVar()
e10_entry = ttk.OptionMenu(root, e10, *values)
e10_entry.grid(row=4, column=7)

e11 = StringVar()
e11_entry = ttk.OptionMenu(root, e11, *values)
e11_entry.grid(row=4, column=8)

e12 = StringVar()
e12_entry = ttk.OptionMenu(root, e12, *values)
e12_entry.grid(row=4, column=9)

e13 = StringVar()
e13_entry = ttk.OptionMenu(root, e13, *values)
e13_entry.grid(row=5, column=7)

e14 = StringVar()
e14_entry = ttk.OptionMenu(root, e14, *values)
e14_entry.grid(row=5, column=8)

e15 = StringVar()
e15_entry = ttk.OptionMenu(root, e15, *values)
e15_entry.grid(row=5, column=9)

e16 = StringVar()
e16_entry = ttk.OptionMenu(root, e16, *values)
e16_entry.grid(row=6, column=7)

e17 = StringVar()
e17_entry = ttk.OptionMenu(root, e17, *values)
e17_entry.grid(row=6, column=8)

e18 = StringVar()
e18_entry = ttk.OptionMenu(root, e18, *values)
e18_entry.grid(row=6, column=9)

e19 = StringVar()
e19_entry = ttk.OptionMenu(root, e19, *values)
e19_entry.grid(row=7, column=7)

e20 = StringVar()
e20_entry = ttk.OptionMenu(root, e20, *values)
e20_entry.grid(row=7, column=8)

e21 = StringVar()
e21_entry = ttk.OptionMenu(root, e21, *values)
e21_entry.grid(row=7, column=9)


def myClick():
    top = Toplevel()
    myLabel = Label(top, text=recipes, justify=LEFT).pack()


myButton = Button(root, text="Click here to see available recipes", command=myClick, fg='blue')
myButton.grid(row=2, rowspan=5, column=0, columnspan=5)



"""
This is where the main functionality of the widget lives. 
Ideally, I would like to have this in another section / another .py file, 
but you end up doing circular imports, so we'll just leave it here...
"""
def executeList():
    myLabel2 = Label(root, text="List has been created.")
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
    df = pd.read_excel(
        r'C:\Users\lewis\venv\python310\python-masterclass-remaster-shared\personal_projects\02_grocery_app\02_02_prepared_data\recipebook.xlsx')
    # print(df)
    recipes = (np.unique(df['Recipe Title']))  # grab each unique recipe from the recipe book and print it so the
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

    x['Duplicate_search'] = x.duplicated(subset='Ingredient',
                                         keep=False)  # This function identifies duplicates, by adding a new column and setting all dups to True.

    duplicates = x.loc[(x['Duplicate_search'] == True)]  # dump all the duplicates into one DataFrame
    duplicates_list = np.unique(duplicates['Ingredient'])  # extract a list of all the duplicate ingredients
    print(duplicates_list)
    print(len(duplicates_list))
    array1 = []
    array2 = []
    type_new = []
    for i in range(0, len(duplicates_list)):
        current = duplicates_list[i]  # focus on the first duplicate of all of the duplicates
        current = duplicates.loc[
            (duplicates['Ingredient'] == current)]  # extract a quick mini dataFrame of only the current ingredient
        string1 = ""
        string2 = ""
        for k in range(0, len(current)):
            row = current.iloc[k]  # access the first row of the mini-dataframe for the first duplicate
            string1 = string1 + str(row['Recipe Title']) + str('_') + str('+') + str(
                '_')  # create a longer string of all the recipes where its used
            string2 = string2 + str(row['Quantity']) + str('_') + str(row['Unit of Measure']) + str('_') + str(
                '+') + str('_')  # create a longer string of the different quntities required

        array1.append(string1)
        array2.append(string2)
        type_new.append(row['Type'])
    print(len(array1))
    print(len(array2))
    print(len(type_new))
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


myButton = Button(root, text="Execute list creation", command=executeList, fg='blue')
myButton.grid(row=9, column=6, columnspan=5)

root.mainloop()
