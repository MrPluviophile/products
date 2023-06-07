import os

# read file
products = []
if os.path.isfile('products.csv'):# check if file exist
	print('File exist')
	with open('products.csv', 'r', encoding='utf-8') as f:
		for line in f:
			if 'Product,Price' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
	print(products)
else:
	print('File not found')

# ask user to input
while True:
	name = input('Please input product name: ')
	if name == 'q':
		break
	price = input('Please input price: ')
	price = int(price)
	products.append([name, price])
print(products)

# print all the buying record
for p in products:
	print(p[0], 's price is', p[1])

# write into file
with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('Product,Price\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')