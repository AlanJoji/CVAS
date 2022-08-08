import csv

def header (file_name) :
    file = open(file_name, "w+", newline="")
    writer = csv.writer(file)

    headings = ["Name", "Time"]

    writer.writerow(headings)

    file.close()

def write_value (file_name, name, time) :
    file = open(file_name, "a", newline="")
    writer = csv.writer(file)
    
    value = [name, time]

    writer.writerow(value)

    file.close()

