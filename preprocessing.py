import numpy as np
import pandas as pd
from finance_functions import long_date_to_decimal_date
import matplotlib.pyplot as plt

def monthly_averages(x_values, y_values):
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
                tempmean = tempsum / len(temparray_x)  # this works fine because it averages the same # repeatedly

                tempsum2 = sum(temparray_y)
                tempmean2 = tempsum2 / len(temparray_y)



                permarray_x.append(tempmean)
                permarray_y.append(tempmean2)

                # print(permarray_x)
                # print(permarray_y)

            # else:
            #     permarray_x.append(x_int + months_min)
            #     permarray_y.append(-999)

    return permarray_x, permarray_y


sc_credit = pd.read_excel(r'C:\Users\lewis\Desktop\Finances_asofJune2022.xlsx', skiprows=0, sheet_name = 'SC_Cap1_0721-0722')
sc_sav = pd.read_excel(r'C:\Users\lewis\Desktop\Finances_asofJune2022.xlsx', skiprows=6, sheet_name = 'SC_BofA_Sav_0721-0722')
sc_check = pd.read_excel(r'C:\Users\lewis\Desktop\Finances_asofJune2022.xlsx', skiprows=0, sheet_name = 'SC_BofA_0721-0722')
anz = pd.read_excel(r'C:\Users\lewis\Desktop\Finances_asofJune2022.xlsx', skiprows=0, sheet_name = 'ANZ_April-July6')
cbl_checking = pd.read_excel(r'C:\Users\lewis\Desktop\bofa\checking_cbl.xlsx', skiprows=6)
cbl_sav = pd.read_excel(r'C:\Users\lewis\Desktop\bofa\cbl_sav.xlsx', skiprows=6)

# Christian's Credit card from the last year
df = pd.read_excel(r'C:\Users\lewis\Desktop\bofa\April2022_5051.xlsx')
df2 = pd.read_excel(r'C:\Users\lewis\Desktop\bofa\May2022_5051.xlsx')
df3 = pd.read_excel(r'C:\Users\lewis\Desktop\bofa\June2022_5051.xlsx')
df4 = pd.read_excel(r'C:\Users\lewis\Desktop\bofa\July2021_5051.xlsx')
df5 = pd.read_excel(r'C:\Users\lewis\Desktop\bofa\August2021_5051.xlsx')
df6 = pd.read_excel(r'C:\Users\lewis\Desktop\bofa\September2021_5051.xlsx')
df7 = pd.read_excel(r'C:\Users\lewis\Desktop\bofa\October2021_5051.xlsx')
df8 = pd.read_excel(r'C:\Users\lewis\Desktop\bofa\December2021_5051.xlsx')
df9 = pd.read_excel(r'C:\Users\lewis\Desktop\bofa\January2022_5051.xlsx')
df10 = pd.read_excel(r'C:\Users\lewis\Desktop\bofa\February2022_5051.xlsx')
df11 = pd.read_excel(r'C:\Users\lewis\Desktop\bofa\March2022_5051.xlsx')
df12 = pd.read_excel(r'C:\Users\lewis\Desktop\bofa\nov.xlsx')
cbl_credit = pd.concat([df, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12]).reset_index(drop = True)

"""
Reformatting SC credit
"""

sc_credit_x = sc_credit['Transaction Date']                     # adjust transcation date for plotting
sc_credit_x = long_date_to_decimal_date(sc_credit_x)            # adjust transcation date for plotting
sc_credit['Decimal_date'] = sc_credit_x                         # adjust transcation date for plotting
sc_credit = sc_credit.rename(columns={"Debit": "Amount"})     # Renaming columns
sc_credit = sc_credit.rename(columns={"Transaction Date": "Long Date"})     # Renaming columns
sc_credit = sc_credit.drop(columns=['Posted Date','Card No.','Credit','Category'], axis = 1)
sc_credit['Incoming/Outgoing'] = 'outgoing'                     # setting categories of incoming or outgoing
sc_credit['Amount'] = sc_credit['Amount'] * -1              # making all outgoing negative.
sc_credit['Origin'] = 'SC Capital 1 Credit Card'



