import numpy as np
from finance_functions import long_date_to_decimal_date
import pandas as pd

df = pd.read_excel(r'C:\Users\lewis\venv\python310\python-masterclass-remaster-shared\finances\brazil.xlsx')
x = df['Brazil']
x = long_date_to_decimal_date(x)
print(x)

