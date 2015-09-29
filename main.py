import csv
from PIL import Image, ImageDraw,ImageFont


# Open the Local Hack Day CSV
with open('data.csv', 'rb') as attendance:
	#Set the reader
    reader = csv.reader(attendance)
    
    #Iterate through
    for row in reader:

		# Main image from base.jpg
		im = Image.open('base.jpg').convert('RGBA')
		W, H = im.size

		MaxSize = 200
		maxFontW = W * .90

		nameSize = MaxSize
        congrats = MaxSize/2

    	#Grab name and surname
    	first_name = row[0].upper()
    	last_name = row[1].upper()
    	full_name = first_name + " " + last_name

    	# Set font and size
        venue = ImageFont.truetype('fonts/Outage.ttf', nameSize)
        address = ImageFont.truetype('fonts/Lato.ttf', congrats)

        draw = ImageDraw.Draw(im)

        # Find size of text
        wVenue, hVenue = draw.textsize(venueName,font=venue)

        # Make size smaller until width is less than size of maxFontW
        while (wVenue > maxFontW):
            nameSize = nameSize - 10
            venue = ImageFont.truetype('fonts/Outage.ttf', nameSize)
            wVenue, hVenue = draw.textsize(venueName,font=venue)

        wAddress, hAddress = draw.textsize(addressDetails,font=address)

        while (wAddress > maxFontW):
            congrats = congrats - 10
            address = ImageFont.truetype('fonts/OpenSansRegular.ttf', congrats)
            wAddress, hAddress = draw.textsize(addressDetails,font=address)

