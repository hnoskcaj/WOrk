
# import sys
# import math
# import random as r
# board = []
# count = 0
# bomb = []
# gameboard = []
# a = 0
# clear = []
# zeros = 0

# width = int(sys.argv[1])+2 
# height = int(sys.argv[2])+2

# board = [[0]*width for x in range (height)]
# print(board)

# if sqrt(z[1]**2 + z[2]**2) >= 2:
# 	board[][] = count
# z[n+1] = z[n]**2 + C

from PIL import Image

xa, xb = -1.01, -0.09
ya, yb = -0.01, 0.01

imgx, imgy = 512,512

maxIt = 500

image = Image.new("RGB", (imgx,imgy))

for y in range(imgy):
	cy = y * (yb-ya)/(imgy-1)+ya
	for x in range(imgx):
		cx = x * (xb-xa)/(imgx-1) + xa
		c = complex(cx,cy)
		z = 0
		for i in range(maxIt):
			if abs(z) >= 2.0:
				break
			z = z**2 + c
		r = i
		g = 256-i
		b = (i*50)%256
		image.putpixel((x,y),(r,g,b))
image.show()