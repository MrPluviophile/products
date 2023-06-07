import os

# read file
def read_file(filename):
	products = []
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			if 'Product,Price' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
	return products

# ask user to input
def user_input(products):
	while True:
		name = input('Please input product name: ')
		if name == 'q':
			break
		price = input('Please input price: ')
		price = int(price)
		products.append([name, price])
	print(products)
	return products

# print all the buying record
def print_products(products):
	for p in products:
		print(p[0], '"s price is', p[1])

# write into file
def write_file(filename, products):
	with open(filename, 'w', encoding='utf-8') as f:
		f.write('Product,Price\n')
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n')

def main():
	filename = 'products.csv'
	if os.path.isfile(filename):# check if file exist
		print('File exist')
		products = read_file(filename)
	else:
		print('File not found')

	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)

main()