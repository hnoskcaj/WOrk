
#10/26/18
#Jackson Haile

#Thise code prints out two mandelbrot sets, and then one julia set. the mandel brot sets are
#colored based off of the number of iterations, the sedonc off of the divisability of the iterations
#and the julia set if colored based off of a sin wave of the iteration number so that if
#fluctuates back and forth gradually


#on my honor i have niether given nor recieved unauthorized aid
# -jackson haile



from PIL import Image
#first mandlebrot set
#seting zoom
xa, xb = -0.213591222, -0.213408518
ya, yb = -0.6862395607, -0.6861375

imgx, imgy = 1000,1000
#number of iterations
maxIt = 200

image = Image.new("RGB", (imgx,imgy))
#looking through all Y points on the board
for y in range(imgy):
	cy = y * (yb-ya)/(imgy-1)+ya
	#looking through all X points on the board
	for x in range(imgx):
		cx = x * (xb-xa)/(imgx-1) + xa
		c = complex(cx,cy)
		z = 0
		for i in range(maxIt):
			if abs(z) >= 2.0:
				break
			z = z**2 + c
		#print color based on itteration
		if i < 150:
			b = i*1.2
			r = i
			g = i*1.2
		elif i < 170:
			b = i*1.2
			r = i*1.2
			g = i
		elif i > 169:
			b = i
			r = i*1.2
			g = i*1.2

		#show image	
		image.putpixel((x,y),(int(r),int(g),int(b)))
image.show()
#set zoom
xa, xb = -0.55160625, -0.5429601
ya, yb = -0.62665495, -0.6180088
#board size
imgx, imgy = 1000,1000
#max iterations
maxIt = 200

image = Image.new("RGB", (imgx,imgy))
#loop through y coordinates
for y in range(imgy):
	cy = y * (yb-ya)/(imgy-1)+ya
	#loop through x coordinates
	for x in range(imgx):
		cx = x * (xb-xa)/(imgx-1) + xa
		c = complex(cx,cy)
		z = 0
		#repeats through iterations to max or break
		for i in range(maxIt):
			if abs(z) >= 2.0:
				break
			z = z**2 + c
			#set color based off of divisability so that is repeats
		if i < 70:
			if i % 7 == 0:
				r = 150
				b = 200
				g = 200
			elif i % 5 == 0:
				r = 150
				b = 150
				g = 200
			elif i % 3 == 0:
				r = 200
				b = 150
				g = 200
			elif i % 2 == 0:
				r = 200
				b = 150
				g = 150
			else:
				r = 200
				b = 200
				g = 150
		else:
			r = 0
			g = 0
			b = 0
		#show image
		image.putpixel((x,y),(int(r),int(g),int(b)))
image.show()


import random
import math
#set zoom for image
xa, xb = -1.5, 1.5
ya, yb = -1.5, 1.5
#set image size
imgx, imgy = 1000,1000
#set maximum iterations
maxIt = 200

image = Image.new("RGB", (imgx,imgy))
#loop through y points
for y in range(imgy):
	cy = y * (yb-ya)/(imgy-1)+ya
	#loop through x points
	for x in range(imgx):
		cx = x * (xb-xa)/(imgx-1) + xa
		#set z to the point coordinates
		z = complex(cx,cy)
		#set c to number
		c = complex(-.1758,-.6614) #random integer(-2,2)
		#loop through iterations
		for i in range(maxIt):
			if abs(z) >= 2.0:
				break
			z = z**2 + c
			#set in flucting sin wave offset to 125 as the zero
		r = math.sin(i/10) *125+125
		b = math.sin((i/10)+1) *125+125
		g = math.sin((i/10)+2) *125+125
#show image
		image.putpixel((x,y),(int(r),int(b),int(g)))
image.show()