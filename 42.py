from PIL import Image as i
import random as r
imgx = 512
imgy = 512
z = 0
y = 0

image = i.new("RGB",(imgx, imgy))
while z < 80:
	x = r.randrange(0,512)
	a = r.randrange(0,200)
	b = r.randrange(0,200)
	c = r.randrange(0,200)
	y = 0
	while y < 512:
		count = r.randrange(0,2)
		if count == 0:
			x = x + r.randrange(-1,2)
		else:
			y = y + 1
		if 512 > x > 1 and 512>y>1:
			image.putpixel((x,y),(a,b,c))
	z = z + 1



image.save("Demo_i.png","PNG")