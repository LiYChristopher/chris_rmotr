"""
Implement a @pretty_result decorator for the "sum(a, b)" function,
that returns the result with this layout:

"The result of the sum is: XXX"

Examples:
    sum(11, 4)  # "The result of the sum is: 15"
"""


def pretty_result(original_function):
    def prettify(*args, **kwargs):
        res = original_function(*args, **kwargs)
        return "The result of the sum is: {0}".format(res)
    return prettify


@pretty_result
def sum(a, b):
    return a + b

if __name__ == '__main__':

    import unittest

    class AssignmentTestCase(unittest.TestCase):

        def test_1(self):
            self.assertEqual(sum(2, 5), 'The result of the sum is: 7')

    unittest.main()
