#!/usr/bin/env python3

# Python 3.9.5

# Purpose:  Calculate the possible combinations from a four digit combination lock 
#           without and with repeating of the numbers.

# Dependencies
from itertools import product
from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement

def get_combinations_with_repeat(values, columns):
    combinations_with_repeat = []
    for permutation in product(values, repeat=columns):
        combinations_with_repeat.append(permutation)
    return combinations_with_repeat

def get_permutations(values, columns):
    combinations_no_repeat = []
    for permutation in permutations(values, columns):
        combinations_no_repeat.append(permutation)
    return combinations_no_repeat

def get_combination(values, columns):
    combos = []
    for combination in combinations(values, columns):
        combos.append(combination)
    return combos

def get_combos_with_replacement(values, columns):
    combos_with_replacement = []
    for combination in combinations_with_replacement(values, columns):
        combos_with_replacement.append(combination)
    return combos_with_replacement

if __name__ == '__main__':
    columns = 4
    values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Get combinations with repeat: cartesian product
    combinations_with_repeat = get_combinations_with_repeat(values, columns)
    len(combinations_with_repeat)
    print((1, 1, 1, 1) in combinations_with_repeat)

    # Get permutations: all possible orderings, no repeating elements
    combinations_no_repeat = get_permutations(values, columns)
    len(combinations_no_repeat)
    print((1, 2, 3, 4) in combinations_no_repeat)

    # Get combinations: in sorted order, no repeating elements
    combos = get_combination(values, columns)
    len(combos) # 210
    print((1, 2, 3, 4) in combos) # True

    # Get combinations with replacements, in sorted order, with repeated elements.
    combos_with_replacement = get_combos_with_replacement(values, columns)
    len(combos_with_replacement) # 715
    print((0, 0, 0, 0) in combos_with_replacement) # True   
