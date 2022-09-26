import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from PyAstronomy import pyasl

def long_date_to_decimal_date(x):
    array = []  # define an empty array in which the data will be stored
    for i in range(0, len(x)):  # initialize the for loop to run the length of our dataset (x)
        j = x[i]  # assign j: grab the i'th value from our dataset (x)
        decy = pyasl.decimalYear(j)  # The heavy lifting is done via this Py-astronomy package
        decy = float(decy)  # change to a float - this may be required for appending data to the array
        array.append(decy)  # append it all together into a useful column of data
    return array  # return the new data


farbe_ansto = '#4575b4' # bhd
farbe_maga = '#d73027'  # heid

df = pd.read_excel(r'C:\Users\lewis\Desktop\newbhdcgo.xlsx')
date = df['date']
df['date'] = long_date_to_decimal_date(date)


fig = plt.figure(1, figsize=(7.5,5))

plt.errorbar(df['date'], df['bhd'], yerr=df['bhd_std'], fmt='o', color=farbe_ansto, ecolor=farbe_ansto, elinewidth=1, capsize=2, label='RRL Wellington (BHD)', alpha = 1)
plt.errorbar(df['date'], df['cgo'], yerr=df['cgo_std'], fmt='o', color=farbe_maga, ecolor=farbe_maga, elinewidth=1, capsize=2, label='Heidelberg Cape Grim (CGO)', alpha = 1)
plt.ylabel('\u0394$^1$$^4$CO$_2$ (\u2030)', fontsize=14)  # label the y axis
plt.xlabel('Date')
plt.legend()
plt.savefig('C:/Users/lewis/Desktop/newbhdcgo.png',
            dpi=300, bbox_inches="tight")

a = stats.ttest_rel(df['bhd'], df['cgo'])
print(a)
x = max(df['date']) - min(df['date'])
print(x)
print(len(df))
print(len(df)/x)