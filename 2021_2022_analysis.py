import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PyAstronomy import pyasl

""""
"long_date_to_decimal_date" function takes dates in the form of dd/mm/yyyy and converts them to a decimal.
This was required for the heidelberg cape grim dataset, and is quite useful overall while date formatting can be in
so many different forms.
Arguments:
x = column of dates in the form dd/mm/yyyy
Outputs:
array = column of dates in the form yyyy.decimal
To see an example, uncomment the following lines of code directly below the function definition:
"""


def long_date_to_decimal_date(x):
    array = []  # define an empty array in which the data will be stored
    for i in range(0, len(x)):  # initialize the for loop to run the length of our dataset (x)
        j = x[i]  # assign j: grab the i'th value from our dataset (x)
        decy = pyasl.decimalYear(j)  # The heavy lifting is done via this Py-astronomy package
        decy = float(decy)  # change to a float - this may be required for appending data to the array
        array.append(decy)  # append it all together into a useful column of data
    return array  # return the new data



def monthly_sums(x_values, y_values):
    x_values = np.array(x_values)
    y_values = np.array(y_values)

    Begin = 0
    Jan = 31
    Feb = 28 + 31
    Mar = 31 + 31 + 28
    Apr = 30 + 31 + 28 + 31
    May = 31 + 31 + 28 + 31 + 30
    June = 30 + 31 + 28 + 31 + 30 + 31
    July = 31 + 31 + 28 + 31 + 30 + 31 + 30
    August = 31 + 31 + 28 + 31 + 30 + 31 + 30 + 31
    Sep = 30 + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31
    Oct = 31 + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30
    Nov = 30 + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 30
    Dec = 31 + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 30 + 30
    months = np.array([Begin, Jan, Feb, Mar, Apr, May, June, July, August, Sep, Oct, Nov, Dec])
    months = months / 365

    # first, enter the available years on file:
    lin1 = np.linspace(int(min(x_values)),
                       int(max(x_values)),
                       (int(max(x_values)) - int(min(x_values)) + 1))

    # initialize some vars
    mean_of_date = 0
    mean_of_y = 0

    permarray_x = []
    permarray_y = []

    for i in range(0, len(lin1)):  # loop in the years
        year = int(lin1[i])  # grab only the integer parts of the years in the data

        for j in range(0, len(months)):  # loop in the months

            temparray_x = []
            temparray_y = []

            # print('The current month is ' + str(months[j]) + 'in year ' + str(year))
            months_min = months[j]
            # TODO fix this line of code to filter between one month and the next more accurately
            months_max = months_min + 0.08

            for k in range(0, len(y_values)):  # grab the data i want to use
                y_current = y_values[k]
                x_current = x_values[k]

                x_decimal_only = x_current - int(x_current)
                x_int = int(x_current)
                # if my data exists in the time frame I'm currently searching through,
                if (x_int == year) and (x_decimal_only >= months_min) and (x_decimal_only < months_max):
                    # append that x and y data to initialized arrays
                    temparray_x.append(x_int + months_min)
                    temparray_y.append(y_current)


            # if at the end of the month, the length of the temporary arrays are non-zero,
            # clean and append that information to a permanent array
            if len(temparray_x) != 0:
                tempsum = sum(temparray_x)
                tempmean = tempsum / len(temparray_x)  # this works fine because it sums the same # repeatedly

                tempsum2 = sum(temparray_y)
                tempmean2 = tempsum2 / len(temparray_y)



                permarray_x.append(tempmean)
                permarray_y.append(tempsum2)

                # print(permarray_x)
                # print(permarray_y)

            # else:
            #     permarray_x.append(x_int + months_min)
            #     permarray_y.append(-999)

    return permarray_x, permarray_y

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

percents = []
for i in range(0, len(types)):
    category = df.loc[(df['Type']) == types[i]]                        # index by category
    percent_of_total = (np.sum(category['Amount'])) / total_outgoing   # find the sum of all transactions in that cat
    if percent_of_total < 0:                                           # flag if it's positive (income)
        print(types[i])
        print(percent_of_total)
    percents.append(percent_of_total)                                  # append to an array for later

    month_sum = monthly_sums(category['Decimal_date'], category['Amount'])  # find the monthly sum from X month.
    x = month_sum[0]  # date                                          # extract the date back out
    y = month_sum[1]  # sum                                           # extract the sum back out.
    summary = pd.DataFrame({"Date": x, "sum": y, "Type": types[i]}).dropna()
    monthly_summaries = pd.concat([monthly_summaries, summary])


# Pie chart, where the slices will be ordered and plotted counter-clockwise:

fig1, ax1 = plt.subplots()
ax1.pie(percents, labels=types, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()



















# edit NAMES to edit the Pie chart and other calculations
# names = list(np.unique(df['Type']))

# names = ['Joint Allowance', 'Car','Subscriptions','Utilities','Gas List','Groceries','Health and Fitness','Clothing','Pottery','Eating Out','Amazon Purchases','Coffees','Household Items','Unexpected','Sammy Allowance','Christian Allowance','Out w Friends','Travel', 'Brazil','New York City']
# print(type(names))
#
# # this loop does some math for each category of data found above from the Pre-processed spreadsheet.
# total_outgoing =
# template = pd.DataFrame()
# categorical_totals = []
#
#
# for i in range(0, len(names)):                                    # run a loop the length of the list above "names"
#     batch = df.loc[(df['Type']) == names[i]]                      # grab a category from the list above.
#     sum_batch = np.sum(batch['Amount'])                           # what's the grand total from that category?
#
#
#
#
#     batch = monthly_sums(batch['Decimal_date'], batch['Amount'])  # find the monthly sum from X month.
#     x = batch[0]  # date                                          # extract the date back out
#     y = batch[1]  # sum                                           # extract the sum back out.
#     summary = pd.DataFrame({"Date": x, "sum": y, "Type": names[i]}).dropna()
#     totals = np.sum(summary['sum'])   # sum of the monthly sums
#     summary = pd.DataFrame({"Date": x, "sum": y, "Type": names[i], "Total": totals}).dropna()  # add total to monthyl averages (I want grand total for a pie chart)
#     template = pd.concat([template, summary])
#
#
# gt = np.sum(template['sum'])
#
# template2 = pd.DataFrame()
# for i in range(0, len(names)):
#     batch = template.loc[(template['Type']) == names[i]]  # access the data with this Type
#     x = batch['Total']
#     x = x.iloc[0]
#     percent = x / gt
#     percents = pd.DataFrame({"Type": names[i], "Percent": percent}, index = [0]).dropna()
#     template2 = pd.concat([template2, percents])
# print(template2)
#























