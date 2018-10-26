from PIL import Image
import random
import math
xa, xb = -1.5, 1.5
ya, yb = -1.5, 1.5

imgx, imgy = 1000,1000

maxIt = 200

image = Image.new("RGB", (imgx,imgy))

for y in range(imgy):
	cy = y * (yb-ya)/(imgy-1)+ya
	for x in range(imgx):
		cx = x * (xb-xa)/(imgx-1) + xa
		z = complex(cx,cy)
		c = complex(-.1758,-.6614) #random.randint(-2,2)
		for i in range(maxIt):
			if abs(z) >= 2.0:
				break
			z = z**2 + c
		r = math.sin(i/10) *125+125
		b = math.sin((i/10)+1) *125+125
		g = math.sin((i/10)+2) *125+125


		# if 199 > i > 20:
		# 	r = i*10
		# 	g = 255-i*2
		# 	b = 255-i*2
		# elif i >199:
		# 	r = 255
		# 	g = 255
		# 	b = 255
		# else:
		# 	r = 0
		# 	b = 0
		# 	g = 0
	

		image.putpixel((x,y),(int(r),int(b),int(g)))
image.show()