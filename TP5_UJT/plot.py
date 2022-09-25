#import for csv reading
import csv
#import for file reading
import os
import sys
#import for plotting
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline
#if arg 4 is not set, ask for file
if len(sys.argv) < 4:
    #ask for file
    file = input("File name: ")
else:
    file = sys.argv[4]

#open the file
with open(file, 'r') as csvfile:
    #read the file
    plots = csv.reader(csvfile, delimiter=',')
    #drop first and second row
    next(plots)
    #next(plots)
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
        colour = input("Color: ")
    else:
        colour = sys.argv[3]
    #plot smooth values red
    plt.plot(xnew, ynew, colour)

    dotted = True
    if dotted:
        #remove rows 1 and 2 from the list
        for i in range(3):
            x.pop(1)
            y.pop(1)
        #plot raw values as discrete points

        plt.plot(x, y, 'o', color=colour)

    #add gray grid to the plot
    plt.grid(color='gray', linestyle='dashed', linewidth=0.5)
    #add x axis label VB
    plt.xlabel(r'I$_E$ [mA]',labelpad=0, loc='right')
    #add y axis label Latex I_B and make it horizontal
    plt.ylabel(r'V$_{Eb1}$ [V]', rotation=0, labelpad=-16, loc='top')    
    #set x axis left limit
    plt.xlim(0, xmax=x[-1])
    #set y axis left limit
    plt.ylim(ymin=0)
    
    #show the plot
    #plt.show()
    #use same scale for x and y axis with adjustable box
    #plt.gca().set_aspect('equal', adjustable='box')

    #Ask for output file name if arg 5 is not set
    if len(sys.argv) < 5:
        output_file = input("Output file name: ")
    else:
        output_file = sys.argv[5]
    #save the plot with high resolution
    plt.savefig(output_file, dpi=300)