from PIL import Image
import sys
import math


im = Image.open(sys.argv[1]) 
x,y = im.size
int(x)
int(y)
pix = im.load()
for i in range(0,x):
	for j in range(0,y):
		r,g,b = (pix[i,j])
	
		r = r + math.sin(i/x) *125
		g = g + math.sin((i/x)+1) *125
		b = b + math.sin((i/x)+2) *125
		
		# print(10*(math.asin(i/x)))
		im.putpixel((i,j),(int(r),int(b),int(g)))
im.show()

#------------------------------------------------------------------

im = Image.open(sys.argv[1]) 
x,y = im.size
int(x)
int(y)
pix = im.load()
for i in range(0,x):
	for j in range(0,y):
		r,g,b = (pix[i,j])
	
		r = r + math.sin(i/10) *125+125
		g = g + math.sin((i/10)+1) *125+125
		b = b + math.sin((i/10)+2) *125+125

		# print(10*(math.asin(i/x)))
		im.putpixel((i,j),(int(r),int(b),int(g)))
im.show()

#------------------------------------------------------------------



from PIL import Image
import sys


im = Image.open(sys.argv[1])
x,y = im.size
int(x)
int(y)
print(x,y)
pix = im.load()
for i in range(x):
	for j in range(y):
		r,g,b = (pix[i,j])
		# print("loops")
		# print(i,j)
		pix[i,j] = (255-r,255-g,255-b)
		# r = 250
		# g = 250
		# b = 250
		im.putpixel((i,j),pix[i,j])
im.show()

