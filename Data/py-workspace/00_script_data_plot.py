#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

filename = './data_sample/Subject_2_LAYING.txt'

# load data from text file
data = np.loadtxt(filename)

# create figure and plot data
plt.figure()
plt.plot(data)

# show created plot(s) 
plt.show()

