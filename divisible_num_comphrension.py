"""
Write a function that receives a list of numbers
and a term 'n' and returns only the elements that are divisible
by that term 'n'. You must use List comprehensions to solve it.

Example:
    divisible_numbers([9, 8, 7, 6, 5, 4, 3, 2, 1], 3)  # [9, 6, 3]

"""


def divisible_numbers(a_list, term):
    return [item for item in a_list if item % term == 0]


if __name__ == '__main__':

	import unittest

	class DivisibleNumbersTestCase(unittest.TestCase):
	    def test_many_divisible_number(self):
	        self.assertEqual(divisible_numbers([9, 8, 7, 6, 5, 4, 3, 2, 1], 3), 
	                                           [9, 6, 3])

	    def test_empty_list(self):
	        self.assertEqual(divisible_numbers([], 2),  [])
	            
	    def test_no_result(self):
	        self.assertEqual(divisible_numbers([2, 4, 8], 5),  [])

	unittest.main()