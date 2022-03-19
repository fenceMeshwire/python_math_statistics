#!/usr/bin/env python3

# Python 3.9.5

# 04_mode.py

# Purpose: Calculating the mode of a given list.
# In statistics, the mode represents the most common value in a data set.

# Dependencies
from collections import Counter

def calculate_mode(numbers):
    c = Counter(numbers)
    mode = c.most_common(1)
    return mode[0][0]

if __name__ == '__main__':
    import random
    numbers = [random.randint(1, 10) for _ in range(20)]
    numbers
    mode = calculate_mode(numbers)
    print('The mode of the list of numbers is {0}'.format(mode))
