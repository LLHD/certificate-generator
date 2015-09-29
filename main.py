import csv
from PIL import Image, ImageDraw,ImageFont

with open('data.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
    	first_name = row[0].upper()
    	last_name = row[1].upper()
        print first_name + " " + last_name
