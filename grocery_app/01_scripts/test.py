# https://www.youtube.com/watch?v=YXPyB4XeYLA&t=2640s&ab_channel=freeCodeCamp.org

"""
ADding some extra fields...
Side1
Side2

"""
from datetime import date
from tkinter import *
from tkinter import ttk
import pandas as pd
import numpy as np

today = date.today()
print("Today's date:", today)
df = pd.read_excel('recipebook_300723.xlsx', comment='#')
type_list = pd.read_excel('recipebook_300723.xlsx', sheet_name='Ingredient List', skiprows=10)


root = Tk()
names = df.Recipe_Title.unique()


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

e29 = StringVar()
e30 = StringVar()
e31 = StringVar()
e32 = StringVar()
e33 = StringVar()
e34 = StringVar()
e35 = StringVar()

e36 = StringVar()
e37 = StringVar()
e38 = StringVar()
e39 = StringVar()
e40 = StringVar()
e41 = StringVar()
e42 = StringVar()

e43 = StringVar()
e44 = StringVar()
e45 = StringVar()
e46 = StringVar()
e47 = StringVar()
e48 = StringVar()
e49 = StringVar()


bfast = df.loc[df['Meal'] == 'breakfast'].sort_values(by='Recipe_Title', ascending=True).reset_index(drop=True)
mid = df.loc[df['Meal'] == 'lunch'].sort_values(by='Recipe_Title', ascending=True).reset_index(drop=True)
dinn = df.loc[df['Meal'] == 'dinner'].sort_values(by='Recipe_Title', ascending=True).reset_index(drop=True)
side = df.loc[df['Meal'] == 'side'].sort_values(by='Recipe_Title', ascending=True).reset_index(drop=True)
des = df.loc[df['Meal'] == 'dessert'].sort_values(by='Recipe_Title', ascending=True).reset_index(drop=True)

all = ['all']+ list(df.Recipe_Title.unique())  # CREATES THE ITEMS IN DROPDOWN LIST
bfast = ['breakfast recipes'] + list(bfast.Recipe_Title.unique())  # CREATES THE ITEMS IN DROPDOWN LIST
mid = ['lunch recipes'] + list(mid.Recipe_Title.unique())  # CREATES THE ITEMS IN DROPDOWN LIST
dinn = ['dinner recipes'] + list(dinn.Recipe_Title.unique())  # CREATES THE ITEMS IN DROPDOWN LIST
side = ['sides'] + list(side.Recipe_Title.unique())  # CREATES THE ITEMS IN DROPDOWN LIST
des = ['dessert'] + list(des.Recipe_Title.unique())  # CREATES THE ITEMS IN DROPDOWN LIST

breakfast_column = 1
lunch_column = 2
dinner_column = 3
side_column1 = 4
side_column2 = 5

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
side1 = Label(root, text="Side #1")
side2 = Label(root, text="Side #2")
extra = Label(root, text="Else?")
dessert = Label(root, text="Dessert")

mon.grid(row=1, column=0)
tues.grid(row=2, column=0)
wed.grid(row=3, column=0)
thurs.grid(row=4, column=0)
fri.grid(row=5, column=0)
sat.grid(row=6, column=0)
sun.grid(row=7, column=0)
breakfast.grid(row=0, column=breakfast_column)
lunch.grid(row=0, column=lunch_column)
dinner.grid(row=0, column=dinner_column)
side1.grid(row=0, column=side_column1)
side2.grid(row=0, column=side_column2)
extra.grid(row=0,column=side_column2+1)
dessert.grid(row=0,column=side_column2+2)