"""
Reformatting SC Savings
"""

sc_save_x = sc_sav['Date']
sc_save_x = long_date_to_decimal_date(sc_save_x)
sc_sav['Decimal_date'] = sc_save_x
# sc_sav = sc_sav.drop(columns=['Date'], axis = 1)
sc_sav = sc_sav.rename(columns={"Date": "Long Date"})
array = []
for i in range(0, len(sc_sav)):
    x = sc_sav.iloc[i]  # grab the first row
    x = x['Amount']
    if (x < 0):
        condition = 'outgoing'
        array.append(condition)
    if (x >= 0):
        condition = 'incoming'
        array.append(condition)
sc_sav['Incoming/Outgoing'] = pd.DataFrame(array)
sc_sav['Origin'] = 'SC Savings'

"""
Reformatting SC Checking
"""
sc_check_x = sc_check['Date']
sc_check_x = long_date_to_decimal_date(sc_check_x)
sc_check['Decimal_date'] = sc_check_x
sc_check = sc_check.rename(columns={"Date": "Long Date"})
array = []
for i in range(0, len(sc_check)):
    x = sc_check.iloc[i]  # grab the first row
    x = x['Amount']
    if (x < 0):
        condition = 'outgoing'
        array.append(condition)
    if (x >= 0):
        condition = 'incoming'
        array.append(condition)
sc_check['Incoming/Outgoing'] = pd.DataFrame(array)
sc_check['Origin'] = 'SC Checking'
# sc_check.to_excel('testing.xlsx')

"""
Reformatting CBL Credit
"""

cbl_credit_x = cbl_credit['Posted Date']
cbl_credit_x = long_date_to_decimal_date(cbl_credit_x)
cbl_credit['Decimal_date'] = cbl_credit_x
cbl_credit = cbl_credit.drop(columns=['Reference Number','testcell'], axis = 1)
cbl_credit = cbl_credit.rename(columns={"Posted Date": "Long Date"})
array = []
for i in range(0, len(cbl_credit)):
    x = cbl_credit.iloc[i]  # grab the first row
    x = x['Amount']
    if (x < 0):
        condition = 'outgoing'
        array.append(condition)
    if (x >= 0):
        condition = 'incoming'
        array.append(condition)
cbl_credit['Incoming/Outgoing'] = pd.DataFrame(array)
cbl_credit['Origin'] = 'CBL Credit Card'
cbl_credit = cbl_credit.rename(columns={"Payee": "Description"})

"""
Reformatting CBL checking
"""

cbl_checking_x = cbl_checking['Date']
cbl_checking_x = long_date_to_decimal_date(cbl_checking_x)
cbl_checking['Decimal_date'] = cbl_checking_x
array = []
for i in range(0, len(cbl_checking)):
    x = cbl_checking.iloc[i]  # grab the first row
    x = x['Amount']
    if (x < 0):
        condition = 'outgoing'
        array.append(condition)
    if (x >= 0):
        condition = 'incoming'
        array.append(condition)
cbl_checking['Incoming/Outgoing'] = pd.DataFrame(array)
cbl_checking['Origin'] = 'CBL Checking'
cbl_checking = cbl_checking.rename(columns={"Date": "Long Date"})

"""
Reformatting CBL saving
"""

cbl_sav_x = cbl_sav['Date']
cbl_sav_x = long_date_to_decimal_date(cbl_sav_x)
cbl_sav['Decimal_date'] = cbl_sav_x
array = []
for i in range(0, len(cbl_sav)):
    x = cbl_sav.iloc[i]  # grab the first row
    x = x['Amount']
    x = float(x)
    if (x < 0):

        condition = 'outgoing'
        array.append(condition)

    if (x >= 0):
        condition = 'incoming'
        array.append(condition)
