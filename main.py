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
	im = Image.open('base.jpg').convert('RGBA')
	nameSize = MaxSize
	finishSize = MaxSize/2

    	#Grab name and surname
    	first_name = row[0].upper()
    	last_name = row[1].upper()
    	full_name = first_name + " " + last_name
    	congrats = "HAS SUCCESSFULLY COMPLETED THE LHD"

    	# Set font and size
        nameFont = ImageFont.truetype('fonts/Outage.ttf', nameSize)
        congratsFont = ImageFont.truetype('fonts/Lato.ttf', finishSize)

        draw = ImageDraw.Draw(im)

        # Find size of text
        wnameFont, hnameFont = draw.textsize(full_name,font=nameFont)

        # Make size smaller until width is less than size of maxFontW
        while (wnameFont > maxFontW):
            nameSize = nameSize - 10
            nameFont = ImageFont.truetype('fonts/Outage.ttf', nameSize)
            wnameFont, hnameFont = draw.textsize(full_name,font=nameFont)

        wcongratsFont, hcongratsFont = draw.textsize(congrats,font=congratsFont)

        while (wcongratsFont > maxFontW):
            finishSize = finishSize - 10
            congratsFont = ImageFont.truetype('fonts/OpenSansRegular.ttf', finishSize)
            wcongratsFont, hcongratsFont = draw.textsize(congrats,font=congratsFont)

        # Put text onto the image
        draw.text(((W-wnameFont)/2,(H-hnameFont)/2 + 100), full_name,font=nameFont, fill="white")
        draw.text(((W-wcongratsFont)/2,((H-hcongratsFont)/2)+hnameFont+125), congrats,font=congratsFont, fill="white")

        # Save out the image
        filename = 'output/' + full_name.strip() + '.png'
        filename = filename.replace (" ", "_")
        print filename
        im.save(filename,'PNG')

