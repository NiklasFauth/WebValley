#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

fs = 50.0;
dT = 1.0/fs;

filename = './data_sample/Subject_2_WALKING.txt'

data = np.loadtxt(filename)

[row, col] = data.shape

WINDOW_SIZE = 50
STEP = 25

data_mean = np.zeros((row, col))
#data_var = np.zeros((row, col))

for i in range(col):
	
	for j in range(0, row, STEP):
	
		# j = index of first element in current window
		# j+WINDOW_SIZE is the window of current elements
		# compute mean of window elements
		#data_mean[j:j+WINDOW_SIZE-1,i] = np.sum(data[j:j+WINDOW_SIZE-1,i]) / WINDOW_SIZE
		data_mean[j:j+WINDOW_SIZE-1,i] = np.mean(data[j:j+WINDOW_SIZE-1,i])
		#data_var[j:j+WINDOW_SIZE-1,i] = np.var(data[j:j+WINDOW_SIZE-1,i])

	# end for j
# end for i

# create figure and plot data
fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax1.plot(data[:,1])
ax2 = fig.add_subplot(2,1,2)
ax2.plot(data_mean[:,1])

plt.show()