cbl_sav['Incoming/Outgoing'] = pd.DataFrame(array)
cbl_sav['Origin'] = 'CBL Savings'
cbl_sav = cbl_sav.rename(columns={"Date": "Long Date"})

"""
Now dealing with ANZ
"""
anz_x = anz['Transaction Date']
anz_x = long_date_to_decimal_date(anz_x)
anz['Decimal_date'] = anz_x
# put the columns "details, particulars, code, and reference" all into one column
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

# convert the "AMoutn format into a normal one so I can add the "incoming outgoing condition"
array = []
for i in range(0, len(anz)):
    x = anz.iloc[i]  # grab first row
    x = x['Amount']
    x = str(x)
    if ',' in x:  # problems with commmas so I'm going to remove them
        x = x.replace(',', '')


    if '--' in x:  # these indicate spent money
        x = (x[4:len(x)])
        x = np.float64(x)
        x = x * -1  # convert to negative to match other formatting
        x = array.append(x)

    else:
        x = array.append(x)  # not multiplying by -1
anz['Amount'] = pd.DataFrame(array)

array = []
for i in range(0, len(anz)):
    x = anz.iloc[i]  # grab the first row
    x = x['Amount']
    x = np.float64(x)
    if (x < 0):
        condition = 'outgoing'
        array.append(condition)
    if (x >= 0):
        condition = 'incoming'
        array.append(condition)
anz['Incoming/Outgoing'] = pd.DataFrame(array)
anz = anz.drop(columns=['Processed Date','Type','Details',
                        'Reference','Code','To/From Account Number',
                        'Conversion Charge','Foreign Currency Amount','Particulars'], axis = 1)
anz = anz.rename(columns={"Balance": "Running Bal."})
anz['Origin'] = 'ANZ'
# todo check data lenght so we're not missing anything
combine = pd.concat([sc_sav, sc_check, sc_credit, cbl_credit, cbl_checking, cbl_sav, anz]).reset_index(drop=True)
combine = combine.drop(columns=['Unnamed: 8'])
combine['Merge_Index'] = np.linspace(0, len(combine)-1, len(combine))
# combine.to_excel('reformat.xlsx')
"""
Now that the data has been pre-processed, I'm going to try to categorize them by searching for these keywords. 
At the end, it will put together a sheet with the added keys, and then I can filter on them and see our spending habits
in more detail. 
I can search faster for those that haven't been added yet then searching for NaN. 
"""

