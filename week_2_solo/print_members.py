"""
Write a function that receives a list and prints all its
items using a list comprehension.

Example:
    print_members(["Hello", 3, True, (1, 2)])

"""

from __future__ import print_function

def print_members(a_list):
	[print(item) for item in a_list]

