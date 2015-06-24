#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

fs = 50.0;
dT = 1.0/fs;

filenames = ['./data_sample/Subject_2_LAYING.txt', './data_sample/Subject_2_SITTING.txt', './data_sample/Subject_2_STANDING.txt', './data_sample/Subject_2_WALKING.txt', './data_sample/Subject_2_WALKDWN.txt', './data_sample/Subject_2_WALKUPS.txt']

labels = ['Laying', 'Sitting', 'Standing', 'Walking', 'Walking UP', 'Walking DOWN'];

N = len(filenames)

data_all = []
norm = []

for i in range(N):
	
	# Add data from next file
	data_all.append(np.loadtxt(filenames[i]))

	norm.append(np.zeros(len(data_all[i])))
		
	for t in range(len(data_all[i])):
		norm[i][t] = np.linalg.norm(data_all[i][t])		

	# create timestamps from sampling interval
	Time = np.arange(len(data_all[i])) * dT

	# create figure and plot data
	fig = plt.figure()
	ax1 = fig.add_subplot(2,1,1)
	ax1.plot(data_all[i])
	ax1.set_title(labels[i])
	ax2 = fig.add_subplot(2,1,2)
	ax2.plot(norm[i])
		
# end for

plt.show()

