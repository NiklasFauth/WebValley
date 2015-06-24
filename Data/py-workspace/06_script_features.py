#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

fs = 50.0;
dT = 1.0/fs;

filenames = ['./data_sample/Subject_2_LAYING.txt', './data_sample/Subject_2_SITTING.txt', './data_sample/Subject_2_STANDING.txt', './data_sample/Subject_2_WALKING.txt', './data_sample/Subject_2_WALKDWN.txt', './data_sample/Subject_2_WALKUPS.txt']

labels = ['Laying', 'Sitting', 'Standing', 'Walking', 'Walking UP', 'Walking DOWN'];

N = len(filenames)

WINDOW_SIZE = 50
STEP = 25

data_all = []
data_mean = []
data_var = []
data_combined = [0, 0, 0];
data_mean_combined = [0, 0, 0];
data_var_combined = [0, 0, 0];

for i in range(N):
	
	# Add data from next file
	data_all.append(np.loadtxt(filenames[i]))
	data_combined = np.vstack([data_combined, data_all[i]])

	
	[row, col] = data_all[i].shape
	
	_mean = np.zeros(( len(range(0, row, STEP)) , col ))
	_var = np.zeros(( len(range(0, row, STEP)) , col ))
	
	for i_col in range(col):
		
		idx = 0
		
		for i_row in range(0, row, STEP):
	
			# compute mean of window elements
			#data_mean[j:j+WINDOW_SIZE-1,i] = np.sum(data[j:j+WINDOW_SIZE-1,i]) / WINDOW_SIZE
			_mean[idx,i_col] = np.mean(data_all[i][i_row:i_row+WINDOW_SIZE-1,i_col])
			_var[idx,i_col] = np.var(data_all[i][i_row:i_row+WINDOW_SIZE-1,i_col])
			idx += 1
		# end for i_row
		
	# end for i_col
		
	data_mean.append(_mean)
	data_mean_combined = np.vstack([data_mean_combined, data_mean[i]])
	
	data_var.append(_var)
	data_var_combined = np.vstack([data_var_combined, data_var[i]])

# end for i

np.save('data_mean', data_mean)
np.save('data_var', data_var)

data_combined = data_combined[1:-1,:]
data_mean_combined = data_mean_combined[1:-1,:]
data_var_combined = data_var_combined[1:-1,:]

plt.figure()
plt.plot(data_combined)

plt.figure()
plt.plot(data_mean_combined)

plt.figure()
plt.plot(data_var_combined)

plt.show()

