import csv
from PIL import Image, ImageDraw,ImageFont



# Main image from base.jpg
im = Image.open('base.jpg').convert('RGBA')
W, H = im.size

MaxSize = 200
maxFontW = W * .90

# Open the Local Hack Day CSV
with open('data.csv', 'rb') as attendance:
	#Set the reader
    reader = csv.reader(attendance)
    #Iterate through
    for row in reader:

    	#Grab name and surname
    	first_name = row[0].upper()
    	last_name = row[1].upper()
    	full_name = first_name + " " + last_name

    	# Set font and size
        NameFont = ImageFont.truetype('fonts/Outage.ttf', venueSize)
        address = ImageFont.truetype('fonts/Lato.ttf', addressSize)
        
