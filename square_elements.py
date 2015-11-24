"""
Write a function that receives a list of integers and
returns a list with all the elements squared using
list comprehensions.

Example:
    square_elements([1, 2, 3, 4, 5]) # [1, 4, 9, 16, 25]

"""

def square_elements(a_list):
	return [item**2 for item in a_list]
    
if __name__ == '__main__':

	import unittest

	class SquareElementsTestCase(unittest.TestCase):
	    def test_square_elements(self):
	        self.assertEqual(square_elements([1, 2, 3, 4, 5]),
	                         [1, 4, 9, 16, 25])
	                         
	    def test_square_elements_repeated(self):
	        self.assertEqual(square_elements([1, 1, 2, 2, 3, 3]),
	                         [1, 1, 4, 4, 9, 9])
	                         
	    def test_square_elements_empty_list(self):
	        self.assertEqual(square_elements([]), [])

	unittest.main()