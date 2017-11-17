# system_trading
system trading team


stockprice = open('stockprice.txt', 'r')
lines = stockprice.readlines()        # open file

list = []                             # make nested list 
for data in lines:                    # make data lists from lines list
	data = data.strip()
	data = data.split("\t")
	list.append(data[0:1])
	list.append(data[1:2])
	list.append(data[2:3])
	list.append(data[3:4])
	list.append(data[4:5])
	list.append(data[5:6])
	list.append(data[6:7])


dict = {}							  # make dic with nested list
i = 0
while i < len(lines):
	dict['date'] = list[2][i] 
while i < len(lines):
	dict['comn'] = list[3][i]
while i < len(lines):
	dict['mktcap'] = int(list[4][i]) * int(list[5][i])

print(dict['mktcap']) 

stockprice.close()
