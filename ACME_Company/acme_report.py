import random
from random import choices
import acme
from acme import *

adj = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Impressive', 'Portable', 'Improved']

noun = ['Anvil', 'Catapult' 'Disguise' 'Mousetrap', '???']



def generate_products():
	
	adj_random = choices(adj, k=30)
	noun_random = choices(noun, k=30)

	random_products = [pair for pair in zip(adj_random, noun_random)]

	print("\nRandom List of Products:\n", random_products)

	return random_products

	print(len(random_products))
	



def inventory_report(products_list):
	prices = []
	weight = []
	flammability = []
	"""
	Run ```inventory_report(generate_products())``` on the 
	python interactive prompt.
	"""
	print("\nList of Products:\n")
	for i, j in products_list:
		print(f'{i} : {j}')

	print()
	print("ACME CORPORATION OFFICIAL INVENTORY REPORT")
	products_list_set = set(products_list)
	print("Unique product names: ", len(products_list_set))
	print()
	for i in range(30):
		prices.append(random.randint(5, 100))
	for i in range(30):
		weight.append(random.randint(5, 100))
	for i in range(30):
		flammability.append(random.uniform(0.0, 2.5))

	average_price = sum(prices) / len(prices)
	average_weight = sum(weight) / len(weight)
	average_flammability = sum(flammability) / len(flammability)

	print("Average Price: ${:.2f} ".format(average_price))
	print("Averae weight: ", average_weight)
	print("Average flammability: ", average_flammability)
	print()





if __name__ == '__main__':
	inventory_report(generate_products())




