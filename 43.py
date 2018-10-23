
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

xa, xb = -0.213591222, -0.213408518
ya, yb = -0.6862395607, -0.6861375

imgx, imgy = 1000,1000

maxIt = 200

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

			# if i > 160*(maxIt/200):
			# 	b = i
			# 	r = i + 50
			# 	g = i
			
			# else:
			# 	b = 0
			# 	r = 0
			# 	g = 0
		image.putpixel((x,y),(int(r),int(g),int(b)))
image.show()