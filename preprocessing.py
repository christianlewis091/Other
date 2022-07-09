import numpy as np
import pandas as pd
from finance_functions import long_date_to_decimal_date

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
sc_credit = sc_credit.drop(columns=['Transaction Date', 'Posted Date','Card No.','Credit','Category'], axis = 1)
sc_credit['Incoming/Outgoing'] = 'outgoing'                     # setting categories of incoming or outgoing
sc_credit['Amount'] = sc_credit['Amount'] * -1              # making all outgoing negative.
sc_credit['Origin'] = 'SC Capital 1 Credit Card'



"""
Reformatting SC Savings
"""

sc_save_x = sc_sav['Date']
sc_save_x = long_date_to_decimal_date(sc_save_x)
sc_sav['Decimal_date'] = sc_save_x
sc_sav = sc_sav.drop(columns=['Date'], axis = 1)
array = []
for i in range(0, len(sc_sav)):
    x = sc_sav.iloc[i]  # grab the first row
    x = x['Amount']
    if (x < 0):
        condition = 'outgoing'
        array.append(condition)
    if (x >= 0):
        condition = 'incoming'
        array.append(condition)
sc_sav['Incoming/Outgoing'] = pd.DataFrame(array)
sc_sav['Origin'] = 'SC Savings'

"""
Reformatting SC Checking
"""
sc_check_x = sc_check['Date']
sc_check_x = long_date_to_decimal_date(sc_check_x)
sc_check['Decimal_date'] = sc_check_x
sc_check = sc_check.drop(columns=['Date'], axis = 1)
array = []
for i in range(0, len(sc_check)):
    x = sc_check.iloc[i]  # grab the first row
    x = x['Amount']
    if (x < 0):
        condition = 'outgoing'
        array.append(condition)
    if (x >= 0):
        condition = 'incoming'
        array.append(condition)
sc_check['Incoming/Outgoing'] = pd.DataFrame(array)
sc_check['Origin'] = 'SC Checking'
# sc_check.to_excel('testing.xlsx')

"""
Reformatting CBL Credit
"""

cbl_credit_x = cbl_credit['Posted Date']
cbl_credit_x = long_date_to_decimal_date(cbl_credit_x)
cbl_credit['Decimal_date'] = cbl_credit_x
cbl_credit = cbl_credit.drop(columns=['Posted Date', 'Reference Number','testcell'], axis = 1)
array = []
for i in range(0, len(cbl_credit)):
    x = cbl_credit.iloc[i]  # grab the first row
    x = x['Amount']
    if (x < 0):
        condition = 'outgoing'
        array.append(condition)
    if (x >= 0):
        condition = 'incoming'
        array.append(condition)
cbl_credit['Incoming/Outgoing'] = pd.DataFrame(array)
cbl_credit['Origin'] = 'CBL Credit Card'
cbl_credit = cbl_credit.rename(columns={"Payee": "Description"})

"""
Reformatting CBL checking
"""

cbl_checking_x = cbl_checking['Date']
cbl_checking_x = long_date_to_decimal_date(cbl_checking_x)
cbl_checking['Decimal_date'] = cbl_checking_x
array = []
for i in range(0, len(cbl_checking)):
    x = cbl_checking.iloc[i]  # grab the first row
    x = x['Amount']
    if (x < 0):
        condition = 'outgoing'
        array.append(condition)
    if (x >= 0):
        condition = 'incoming'
        array.append(condition)
cbl_checking['Incoming/Outgoing'] = pd.DataFrame(array)
cbl_checking['Origin'] = 'CBL Checking'
cbl_checking= cbl_checking.drop(columns=['Date'], axis = 1)

"""
Reformatting CBL saving
"""

cbl_sav_x = cbl_sav['Date']
cbl_sav_x = long_date_to_decimal_date(cbl_sav_x)
cbl_sav['Decimal_date'] = cbl_sav_x
array = []
for i in range(0, len(cbl_sav)):
    x = cbl_sav.iloc[i]  # grab the first row
    x = x['Amount']
    x = float(x)
    if (x < 0):

        condition = 'outgoing'
        array.append(condition)

    if (x >= 0):
        condition = 'incoming'
        array.append(condition)
cbl_sav['Incoming/Outgoing'] = pd.DataFrame(array)
cbl_sav['Origin'] = 'CBL Savings'
cbl_sav = cbl_sav.drop(columns=['Date'], axis = 1)

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

