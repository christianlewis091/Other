import numpy as np
import pandas as pd
from finance_functions import long_date_to_decimal_date, monthly_averages, monthly_sums
import matplotlib.pyplot as plt
from Transaction_Library import library, names
"""
Steps to use this MONTHLY FINANCE ANALYSIS script: 
1. Import the data from ANZ site in .CSV format and save.
2. Run the script, which will create an outfile called Results.xlsx.
3. Check the outfile is the same length as the original file with the data.
4. Find where Type is TBD, and add keywords to the Transaction Library (there will be less and less TBD's as the months
   go on, and the library is built up). 
5. After adding keys, run again.
6. After you're happy with the categorization, then you can look at the results.  
"""

# Step 1: Import that data you're interested in in CSV Format.
anz = pd.read_csv(r'G:\My Drive\Money\BudgetAnalysis\python_input_files\anzJuly2022.csv')

"""
Pre-process the ANZ file for budget analysis. The exporting is doing odd things to the date format so I'm going 
to ignore that for now, hence the first block of code is commented out. 
"""
# anz_x = anz['Date']                           # The next three lines converts the "Date" column to a decimal date
# anz_x = long_date_to_decimal_date(anz_x)      # and adds it onto the DataFrame
# anz['Decimal_date'] = anz_x

# Because with ANZ, the details of the transaction may be written in "Details" columns, on "Particulars" I lump
# them all together for the later indexer to search and categorize. This is what this for loop does
# In the 2021_2022 financial analysis, the ANZ data was exported differently and the "Amount" column needed additional
# work. Here that's not needed so that second for-loop is omitted.
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

# These next two lines help with the categorization step in the future. Let's pre-set all "types" to TBD, and also
# add an index to merge on later. This Index will be used to check for duplicates after categorization.
anz['Type'] = 'TBD'
anz['Merge_Index'] = np.linspace(0, len(anz)-1, len(anz))

# This loop will go through each of the lists in the library, each containing a key word related to some transaction
# Inside each of the lists, the code will loop through the ANZ file and assign each row a "type" if it finds
# the transaction description meets something in the list.
# While the loop runs, it compiles only data where a match is found, therefore, we have to merge the new file with
# the original file to the the "TBD's" back, where matches have not been found.
templaterow = pd.DataFrame()
for k in range(0, len(library)):
    mt_array = []
    for i in range(0, len(anz)):
        row = anz.iloc[i]  # access the first row
        descrip = row['Description']  # access the column "descriptions"
        for item in library[k]:
            if item in descrip:
                mt_array.append(row)
    x = pd.DataFrame(mt_array).reset_index(drop = True)
    x['Type'] = names[k]
    templaterow = pd.concat([templaterow, x])


anz = pd.concat([templaterow, anz]).drop_duplicates(subset = 'Merge_Index', keep='first')
anz = anz[['Type','Description','Date','Amount']]
# anz.to_excel('Results.xlsx')

transactions = anz.loc[(anz['Amount'] < 0)]
transactions = np.sum(transactions['Amount'])

income = anz.loc[(anz['Type'] == 'Income')]
income = np.sum(income['Amount'])

utility_goal = 0.5 * income
savings_goal = 0.25 * income
spend_goal = 0.25 * income
amount_saved = income + transactions  # transactions are already negative so don't subtract
print("At 25% of the income, your savings goal was {}, while your actual savings is {}.".format(savings_goal, amount_saved))


df = anz.loc[(anz['Type'] != 'Investments') &                  # The renaming of the dataset that happens here
             (anz['Type'] != 'Paying Off Credit Cards') &      # is simply a holdover from when the code was adapted
             (anz['Type'] != 'Income') &                       # from an earlier version.
             (anz['Type'] != 'IntraTransfer')]

types = np.unique(df['Type'])
monthly_summaries = pd.DataFrame()
sums_array = []
percents = []
for i in range(0, len(types)):
    category = df.loc[(df['Type']) == types[i]]                        # index according to the first type of category in the dataset
    sums = (np.sum(category['Amount']))
    percent_of_total = ((np.sum(category['Amount'])) / transactions) * 100   # find the sum of all transactions in that cat
    if percent_of_total < 0:                                           # flag if it's positive (income)
        print(types[i])
        print(percent_of_total)
    percents.append(percent_of_total)                                  # append to an array for later
    sums_array.append(sums)                                            # append to an array for later
    summary = pd.DataFrame({"sum": sums, "Type": types[i]}, index = [0]).dropna()
    monthly_summaries = pd.concat([monthly_summaries, summary])

summary2 = pd.DataFrame({"Type": types, "Sum": sums_array, "Percents": percents}).dropna()

writer = pd.ExcelWriter(r'G:/My Drive/Money/BudgetAnalysis/python_output_files/July_2022_Results.xlsx', engine='openpyxl')
anz.to_excel(writer, sheet_name='Categorized Transactions')
summary2.to_excel(writer, sheet_name='Spending Summary')
writer.save()


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

plt.savefig(r'G:/My Drive/Money/BudgetAnalysis/python_pie_charts/July_2022_Results.png',
            dpi=300, bbox_inches="tight")
plt.close()












