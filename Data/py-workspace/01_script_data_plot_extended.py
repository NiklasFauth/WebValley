#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

filename = './data_sample/Subject_2_LAYING.txt'

# load data from text file
data = np.loadtxt(filename)

fs = 50.0;
dT = 1.0/fs;

# create timestamps from sampling interval
Time = np.arange(len(data)) * dT

# create figure and plot data
plt.figure()
plt.plot(Time, data)

# Set plot proprieties
plt.xlabel('Time [s]')
plt.ylabel('Acceleration [g]')
plt.title('Laying')
plt.grid(True)

# show created plot(s) 
plt.show()

