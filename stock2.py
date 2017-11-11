import pandas
import math

df = pandas.read_excel('seryung111.xlsx') # load xlsx file by pandas

date = df['Data Date - Daily Prices'] # divide excel data by column name
comp_name = df['Company Name']
shares_out = df['Shares Outstanding']
close_price = df['Price - Close - Daily']

pro_dict = {} # total databook[company name][month][date_year]

set = set(comp_name) # remove duplicates from company name
comp_list = list(set)

for i in range(0, len(comp_list)):
    pro_dict[comp_list[i]] = [[], [], [], [], [], [], [], [], [], [], [], [], []]

for i in range(0, len(date)):
    if int(date[i]) % 100 == 27: # one per month
        tup = (date[i], comp_name[i], shares_out[i], close_price[i], math.log(float(shares_out[i]) * float(close_price[i])))
        month_index = int(date[i]) % 10000 // 100
        pro_dict[comp_name[i]][month_index].append(tup)
        continue

for i in range(0, 10):
    print(pro_dict[comp_list[i]])