invest_list = ['BETTER', 'BRK 6878', 'Acorns Invest']
Intra_transfer_list = ['DEPOSIT *MOBILE MD','WIRE TYPE:FX OUT DATE','Online Banking Transfer','CHK 7388','KEEP THE CHANGE TRANSFER']
subs_list = ['Skinny','Aa Insurance','Subscription DES:Acorns','Shopify','NOTION','SPOTIFY', 'Netflix','HBO','ADOBE CREATIVE','APPLE','GOOGLE','KPCC','WNYC','SQ *CENTER FOR INDIVIDUAL']
utility_list = ['Frank Energy','LEMONADE','Spark','SPARK','SKINNY','Marterra', 'SO CAL GAS', 'SO CAL EDISON', 'ATT*BILL','ALLSTATE','TMOBILE']
gas_list = ['EXXONMOBIL','SHELL OIL','76 - SAND CANYON','76 - PEPPER TREE', '76 - NEWPORT','Bp Hutt Road Truckst','CHEVRON','76 - COSTA MESA']
grocery_list = ['HAERE MAI','TANAKA FARMS','Commonsense','Goods Shed','Bin Inn','Oriental Pan','Countdown','Pak N Save','New World','H MART','ORIENTAL PANTRY','NEW WORLD','99 RANCH', 'SPROUTS FARMERS MAR', 'ZION','SEIWA','TOKYO CENTRAL','RALPHS','VONS','TRADER JOE','WHOLESOME','SMART AND FINAL']
health_list = ['COMPETITIVE AQUATIC SUPPLHUNTINGTON BECA','RACQUET CLUB OF IRVINE 949-786-3000 CA','SQ *LIVING SUCCESS CENTER','RITE AID','Sephora','Unichem','Salon Villair','Unichem Willis','Life Pharmacy', 'Paulas Choice LLC','CVS','WALGREENS','WHOLE HEALTH PHARMACY']
clothing_list = ['NORDSTROM','ANTHROPOLOGIE','GLASSONS - LAMBTON QUAY','Cotton On Body','ZARA','UNIQLO','NORDSTROM-RACK','Kathmandu','Macpac','Skechers','BAGGU','LULULEMON','BANANAREPUBLIC US 8045','Uniqlo','EVERLANE','OUTDOOR VOICES','URBAN OUTFITTERS','MADEWELL']
pottery_list = ['VESSEL','PAPER MART','SQ *KENNY SMITH POT TUSTIN CA','SQ *SAWDUST FESTIVAL ONLIgosq.com CA','SP * SHOP TENZO','Etsy.com - hsinchuen','SP * DIAMONDCORE TOOLS','Wellington Potters','SQ *TIM HAHNE DESIGNS','TICKETS-WELLINGTON POTTE','USPS','FEDEX','BAKER PARTY RENTALS','AARDVARK', 'SQ *COSTA MESA CERAMICS S', 'CITY OF IRVINE COMMUNITY']
eatout_list = ['TICK TOCK DINER','KATZS DELICATESSEN','TST* IVAN RAMEN USA','SUPER POLLO','YANG CHOW RESTAURANT','MADEE THAI KITCHEN','SONOKO SAKAI','TST* PANDA EXPRESS','BEST UGLY BAGELS','RUTABEGORZ','DINTAI FUNG COSTA','MUGIMARU','LUCKY BOY HAMBURGERS','WAWONA PIONEER MARKET','WURSTKUCHE','ALOHA HAWAIIAN BBQ','SQ *SGT. PEPPERONI','PHO BA CO','KOJI RAMEN. ','SQ *WOON','SQ *GOLDEN REEF DINER Rockville CenNY','MALULU SUSHI','LUNA GRILL','THE CRACK SHACK','KITAKATA RAMEN BAN','MOCHI BEARD','POKE ME','TENDER GREENS IRVINE SP','Food For The','St Pierr', 'Simply India','Dragons','WAYFARER BREAD','ISO RESTAURANTE BIST','SQ *FOUR SEA RESTAU','PIZZA', 'TAGLIARE PIZZA','FUKADA','KABOB REPUBLIC ','SANTOUKA','TACO MESA','F O L K S Costa Mesa CA','CAPITAL DIM SUM','CAPITAL NOODLE BAR','HA LONG','MEIJI SEIMEN','STACKS PANCAKE HOUSE','THE CLUBHOUSE - RESTAURANANAHEIM CA','EUREKA','IN N OUT BURGER','Main St Deli','Winnerwinner','Superm','Tj Katsu-Man','Bordeaux Bak','Pickle & Pie','Maranui Surf','Great India','Garage Proje','Pastari','Pizzeria Nap','Porno Doughn ','Abrakebabra','KAIZEN SHABU','TST* PARADISE DYNASTY LLC','SQ *HUDSONS COOKIES','BCD-IRVINE','WAHOO','SQ *FOUR SEA RESTAURANT','IN N OUT BURGER 038','LANTERN CAFE PHO VIETNAME','TST* Jans Health Bar - C','KAZUYAKITORI & SAKEBAR',
               'QILIN TEA HOUSE','MITSUWA','JJ BAKERY']
