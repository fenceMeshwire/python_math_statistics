#!/usr/bin/env python3

# Python 3.9.5

# 06_variance_std_deviation.py

# Purpose: Variance and Standard Deviation of a list of numbers
# The variance measures variability from the average or mean.

def calculate_mean(numbers):
    s = sum(numbers)
    N = len(numbers)
    mean = s/N
    return mean

def find_differences(numbers):
    mean = calculate_mean(numbers)
    diff = []
    for num in numbers:
        diff.append(num - mean)
    return diff

def calculate_variance(numbers):
    diff = find_differences(numbers)
    squared_diff = []
    for d in diff:
        squared_diff.append(d ** 2)
    sum_squared_diff = sum(squared_diff)
    variance = sum_squared_diff / len(numbers)
    return variance

if __name__ == '__main__':
    import random
    numbers = [random.randint(1, 50) for _ in range(20)]
    variance = calculate_variance(numbers)
    print('Variance of the list of numbers: {0}'.format(variance))
    std = variance ** 0.5
    print('Standard Deviation of the list of numbers is {0}'.format(std))
