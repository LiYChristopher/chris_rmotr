''' Implementation of Insertion Sort, for rmotr class 2. Test cases included. '''

def insertion_sort(seq):
	''' When we come across a list element that's greater than CUR, and
	on the left-side of CUR, we will continually move this element down the
	list until we reach the correct index.
	'''
	if not isinstance(seq, list):
		raise ValueError('This is not a list.')

	for i in range(len(seq)):
		x = seq[i]
		j = i
		while j > 0 and seq[j - 1] > x:
			seq[j] = seq[j - 1]
			j -= 1
		seq[j] = x
	return seq

if __name__ == '__main__':

	import unittest

	class InsertionSortTest(unittest.TestCase):

		def test_insertion_five(self):
			self.assertEqual(insertion_sort([3, 4, 5, 1, 2]), [1, 2, 3, 4, 5])

		def test_insertion_ten(self):
			self.assertEqual(insertion_sort([19, 16, 17, 30, 27, 7, 80, 29, 99, 104]),
											[7, 16, 17, 19, 27, 29, 30, 80, 99, 104])

		def test_insertion_fifteen(self):
			self.assertEqual(insertion_sort([63, 21, 52, 77, 61, 24, 1, 1, 53, 23, 2, 60, 4120, 1222, 30]),
											[1, 1, 2, 21, 23, 24, 30, 52, 53, 60, 61, 63, 77, 1222, 4120])

		def test_valueerror_raise(self):
			with self.assertRaises(ValueError):
				insertion_sort(set([3, 2, 2, 3, 1]))

	unittest.main()
