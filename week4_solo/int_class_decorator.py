"""
Implement an @only_int_arguments decorator for the "sum_integers(*args)" function. It must
validate that all arguments passed to the function are integers, or raise
ValueError otherwise.

NOTE: Use a class decorator, not a function.

Examples:
    sum_integers(2, 4, 6, 8)  # 20
    sum_integers("a", "b", "c")  # ValueError
"""


class only_int_arguments(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args):
        all_int = all(map(lambda x: True if isinstance(x, int) else False, args))
        if not all_int:
            raise ValueError('All arguments must be {}'.format(int))
        return self.original_function(args)


@only_int_arguments
def sum_integers(*args):
    return sum(list(*args))

if __name__ == '__main__':

    import unittest

    class AssignmentTestCase(unittest.TestCase):

        def test_1(self):
            self.assertEqual(sum_integers(2, 5, 3), 10)

        def test_2(self):
            with self.assertRaises(ValueError):
                sum_integers("Hello", "world")

    unittest.main()