amazon_list = ['AMZN Mktp','AMAZON.COM']
coffee_list = ['PLUMERIA CAFE & CATERING','COFFEE LAB','CAFE MOARA','LION & LAMB','CHA FOR TEA','STEREOSCOPE COFFEE','SQ *PHILZ COFFEE ','HUNTINGTON CAFE SAN MARINO','SQ *ESPRESSO ON THE PALM SPRINGS CA','COFFEE TOMO','THE LOST BEAN','BIRD ROCK COFFEE','FLAGSHIP - MOONGOAT','STARBUCKS','WORK IN PROGRESS','HIDDEN HOUSE COFFEE','PEETS','CAFE ESPRESSO','Cafe Soleil','Havana Bar','Hudsons Coff','Df Espresso','Peoplescoffeeretailc','Machete Coffee','Machete Coff','SQ *BACIO DI LATTE','SQ *NEAT COFFEE','THE COFFEE BEAN Y TEA LEA']
household_list = ['3 DOLLAR JAPAN','THE INCONVENIENCE','TJMAXX','TORTOISEGENERALST','CULVER AUTO SPA','SP * THE INCONVENIENCE','The Warehous','Futon', 'The Salvatio','Noel Leeming','Trademe','DAISO', 'IKEA','FIVE STAR EXPRESS','TARGET','SUR LA TABLE','Mitre 10','Irugs.Co.Nz','Briscoes','H&M','Barry','Kmart','BEST BUY','HOME DEPOT','IKEA ORANGE COUNTY LLC']
unexpected_list = ['HAD*HARRY & DAVID','UNITY BOOKS','UNITED','NATURAL HISTORY MUSEUM','GUITAR CENTER','HARRY & DAVID','LS THE CYCLIST','LYFT RIDE','NYC FERRY QUEENS NY','ROCKVILLE','I LOVE LA TERMINAL','L & L HAWAIIAN BBQ ','REI #17 TUSTIN','MCMASTER-CARR','FOGO DE CHAO','AIRBNB','Air New Zealand','Kopata Medic','ITAMAMBUCA ECO RESORT', 'POTTERYWEST.CO.UK','ST OF CA DMV','TST* HABANA','UBER TRIP','PET HOSPITAL','BEVERLY RADIOLOGY MEDICAL''EXPRESSCARE MEDICAL CLINI','FBI IDENTIFICATION RECORD']
sammy_allowance = ['ARTIFACTUPRISING.COM','FABRIC MART INC','CAMERA, INC.','NAIL CENTER AND SPA','B&H PHOTO 800-606-6969','GEN FOOT SPA','The Fabric S','Pegasus Book','ARTARAMA','NRB FASHION COMPANY LT','ROOTS JEWELRY','GDP*AHRITTAUM BEAUTY SALO','SEPHORA.COM']
income = [' CHOU, KEH','DEPOSIT *MOBILE NJ','WIRE TYPE:FX IN DATE:','UNIVERSITY OF CA DES:','MARUGAME UDON ','Online scheduled transfer from CHK 7727','VENMO DES:CASHOUT','UC IRVINE DES:UCI','Counter Credit','Inst Geo Nuc Sc','Inst Geological Nuc nan nan Salary','Interest_Earned','ALTIUM INC','IRS TREAS','KEEPTHECHANGE','Interest Earned']
paying_off_cards = ['Online Banking payment','Online Banking transfer','CAPITAL ONE DES:']
christian_allowance = ['HI-TIME','COSTA MESA COUNTRY CLUB','SURFLINE','YOGURTLAND ','MAGS DONUTS','STAWBERRY FARMS G C','STAPLES','NEWPORT BEACH GC','RANCHO SAN JOAQUIN','7 LEAVES','MICHAELS','MESAVERDEGOLF','CHIPOTLE','DUNKIN','SAN DIEGO UNION','BEVERAGES & MORE','SHIRLEYS BAGELS','ANAHEIM HILLS','TST* GUNWHALE ALES','CITY OF NEWPORT BEACH NEWPORT','PALM DESERT COUNTRY CLUB','GOLF','Gordon Harri','Golf','Hiroshi']
out_w_friends = ['PARKING CONCEPTS','IRVINE LANES IRVINE CA','SALTY BEAR','ALL THAT BBQ','KARL STRAUSS BREWING','85C BAKERY CAFE','THE LOT FASHION ISLAND','NIGHT MARKET-O','Moshtix','Meow','Mad Butcher','SPEEDWAY','Parking Serv','NINTENDO *AMERICAUS','THE CLUBHOUSE','The Lanes','Rogue & Vaga','Sidecar Doughnuts','SIDECAR DOUGHNUTS']
combine['Type'] = 'TBD'


