#import pillow and commandline arguments
from PIL import Image
import sys
import math
#big rainbow effect

#open image form command line
im = Image.open(sys.argv[1]) 
#read image size and set to cariables
x,y = im.size
int(x)
int(y)
pix = im.load()
#go through all of the pixles, read the rgb values, and offset them
for i in range(0,x):
	for j in range(0,y):
		r,g,b = (pix[i,j])
	#set the colors to the color plus a rainbow the length of the picture
		r = r + math.sin(i/x) *125
		g = g + math.sin((i/x)+1) *125
		b = b + math.sin((i/x)+2) *125
		
		# print image
		im.putpixel((i,j),(int(r),int(b),int(g)))
im.show()
im.save('rain.png',"PNG")

#------------------------------------------------------------------

#rap god effect

#open image form command line
im = Image.open(sys.argv[2]) 
#read image size and set to cariables
x,y = im.size
int(x)
int(y)
pix = im.load()
#go through all of the pixles, read the rgb values, and offset them
for i in range(0,x):
	for j in range(0,y):
		r,g,b = (pix[i,j])
	#set the colors to look like lines that are small rainbows across the screen (eminem rap god effect)
		r = r + math.sin(i) *125+125
		g = g + math.sin((i)+1) *125+125
		b = b + math.sin((i)+2) *125+125

		##print image
		im.putpixel((i,j),(int(r),int(b),int(g)))
im.show()
im.save('rapgod.png',"PNG")

#------------------------------------------------------------------


#inverse effect

#open image form command line
im = Image.open(sys.argv[3])
#read image size and set to cariables
x,y = im.size
int(x)
int(y)
print(x,y)
pix = im.load()
#go through all of the pixles, read the rgb values, and offset them
for i in range(x):
	for j in range(y):
		r,g,b = (pix[i,j])
		#set the colors to the inverse of what they originaly were
		pix[i,j] = (255-r,255-g,255-b)
		# print image
		im.putpixel((i,j),pix[i,j])
im.show()
im.save('inverse.png',"PNG")
