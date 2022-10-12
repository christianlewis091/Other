import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import pandas as pd
from finance_functions import long_date_to_decimal_date

c1 = '#4575b4'
c2 = '#74add1'
c3 = '#f46d43'
c4 = '#fdae61'
c5 = '#d73027'
c6 = '#8073ac'
c7 = '#fee0b6'
c8 = '#e08214'

# Add months here as they come
Aug2022 = pd.read_excel(r'C:\Users\lewis\venv\python310\python-masterclass-remaster-shared\personal_projects\anz_calculator\04_output_data\August_2022_Results.xlsx', sheet_name = 'Spending Summary')
Sep2022 = pd.read_excel(r'C:\Users\lewis\venv\python310\python-masterclass-remaster-shared\personal_projects\anz_calculator\04_output_data\September_2022_Results.xlsx', sheet_name = 'Spending Summary')
June2022 = pd.read_excel(r'C:\Users\lewis\venv\python310\python-masterclass-remaster-shared\personal_projects\anz_calculator\04_output_data\June_2022_Results.xlsx', sheet_name = 'Spending Summary')
July2022 = pd.read_excel(r'C:\Users\lewis\venv\python310\python-masterclass-remaster-shared\personal_projects\anz_calculator\04_output_data\July_2022_Results.xlsx', sheet_name = 'Spending Summary')
May2022 = pd.read_excel(r'C:\Users\lewis\venv\python310\python-masterclass-remaster-shared\personal_projects\anz_calculator\04_output_data\May_2022_Results.xlsx', sheet_name = 'Spending Summary')

# And here
May2022['Month'] = 'May'
June2022['Month'] = 'June'
July2022['Month'] = 'July'
Aug2022['Month'] = 'August'
Sep2022['Month'] = 'Sep'

# And here
cat = pd.concat([May2022, July2022, July2022, Aug2022, Sep2022])

cbl_allowance = cat.loc[cat['Type'] == 'Christian Allowance']
clothing = cat.loc[cat['Type'] == 'Clothing']
coffees =  cat.loc[cat['Type'] == 'Coffees']
eatout =  cat.loc[cat['Type'] == 'Eating Out']
groceries =  cat.loc[cat['Type'] == 'Groceries']
health =  cat.loc[cat['Type'] == 'Health and Fitness']
house =  cat.loc[cat['Type'] == 'Household Items']
joint =  cat.loc[cat['Type'] == 'Joint Allowance']
friends =  cat.loc[cat['Type'] == 'Out w Friends']
pottery =  cat.loc[cat['Type'] == 'Pottery']
sammy_allowance =  cat.loc[cat['Type'] == 'Sammy Allowance']
subs =  cat.loc[cat['Type'] == 'Subscriptions']
tbd =  cat.loc[cat['Type'] == 'TBD']
unexpected =  cat.loc[cat['Type'] == 'Unexpected']
utilities =  cat.loc[cat['Type'] == 'Utilities']


fig = plt.figure(1)
plt.plot(cbl_allowance['Month'], cbl_allowance['Sum'], color = c1, label = 'CBL Allowance', marker = 'o')
plt.plot(sammy_allowance['Month'], sammy_allowance['Sum'], color = c2, label = 'Sammy Allowance', marker = 'x')
plt.plot(joint['Month'], joint['Sum'], color = c3, label = 'Joint Allowance', marker = '^')
plt.legend()
plt.savefig('C:/Users/lewis/venv/python310/python-masterclass-remaster-shared/personal_projects/anz_calculator/05_texfiles/sum1.png',
            dpi=300, bbox_inches="tight")
plt.close()

fig = plt.figure(2)
plt.plot(subs['Month'], subs['Sum'], color = c1, label = 'subscriptions', marker = 'o')
plt.plot(utilities['Month'], utilities['Sum'], color = c2, label = 'utilities', marker = 'x')
plt.legend()
plt.savefig('C:/Users/lewis/venv/python310/python-masterclass-remaster-shared/personal_projects/anz_calculator/05_texfiles/sum2.png',
            dpi=300, bbox_inches="tight")
plt.close()

fig = plt.figure(3)
plt.plot(health['Month'], health['Sum'], color = c1, label = 'health', marker = 'o')
plt.plot(house['Month'], house['Sum'], color = c2, label = 'house', marker = 'x')
plt.plot(clothing['Month'], clothing['Sum'], color = c3, label = 'clothing', marker = '^')
plt.plot(groceries['Month'], groceries['Sum'], color = c4, label = 'groceries', marker = '>')
plt.legend()
plt.savefig('C:/Users/lewis/venv/python310/python-masterclass-remaster-shared/personal_projects/anz_calculator/05_texfiles/sum3.png',
            dpi=300, bbox_inches="tight")
plt.close()

fig = plt.figure(4)
plt.plot(coffees['Month'], coffees['Sum'], color = c1, label = 'coffees', marker = 'o')
plt.plot(eatout['Month'], eatout['Sum'], color = c2, label = 'Eating out', marker = 'x')
plt.plot(friends['Month'], friends['Sum'], color = c3, label = 'Friends', marker = '^')
plt.plot(pottery['Month'], pottery['Sum'], color = c4, label = 'Pottery', marker = '>')
plt.legend()
plt.savefig('C:/Users/lewis/venv/python310/python-masterclass-remaster-shared/personal_projects/anz_calculator/05_texfiles/sum4.png',
            dpi=300, bbox_inches="tight")
plt.close()

fig = plt.figure(4)
plt.plot(tbd['Month'], tbd['Sum'], color = c1, label = 'Yet Uncategorized', marker = 'o')
plt.legend()
plt.savefig('C:/Users/lewis/venv/python310/python-masterclass-remaster-shared/personal_projects/anz_calculator/05_texfiles/sum5.png',
            dpi=300, bbox_inches="tight")
plt.close()
