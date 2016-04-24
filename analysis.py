# stochastic processes - analysis
# mike saint-antoine


import pandas
import math


print(' ')
print('Properties of macro-finance data')
print('---------------------------------------------------------------')
print(' ')
print('0. Data input')


data = pandas.ExcelFile("FRED_qtrly.xls")
data = data.parse("edited")



# getting an array of dates
dates = []
for row in data["DATE"]:
    dates.append(row)


nobs = len(dates)
# should be 208


# getting the data into arrays

# levels
GDPC96 = []
for row in data["GDPC96"]:
    GDPC96.append(math.log(row))

PCECC96 = []
for row in data["PCECC96"]:
    PCECC96.append(math.log(row))

SP500 = []
for row in data["SP500"]:
    SP500.append(math.log(row))

INDPRO = []
for row in data["INDPRO"]:
    INDPRO.append(math.log(row))

GS10 = []
for row in data["GS10"]:
    GS10.append(math.log(row))

# rates

PAYEMS = []
for row in data["PAYEMS"]:
    PAYEMS.append(row)

FEDFUNDS = []
for row in data["FEDFUNDS"]:
    FEDFUNDS.append(row)





# calculating growth
GDPC96_growth = []
for i in range(len(GDPC96)-1):
    GDPC96_growth.append(400 * (GDPC96[i+1] - GDPC96[i]))

PCECC96_growth = []
for i in range(len(PCECC96)-1):
    PCECC96_growth.append(400 * (PCECC96[i+1] - PCECC96[i]))

SP500_growth = []
for i in range(len(SP500)-1):
    SP500_growth.append(400 * (SP500[i+1] - SP500[i]))

INDPRO_growth = []
for i in range(len(INDPRO)-1):
    INDPRO_growth.append(400 * (INDPRO[i+1] - INDPRO[i]))

GS10_growth = []
for i in range(len(GS10)-1):
    GS10_growth.append(400 * (GS10[i+1] - GS10[i]))


# calculating yearly growth
GDPC96_growth2 = []
for i in range(len(GDPC96)-4):
    GDPC96_growth2.append(100 * (GDPC96[i+4] - GDPC96[i]))

PCECC96_growth2 = []
for i in range(len(PCECC96)-4):
    PCECC96_growth2.append(100 * (PCECC96[i+4] - PCECC96[i]))

SP500_growth2 = []
for i in range(len(SP500)-4):
    SP500_growth2.append(100 * (SP500[i+4] - SP500[i]))

INDPRO_growth2 = []
for i in range(len(INDPRO)-4):
    INDPRO_growth2.append(100 * (INDPRO[i+4] - INDPRO[i]))

GS10_growth2 = []
for i in range(len(GS10)-4):
    GS10_growth2.append(100 * (GS10[i+4] - GS10[i]))




print(' ')
print('1. Autocorrelation functions')























print("done")
