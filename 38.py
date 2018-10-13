from PIL import Image as i
imgx = 512
imgy = 512
z = 0
w = -100

image = i.new("RGB",(imgx, imgy))

for x in range(0,512):
	for y in range(0,512):
		image.putpixel((x,y),(w,100,z))
	z = z + 1
	w = w + 1


image.save("Demo_i.png","PNG")