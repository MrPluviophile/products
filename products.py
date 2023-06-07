products = []
while True:
	name = input('Please input product name: ')
	if name == 'q':
		break
	price = input('Please input price: ')
	products.append([name, price])
print(products)

for p in products:
	print(p[0], 's price is', p[1])