from PIL import Image

xa, xb = 2, -2
ya, yb = 2, -2

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
			z = z**5 + c - .9

		r = i
		b = 0
		g = 0
		

			
		image.putpixel((x,y),(int(r),int(g),int(b)))
image.show()