# # master_array = [invest_list, Intra_transfer_list, subs_list, utility_list, gas_list, grocery_list, health_list, clothing_list, pottery_list, eatout_list, amazon_list, coffee_list,
# #                 household_list, unexpected_list, sammy_allowance]

# Now I'm going to change all values with "Betterment and Acorn" from transactions to investments.
mt_array = []
for i in range(0, len(combine)):
    row = combine.iloc[i]  # access the first row
    descrip = row['Description']  # access the column "descriptions"
    for item in invest_list:
        if item in descrip:
            mt_array.append(row)
Investments = pd.DataFrame(mt_array).reset_index(drop = True)
Investments['Type'] = 'Investments'

invest_av = monthly_averages(Investments['Decimal_date'], Investments['Amount'])

# Intra transfers
mt_array = []
for i in range(0, len(combine)):
    row = combine.iloc[i]  # access the first row
    descrip = row['Description']  # access the column "descriptions"
    for item in Intra_transfer_list:
        if item in descrip:
            mt_array.append(row)
Intra_transfers = pd.DataFrame(mt_array).reset_index(drop = True)
Intra_transfers['Type'] = 'Intra_transfers'

# Subscriptions
mt_array = []
for i in range(0, len(combine)):
    row = combine.iloc[i]  # access the first row
    descrip = row['Description']  # access the column "descriptions"
    for item in subs_list:
        if item in descrip:
            mt_array.append(row)
Subscriptions = pd.DataFrame(mt_array).reset_index(drop = True)
Subscriptions['Type'] = 'Subscriptions'
subs_av = monthly_averages(Subscriptions['Decimal_date'], Subscriptions['Amount'])


# Rent/Utilities
mt_array = []
for i in range(0, len(combine)):
    row = combine.iloc[i]  # access the first row
    descrip = row['Description']  # access the column "descriptions"
    for item in utility_list:
        if item in descrip:
            mt_array.append(row)
Rent_Utilities = pd.DataFrame(mt_array).reset_index(drop = True)
Rent_Utilities['Type'] = 'Rent_Utilities'
rent_av = monthly_averages(Rent_Utilities['Decimal_date'], Rent_Utilities['Amount'])


# Gas
mt_array = []
for i in range(0, len(combine)):
    row = combine.iloc[i]  # access the first row
    descrip = row['Description']  # access the column "descriptions"
    for item in gas_list:
        if item in descrip:
            mt_array.append(row)
Gas = pd.DataFrame(mt_array).reset_index(drop = True)
Gas['Type'] = 'Gas'
gas_av = monthly_averages(Gas['Decimal_date'], Gas['Amount'])


# Groceries
mt_array = []
for i in range(0, len(combine)):
    row = combine.iloc[i]  # access the first row
    descrip = row['Description']  # access the column "descriptions"
    for item in grocery_list:
        if item in descrip:
            mt_array.append(row)
Groceries = pd.DataFrame(mt_array).reset_index(drop = True)
Groceries['Type'] = 'Groceries'
grocer_av = monthly_averages(Groceries['Decimal_date'], Groceries['Amount'])

