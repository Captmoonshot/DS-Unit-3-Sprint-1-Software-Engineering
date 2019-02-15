import unittest
from acme import Product
from acme_report import *


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)
    # More tests following the acme_test.py report
    def test_default_product_weight(self):
    	prod = Product('Test Product')
    	self.assertEqual(prod.weight, 20)

class AcmeReportTests(unittest.TestCase):
	"""Tests for Acme Reports"""
	def test_default_num_proucts(self):
		self.assertEqual(len(generate_products()), 30)
"""
    def test_legal_names
    ### I could not figure this one out after googling for 20 minutes ###
"""




if __name__ == '__main__':
    unittest.main()