import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import seaborn as sns
from preprocessing import combine

# general plot parameters
colors = sns.color_palette("rocket", 6)
colors2 = sns.color_palette("mako", 6)
mpl.rcParams['pdf.fonttype'] = 42
mpl.rcParams['font.size'] = 10
size1 = 5


fig = plt.figure(4, figsize=(10,10))
gs = gridspec.GridSpec(4, 4)
gs.update(wspace=1, hspace=1)
# Generate first panel


ins = combine.loc[(combine['Incoming/Outgoing'] == 'incoming')]
outs = combine.loc[(combine['Incoming/Outgoing'] == 'outgoing')]
sc_savings = combine.loc[(combine['Origin'] == 'SC Savings')]
sc_checking = combine.loc[(combine['Origin'] == 'SC Checking')]
cbl_checking = combine.loc[(combine['Origin'] == 'CBL Checking')]
cbl_savings = combine.loc[(combine['Origin'] == 'CBL Savings')]

anz = combine.loc[(combine['Origin'] == 'ANZ')]
print(anz)
cbl_savings = combine.loc[(combine['Origin'] == 'CBL Savings')]
x = ins['Amount']
x.to_excel('testing2.xlsx')

# xtr_subsplot = fig.add_subplot(gs[0:3, 0:4])
plt.scatter(ins['Decimal_date'], ins['Amount'], label='Ins')
plt.plot(anz['Decimal_date'], anz['Running Bal.'], color=colors2[3], label='ANZ')
plt.plot(sc_savings['Decimal_date'], sc_savings['Running Bal.'], color=colors[1], label='SC Savings')
plt.plot(sc_checking['Decimal_date'], sc_checking['Running Bal.'], color=colors[5], label='SC Checking')
plt.plot(cbl_checking['Decimal_date'], cbl_checking['Running Bal.'], color=colors2[1], label='cbl_checking')
plt.plot(cbl_savings['Decimal_date'], cbl_savings['Running Bal.'], color=colors2[5], label='cbl_savings')
plt.scatter(outs['Decimal_date'], outs['Amount'], color=colors[3], label='outs')
plt.legend()
# xtr_subsplot = fig.add_subplot(gs[3:4, 0:4])
# plt.scatter(outs['Decimal_date'], outs['Amount'], color=colors[3], label='outs')
# plt.legend()
# plt.savefig('p1.png', dpi=300, bbox_inches="tight")
# plot data for left panel
plt.show()
