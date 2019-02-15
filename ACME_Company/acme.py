from collections import defaultdict
import random

class Product:
	"""
	Product class which has information about price and weight and various
	other factors
	"""
	def __init__(self, name='Amazon Products'):
		self.name = name
		self.product = defaultdict(str)
		self.price = 10
		self.weight = 20
		self.flammability = 0.5
		self.identifier = int(random.uniform(1000000, 9999999))
		

	def add_product(self, product_type):
		if isinstance(product_type, str):
			self.product[product_type] += 1
		else: 
			print("That doesn't look like product type.")
	"""
	def add_price(self, price_of_product):
		if isinstance(price_of_product, int):
			self.price[price_of_product] += 1
		else:
			print("That doesn't look like a price for our product.")
	
	
	def add_weight(self, weight_of_product):
		if isinstance(weight_of_product, int):
			self.weight[weight_of_product] += 1
		else: 
			print("That doesn't look like a correct weight.")

	def add_flammable(self, flammability_of_product):
		if isinstance(flammability_of_product, float):
			self.flammability[flammability_of_product] +1


	def add_identifier(self, product_identifier=int(random.uniform(1000000, 9999999))):
		if isinstance(product_identifier, int):
			self.identifier[product_identifier] +1
	"""

	def stealability(self):
		if (self.price / self.weight) < 0.5:
			print("kinda stealable...")
		elif (self.price / self.weight) >= 0.5 and (self.price / self.weight) < 1.0:
			print("Kinda stealable.")
		else:
			print("Very stealable")

	def explode(self):
		if (self.weight * self.flammability) < 10.0:
			print("...fizzle")
		elif (self.weight * self.flammability) >= 10 and (self.weight * self.flammability) < 50:
			print("...boom!")
		else:
			print("...BABOOM!")



class BoxingGlove(Product):
	def __init__(self, name='BoxingGlove'):
		self.name = name
		self.weight = 10
		Product.__init__(self)

	def explode(self):
		print("...it's a glove")

	def punch(self):
		if self.weight < 5:
			print("That tickles")
		elif self.weight >= 5 and self.weight < 15:
			print("Hey that hurt!")
		else:
			print("OUCH!")








