

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

			
		image.putpixel((x,y),(int(r),int(g),int(b)))
image.show()



from PIL import Image

xa, xb = -0.55160625, -0.5429601
ya, yb = -0.62665495, -0.6180088

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
		if i < 50:
			r = 250-i*2
			b = 250
			g = 250
		elif i < 100:
			r = 150
			b = 250-i*3
			g = 200
		else:
			r = 150
			b = 0
			g = 250-i*2

			
		image.putpixel((x,y),(int(r),int(g),int(b)))
image.show()