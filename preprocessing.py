import numpy as np
import pandas as pd
from finance_functions import long_date_to_decimal_date
import matplotlib.pyplot as plt
from Transaction_Library import invest_list, Intra_transfer_list, subs_list, utility_list, gas_list, grocery_list, health_list, clothing_list, pottery_list, eatout_list, amazon_list, coffee_list, household_list, unexpected_list, sammy_allowance, income, paying_off_cards, christian_allowance, out_w_friends

"""
The GOAL of the "Preprocessing.py" is just to pre-process the data into a nice excel sheet 
for later analysis, and to create a template for future use of financial analyses. 
This sheet preprocesses data for Financial year 2021-2022. 

All transactions with ANZ have been converted to USD according to the exchange rate on July 12, 2022. 

"""
sc_credit = pd.read_excel(r'C:\Users\lewis\Desktop\Finances_asofJune2022.xlsx', skiprows=0, sheet_name = 'SC_Cap1_0721-0722')
sc_sav = pd.read_excel(r'C:\Users\lewis\Desktop\Finances_asofJune2022.xlsx', skiprows=6, sheet_name = 'SC_BofA_Sav_0721-0722')
sc_check = pd.read_excel(r'C:\Users\lewis\Desktop\Finances_asofJune2022.xlsx', skiprows=0, sheet_name = 'SC_BofA_0721-0722')
anz = pd.read_excel(r'C:\Users\lewis\Desktop\Finances_asofJune2022.xlsx', skiprows=0, sheet_name = 'ANZ_April-July6')
cbl_checking = pd.read_excel(r'C:\Users\lewis\Desktop\bofa\checking_cbl.xlsx', skiprows=6)
cbl_sav = pd.read_excel(r'C:\Users\lewis\Desktop\bofa\cbl_sav.xlsx', skiprows=6)
# Christian's Credit card from the last year
df = pd.read_excel(r'C:\Users\lewis\Desktop\bofa\April2022_5051.xlsx')
df2 = pd.read_excel(r'C:\Users\lewis\Desktop\bofa\May2022_5051.xlsx')
df3 = pd.read_excel(r'C:\Users\lewis\Desktop\bofa\June2022_5051.xlsx')
df4 = pd.read_excel(r'C:\Users\lewis\Desktop\bofa\July2021_5051.xlsx')
df5 = pd.read_excel(r'C:\Users\lewis\Desktop\bofa\August2021_5051.xlsx')
df6 = pd.read_excel(r'C:\Users\lewis\Desktop\bofa\September2021_5051.xlsx')
df7 = pd.read_excel(r'C:\Users\lewis\Desktop\bofa\October2021_5051.xlsx')
df8 = pd.read_excel(r'C:\Users\lewis\Desktop\bofa\December2021_5051.xlsx')
df9 = pd.read_excel(r'C:\Users\lewis\Desktop\bofa\January2022_5051.xlsx')
df10 = pd.read_excel(r'C:\Users\lewis\Desktop\bofa\February2022_5051.xlsx')
df11 = pd.read_excel(r'C:\Users\lewis\Desktop\bofa\March2022_5051.xlsx')
df12 = pd.read_excel(r'C:\Users\lewis\Desktop\bofa\nov.xlsx')
cbl_credit = pd.concat([df, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12]).reset_index(drop = True)

"""
Reformatting SC credit
"""
sc_credit_x = sc_credit['Transaction Date']                     # adjust transcation date for plotting
sc_credit_x = long_date_to_decimal_date(sc_credit_x)            # adjust transcation date for plotting
sc_credit['Decimal_date'] = sc_credit_x                         # adjust transcation date for plotting
sc_credit = sc_credit.rename(columns={"Debit": "Amount"})     # Renaming columns
sc_credit = sc_credit.rename(columns={"Transaction Date": "Long Date"})     # Renaming columns
sc_credit = sc_credit.drop(columns=['Posted Date','Card No.','Credit','Category'], axis = 1)
# sc_credit['Incoming/Outgoing'] = 'outgoing'                     # setting categories of incoming or outgoing
sc_credit['Amount'] = sc_credit['Amount'] * -1              # making all outgoing negative.
sc_credit['Origin'] = 'SC Capital 1 Credit Card'

