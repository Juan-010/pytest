#import for csv reading
import csv
#import for file reading
import os
#import for plotting
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline
#open the file
with open('TP5_UJT/data.csv', 'r') as csvfile:
    #read the file
    plots = csv.reader(csvfile, delimiter=',')
    #drop first row
    next(plots)
    #create empty lists
    x = []
    y = []
    #fill the lists
    for row in plots:
        x.append(float(row[1]))
        y.append(float(row[2]))
    #drop first row
    #smooth the values using splines
    xnew = np.linspace(x[0], x[-1], 1000)
    spl = make_interp_spline(x, y, k=3)
    ynew = spl(xnew)

    #plot smooth values red
    plt.plot(xnew, ynew, 'red')
    #add gray grid to the plot
    plt.grid(color='gray', linestyle='dashed', linewidth=0.5)
    #add x axis label VB
    plt.xlabel(r'V$_B$ [V]')
    #add y axis label Latex I_B and make it horizontal
    plt.ylabel(r'I$_B$ [mA]', rotation=0, labelpad=20)
    #add title
    plt.title("Curva característica de UJT")        
    #show the plot
    plt.show()