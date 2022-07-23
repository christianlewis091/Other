import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PyAstronomy import pyasl
import seaborn as sns
from finance_functions import long_date_to_decimal_date, monthly_averages, monthly_sums

size1 = 5
colors = sns.color_palette("rocket", 6)
colors2 = sns.color_palette("mako", 6)
seshadri = ['#c3121e', '#0348a1', '#ffb01c', '#027608', '#0193b0', '#9c5300', '#949c01', '#7104b5']

"""
The file I'm reading in was mostly processed in the Preprocessing file but a little bit by hand at the end
because I got tired of adding to the libraries. It will be easier at the end of coming months. 
Here I'm going to analyze data from the 2022 to 2021 year. 
"""

df = pd.read_excel(r'C:\Users\lewis\venv\python310\python-masterclass-remaster-shared\finances\combined_edited.xlsx')

"""
# Here is the output from the print line above: 
['Amazon Purchases' 'Brazil' 'CBL Allowance' 'Car' 'Christian Allowance'
 'Clothing' 'Coffees' 'Eating Out' 'Gas List' 'Groceries'
 'Health and Fitness' 'Household Items' 'Income' 'IntraTransfer'
 'Investments' 'Joint Allowance' 'Negligible' 'New York City'
 'Out w Friends' 'Paying Off Credit Cards' 'Pottery' 'Reimbursed'
 'Sammy Allowance' 'Subscriptions' 'TBD' 'Taxes' 'Travel' 'Unexpected'
 'Utilities' 'Wellington Month 1']
 
 I want to do calculations but exclude a few categories that will muddle the calculation. These include, 
 Investments (these aren't really "outgoing" but moving money from one place to another"
 Paying off credit cards (If we kept this in, as well as the credit transactino itself, 
 each purchase would be essentially doubled) 
 """

df = df.loc[(df['Type'] != 'Investments') &
            (df['Type'] != 'Paying Off Credit Cards') &
            (df['Type'] != 'Income') &
            (df['Type'] != 'IntraTransfer')]
total_outgoing = np.sum(df['Amount'])

types = np.unique(df['Type'])
monthly_summaries = pd.DataFrame()
sums_array = []
percents = []
for i in range(0, len(types)):
    # Data for the WHOLE YEAR
    category = df.loc[(df['Type']) == types[i]]                        # index by category
    sums = (np.sum(category['Amount']))
    percent_of_total = ((np.sum(category['Amount'])) / total_outgoing) * 100   # find the sum of all transactions in that cat
    if percent_of_total < 0:                                           # flag if it's positive (income)
        print(types[i])
        print(percent_of_total)
    percents.append(percent_of_total)                                  # append to an array for later
    sums_array.append(sums)                                            # append to an array for later

    # Data for MONTH TO MONTH
    month_sum = monthly_sums(category['Decimal_date'], category['Amount'])  # find the monthly sum from X month.
    x = month_sum[0]  # date                                          # extract the date back out
    y = month_sum[1]  # sum                                           # extract the sum back out.
    summary = pd.DataFrame({"Date": x, "sum": y, "Type": types[i]}).dropna()
    monthly_summaries = pd.concat([monthly_summaries, summary])

summary2 = pd.DataFrame({"Type": types, "Sum": sums_array, "Percents": percents}).dropna()


# https://matplotlib.org/3.1.0/gallery/pie_and_polar_charts/pie_and_donut_labels.html
fig, ax = plt.subplots(figsize=(16, 8), subplot_kw=dict(aspect="equal"))

wedges, texts = ax.pie(percents, wedgeprops=dict(width=0.5), startangle=-40)

bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
kw = dict(arrowprops=dict(arrowstyle="-"),
          bbox=bbox_props, zorder=0, va="center")

