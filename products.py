products = []
while True:
	name = input('Please input product name: ')
	if name == 'q':
		break
	price = input('Please input price: ')
	price = int(price)
	products.append([name, price])
print(products)

for p in products:
	print(p[0], 's price is', p[1])

with open('product.csv', 'w', encoding='utf-8') as f:
	f.write('Product,Price\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')