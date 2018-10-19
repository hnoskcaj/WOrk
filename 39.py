## Homework_Red_Pixels
## October 11, 2018
## Draw a red picture using PILLOW

from PIL import Image

## Initialize variables
imgX = 512
imgY = 512
locX = 0
locY = 0
redGradient = 0

## Set size of image
image = Image.new("RGB", (imgX, imgY))




def loopMe():
	for a in range(0, 512):
		global locY
		image.putpixel((locX, locY), (255, 0, 0))
		locY = a
		

	## Save name/file type
	image.save("Homework_Red_Pixels.png", "PNG")

for a in range(0, 512):
	loopMe()
	locX = a
	