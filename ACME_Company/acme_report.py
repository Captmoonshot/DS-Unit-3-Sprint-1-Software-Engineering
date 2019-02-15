import random
from random import choices
import acme
from acme import *

adj = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Impressive', 'Portable', 'Improved']

noun = ['Anvil', 'Catapult' 'Disguise' 'Mousetrap', '???']

def generate_products():
	
	adj_random = choices(adj, k=30)
	noun_random = choices(noun, k=30)

	random_products = [list(pair) for pair in zip(adj_random, noun_random)]

	print(random_products)

	return random_products


def inventory_report():
	for i, j in generate_products():
		print(f'{i}:{j}')




