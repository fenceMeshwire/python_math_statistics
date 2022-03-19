#!/usr/bin/env python3

# Python 3.9.5

# 05_frequency_table.py

# Purpose: Mapping the frequency of various outcomes in a sample.

# Dependencies
from collections import Counter

def frequency_table(numbers):
    table = Counter(numbers)
    print('Number\tFrequency')
    for number in table.most_common():
        print('{0}\t{1}'.format(number[0], number[1]))

if __name__ == '__main__':
    import random
    numbers = [random.randint(1, 10) for _ in range(20)]
    frequency_table(numbers)
