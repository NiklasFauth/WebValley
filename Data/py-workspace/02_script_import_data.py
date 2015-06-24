#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

fs = 50.0;
dT = 1.0/fs;

filenames = ['./data_sample/Subject_2_LAYING.txt', './data_sample/Subject_2_SITTING.txt', './data_sample/Subject_2_STANDING.txt', './data_sample/Subject_2_WALKING.txt', './data_sample/Subject_2_WALKDWN.txt', './data_sample/Subject_2_WALKUPS.txt']

labels = ['Laying', 'Sitting', 'Standing', 'Walking', 'Walking UP', 'Walking DOWN'];

N = len(filenames)

data_all = []

for i in range(N):
	
	# Add data from next file
	data_all.append(np.loadtxt(filenames[i]))
	
	# create timestamps from sampling interval
	Time = np.arange(len(data_all[i])) * dT

	# create figure and plot data
	plt.figure()
	plt.plot(Time, data_all[i])

	# Set plot proprieties
	plt.xlabel('Time [s]')
	plt.ylabel('Acceleration [g]')
	plt.title(labels[i])
	plt.grid(True)
# end for

plt.show()

