#import for csv reading
import csv
#import for file reading
import os
import sys
#import for plotting
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline
#open the file
with open(sys.argv[4], 'r') as csvfile:
    #read the file
    plots = csv.reader(csvfile, delimiter=',')
    #drop first row
    next(plots)
    #create empty lists
    x = []
    y = []
    #ask for x_col if arg 1 is not set
    if len(sys.argv) < 2:
        x_col = int(input("Enter x column: ")) - 1
        
    else:
        x_col = int(sys.argv[1]) - 1
    #ask for y_col if arg 2 is not set
    if len(sys.argv) < 3:
        y_col = int(input("Enter y column: ")) - 1
    else:
        y_col = int(sys.argv[2]) - 1
    #fill the lists
    for row in plots:
        x.append(float(row[x_col]))
        y.append(float(row[y_col]))
    #drop first row
    #smooth the values using splines
    xnew = np.linspace(x[0], x[-1], 1000)
    spl = make_interp_spline(x, y, k=3)
    ynew = spl(xnew)
    #ask for desired color if arg 3 is not set
    if len(sys.argv) < 4:
        print("Which color do you want to use?")
        color = input("Color: ")
    else:
        color = sys.argv[3]
    #plot smooth values red
    plt.plot(xnew, ynew, color)
    #plot raw values as discrete points
    plt.plot(x, y, 'bo', color=color)

    #add gray grid to the plot
    plt.grid(color='gray', linestyle='dashed', linewidth=0.5)
    #add x axis label VB
    plt.xlabel(r'V$_B$ [V]')
    #add y axis label Latex I_B and make it horizontal
    plt.ylabel(r'I$_B$ [mA]', rotation=0, labelpad=20)       
    #show the plot
    plt.show()