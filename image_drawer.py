from PIL import Image, ImageColor

im = Image.new('image', (540,960)) # create the Image of size 1 pixel 

file=open("DS4.txt", "r")

for (x, y) in file:
	im.putpixel((x,y), ImageColor.getcolor('black', 'image')) # or whatever color you wish	

im.save('simplePixel.png') # or any image format