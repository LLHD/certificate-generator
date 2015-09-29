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
        wnameFont, hnameFont = draw.textsize(nameFontName,font=nameFont)

        # Make size smaller until width is less than size of maxFontW
        while (wnameFont > maxFontW):
            nameSize = nameSize - 10
            nameFont = ImageFont.truetype('fonts/Outage.ttf', nameSize)
            wnameFont, hnameFont = draw.textsize(nameFontName,font=nameFont)

        wcongratsFont, hcongratsFont = draw.textsize(congratsFontDetails,font=congratsFont)

        while (wcongratsFont > maxFontW):
            finishSize = finishSize - 10
            congratsFont = ImageFont.truetype('fonts/OpenSansRegular.ttf', finishSize)
            wcongratsFont, hcongratsFont = draw.textsize(congratsFontDetails,font=congratsFont)

        # Put text onto the image
        draw.text(((W-wnameFont)/2,(H-hnameFont)/2 + 100), nameFontName,font=nameFont, fill="white")
        draw.text(((W-wcongratsFont)/2,((H-hcongratsFont)/2)+hnameFont+125), congratsFontDetails,font=congratsFont, fill="white")

        # Save out the image
        filename = 'output/' + nameFontName.strip() + '.png'
        filename = filename.replace (" ", "_")
        print filename
        im.save(filename,'PNG')

