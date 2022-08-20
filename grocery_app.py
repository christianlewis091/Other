"""
This code will output a grocery list, based on the items a user selects. The options only include those that
currently exist in the "Recipe Book".

Date: August 20, 2022
Author: Dr. Christian Lewis
"""
from tkinter import *
import numpy as np
import pandas as pd

pd.options.mode.chained_assignment = None  # this supresses an annoying error
df = pd.read_excel(r'C:\Users\lewis\venv\python310\python-masterclass-remaster-shared\finances\recipebook.xlsx')
recipes = (np.unique(df['Recipe Title']))  # grab each unique recipe from the recipe book and print it so the
# user can see what their options are. This will be superceded by a
# dropdown menu when I get the GUI running.


print(recipes)  # shows the user what the options are
print("Please choose from the above options")
dinner1 = input("Dinner on day 1: ")
dinner2 = input("Dinner on day 2: ")
dinner3 = input("Dinner on day 3: ")
# dinner1 = 'Coffee Cake'
# dinner2 = 'Teriyake Salmon'
# dinner3 = 'Kitsune Udon'

x = pd.DataFrame()
for i in range(0, len(recipes)):
    item = recipes[i]
    if dinner1 == item:  # if the input is equal to a specific item,
        df_new = df.loc[(df['Recipe Title'] == item)]  # take the first input from the user, and find where in the
        # recipe book all items with that Recipe Title
        x = pd.concat([x, df_new])  # then add it to the DataFrame that we're building for the grocery list

    if dinner2 == item:
        df_new = df.loc[(df['Recipe Title'] == item)]  # isolate that recipe from the dataframe
        x = pd.concat([x, df_new])
    if dinner3 == item:
        df_new = df.loc[(df['Recipe Title'] == item)]  # isolate that recipe from the dataframe
        x = pd.concat([x, df_new])

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

# # TODO build up the library
# # TODO sort based on food type

