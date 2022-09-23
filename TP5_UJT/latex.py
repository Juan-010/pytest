#output latex table from csv
import csv
import sys
import os

#open the file
with open('TP5_UJT/data.csv', 'r') as csvfile:
    #read the file
    plots = csv.reader(csvfile, delimiter=',')
    #create csv matrix
    columns = []
    #fill the matrix
    for row in plots:
        columns.append(row)
    
    tab = 4*" "
    #output latex table
    print(tab +r"\begin{table}[H]")
    print(2*tab + r"\centering")
    print(2*tab + r"\begin{tabular}{cc}")
    print(3*tab + r"\toprule")
    print(3*tab + columns[0][0] + " & " + columns[0][1] + " & " + columns[0][2] + r" \\")
    print(3*tab + r"\midrule")
    for i in range(len(columns)-1):
        print(3*tab + columns[i+1][0] + " & " + columns[i+1][1] + " & " + columns[i+1][2] + r" \\") 
    print(3*tab + r"\bottomrule")
    print(2*tab + r"\end{tabular}")
    print(2*tab + r"\caption{Table}")
    print(2*tab + r"\label{tab:my_label}")
    print(tab + r"\end{table}")
    