"""
Reformatting SC Savings
"""
sc_save_x = sc_sav['Date']
sc_save_x = long_date_to_decimal_date(sc_save_x)
sc_sav['Decimal_date'] = sc_save_x
# sc_sav = sc_sav.drop(columns=['Date'], axis = 1)
sc_sav = sc_sav.rename(columns={"Date": "Long Date"})
sc_sav['Origin'] = 'SC Savings'

"""
Reformatting SC Checking
"""
sc_check_x = sc_check['Date']
sc_check_x = long_date_to_decimal_date(sc_check_x)
sc_check['Decimal_date'] = sc_check_x
sc_check = sc_check.rename(columns={"Date": "Long Date"})
sc_check['Origin'] = 'SC Checking'
# sc_check.to_excel('testing.xlsx')

"""
Reformatting CBL Credit
"""

cbl_credit_x = cbl_credit['Posted Date']
cbl_credit_x = long_date_to_decimal_date(cbl_credit_x)
cbl_credit['Decimal_date'] = cbl_credit_x
cbl_credit = cbl_credit.drop(columns=['Reference Number','testcell'], axis = 1)
cbl_credit = cbl_credit.rename(columns={"Posted Date": "Long Date"})
cbl_credit['Origin'] = 'CBL Credit Card'
cbl_credit = cbl_credit.rename(columns={"Payee": "Description"})

"""
Reformatting CBL checking
"""

cbl_checking_x = cbl_checking['Date']
cbl_checking_x = long_date_to_decimal_date(cbl_checking_x)
cbl_checking['Decimal_date'] = cbl_checking_x
array = []
cbl_checking['Origin'] = 'CBL Checking'
cbl_checking = cbl_checking.rename(columns={"Date": "Long Date"})

"""
Reformatting CBL saving
"""

cbl_sav_x = cbl_sav['Date']
cbl_sav_x = long_date_to_decimal_date(cbl_sav_x)
cbl_sav['Decimal_date'] = cbl_sav_x
cbl_sav['Origin'] = 'CBL Savings'
cbl_sav = cbl_sav.rename(columns={"Date": "Long Date"})

"""
Now dealing with ANZ
"""
anz_x = anz['Transaction Date']
anz_x = long_date_to_decimal_date(anz_x)
anz['Decimal_date'] = anz_x
# put the columns "details, particulars, code, and reference" all into one column
array = []
for i in range(0, len(anz)):
    x = anz.iloc[i]  # grab the first row
    a = x['Particulars']
    b = x['Code']
    c = x['Reference']
    d = x['Details']
    e = str(d) + ' ' + str(b) + ' ' + str(c) + ' ' + str(a)
    array.append(e)
anz['Description'] = pd.DataFrame(array)

# convert the "AMoutn format into a normal one so I can add the "incoming outgoing condition"
array = []
for i in range(0, len(anz)):
    x = anz.iloc[i]  # grab first row
    x = x['Amount']
    x = str(x)
    if ',' in x:  # problems with commmas so I'm going to remove them
        x = x.replace(',', '')
    if '--' in x:  # these indicate spent money
        x = (x[4:len(x)])
        x = np.float64(x)
        x = x * -1  # convert to negative to match other formatting
        x = array.append(x)

    else:
        x = array.append(x)  # not multiplying by -1
anz['Amount'] = pd.DataFrame(array)

anz['Amount'] = np.float64(anz['Amount']) * 0.61  # covert to usd according to exchange rate on 7/12/22
anz = anz.drop(columns=['Processed Date','Type','Details',
                        'Reference','Code','To/From Account Number',
                        'Conversion Charge','Foreign Currency Amount','Particulars'], axis = 1)
