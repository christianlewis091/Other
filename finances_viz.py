import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
colors = sns.color_palette("rocket", 6)
colors2 = sns.color_palette("mako", 6)
mpl.rcParams['pdf.fonttype'] = 42
mpl.rcParams['font.size'] = 10
size1 = 5

df = pd.read_excel(r'G:\My Drive\Money\snapshots.xlsx')
df = df.dropna(subset = 'Amount')
cbl_sav = df.loc[(df['Description'] == 'CBL savings')]
sc_gen = df.loc[(df['Description'] == 'SC gen investing')]
sc_better = df.loc[(df['Description'] == 'SC betterment savings (cash reserve)')]
sc_check = df.loc[(df['Description'] == 'SC BoA checking')]
sc_sav = df.loc[(df['Description'] == 'SC BoA savings')]
cbl_check = df.loc[(df['Description'] == 'CBL Checking')]
sc_mer = df.loc[(df['Description'] == 'SC Merrill investing')]
bit = df.loc[(df['Description'] == 'Bitcoin')]
cap1 = df.loc[(df['Description'] == 'Capital 1 rewards')]
sc_acorns = df.loc[(df['Description'] == 'SC Acorns account')]
venmo = df.loc[(df['Description'] == 'Venmo')]
anz = df.loc[(df['Description'] == 'ANZ Freedom Acct')]
tot = df.loc[(df['Description'] == 'Total')]




plt.scatter(cbl_sav['Date'], cbl_sav['Amount'], color = colors[0], label = 'CBL_Savings', marker = 'x')
plt.scatter(sc_gen['Date'], sc_gen['Amount'], color = colors[1], label = 'SC Betterment Investing', marker = '^')
plt.scatter(sc_better['Date'], sc_better['Amount'], color = colors[2], label = 'SC Betterment Savings', marker = 'D')
plt.scatter(sc_check['Date'], sc_check['Amount'], color = colors[3], label = 'SC Checking', marker = 'o')
plt.scatter(sc_sav['Date'], sc_sav['Amount'], color = colors[4], label = 'SC Savings', marker = 'x')
plt.scatter(sc_mer['Date'], sc_mer['Amount'], color = colors[5], label = 'SC Merril', marker = '^')
plt.scatter(bit['Date'], bit['Amount'], color = colors2[4], label = 'Bitcoin', marker = 'D')
plt.scatter(cap1['Date'], cap1['Amount'], color = colors2[0], label = 'Capitol 1', marker = 'o')
plt.scatter(sc_acorns['Date'], sc_acorns['Amount'], color = colors2[1], label = 'Acorns', marker = '^')
plt.scatter(venmo['Date'], venmo['Amount'], color = colors2[2], label = 'Venmo', marker = 'D')
plt.scatter(anz['Date'], anz['Amount'], color = colors2[3], label = 'ANZ', marker = 'o')
# plt.xlim([1980, 2020])
plt.ylim([0, 30000])
plt.legend()
plt.show()
plt.close()

# plt.plot(cbl_sav['Date'], cbl_sav['Amount'], color = colors[0], label = 'CBL_Savings')
# plt.plot(sc_gen['Date'], sc_gen['Amount'], color = colors[1], label = 'SC Betterment Investing')
# plt.plot(sc_better['Date'], sc_better['Amount'], color = colors[2], label = 'SC Betterment Savings')
# plt.plot(sc_check['Date'], sc_check['Amount'], color = colors[3], label = 'SC Checking')
# plt.plot(sc_sav['Date'], sc_sav['Amount'], color = colors[4], label = 'SC Savings')
# plt.plot(sc_mer['Date'], sc_mer['Amount'], color = colors[5], label = 'SC Merril')
# plt.plot(bit['Date'], bit['Amount'], color = colors2[4], label = 'Bitcoin')
# plt.plot(cap1['Date'], cap1['Amount'], color = colors2[0], label = 'Capitol 1')
# plt.plot(sc_acorns['Date'], sc_acorns['Amount'], color = colors2[1], label = 'Acorns')
# plt.plot(venmo['Date'], venmo['Amount'], color = colors2[2], label = 'Venmo')
# plt.plot(anz['Date'], anz['Amount'], color = colors2[3], label = 'ANZ')
# plt.legend()
# plt.show()

plt.scatter(tot['Date'], tot['Amount'], color = colors2[3], label = 'ANZ', marker = 'o')
plt.legend()
plt.show()
plt.close()