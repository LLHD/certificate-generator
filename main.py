import csv
with open('data.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
    	first_name = row[0]
    	last_name = row[1]
        print str(first_name).upper + " " + Strlast_name.upper
