# Including libraries
# Numpy to store arrays of values of functions + random numbers generator
import numpy as np
from numpy import random
# MatPlotLib to do basic generating and exporting graphs
import matplotlib.pyplot as plt
# SeaBorn to decorate graphs, generated by MatPlotLib
import seaborn as sns

import os
import sys

# decorating graphs
sns.set(context='notebook', style='whitegrid', palette='deep', font='sans-serif', font_scale=1, rc=None)

# generating the seed based on the number 2926
dk2926 = 2926
test_seed = np.random.seed(dk2926)

# generating 100 2-dimentional datapoints that have a normal distribution 
gaussian100 = np.random.randn(100, 2)

# generating 50 2-dimentional datapoints that have a normal distribution, multiplied by a sigma = 0.86 and shifted by a mean of 3 and 4 for each variable correspondingly
gaussian50 = np.random.randn(50,2) * 0.86 + (3, 4)

# transposig the arrays from a vertical to horizontal one, so it is plottable
gaussian100T = np.transpose(gaussian100)
gaussian50T = np.transpose(gaussian50)

# plotting the arrays together, using the same green color and no legend 
fig = plt.figure(figsize=(12, 10))
plt.scatter (gaussian100T[0], gaussian100T[1], color="green")
plt.scatter (gaussian50T[0], gaussian50T[1], color="green")
# saving the resulting image as a jpg file
fig.savefig("Gaussian100_and_50_same_color_no_legend.jpg")

# plotting the arrays together, using green and blue colors and a legend
fig1 = plt.figure(figsize=(12, 10))
pic100 = plt.scatter (gaussian100T[0], gaussian100T[1], color="green")
pic50 = plt.scatter (gaussian50T[0], gaussian50T[1], color="blue")
# adding the legend above the graph and x/y labels
plt.legend((pic100, pic50), ('size = 100, mean = (0, 0), standard deviation = 1', 'size = 50, mean = (3, 4), standard deviation = 0.86'), fontsize=20, loc = 'lower right',  bbox_to_anchor=(1, 1))
plt.xlabel(r'$variable 1$', fontsize = 16)
plt.ylabel(r'$variable 2$', fontsize = 16)

# saving the resulting image as a jpg file
fig1.savefig("Gaussian100_and_50_different_color_+_legend.jpg")

print "done"
