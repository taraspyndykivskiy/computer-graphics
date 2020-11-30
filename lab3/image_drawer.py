from PIL import Image, ImageColor
from math import *
im = Image.new('1', (960, 960)) # create the Image of size 1 pixel 

file=open("DS4.txt", "r")

angle = 50*3.14/180

with open("DS4.txt", "r") as file:
	for line in file:
		line=file.readline()
		x, y = (int(i) for i in line.strip().split(' '))
		'''
		x_new=int((x-480)*cos(angle)-(y-480)*sin(angle))
		y_new=int((x-480)*sin(angle)+(y-480)*cos(angle))
		'''
		x_new=int((x)*cos(angle)-(y)*sin(angle))
		y_new=int((x)*sin(angle)+(y)*cos(angle))

		im.putpixel((x, y), ImageColor.getcolor('yellow', '1')) # or whatever color you wish	

im.save('cartoons.png') # or any image format
