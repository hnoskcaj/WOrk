from PIL import Image as i
import math

imgx = 500
imgy = 500
a = 10
x = 1
y = 1

image = i.new("RGB",(imgx, imgy))


x**2+y**2 = (a**2)[math.atan2(y/x)]**2
image.putpixel(x,y)

image.save("Demo_i.png","PNG")