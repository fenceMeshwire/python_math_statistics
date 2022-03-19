#!/usr/bin/env python3

# Python 3.9.5

# 02_median.py

# Purpose: Calculate the median of a given list of numbers (integer, float).
# The median is the middle value when a data set is ordered from least to greatest.

def calculate_median(numbers):
    N = len(numbers)
    numbers.sort()

    if N % 2 == 0:
        m1 = N/2
        m2 = (N/2) + 1
        m1 = int(m1) - 1
        m2 = int(m2) - 1
        median = (numbers[m1] + numbers[m2])/2
    else:
        m = (N + 1) / 2
        m = int(m) - 1
        median = numbers[m]
    
    return median

if __name__ == '__main__':
    numbers = [10, 6, 7, 90, 10, 20, 50, 5, 53, 60, 10, 10]
    median = calculate_median(numbers)
    print('Median number is: {0}'.format(median))
