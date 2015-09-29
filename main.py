import csv
from PIL import Image, ImageDraw,ImageFont



# Main image from base.jpg
im = Image.open('base.jpg').convert('RGBA')
W, H = im.size

MaxSize = 200
maxFontW = W * .90

# Open the Local Hack Day CSV
with open('data.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:

    	#Grab name and surname
    	first_name = row[0].upper()
    	last_name = row[1].upper()
    	full_name = first_name + " " + last_name
    	
        
