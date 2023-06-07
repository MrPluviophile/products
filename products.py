products = []
while True:
	name = input('Please input product name: ')
	if name == 'q':
		break
	price = input('Please input price: ')
	products.append([name, price])
print(products)

products[0][0]