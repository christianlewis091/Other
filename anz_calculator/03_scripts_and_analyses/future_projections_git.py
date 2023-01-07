"""
I'm going to try to predict how a future budget would look with the following
variable parameters
# Variable Income (Is CBL working only i.e., is sammy staying home caring for child;
                   is Sammy still working at Altium, is Sammy working w/ NZ salary)
# Variable Mortgage Payments (I'm going to back-calculate/use the data to figure out
                              what cost of house we can afford in each situation)
# Variable amount of "Fun" Money

I'm using the 50/30/20 Framework, where 50% of income should go to expenses,
30 to fun (X), and 20 to savings (S). This will be the basis for then initial framework of the
script. X and S will grown and shrink; however when these numbers get too low
(i.e., savings is at or below zero) we know that specific situation won't work.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


"""
Chapter 1: Defining present and future income streams
"""
# First lets define the variable amounts of income
cbl_now = 5091 * 12      # currently I'm making 90k/year
cbl_raise = (95000 * 0.67)    # CBL at top tier of Sci I
cbl_raise2 = (109000 * 0.67)  # cbl at top tier of Sci II
sammy_now = (180000 * 0.39)   # Sammy's Current Salary at Altium, removing 30% for taxes
sammy_fut = (80000 * 0.67)

# Scenario A is the present, my current income plus sammy's
scen_a = cbl_now + sammy_now

# Scenario B is I get a raise, and sammy stays at Altium
scen_b = cbl_raise + sammy_now

# Scenario C is I get a bigger raise, and sammy stays at Altium
scen_c = cbl_raise2 + sammy_now

# Scenario D is the present CBL salary, sammy's not working
scen_d = cbl_now

# Scenario E is I get a raise, and sammy stays at home
scen_e = cbl_raise

# Scenario F is I get a bigger raise, and sammy stays at home
scen_f = cbl_raise2

# Scenario G is I get a raise, and sammy works for NZ company @ 80000
scen_g = cbl_raise + sammy_fut

# Scenario h is I get a raise, and sammy works for NZ company @ 90000
scen_h = cbl_raise + sammy_fut + 10000

# Scenario i is I get a bigger raise, and sammy works for NZ company @ 80000
scen_i = cbl_raise2 + sammy_fut

# Scenario j is I get a bigger raise, and sammy works for NZ company @ 90000
scen_j = cbl_raise2 + sammy_fut + 10000

income_streams = [scen_a, scen_b, scen_c, scen_d, scen_e, scen_f,
                  scen_g, scen_h, scen_i, scen_j]
income_descrips = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

"""
Chapter 2: Defining potential mortgage costs based on housing prices and 
different interest rates
"""

# Thanks Chat GPT for writing this function for me based on websites in NZ
# that calculate mortgage payments
def calculate_monthly_payment(principal, interest_rate, num_payments):
    i = interest_rate / 100 / 12
    n = num_payments
    # principal * 0.8 takes into account 20% down payment
    monthly_payment = (principal * 0.8) * (i / (1 - (1 + i)**(-n)))
    return monthly_payment


interests = np.arange(3, 8, 1)
principal = np.arange(600000, 1100000, 100000)
num_payments = 360

a = []
b = []
c = []
for i in range(0, len(interests)):
    int = interests[i]

    for j in range(0, len(principal)):
        p = principal[j]

        monthly_payment = calculate_monthly_payment(p, int, num_payments)

        a.append(int)
        b.append(p)
        c.append(monthly_payment)

data = pd.DataFrame({"Interest": a, "Principal": b, "Monthly Payment": c})
# print(data)


"""
Chapter 3: Calculate which monthly payments are viable in each scenario

We've already defined our income streams, and we have a nice matrix of 
housing data to play with. Now, using to 50/30/20 framework, lets calculate which
income scenarios are best with each monthly payment. 

Expenses = Monthly Payment - Utilities - Food - X - S
where, monthly payments were calculated in Chapter 2, Utilities is (98+209) which is 
our monthly payments to Spark and Frank's, respectively, and Food is 1100/month, which
has been our average. 

So, first, lets calculate, for the different income streams and monthly payments, 
the values of X and S. 

"""
uts = 98 + 209
food = 1100

d = []
e = []
f = []
g = []
h = []
aa = []
ab = []
ac = []
# loop through the income scenarios
for k in range(0, len(income_streams)):
    current_stream = income_streams[k]
    current_descrip = income_descrips[k]
    monthly_stream = current_stream / 12

    # nested looping through the monthly payments
    for l in range(0, len(data['Monthly Payment'])):
        x = data['Monthly Payment']
        x = x[l]
        d.append(x)

        y = data['Interest']
        y = y[l]
        e.append(y)

        z = data['Principal']
        z = z[l]
        f.append(z)


        # with this income and monthly payment, what is the percentage of money left
        s = 0.2 * monthly_stream
        remainder = monthly_stream - (x + uts + food) - s

        g.append(remainder)
        h.append(current_descrip)
        aa.append(s)

        if remainder < 0:
            comment = "Yikes"
        else:
            comment = "OK"

        ab.append(comment)
        ac.append(current_stream)

data2 = pd.DataFrame({"Income Scenario": h, "Income": ac, "Interest": e, "Principal": f, "Monthly Mortgage Payment": d,
                      "Amount Saved Per Month": s, "Remaining Money": g, "Comment": ab})
data2.to_csv(r'C:\Users\lewis\venv\python310\python-masterclass-remaster-shared\mortgage_budget\future_proj.csv')


"""
Chapter 4: Some Basic Analysis

4.1. Which Scenarios Definitely don't work? 
"""

sink = data2.loc[(data2['Income Scenario'] == 'd') | (data2['Income Scenario'] == 'e') | (data2['Income Scenario'] == 'f')]
sink.to_csv(r'C:\Users\lewis\venv\python310\python-masterclass-remaster-shared\mortgage_budget\meonly.csv')

dink = data2.loc[(data2['Income Scenario'] == 'g') | (data2['Income Scenario'] == 'a')]
dink.to_csv(r'C:\Users\lewis\venv\python310\python-masterclass-remaster-shared\mortgage_budget\us.csv')












#
# # Create a figure and a 3D Axes
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
#
# # Plot the data
# scatter = ax.scatter(sink['Interest'], sink['Principal'], sink['Income'], c=sink['Remaining Money'])  # c is an optional argument that specifies the colors of the points
#
# # Add a colorbar
# colorbar = fig.colorbar(scatter, ax=ax)
# colorbar.set_label('Color')
#
# # Show the plot
# plt.show()
#