array = []
for i in range(0, len(anz)):
    x = anz.iloc[i]  # grab the first row
    x = x['Amount']
    x = np.float64(x)
    if (x < 0):
        condition = 'outgoing'
        array.append(condition)
    if (x >= 0):
        condition = 'incoming'
        array.append(condition)
anz['Incoming/Outgoing'] = pd.DataFrame(array)
anz = anz.drop(columns=['Transaction Date','Processed Date','Type','Details',
                        'Reference','Code','To/From Account Number',
                        'Conversion Charge','Foreign Currency Amount','Particulars'], axis = 1)
anz = anz.rename(columns={"Balance": "Running Bal."})
anz['Origin'] = 'ANZ'
# todo check data lenght so we're not missing anything
combine = pd.concat([sc_sav, sc_check, sc_credit, cbl_credit, cbl_checking, cbl_sav, anz]).reset_index(drop=True)
combine = combine.drop(columns=['Unnamed: 8'])
combine['Merge_Index'] = np.linspace(0, len(combine)-1, len(combine))
combine.to_excel('reformat.xlsx')
"""
Now that the data has been pre-processed, I'm going to try to categorize them by searching for these keywords. 
At the end, it will put together a sheet with the added keys, and then I can filter on them and see our spending habits
in more detail. 
I can search faster for those that haven't been added yet then searching for NaN. 
"""

invest_list = ['BETTER', 'BRK 6878', 'Acorns Invest']
Intra_transfer_list = ['CHK 7388']
subs_list = ['NOTION','SPOTIFY', 'Netflix','HBO','ADOBE CREATIVE','APPLE','GOOGLE','KPCC','WNYC','SQ *CENTER FOR INDIVIDUAL']
utility_list = ['SPARK','SKINNY','Marterra', 'SO CAL GAS', 'SO CAL EDISON', 'ATT*BILL','ALLSTATE','TMOBILE']
gas_list = ['CHEVRON','76 - COSTA MESA']
grocery_list = ['H MART','ORIENTAL PANTRY','NEW WORLD','99 RANCH MARKET', 'SPROUTS FARMERS MAR', 'ZION','SEIWA','TOKYO CENTRAL','RALPHS','VONS','TRADER JOE','WHOLESOME','SMART AND FINAL']
health_list = ['Paulas Choice LLC','CVS','WALGREENS','WHOLE HEALTH PHARMACY']
clothing_list = ['BAGGU','LULULEMON','BANANAREPUBLIC US 8045','Uniqlo','EVERLANE','OUTDOOR VOICES','URBAN OUTFITTERS','MADEWELL']
pottery_list = ['AARDVARK', 'SQ *COSTA MESA CERAMICS S', 'CITY OF IRVINE COMMUNITY']
eatout_list = ['KAIZEN SHABU','TST* PARADISE DYNASTY LLC','SQ *HUDSONS COOKIES','BCD-IRVINE','WAHOO','SQ *FOUR SEA RESTAURANT','IN N OUT BURGER 038','LANTERN CAFE PHO VIETNAME','TST* Jans Health Bar - C','KAZUYAKITORI & SAKEBAR',
               'QILIN TEA HOUSE','MITSUWA','JJ BAKERY']
amazon_list = ['AMZN Mktp']
coffee_list = ['SQ *BACIO DI LATTE','SQ *NEAT COFFEE','THE COFFEE BEAN Y TEA LEA']
household_list = ['BEST BUY','HOME DEPOT','IKEA ORANGE COUNTY LLC']
unexpected_list = ['UBER TRIP','PET HOSPITAL','BEVERLY RADIOLOGY MEDICAL''EXPRESSCARE MEDICAL CLINI','FBI IDENTIFICATION RECORD']
sammy_allowance = ['ARTARAMA','NRB FASHION COMPANY LT','ROOTS JEWELRY','GDP*AHRITTAUM BEAUTY SALO','SEPHORA.COM']

master_array = [invest_list, Intra_transfer_list, subs_list, utility_list, gas_list, grocery_list, health_list, clothing_list, pottery_list, eatout_list, amazon_list, coffee_list,
                household_list, unexpected_list, sammy_allowance]
array = []

for i in range(0, len(master_array)):
    x = master_array[i]      # access the first sublist
    print(x)
    for item in x:
        array.append(item)

new_master_array = array









