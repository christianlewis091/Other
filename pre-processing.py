import numpy as np
import pandas as pd
from finance_functions import long_date_to_decimal_date

sc_credit = pd.read_excel(r'C:\Users\lewis\Desktop\Finances_asofJune2022.xlsx', skiprows=0, sheet_name = 'SC_Cap1_0721-0722')
sc_sav = pd.read_excel(r'C:\Users\lewis\Desktop\Finances_asofJune2022.xlsx', skiprows=6, sheet_name = 'SC_BofA_Sav_0721-0722')
sc_check = pd.read_excel(r'C:\Users\lewis\Desktop\Finances_asofJune2022.xlsx', skiprows=0, sheet_name = 'SC_BofA_0721-0722')
anz = pd.read_excel(r'C:\Users\lewis\Desktop\Finances_asofJune2022.xlsx', skiprows=0, sheet_name = 'ANZ_April-July6')
cbl_checking = pd.read_csv(r'C:\Users\lewis\Desktop\bofa\checking_cbl.csv', skiprows=6)
cbl_sav = pd.read_csv(r'C:\Users\lewis\Desktop\bofa\cbl_sav.csv', skiprows=6)
# Christian's Credit card from the last year
df = pd.read_csv(r'C:\Users\lewis\Desktop\bofa\April2022_5051.csv')
df2 = pd.read_csv(r'C:\Users\lewis\Desktop\bofa\May2022_5051.csv')
df3 = pd.read_csv(r'C:\Users\lewis\Desktop\bofa\June2022_5051.csv')
df4 = pd.read_csv(r'C:\Users\lewis\Desktop\bofa\July2021_5051.csv')
df5 = pd.read_csv(r'C:\Users\lewis\Desktop\bofa\August2021_5051.csv')
df6 = pd.read_csv(r'C:\Users\lewis\Desktop\bofa\September2021_5051.csv')
df7 = pd.read_csv(r'C:\Users\lewis\Desktop\bofa\October2021_5051.csv')
df8 = pd.read_csv(r'C:\Users\lewis\Desktop\bofa\December2021_5051.csv')
df9 = pd.read_csv(r'C:\Users\lewis\Desktop\bofa\January2022_5051.csv')
df10 = pd.read_csv(r'C:\Users\lewis\Desktop\bofa\February2022_5051.csv')
df11 = pd.read_csv(r'C:\Users\lewis\Desktop\bofa\March2022_5051.csv')
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
print(sc_credit.columns)


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
    print(x)
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

print(sc_check.columns)
sc_check.to_excel('testing.xlsx')

"""
Reformatting CBL Credit
"""
cbl_credit_x = cbl_credit['Posted Date']
cbl_credit_x = long_date_to_decimal_date(cbl_credit_x)
cbl_credit['Decimal_date'] = cbl_credit_x