"""
breakfast column  
"""
e1_entry = ttk.OptionMenu(root, e1, *bfast)
e2_entry = ttk.OptionMenu(root, e2, *bfast)
e3_entry = ttk.OptionMenu(root, e3, *bfast)
e4_entry = ttk.OptionMenu(root, e4, *bfast)
e5_entry = ttk.OptionMenu(root, e5, *bfast)
e6_entry = ttk.OptionMenu(root, e6, *bfast)
e7_entry = ttk.OptionMenu(root, e7, *bfast)
e1_entry.grid(row=1, column=breakfast_column)
e2_entry.grid(row=2, column=breakfast_column)
e3_entry.grid(row=3, column=breakfast_column)
e4_entry.grid(row=4, column=breakfast_column)
e5_entry.grid(row=5, column=breakfast_column)
e6_entry.grid(row=6, column=breakfast_column)
e7_entry.grid(row=7, column=breakfast_column)
"""
lunch
"""
e8_entry = ttk.OptionMenu(root, e8, *mid)
e9_entry = ttk.OptionMenu(root, e9, *mid)
e10_entry = ttk.OptionMenu(root, e10, *mid)
e11_entry = ttk.OptionMenu(root, e11, *mid)
e12_entry = ttk.OptionMenu(root, e12, *mid)
e13_entry = ttk.OptionMenu(root, e13, *mid)
e14_entry = ttk.OptionMenu(root, e14, *mid)
e8_entry.grid(row=1, column=lunch_column)
e9_entry.grid(row=2, column=lunch_column)
e10_entry.grid(row=3, column=lunch_column)
e11_entry.grid(row=4, column=lunch_column)
e12_entry.grid(row=5, column=lunch_column)
e13_entry.grid(row=6, column=lunch_column)
e14_entry.grid(row=7, column=lunch_column)
"""
dinner
"""
e15_entry = ttk.OptionMenu(root, e15, *dinn)
e16_entry = ttk.OptionMenu(root, e16, *dinn)
e17_entry = ttk.OptionMenu(root, e17, *dinn)
e18_entry = ttk.OptionMenu(root, e18, *dinn)
e19_entry = ttk.OptionMenu(root, e19, *dinn)
e20_entry = ttk.OptionMenu(root, e20, *dinn)
e21_entry = ttk.OptionMenu(root, e21, *dinn)
e15_entry.grid(row=1, column=dinner_column)
e16_entry.grid(row=2, column=dinner_column)
e17_entry.grid(row=3, column=dinner_column)
e18_entry.grid(row=4, column=dinner_column)
e19_entry.grid(row=5, column=dinner_column)
e20_entry.grid(row=6, column=dinner_column)
e21_entry.grid(row=7, column=dinner_column)

"""
side1
"""
e22_entry = ttk.OptionMenu(root, e22, *side)
e23_entry = ttk.OptionMenu(root, e23, *side)
e24_entry = ttk.OptionMenu(root, e24, *side)
e25_entry = ttk.OptionMenu(root, e25, *side)
e26_entry = ttk.OptionMenu(root, e26, *side)
e27_entry = ttk.OptionMenu(root, e27, *side)
e28_entry = ttk.OptionMenu(root, e28, *side)
e22_entry.grid(row=1, column=side_column1)
e23_entry.grid(row=2, column=side_column1)
e24_entry.grid(row=3, column=side_column1)
e25_entry.grid(row=4, column=side_column1)
e26_entry.grid(row=5, column=side_column1)
e27_entry.grid(row=6, column=side_column1)
e28_entry.grid(row=7, column=side_column1)

"""
side2
"""
e29_entry = ttk.OptionMenu(root, e29, *side)
e30_entry = ttk.OptionMenu(root, e30, *side)
e31_entry = ttk.OptionMenu(root, e31, *side)
e32_entry = ttk.OptionMenu(root, e32, *side)
e33_entry = ttk.OptionMenu(root, e33, *side)
e34_entry = ttk.OptionMenu(root, e34, *side)
e35_entry = ttk.OptionMenu(root, e35, *side)
e29_entry.grid(row=1, column=side_column2)
e30_entry.grid(row=2, column=side_column2)
e31_entry.grid(row=3, column=side_column2)
e32_entry.grid(row=4, column=side_column2)
e33_entry.grid(row=5, column=side_column2)
e34_entry.grid(row=6, column=side_column2)
e35_entry.grid(row=7, column=side_column2)

"""
extra
"""
e36_entry = ttk.OptionMenu(root, e36, *all)
e37_entry = ttk.OptionMenu(root, e37, *all)
e38_entry = ttk.OptionMenu(root, e38, *all)
e39_entry = ttk.OptionMenu(root, e39, *all)
e40_entry = ttk.OptionMenu(root, e40, *all)
e41_entry = ttk.OptionMenu(root, e41, *all)
e42_entry = ttk.OptionMenu(root, e42, *all)
e36_entry.grid(row=1, column=6)
e37_entry.grid(row=2, column=6)
e38_entry.grid(row=3, column=6)
e39_entry.grid(row=4, column=6)
e40_entry.grid(row=5, column=6)
e41_entry.grid(row=6, column=6)
e42_entry.grid(row=7, column=6)

"""
Dessert
"""

