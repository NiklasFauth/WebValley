#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

fs = 50.0;
dT = 1.0/fs;

filenames = ['./data_sample/Subject_2_LAYING.txt', './data_sample/Subject_2_SITTING.txt', './data_sample/Subject_2_STANDING.txt', './data_sample/Subject_2_WALKING.txt', './data_sample/Subject_2_WALKDWN.txt', './data_sample/Subject_2_WALKUPS.txt']

labels = ['Laying', 'Sitting', 'Standing', 'Walking', 'Walking UP', 'Walking DOWN'];

N = len(filenames)

# init data arrays
data_all = []
data_combined = [0, 0, 0];

for i in range(N):

	data_all.append(np.loadtxt(filenames[i]))
	data_combined = np.vstack([data_combined, data_all[i]])

# end for

# remove firs row of zeros
data_combined = data_combined[1:-1,:]

# create timestamps from sampling interval
Time = np.arange(len(data_combined)) * dT

# create figure and plot data
plt.figure()
plt.plot(Time, data_combined)

# Set plot proprieties
plt.xlabel('Time [s]')
plt.ylabel('Acceleration [g]')
plt.title('All Actions')
plt.grid(True)

plt.show()

