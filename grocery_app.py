# https://www.youtube.com/watch?v=YXPyB4XeYLA&t=2640s&ab_channel=freeCodeCamp.org
from tkinter import *
from tkinter import ttk
import pandas as pd
import numpy as np

# TODO fix the format of the window, the user interface essentially is hard to read/ugly at the moment, but it works!
df = pd.read_excel(r'C:\Users\lewis\venv\python310\python-masterclass-remaster-shared\finances\recipebook.xlsx')
recipes = (np.unique(df['Recipe Title']))  # grab each unique recipe from the recipe book and print it so the
recipes = pd.DataFrame({"Recipe": recipes})
recipes = recipes.sort_values(by='Recipe')

root = Tk()
# root['bg'] = '#ffbf00'
# root.geometry("700x500")
hello_message = Label(root, text=
"Hello! Welcome to the grocery list generator")
hello_message.grid(row=0, rowspan=2, column=0, columnspan=5)

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

values = ['all'] + list(recipes['Recipe'].unique())
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


def executeList():
    myLabel2 = Label(root, text="List has been created...I think")
    myLabel2.grid(row=10, column=6, columnspan=5)
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

    x['Duplicate_search'] = x.duplicated(subset='Ingredient',
                                         keep=False)  # This function identifies duplicates, by adding a new column and setting all dups to True.
    # by setting keep = False, all dups are True
    x = x.sort_values(by='Ingredient')
    x.to_excel('step1.xlsx')

    nondups = x.loc[(x['Duplicate_search'] == False)]  # locate a list of all NON duplicates, and save for later use
    dups = x.loc[(x['Duplicate_search'] == True)]  # locate a lost of ALL duplicates, to work with now
    dups = np.unique(dups['Ingredient'])  # Create a list of all the unique ingredients that are duplicated
    print(dups)
    for item in dups:  # iterate through the list of duplicates
        current_ingredient = x.loc[(x['Ingredient'] == item)]  # search the ENTIRE grocery list for all instances of the iterable item

        if len(np.unique(current_ingredient['Unit of Measure'])) == 1:  # if there is only one type of unit measure,
            sum_of_ingredients = np.sum(current_ingredient['Quantity'])  # add the quantities together
            current_ingredient['Quantity'] = sum_of_ingredients  # change the "quantity" to the sum:
            #       # currently, there will be dups on the main sheet, but they'll all have the total quantity, and I'll just drop the dups later
            #
            for_tildas = np.unique(current_ingredient['Recipe Title'])     # this next block of code will string all the recipes together that call for the duplicate items
            strings = ""                                                # so that the user can see at a glance when looking at the grocery list
            for k in range(0, len(for_tildas)):
                name = for_tildas[k]
                strings = strings + str(name) + str("\u007e")
            current_ingredient['Recipe Title'] = strings
            nondups = pd.concat([nondups, current_ingredient])          # concat this duplicated ingredient onto the list of nondups
        #
        elif len(np.unique(current_ingredient['Unit of Measure'])) != 1:  # if theres duplicates that aren't the same unit of measure
            nondups = pd.concat([nondups, current_ingredient])          # make sure that's back on the main list as well.

    nondups.to_excel('step2.xlsx')
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
myButton.grid(row=9, column=6, columnspan=5)

root.mainloop()
