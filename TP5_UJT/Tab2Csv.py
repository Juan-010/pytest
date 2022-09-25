#Program that converts latex table to csv
input_file = open("table.txt", "r")
output_file = open("table.csv", "w")
for line in input_file:
    line = line.strip()
    line = line.replace(" & ", ",")
    line = line.replace(" \\\\", "")
    output_file.write(line + "\n")
input_file.close()
output_file.close()