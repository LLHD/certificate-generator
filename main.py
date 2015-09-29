import csv
with open('data.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        print row[] + " " +row[2]
        print "-------------------"