e43_entry = ttk.OptionMenu(root, e43, *des)
e44_entry = ttk.OptionMenu(root, e44, *des)
e45_entry = ttk.OptionMenu(root, e45, *des)
e46_entry = ttk.OptionMenu(root, e46, *des)
e47_entry = ttk.OptionMenu(root, e47, *des)
e48_entry = ttk.OptionMenu(root, e48, *des)
e49_entry = ttk.OptionMenu(root, e49, *des)
e43_entry.grid(row=1, column=7)
e44_entry.grid(row=2, column=7)
e45_entry.grid(row=3, column=7)
e46_entry.grid(row=4, column=7)
e47_entry.grid(row=5, column=7)
e48_entry.grid(row=6, column=7)
e49_entry.grid(row=7, column=7)



version_message = Label(root, text="Created by: Dr. Christian B. Lewis, Version 3.0, September 28, 2022")
version_message.grid(row=11, column=0, columnspan=5)
version_message = Label(root, text="For issues reach out to christian.lewis091@gmail.com")
version_message.grid(row=12, column=0, columnspan=5)


def executeList():

    # grab all the variables
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
    value29 = str(e29.get())
    value30= str(e30.get())
    value31= str(e31.get())
    value32= str(e32.get())
    value33= str(e33.get())
    value34= str(e34.get())
    value35= str(e35.get())
    value36= str(e36.get())
    value37= str(e37.get())
    value38= str(e38.get())
    value39= str(e39.get())
    value40= str(e40.get())
    value41= str(e41.get())
    value42 = str(e42.get())

    value43 = str(e43.get())
    value44 = str(e44.get())
    value45 = str(e45.get())
    value46 = str(e46.get())
    value47 = str(e47.get())
    value48 = str(e48.get())
    value49 = str(e49.get())

    varlist = [value1, value2, value3, value4, value5, value6, value7,
               value8, value9, value10, value11, value12, value13, value14,
               value15, value16, value17, value18, value19, value20, value21,
               value22, value23, value24, value25, value26, value27, value28,
               value29, value30, value31, value32, value33, value34, value35,
               value36, value37, value38, value39, value40, value41, value42,
               value43, value44, value45, value46, value47, value48, value49]

    # ASSEMBLE THE LIST
    x = pd.DataFrame()
    for i in range(0, len(names)):        # for the length of the range of the unique recipe names:
        item = names[i]                   # grab the first recipe of the unique list...
        for j in range(0, len(varlist)):               # now run through the variables (each of the dropdown boxes)
            if varlist[j] == item:                 # if the input is equal to a specific item (if you find a match)
                df_new = df.loc[(df['Recipe_Title'] == item)]  # locate this item from the database,
                x = pd.concat([x, df_new])                     # concat it to our growing database

    # Once the list has been assembled, we can append the Types and Units of Measure of each of the ingredients
    ingredient_list = x['Ingredient'].reset_index(drop=True)
    type_list_ing = type_list['Ingredient'].reset_index(drop=True)
    type_list_types = type_list['Type'].reset_index(drop=True)
    type_list_units = type_list['Unit'].reset_index(drop=True)
    type_array = []
    unit_array = []
    for m in range(0, len(x)):
        y = 1
        # loop through the ingredient database
        for n in range(0, len(type_list)):

            if str(ingredient_list[m]) == str(type_list_ing[n]):
                # print(f"{ingredient_list[m]}, {type_list_ing[n]}")
                type_array.append(type_list_types[n])
                unit_array.append(type_list_units[n])
                y = 2  #found a match

        if y == 1:  # a match hasn't been found
            type_array.append("no type")
            unit_array.append("no unit")

    working_list = pd.DataFrame({"Ingredient": ingredient_list, "Type": type_array, "Unit": unit_array, "Recipe Title": x['Recipe_Title'], "Quantity": x['Quantity']})


    # FIND AND REMOVE DUPLICATES IN THE LIST
    working_list['Duplicate_search'] = working_list.duplicated(subset='Ingredient', keep=False)  # This function identifies duplicates, by adding a new column and setting all dups to True.

    # Find Only where the duplicates are TRUE
    duplicates = working_list.loc[(working_list['Duplicate_search'] == True)]                    # dump all the duplicates into one DataFrame (here, there are still multiples of the same things in the dataframe)
    non_duplicates = working_list.loc[(working_list['Duplicate_search'] == False)]               # Well need this later for concatonation

    # create a quick unique list of duplicated ingredient names that we can use to initate a loop
    duplicates_list = np.unique(duplicates['Ingredient'])                                        # extract a list of all the duplicate ingredients

    # create empty arrays to fill
    titles = []
    quantity = []
    type_new = []
    units = []
    for i in range(0, len(duplicates_list)):
        current = duplicates_list[i]                                     # focus on the first duplicate of all of the duplicates
        current = duplicates.loc[(duplicates['Ingredient'] == current)]  # extract a quick mini dataFrame of only the current ingredient
        quant = np.sum(current['Quantity'])
        quantity.append(quant)                                           # Whats the total quantity of this ingredient
        type_new.append(current['Type'])
        units.append(current['Unit'])

        string1 = ""
        for k in range(0, len(current)):
            row = current.iloc[k]  # access the first row of the mini-dataframe for the first duplicate
            string1 = string1 + str(row['Recipe_Title']) + str('_') + str('+') + str('_')  # create a longer string of all the recipes where its used
        titles.append(string1)

    cleaned_data = pd.DataFrame({"Ingredient": duplicates_list, "Quantity": quantity, "Type": type_new, "Recipe_Title": titles, "Unit": units})
    final_list = pd.concat([cleaned_data, non_duplicates])

    final_list = final_list.sort_values(by='Type', ascending=False).reset_index(drop=True)




    # adding printing of the list functionality
    a = [value1, value2, value3, value4, value5, value6, value7]
    b = [value8, value9, value10, value11, value12, value13, value14]
    c = [value15, value16, value17, value18, value19, value20, value21]
    d = [value22, value23, value24, value25, value26, value27, value28]
    e = [value29, value30, value31, value32, value33, value34, value35]
    f = [value36, value37, value38, value39, value40, value41, value42]
    g = [value43, value44, value45, value46, value47, value48, value49]
    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    print_post = pd.DataFrame({"Day of Week": days, "Breakfast": a, "Lunch": b, "Dinner": c, "Side #1": d, "Side #2": e, "Extra": f, "Dessert": g})

    for item in ['breakfast recipes','lunch recipes','dinner recipes','sides','all']:
        print_post = print_post.replace(item, '')
    # print_post.to_excel(f'choicesV4_{today}.xlsx')

    # ASSEMBLE A SOURCE LIST
    sourceDF = pd.DataFrame()
    for i in range(0, len(names)):        # for the length of the range of the unique recipe names:
        item = names[i]                   # grab the first recipe of the unique list...
        for j in range(0, len(varlist)):               # now run through the variables (each of the dropdown boxes)
            if varlist[j] == item:                 # if the input is equal to a specific item (if you find a match)
                df_new = df.loc[(df['Recipe_Title'] == item)]  # locate this item from the database,
                sourceDF = pd.concat([x, df_new])                     # concat it to our growing database

    sourceDF = sourceDF[['Recipe_Title','Source']]
    sourceDF = sourceDF.drop_duplicates()

    with pd.ExcelWriter(f'Output_{today}.xlsx') as writer:
        final_list.to_excel(writer, sheet_name="Final List", index=False)
        print_post.to_excel(writer, sheet_name="Choices", index=False)
        sourceDF.to_excel(writer, sheet_name="Chosen Recipe Sources", index=False)


    end_message = Label(root,
                        text="Output data created! \nPlease check the folder where the .exe file is located ",
                        anchor="e", justify=LEFT)
    end_message.grid(row=16, rowspan=1, column=0, columnspan=5)


myButton = Button(root, text="Run", command=executeList, fg='blue')
myButton.grid(row=10, column=0, columnspan=7)

summary = 'This app was created by Dr. Christian B Lewis. The current version is 3.0, finalized on September 29, 2022, on a train from Berlin to the Nethlands. ' \
          'Current issues, troubleshooting comments will be listed here. ' \
          'In the future, I want to add the following:' \
          '1. I want to sort the ingredients based on what I can by at Bin Inn, and at the Farmers Market.'


def in_dev():
    top = Toplevel()
    top.geometry('500x500')
    myLabel = Label(top, text=summary, justify=LEFT, wraplength=300).pack()

myButton2 = Button(root, text="See Documentation", command=in_dev, fg='blue')
myButton2.grid(row=13, column=0, columnspan=7)


root.mainloop()

"""
Changes made between version 3 and version 3.1 (this version) is that I want to add the capability
to print the actual choices that you made. Otherwise, the options you selected are turned into a
list but the actual options are lost , which is quite unhelpful.
"""