from PIL import Image as i
import random as r
imgx = 512
imgy = 512
z = 0

image = i.new("RGB",(imgx, imgy))
while z < 100:
	x = r.randrange(0,512)
	a = r.randrange(0,200)
	b = r.randrange(0,200)
	c = r.randrange(0,200)
	for y in range(0,512):
		x = x + r.randrange(-1,2)
		if 512 > x > 1:
			image.putpixel((x,y),(a,b,c))
	z = z + 1



image.save("Demo_i.png","PNG")