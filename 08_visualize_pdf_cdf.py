#!/usr/bin/env python3

# Python 3.9.5

# 08_visualize_pdf_cdf.py

# Dependencies:
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Calculate mean and standard deviation:
mean = 30.42
std_dev = 2.74

# Set lower and upper boundary for visualization:
lbound = 15
ubound = 45

# Determine the PDF (probability density function) and CDF (cumulative distribution function) as Series objects:
pdf = pd.Series([norm.pdf(i, mean, std_dev) for i in range(lbound, ubound)], index=np.arange(lbound, ubound))
cdf = pd.Series([norm.cdf(i, mean, std_dev) for i in range(lbound, ubound)], index=np.arange(lbound, ubound))

# Plot both functions:
pdf.plot()
cdf.plot()

# Visualize the plot:
plt.show()
