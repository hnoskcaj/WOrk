from PIL import Image as i
imgx = 512
imgy = 512

image = i.new("RGB",(imgx, imgy))

image.putpixel((0,0),(255,0,0))

image.save("Demo_i.png","PNG")