anz = anz.rename(columns={"Balance": "Running Bal.", "Transaction Date": "Long Date"})

anz['Origin'] = 'ANZ'
# todo check data lenght so we're not missing anything
combine = pd.concat([sc_sav, sc_check, sc_credit, cbl_credit, cbl_checking, cbl_sav, anz]).reset_index(drop=True)
combine = combine.drop(columns=['Unnamed: 8'])
combine['Merge_Index'] = np.linspace(0, len(combine)-1, len(combine))
combine['Type'] = 'TBD'
combine.to_excel('combined.xlsx')
"""
Now that the data has been pre-processed, I'm going to try to categorize them by searching for these keywords. 
At the end, it will put together a sheet with the added keys, and then I can filter on them and see our spending habits
in more detail. 
I can search faster for those that haven't been added yet then searching for NaN. 
"""
# Search through the libraries and add keys to the items that fit each description
templaterow = pd.DataFrame()
library = [invest_list, Intra_transfer_list, subs_list, utility_list, gas_list, grocery_list, health_list, clothing_list, pottery_list, eatout_list, amazon_list, coffee_list, household_list, unexpected_list, sammy_allowance, income, paying_off_cards, christian_allowance, out_w_friends]
names = ['Investments','IntraTransfer','Subscriptions','Utilities','Gas List','Groceries','Health and Fitness','Clothing','Pottery','Eating Out','Amazon Purchases','Coffees','Household Items','Unexpected','Sammy Allowance','Income','Paying Off Credit Cards','Christian Allowance','Out w Friends']
for k in range(0, len(library)):
    mt_array = []
    for i in range(0, len(combine)):
        row = combine.iloc[i]  # access the first row
        descrip = row['Description']  # access the column "descriptions"
        for item in library[k]:
            if item in descrip:
                mt_array.append(row)
    x = pd.DataFrame(mt_array).reset_index(drop = True)
    x['Type'] = names[k]
    templaterow = pd.concat([templaterow, x])
templaterow.to_excel('diditwork.xlsx')

# add key for when we were traveling, and our first Month in Wellington.
df = pd.read_excel(r'C:\Users\lewis\venv\python310\python-masterclass-remaster-shared\finances\brazil.xlsx')
x = df['Brazil']
x = long_date_to_decimal_date(x)
x1 = x[0]
x2 = x[1]

mt_array = []
for i in range(0, len(combine)):
    row = combine.iloc[i]  # access the first row
    day = row['Decimal_date']
    if x1 < day < x2:
        mt_array.append(row)
Brazil = pd.DataFrame(mt_array).reset_index(drop = True)
Brazil['Type'] = 'Brazil'

df = pd.read_excel(r'C:\Users\lewis\venv\python310\python-masterclass-remaster-shared\finances\brazil.xlsx')
x = df['Welly']
x = long_date_to_decimal_date(x)

x1 = x[0]
x2 = x[1]

mt_array = []
for i in range(0, len(combine)):
    row = combine.iloc[i]  # access the first row
    day = row['Decimal_date']
    if x1 < day < x2:
        mt_array.append(row)
Welly = pd.DataFrame(mt_array).reset_index(drop = True)
Welly['Type'] = 'Wellington Month 1'


# add the two traveling dataframes to that created from the big loop above.
categorizing = pd.concat([templaterow, Brazil, Welly])
categorizing['Amount'] = np.float64(categorizing['Amount'])
combine['Amount'] = np.float64(combine['Amount'])
combine_labeled = pd.concat([categorizing, combine]).drop_duplicates(subset = 'Merge_Index', keep='first')
combine_labeled = combine_labeled.drop(columns=['Address', 'Merge_Index'])
combine_labeled.to_excel('test.xlsx')


