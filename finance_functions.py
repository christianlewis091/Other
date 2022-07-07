import numpy as np
import pandas as pd
from PyAstronomy import pyasl
from tabulate import tabulate

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