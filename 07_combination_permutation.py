#!/usr/bin/env python3

# Python 3.9.5

# Purpose:  Calculate the possible combinations from a combination lock 
#           without and with repeating of the numbers.

# Dependency
from itertools import permutations, product

columns = 4
values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def get_combinations_with_repeat(values, columns):
    combinations_with_repeat = []
    for permutation in product(values, repeat=columns):
        combinations_with_repeat.append(permutation)
    return combinations_with_repeat

def get_permutations(values):
    combinations_no_repeat = []
    for permutation in permutations(values, columns):
        combinations_no_repeat.append(permutation)
    return combinations_no_repeat

if __name__ == '__main__':
    columns = 4
    values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Get combinations with repeat: cartesian product
    combinations_with_repeat = get_combinations_with_repeat(values, columns)
    len(combinations_with_repeat) # 10000
    print((1, 1, 1, 1) in combinations_with_repeat) # True

    # Get permutations: all possible orderings, no repeated elements
    combinations_no_repeat = get_permutations(values)
    len(combinations_no_repeat) # 5040
    print((1, 2, 3, 4) in combinations_no_repeat) # True
