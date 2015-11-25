"""
Write a function that receives a list and
returns a dictionary with the elements initialized with the value 0.

You MUST use dict comprehensions.

Example:
    init_dict(['a', 'b', 'c']) # {'a': 0, 'b': 0, 'c': 0}

"""

def init_dict(a_list):
    return { i : 0 for i in a_list }


if __name__ == '__main__':

	import unittest

	class InitDictTestCase(unittest.TestCase):

	    def test_two_keys(self):
	        self.assertEqual(
	            init_dict(['a', 'b']),
	            {'a': 0, 'b': 0}
	        )

	    def test_three_keys(self):
	        self.assertEqual(
	            init_dict(['a', 'b', 'c']),
	            {'a': 0, 'b': 0, 'c': 0} 
	        )

	    def test_integer_keys(self):
	        self.assertEqual(
	            init_dict([1, 2, 3]),
	            {1: 0, 2: 0, 3: 0} 
	        )

	    def test_empty_list(self):
	        self.assertEqual(init_dict([]), {})

	unittest.main()