# Health and Cosmetics
mt_array = []
for i in range(0, len(combine)):
    row = combine.iloc[i]  # access the first row
    descrip = row['Description']  # access the column "descriptions"
    for item in health_list:
        if item in descrip:
            mt_array.append(row)
Health = pd.DataFrame(mt_array).reset_index(drop = True)
Health['Type'] = 'Health'
health_av = monthly_averages(Health['Decimal_date'], Health['Amount'])


# Clothing
mt_array = []
for i in range(0, len(combine)):
    row = combine.iloc[i]  # access the first row
    descrip = row['Description']  # access the column "descriptions"
    for item in clothing_list:
        if item in descrip:
            mt_array.append(row)
Clothing = pd.DataFrame(mt_array).reset_index(drop = True)
Clothing['Type'] = 'Clothing'
clothing_av = monthly_averages(Clothing['Decimal_date'], Clothing['Amount'])


# Eating Out
mt_array = []
for i in range(0, len(combine)):
    row = combine.iloc[i]  # access the first row
    descrip = row['Description']  # access the column "descriptions"
    for item in eatout_list:
        if item in descrip:
            mt_array.append(row)
EatingOut= pd.DataFrame(mt_array).reset_index(drop = True)
EatingOut['Type'] = 'EatingOut'
eatout_av = monthly_averages(EatingOut['Decimal_date'], EatingOut['Amount'])


# pottery
mt_array = []
for i in range(0, len(combine)):
    row = combine.iloc[i]  # access the first row
    descrip = row['Description']  # access the column "descriptions"
    for item in pottery_list:
        if item in descrip:
            mt_array.append(row)
Pottery = pd.DataFrame(mt_array).reset_index(drop = True)
Pottery['Type'] = 'Pottery'
pottery_av = monthly_averages(Pottery['Decimal_date'], Pottery['Amount'])


mt_array = []
for i in range(0, len(combine)):
    row = combine.iloc[i]  # access the first row
    descrip = row['Description']  # access the column "descriptions"
    for item in amazon_list:
        if item in descrip:
            mt_array.append(row)
Amazon = pd.DataFrame(mt_array).reset_index(drop = True)
Amazon['Type'] = 'Amazon'
amazon_av = monthly_averages(Amazon['Decimal_date'], Amazon['Amount'])

mt_array = []
for i in range(0, len(combine)):
    row = combine.iloc[i]  # access the first row
    descrip = row['Description']  # access the column "descriptions"
    for item in coffee_list:
        if item in descrip:
            mt_array.append(row)
Coffee = pd.DataFrame(mt_array).reset_index(drop = True)
Coffee['Type'] = 'Coffee'
coffee_av = monthly_averages(Coffee['Decimal_date'], Coffee['Amount'])


mt_array = []
for i in range(0, len(combine)):
    row = combine.iloc[i]  # access the first row
    descrip = row['Description']  # access the column "descriptions"
    for item in household_list:
        if item in descrip:
            mt_array.append(row)
Household = pd.DataFrame(mt_array).reset_index(drop = True)
Household['Type'] = 'Household'
house_av = monthly_averages(Household['Decimal_date'], Household['Amount'])


mt_array = []
for i in range(0, len(combine)):
    row = combine.iloc[i]  # access the first row
    descrip = row['Description']  # access the column "descriptions"
    for item in unexpected_list:
        if item in descrip:
            mt_array.append(row)
Unexpected = pd.DataFrame(mt_array).reset_index(drop = True)
Unexpected['Type'] = 'Unexpected'
unex_av = monthly_averages(Unexpected['Decimal_date'], Unexpected['Amount'])


mt_array = []
for i in range(0, len(combine)):
    row = combine.iloc[i]  # access the first row
    descrip = row['Description']  # access the column "descriptions"
    for item in sammy_allowance:
        if item in descrip:
            mt_array.append(row)
