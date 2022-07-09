import numpy as np
import pandas as pd
from finance_functions import long_date_to_decimal_date

x = pd.DataFrame({"A": [ 1, 3, 4, 5],
                  "B": [ 10, 13, 14, 15],
                  "C": [ 21, 23, 24, 25],
                  })

y = pd.DataFrame({"A": [ 1, 3],
                  "B": [ 10, 13],
                  "C": [ 21, 23],
                  "Keys": ['K1', 'k2']})

z = pd.merge(x, y, how='outer')

print(x)
print(y)
print()
print(z)
