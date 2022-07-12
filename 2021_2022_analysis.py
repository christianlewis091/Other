import numpy as np
import pandas as pd
from finance_functions import long_date_to_decimal_date, monthly_sums
import matplotlib.pyplot as plt

"""
The file I'm reading in was mostly processed in the Preprocessing file but a little bit by hand at the end
because I got tired of adding to the libraries. It will be easier at the end of coming months. 
Here I'm going to analyze data from the 2022 to 2021 year. 
"""

df = pd.read_excel(r'C:\Users\lewis\venv\python310\python-masterclass-remaster-shared\finances\combined_edited.xlsx')

# edit NAMES to edit the Pie chart and other calculations
names = ['Subscriptions','Utilities','Gas List','Groceries','Health and Fitness','Clothing','Pottery','Eating Out','Amazon Purchases','Coffees','Household Items','Unexpected','Sammy Allowance','Income','Paying Off Credit Cards','Christian Allowance','Out w Friends','Travel', 'Brazil','New York City']
# names = ['Investments','IntraTransfer','Subscriptions','Utilities','Gas List','Groceries','Health and Fitness','Clothing','Pottery','Eating Out','Amazon Purchases','Coffees','Household Items','Unexpected','Sammy Allowance','Income','Paying Off Credit Cards','Christian Allowance','Out w Friends','Travel', 'Brazil','New York City']

# This for loop calculates the monthly averages of every category of data
template = pd.DataFrame()
for i in range(0, len(names)):
    batch = df.loc[(df['Type']) == names[i]]
    batch = monthly_sums(batch['Decimal_date'], batch['Amount'])
    x = batch[0]  # date
    y = batch[1]  # sum
    summary = pd.DataFrame({"Date": x, "sum": y, "Type": names[i]}).dropna()
    totals = np.sum(summary['sum'])                                              # calculate grand total
    summary = pd.DataFrame({"Date": x, "sum": y, "Type": names[i], "Total": totals}).dropna()  # add total to monthyl averages (I want grand total for a pie chart)
    template = pd.concat([template, summary])

template.to_excel('test.xlsx')