Sammy_allowance = pd.DataFrame(mt_array).reset_index(drop = True)
Sammy_allowance['Type'] = 'Sammy_allowance'
SCA_av = monthly_averages(Sammy_allowance['Decimal_date'], Sammy_allowance['Amount'])


mt_array = []
for i in range(0, len(combine)):
    row = combine.iloc[i]  # access the first row
    descrip = row['Description']  # access the column "descriptions"
    for item in income:
        if item in descrip:
            mt_array.append(row)
Income = pd.DataFrame(mt_array).reset_index(drop = True)
Income['Type'] = 'Income'
# income_av = monthly_averages(Income['Decimal_date'], Income['Amount'])

mt_array = []
for i in range(0, len(combine)):
    row = combine.iloc[i]  # access the first row
    descrip = row['Description']  # access the column "descriptions"
    for item in paying_off_cards:
        if item in descrip:
            mt_array.append(row)
Paying_off_cards = pd.DataFrame(mt_array).reset_index(drop = True)
Paying_off_cards['Type'] = 'Paying_off_cards'


mt_array = []
for i in range(0, len(combine)):
    row = combine.iloc[i]  # access the first row
    descrip = row['Description']  # access the column "descriptions"
    for item in christian_allowance:
        if item in descrip:
            mt_array.append(row)
CBL_allowance = pd.DataFrame(mt_array).reset_index(drop = True)
CBL_allowance['Type'] = 'CBL allowance'
CBLA_av = monthly_averages(CBL_allowance['Decimal_date'], CBL_allowance['Amount'])


mt_array = []
for i in range(0, len(combine)):
    row = combine.iloc[i]  # access the first row
    descrip = row['Description']  # access the column "descriptions"
    for item in out_w_friends:
        if item in descrip:
            mt_array.append(row)
out_w_friends = pd.DataFrame(mt_array).reset_index(drop = True)
out_w_friends['Type'] = 'out w friends'

plt.scatter(invest_av[0], invest_av[1], label='Investments', marker='o')
plt.scatter(rent_av[0], rent_av[1], label='Rent/Utilities', marker='D')
plt.scatter(gas_av[0], gas_av[1], label='Gas', marker='X')
plt.scatter(grocer_av[0], grocer_av[1], label='Groceries', marker='^')
plt.scatter(CBLA_av[0], CBLA_av[1], label='CBL_allowance', marker='.')
plt.scatter(SCA_av[0], SCA_av[1], label='SC_allowance', marker='o')
plt.legend()
# plt.xlim(1980, 2020)
plt.ylim(-750, 0)
plt.show()
# TODO the plot describes that the code isn't working properly. All numbers are way too low


# Check what I'm missing by seeing what doesnt have a key yet
categorizing = pd.concat([Investments, Intra_transfers, Rent_Utilities, Subscriptions, Rent_Utilities,
                          Gas, Groceries, Health, Clothing, EatingOut, Pottery, Amazon, Coffee, Household,
                          Unexpected, Sammy_allowance, Income, Paying_off_cards, CBL_allowance, out_w_friends])
# , income, paying_off_cards, christian_allowance, out_w_friends
categorizing['Amount'] = np.float64(categorizing['Amount'])
combine['Amount'] = np.float64(combine['Amount'])
print(len(categorizing))
print(len(combine))
x = pd.concat([categorizing, combine]).drop_duplicates(subset = 'Merge_Index', keep='first')
print(len(x))
# x.to_excel('check.xlsx')

  
"""
Im going to check for what doesn't have a key yet by running a for loop and checking 
the Merge Indexes. 
"""
# nyc = x.loc[(x['Type'] == 'TBD')]
# nyc.to_excel('nyc.xlsx')

# TODO ADD THE REMAINING TRANSACTION KEYS INTO THE LIBRARY AND CONTINUE TO RUN UNTIL NO TBD's remain.
# THEN CAN START THE ANALYSIS


plt.show()