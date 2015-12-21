"""
The objective of this assignment is to write a factorial function (https://en.wikipedia.org/wiki/Factorial).

In order to do that we'll define 2 helper functions:
 * factorial_terms: will receive a number and return the
                            list of terms to compute the factorial.
 * compute_factorial: Will receive a list of terms and compute de factorial.
                                *You must use the `reduce` function*

Finally, the `factorial` function will get a number and using both helper functions will compute
the answer. The `factorial` function can have just 1 line.

Use the tests to see the complete specification of what you're required to write.

"""

def factorial_terms(a_number):
	if a_number < 0:
		raise AttributeError("Number can't be negative.")
	elif a_number == 0:
		return [1]
	else:
		return range(a_number, 0, -1)

def compute_factorial(terms):
	if len(terms) < 1:
		raise AttributeError("No input to compute.")
	else:
		f = reduce(lambda x, y: x * y, terms)
	return f

def factorial(number):
	return compute_factorial(factorial_terms(number))
   
if __name__ == '__main__':

	import unittest

	class FactorialTermsTestCase(unittest.TestCase):
	    def test_factorial_terms_of_zero(self):
	        """Should return [1]"""
	        self.assertEqual(factorial_terms(0), [1])

	    def test_factorial_terms_with_an_invalid_value(self):
	        """Should raise an exception if an invalid number is provided"""
	        with self.assertRaises(AttributeError):
	            factorial_terms(-1)

	    def test_factorial_terms_are_generated_ok(self):
	        """Should return the correct terms for a number"""
	        self.assertEqual(factorial_terms(5), [5, 4, 3, 2, 1])


	class ComputeFactorialTestCase(unittest.TestCase):
	    def test_compute_factorial_for_regular_integers(self):
	        """Should return the factorial number for the terms"""
	        self.assertEqual(compute_factorial([5, 4, 3, 2, 1]), 120)

	    def test_compute_factorial_with_no_arguments(self):
	        """Should raise an exception"""
	        with self.assertRaises(AttributeError):
	            compute_factorial([])

	    def test_compute_factorial_invoked_with_one(self):
	        """Should return 1"""
	        self.assertEqual(compute_factorial([1]), 1)


	class FactorialTestCase(unittest.TestCase):
	    def test_factorial_for_regular_integers(self):
	        """Should return the factorial number for the terms"""
	        self.assertEqual(factorial(5), 120)

	    def test_factorial_with_negative_number(self):
	        """Should raise an exception"""
	        with self.assertRaises(AttributeError):
	            factorial(-1)

	    def test_factorial_of_zero(self):
	        """Should return 1"""
	        self.assertEqual(factorial(0), 1)

	unittest.main()
