#!/usr/bin/env python3

# Python 3.9.5

# 04_range.py

# Purpose: Calculate the range of a list.
# The range of a set of data is the difference between the largest and smallest values

def find_range(numbers):
    lowest = min(numbers)
    highest = max(numbers)
    r = highest - lowest
    return lowest, highest, r

if __name__ == '__main__':
    import random
    numbers = [random.randint(1, 100) for _ in range(20)]
    lowest, highest, r = find_range(numbers)
    print('Lowest: {0}, Highest: {1}, Range: {2}'.format(lowest, highest, r))