for i, p in enumerate(wedges):
    ang = (p.theta2 - p.theta1)/2. + p.theta1
    y = np.sin(np.deg2rad(ang))
    x = np.cos(np.deg2rad(ang))
    horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
    connectionstyle = "angle,angleA=0,angleB={}".format(ang)
    kw["arrowprops"].update({"connectionstyle": connectionstyle})
    ax.annotate(types[i], xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
                horizontalalignment=horizontalalignment, **kw)

plt.savefig('pie.png',
            dpi=300, bbox_inches="tight")
plt.close()

"""
Now that I've gotten a broad idea of our spending overall, 
lets try to understand our savings. 

I'm going to define our savings as: 

Savings = Incoming - outgoing - investments. 
Savings = Income - (all transactions) - investments [ leaving out the same categories above that are confusing]

I'm reading the file back in because I removed these columns from the DataFrame before
"""
df = pd.read_excel(r'C:\Users\lewis\venv\python310\python-masterclass-remaster-shared\finances\combined_edited.xlsx')
df_adjusted = df.loc[(df['Type'] != 'Paying Off Credit Cards') &
             (df['Type'] != 'IntraTransfer') &
             (df['Type'] != 'Income') &
             (df['Type'] != 'Investments') &
             (df['Type'] != 'Car')]

income = df.loc[(df['Type']) == 'Income']
investments = df.loc[(df['Type']) == 'Investments']
car = df.loc[(df['Type']) == 'Car']

income = np.sum(income['Amount'])
investments = np.sum(investments['Amount'])
car = np.sum(car['Amount'])

total_outgoing = np.sum(df_adjusted['Amount'])  # all outgoing real transactions

proj_sav = income + total_outgoing
print(proj_sav)

"""
Now I want to calculate our ACTUAL SAVINGS.

THis is the sum of our accounts THEN - our accounts NOW. 
"""

df = pd.read_excel(r'C:\Users\lewis\venv\python310\python-masterclass-remaster-shared\finances\combined_edited.xlsx')
cbl_sav = df.loc[(df['Origin'] == 'CBL Savings')]
cbl_check = df.loc[(df['Origin'] == 'CBL Checking')]
sc_sav = df.loc[(df['Origin'] == 'SC Savings')]
sc_check = df.loc[(df['Origin'] == 'SC Checking')]
anz = df.loc[(df['Origin'] == 'ANZ')]
plt.scatter(cbl_sav['Decimal_date'], cbl_sav['Running Bal.'], color = colors2[1], label = 'CBL Savings', marker = 'D')
plt.scatter(cbl_check['Decimal_date'], cbl_check['Running Bal.'], color = colors2[2], label = 'CBL Checking', marker = '^')
plt.scatter(sc_sav['Decimal_date'],sc_sav['Running Bal.'], color = colors2[3], label = 'SC Savings', marker = 'o')
plt.scatter(sc_check['Decimal_date'], sc_check['Running Bal.'], color = colors2[4], label = 'SC Checking', marker = 'X')
plt.scatter(anz['Decimal_date'], anz['Running Bal.'], color = colors2[5], label = 'SC Checking', marker = '*')
plt.axvline(x = 2021.99, color = 'black', alpha = 0.2, linestyle = 'solid')
plt.axvline(x = 2022.04, color = 'black', alpha = 0.2, linestyle = 'solid') # BRazil

plt.axvline(x = 2021.44, color = 'black', alpha = 0.2, linestyle = 'solid')
plt.axvline(x = 2021.47, color = 'black', alpha = 0.2, linestyle = 'solid') # NYC
plt.axvline(x = 2022.40, color = 'black', alpha = 0.2, linestyle = 'solid')
plt.axvline(x = 2022.42, color = 'black', alpha = 0.2, linestyle = 'solid') # car
plt.legend()
plt.xlabel('Date', fontsize=14)
plt.ylabel('$ USD', fontsize=14)  # label the y axis


plt.savefig('scatter.png',
            dpi=300, bbox_inches="tight")
plt.close()

