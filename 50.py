from PIL import Image
import sys


im = Image.open(sys.argv[1])
x,y = im.size
int(x)
int(y)
print(x,y)
pix = im.load()
for i in range(x):
	for j in range(y):
		r,g,b = (pix[i,j])
		# print("loops")
		# print(i,j)
		pix[i,j] = (255-r,255-g,255-b)
		# r = 250
		# g = 250
		# b = 250
		im.putpixel((i,j),pix[i,j])
im.show()