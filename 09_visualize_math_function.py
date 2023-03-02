#!/usr/bin/env python3

# Python 3.9.5

# 09_visualize_math_function.py

# Dependencies
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def get_data():
    x = np.linspace(0, 10, 1000)
    data = np.array([(np.e)**(-np.cos(i)) for i in x])
    series = pd.Series(data, index=x)

def plot(series):
    fig, ax = plt.subplots()
    ax.plot(series, label='y = e ** cos(x)')
    plt.legend(['y = e ** cos(x)'], loc='best')
    plt.show()

if __name__ == '__main__':
    series = get_data()
    plot(series)
