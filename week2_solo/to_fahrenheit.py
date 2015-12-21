"""
Write a function that combines list comprehensions and lambdas
to transform temperatures given in celsius to fahrenheit.

Example:
    to_fahrenheit([0, 10, 25, 30, 100]) # [32.0, 50.0, 77.0, 86.0, 212.0]

"""
from __future__ import division

def to_fahrenheit(a_list):
	c_to_f = lambda c: c * (9/5) + 32
	return [c_to_f(temp) for temp in a_list]

if __name__ == '__main__':

	import unittest

	class ToFahrenheitTestCase(unittest.TestCase):
	    def test_to_fahrenheit(self):
	        self.assertEqual(to_fahrenheit([0, 10, 25, 30, 100]),
	                         [32.0, 50.0, 77.0, 86.0, 212.0])
	                         
	    def test_to_fahrenheit_repeated_values(self):
	        self.assertEqual(to_fahrenheit([0, 10, 10, 100]),
	                         [32.0, 50.0, 50.0, 212.0])
	                         
	    def test_to_fahrenheit_empty_list(self):
	        self.assertEqual(to_fahrenheit([]), [])

	unittest.main()