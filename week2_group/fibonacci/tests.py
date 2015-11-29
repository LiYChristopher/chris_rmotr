''' Run tests in command-line with

python -m unittest tests '''

import unittest
from fib import recursive_fib, iterative_fib, InputError

class FibonacciTestCase(unittest.TestCase):

    def test_recursive_data_val(self):
        with self.assertRaises(InputError):
            recursive_fib(-1)

    def test_recursive_zero(self):
        self.assertEqual(recursive_fib(0), 0)

    def test_recursive_one(self):
        self.assertEqual(recursive_fib(1), 0)

    def test_recursive_twelve(self):
        self.assertEqual(recursive_fib(12), 89)

    def test_recursive_twenty(self):
        self.assertEqual(recursive_fib(20), 4181)
    
    def test_recursive_thirty(self):
        self.assertEqual(recursive_fib(30), 514229)

    def test_iterative_zero(self):
        self.assertEqual(iterative_fib(0), recursive_fib(0))

    def test_iterative_one(self):
        self.assertEqual(iterative_fib(1), recursive_fib(0))

    def test_iterative_twelve(self):
        self.assertEqual(iterative_fib(12), recursive_fib(12))

    def test_iterative_twenty(self):
        self.assertEqual(iterative_fib(20), recursive_fib(20))

    def test_iterative_thirty(self):
        self.assertEqual(iterative_fib(30), recursive_fib(30)) 