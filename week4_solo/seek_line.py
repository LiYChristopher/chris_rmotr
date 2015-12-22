"""
Write a function, that receives a file path and a string as parameters, and
returns the line number where that string is in the file. If the string
is not in the file, it should return None.

Example:
  which_line('file1.txt', 'hello world')  # 10
  which_line('file1.txt', 'this is not in the file')  # None

"""


def which_line(filepath, a_string):
    with open(filepath, 'r') as f:
        all_lines = [l.strip('\n') for l in f.readlines()]
        if a_string in all_lines:
            return all_lines.index(a_string) + 1
        return None

if __name__ == '__main__':

    import unittest

    class AssignmentTestCase(unittest.TestCase):

        def setUp(self):
            with open('file1.txt', 'w') as f:
                f.write('this is line 1\n')
                f.write('this is line 2\n')
                f.write('this is line 3\n')

        def test_1(self):
            self.assertEqual(which_line('file1.txt', 'this is line 2'), 2)

        def test_2(self):
            self.assertEqual(which_line('file1.txt', 'foobar'), None)

    unittest.main()

