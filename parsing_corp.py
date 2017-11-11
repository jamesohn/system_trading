import numpy as np
import pandas as pd
from math import log10

# should return log(mark cap)
# time consuming
def findmarketcap(date, company_name):
    date = int(date)
    count = 0
    while count < 5:
        for data in companies[company_name]:
            if date == int(data[0]):
                print("targeted date : %s, returned data : %s" % (data[0], data[1]))
                return data[1]
        count += 1
        date += 1

def compute_growth(base, year_after):
    if year_after != None :
        return (year_after/base - 1) * 100.0
    else :
        return 0


in_file = open('seryung1.txt', 'r')

#finance_dict = {"date":{}, "company_name":{}, "cshoc":{}, "prccd" :{}}


id = 0

labels = []

firstLine = in_file.readline()
firstLine = firstLine.strip()
firstLine = firstLine.split()

labels.append(firstLine[2])
labels.append(firstLine[3])
labels.append(firstLine[4])
labels.append(firstLine[5])


# Dictionary
companies = {}

prev = 0
for row in in_file:
    row = row.strip()
    row = row.split("\t")
    row = row[2:6]
    stock = []
    if len(row) == 4 and row[0] != 'datadate' and row[2] != '' and row[3] != '': # for irregular data
        # date
        row[0] = int(row[0])
        if row[0] % 100 < 5:
            stock.append(row[0])
            # company name
            company = row[1]
            # share of outstanding
            row[2] = int(float(row[2]))
            # share price
            row[3] = int(float(row[3]))

            if row[2]*row[3] > 0:
                mkt_cap = round(log10(row[2]*row[3]), 2)
                # ln(market capitalization)
                stock.append(mkt_cap)
                # list Structure __ stock = [Date, ln(market cap)]

                # if the company already exists as a key
                if company in companies:
                    companies[company].append(stock)
                # company doesn't exist so you have to add one
                else:
                    companies[company] = []
                    companies[company].append(stock)
# finished making up dictionary(key == company name). 
# inside the key, there are bunch of lists [date, log(market Cap)]

portfolios = {}

prev = 0
f = open("newStockList.txt", 'w')
for company in companies:
    f.write('%s\n' % company)
    for row in companies[company]:
        data = [None] * 9
        # find the first day of the month
        data[0] = row[0]//100 * 100 + 1
        print("data[0]: %d, row[0]: %d" % (data[0], row[0]))
        if prev < data[0] :
            # row[1] == company name
            data[1] = row[1] # market capitalization
            one_year = data[0] + 10000
            two_year = data[0] + 20000
            three_year = data[0] + 30000

            mkt_cap_one = findmarketcap(one_year, company)
            data[2] = mkt_cap_one
            data[3] = compute_growth(data[1], mkt_cap_one) # growth rate a year after
            #return_one = int(data[3])

            mkt_cap_two = findmarketcap(two_year, company)
            data[4] = mkt_cap_two
            data[5] = compute_growth(data[1], mkt_cap_two) # growth rate two years after
            #return_two = int(compute_growth(data[1], mkt_cap_two))

            mkt_cap_three = findmarketcap(three_year, company)
            data[6] = mkt_cap_three
            data[7] = compute_growth(data[1], mkt_cap_three) # growth rate three years after
            #return_three = int(compute_growth(data[1], mkt_cap_three))
            data[8] = company

            if data[0] in portfolios:
                portfolios[data[0]]["data"] += data[1:]
            else:
                portfolios[data[0]]["data"] = []
                portfolios[data[0]]["data"] += data[1:]

            print("<base year: %s> 1 year later market cap : %s( %f)/ "
                  "2 years later market cap : %s( %f)/ 3 years later market cap : %s( %f)"
                  % (data[1], data[2], data[3], data[4], data[5], data[6], data[7]))

            sorted(companies.keys())
            # date, marketCapitalization
            f.write('{:10}'.format(data[0]) + '{:10.2f}  '.format(data[1]))
            for i in range(1, 4):
                i = 2*i
                if data[i] is not None:
                    f.write('{:7.2f}'.format(float(data[i])) + '(' + '{:4.1f}'.format(data[i+1]) + ')')
                else:
                    f.write('   None(None)')
            f.write('\n')
            prev = data[0]
f.close()


# initialize
for portfolio in portfolios:
    portfolio["stat"]["base_year"]["count"] = 0
    portfolio["stat"]["one_year"]["count"] = 0
    portfolio["stat"]["two_year"]["count"] = 0
    portfolio["stat"]["three_year"]["count"] = 0











in_file.close()
