#output latex table from csv
import csv
import sys
import os

#open the file
with open(sys.argv[1], 'r') as csvfile:
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
    print(3*tab, end='')
    for j in range(int(sys.argv[2])-1):
        print(columns[0][j], end=' & ')
    print(columns[0][int(sys.argv[2])-1], end=' \\\\\n')
    print(3*tab + r"\midrule")
    for i in range(len(columns)-1):
        #print inline
        print(3*tab, end='')
        for j in range(int(sys.argv[2])-1):
            print(columns[i+1][j], end=' & ')
        print(columns[i+1][int(sys.argv[2])-1], end=' \\\\\n') 
    print(3*tab + r"\bottomrule")
    print(2*tab + r"\end{tabular}")
    print(2*tab + r"\caption{Table}")
    print(2*tab + r"\label{tab:my_label}")
    print(tab + r"\end{table}")
    