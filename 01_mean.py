#!/usr/bin/env python3

# Python 3.9.5

# 01_mean.py

# Purpose: Calculate the mean of a given list of numbers (integer, float).
# The mean (average) of a data set is found by adding all numbers in the data set 
# and then dividing by the number of values in the set.

def calculate_mean(numbers):
    s = sum(numbers)
    N = len(numbers)
    mean = s/N
    return mean

if __name__ == '__main__':
    numbers = [10, 6, 7, 90, 10, 20, 50, 5, 53, 60, 10, 12]
    mean = calculate_mean(numbers)
    print('Mean number is: {0}'.format(mean))
    