# Now I'm going to change all values with "Betterment and Acorn" from transactions to investments.
mt_array = []
for i in range(0, len(combine)):
    row = combine.iloc[i]  # access the first row
    descrip = row['Description']  # access the column "descriptions"
    for item in invest_list:
        if item in descrip:
            mt_array.append(row)
Investments = pd.DataFrame(mt_array).reset_index(drop = True)
Investments['Type'] = 'Investments'

# Intra transfers
mt_array = []
for i in range(0, len(combine)):
    row = combine.iloc[i]  # access the first row
    descrip = row['Description']  # access the column "descriptions"
    for item in Intra_transfer_list:
        if item in descrip:
            mt_array.append(row)
Intra_transfers = pd.DataFrame(mt_array).reset_index(drop = True)
Intra_transfers['Type'] = 'Intra_transfers'

# Subscriptions
mt_array = []
for i in range(0, len(combine)):
    row = combine.iloc[i]  # access the first row
    descrip = row['Description']  # access the column "descriptions"
    for item in subs_list:
        if item in descrip:
            mt_array.append(row)
Subscriptions = pd.DataFrame(mt_array).reset_index(drop = True)
Subscriptions['Type'] = 'Subscriptions'

# Rent/Utilities
mt_array = []
for i in range(0, len(combine)):
    row = combine.iloc[i]  # access the first row
    descrip = row['Description']  # access the column "descriptions"
    for item in utility_list:
        if item in descrip:
            mt_array.append(row)
Rent_Utilities = pd.DataFrame(mt_array).reset_index(drop = True)
Rent_Utilities['Type'] = 'Rent_Utilities'

# Gas
mt_array = []
for i in range(0, len(combine)):
    row = combine.iloc[i]  # access the first row
    descrip = row['Description']  # access the column "descriptions"
    for item in gas_list:
        if item in descrip:
            mt_array.append(row)
Gas = pd.DataFrame(mt_array).reset_index(drop = True)
Gas['Type'] = 'Gas'

# Groceries
mt_array = []
for i in range(0, len(combine)):
    row = combine.iloc[i]  # access the first row
    descrip = row['Description']  # access the column "descriptions"
    for item in grocery_list:
        if item in descrip:
            mt_array.append(row)
Groceries = pd.DataFrame(mt_array).reset_index(drop = True)
Groceries['Type'] = 'Groceries'

# Health and Cosmetics
mt_array = []
for i in range(0, len(combine)):
    row = combine.iloc[i]  # access the first row
    descrip = row['Description']  # access the column "descriptions"
    for item in health_list:
        if item in descrip:
            mt_array.append(row)
Health = pd.DataFrame(mt_array).reset_index(drop = True)
Health['Type'] = 'Health'

# Clothing
mt_array = []
for i in range(0, len(combine)):
    row = combine.iloc[i]  # access the first row
    descrip = row['Description']  # access the column "descriptions"
    for item in clothing_list:
        if item in descrip:
            mt_array.append(row)
Clothing = pd.DataFrame(mt_array).reset_index(drop = True)
Clothing['Type'] = 'Clothing'

# Eating Out
mt_array = []
for i in range(0, len(combine)):
    row = combine.iloc[i]  # access the first row
    descrip = row['Description']  # access the column "descriptions"
    for item in eatout_list:
        if item in descrip:
            mt_array.append(row)
EatingOut= pd.DataFrame(mt_array).reset_index(drop = True)
EatingOut['Type'] = 'EatingOut'

# pottery
mt_array = []
for i in range(0, len(combine)):
    row = combine.iloc[i]  # access the first row
    descrip = row['Description']  # access the column "descriptions"
    for item in pottery_list:
        if item in descrip:
            mt_array.append(row)
Pottery = pd.DataFrame(mt_array).reset_index(drop = True)
Pottery['Type'] = 'Pottery'

result = []
mt_array = []
for i in range(0, len(combine)):
    row = combine.iloc[i]  # access the first row
    descrip = row['Description']  # access the column "descriptions"
    if item in master_array in descrip:
        print('yes')

# Categorized = pd.DataFrame(mt_array).reset_index(drop = True)
# Pottery['Type'] = 'Pottery'

# # Check what I'm missing by seeing what doesnt have a key yet
categorizing = pd.concat([Investments, Intra_transfers, Rent_Utilities, Subscriptions, Rent_Utilities, Gas, Groceries, Health, Clothing, EatingOut, Pottery, NoKey])

# print(len(categorizing))
# # categorizing.to_excel('test.xlsx')