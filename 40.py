from PIL import Image as i
import math
imgx = 500
imgy = 500
county = 0
countx = 0
a = 100
b = 100
c = 100

image = i.new("RGB",(imgx, imgy))

for x in range(0,500):
	countx = countx + 1
	if countx == 50:
			countx = 0
			b = math.sqrt((b - 100)**2)
			c = math.sqrt((c - 100)**2)
	for y in range(0,500):
		county = county + 1
		if county == 50:
			county = 0
			b = math.sqrt((b - 100)**2)
			c = math.sqrt((c - 100)**2)

		image.putpixel((x,y),(int(a),int(b),int(c)))
image.save("Demo_i.png","PNG")