"""
Write a function, that receives one or many file paths
as parameters and returns the name of the file
with max amount of lines.

Example:
  max_lines('file1.txt', 'file2.txt')  # 'file1.txt
  max_lines('file1.txt')  # 'file1.txt
  max_lines('file1.txt', 'file2.txt', 'file3.txt)  # 'file3.txt

"""


def max_lines(*file_names):
    files = {}
    for f in file_names:
        with open(f, 'r') as current_file:
            files[len(current_file.readlines())] = f
    return files[max(files.keys())]


if __name__ == '__main__':

    import unittest

    class AssignmentTestCase(unittest.TestCase):

        def setUp(self):
            with open('file1.txt', 'w') as f:
                f.write('this is line 1\n')
                f.write('this is line 2\n')
                f.write('this is line 3\n')
            with open('file2.txt', 'w') as f:
                f.write('this is line 1\n')
                f.write('this is line 2\n')
                f.write('this is line 3\n')
                f.write('this is line 4\n')

        def test_1(self):
            self.assertEqual(max_lines('file1.txt', 'file2.txt'),
                             'file2.txt')

        def test_2(self):
            self.assertEqual(max_lines('file1.txt'), 'file1.txt')

    unittest.main()
