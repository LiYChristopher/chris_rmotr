import unittest

def bubble_sort(seq):
	''' Accepts a sequence (list) as an argument,
	sorts sequence using Bubble Sort. '''

	if not isinstance(seq, list):
		raise ValueError('This is not a list.')

	sort = lambda x, y: (x, y) if x < y else (y, x)
	check = lambda x: all(x[i] < x[i + 1] or
						x[i] == x[i + 1] for i in range(len(x) - 1))

	while not check(seq):
		for i in range(len(seq) - 1):
			res = sort(seq[i], seq[i + 1])
			seq[i], seq[i + 1] = res
	return seq


if __name__ == '__main__':

	class BubbleSortTest(unittest.TestCase):

		def test_array_size_five(self):
			self.assertEqual(bubble_sort([5, 2, 1, 4, 8]), [1, 2, 4, 5, 8])

		def test_array_size_six(self):
			self.assertEqual(bubble_sort([100, 101, 30, 24, 11, 300]), [11, 24, 30, 100, 101, 300])

		def test_array_size_eleven(self):
			self.assertEqual(bubble_sort([10, 2, 3, 5, 10, 22, 12, 31, 4, 6, 3]), [2, 3, 3, 4, 5, 6, 10, 10, 12, 22, 31])

		def test_valueerror_raise(self):
			with self.assertRaises(ValueError):
				bubble_sort(set([1, 2, 3]))

	unittest.main()