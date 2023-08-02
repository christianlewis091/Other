import pandas as pd


db1 = pd.read_excel('recipebookV4.xlsx', comment='#')
db2 = pd.read_excel('recipebookV3.xlsx', comment='#')

db1 = db1.merge(db2, how='outer')
db1 = db1.drop_duplicates()
db1.to_excel('recipebook_300723.xlsx')