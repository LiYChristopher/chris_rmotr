'''
Write a program that generates the nth number in a fibonacci sequence (starting at 0).
The program should start and ask two things:

The number that will describe the nth term you want to get if the function should be recursive
or not The program should count with data validation. It means that the program must inform the
user when the number she inserted is invalid.

Extra: If the user passes a --recursive argument, the program should not ask for the function to
use and use the recursive function.
'''

import unittest
from argparse import ArgumentParser

class InputError(Exception):
    pass

def recurse():
    parser = ArgumentParser(description='check recurse option')
    parser.add_argument('--recursive', action='store_true', dest='recurse_switch',
                        help='will use recursive function by default.')
    args = parser.parse_args()

    # get True or False value for:
    # python fib.py --recursive     --> True
    # python fib.py                 --> False
    
    recurse_flag = args.recurse_switch
    return recurse_flag

def recursive_fib(n):
    ''' calculate fib recursively. slow as hell. use memoization.
    '''
    if n == 1 or n == 0:
        return 0
    if n == 2:
        return 1
    if n < 0:
        raise InputError('Negative means nothing. Enter +ve number.')
    return recursive_fib(n-1) + recursive_fib(n-2)


def iterative_fib(n):
    ''' calculate fib iteratively. decently fast. better methods?
    '''
    first = 0
    second = 1
    for i in xrange(1, n):
        first, second = second, first+second
    return first


def main():
    try:
        n = int(raw_input('Enter nth number: '))
    except Exception, e:
        raise InputError('Enter a number: ', e)
    if recurse():
        print 'Using recursive_fib({i})'.format(i=n)
        return recursive_fib(n)
    else:
        f = str(raw_input('Want to use recursion?: Y/N: '))
        if f in ['Y', 'y', 'yes', 'YES', 'Yes']:
            print 'Using recursive_fib({i})'.format(i=n)
            return recursive_fib(n)
        elif f in ['n', 'N', 'no', 'No', 'NO']:
            print 'Using iterative_fib({i})'.format(i=n)
            return iterative_fib(n)
        else:
            raise InputError('Invalid input')                      

if __name__ == '__main__':
    print main()

