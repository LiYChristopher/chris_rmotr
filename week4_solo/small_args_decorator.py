"""
Implement a @small_arguments decorator for the "sum(a, b)" function,
that raises ValueError if any of given arguments are greater than 10.

Examples:
    sum(2, 4)  # 6
    sum(11, 4)  # ValueError
"""


def small_arguments(original_function):
    def check(*args):
        for num in args:
            if num > 10:
                raise ValueError('One or more arguments > 10.')
        return original_function(*args)
    return check


@small_arguments
def sum(a, b):
    return a + b


if __name__ == '__main__':

    import unittest

    class AssignmentTestCase(unittest.TestCase):

        def test_1(self):
            self.assertEqual(sum(2, 5), 7)

        def test_2(self):
            with self.assertRaises(ValueError):
                sum(11, 9)

    unittest.main()
