from PIL import Image, ImageColor

im = Image.new('1', (540,960))  


with open("DS4.txt", "r") as file:
	for line in file:
		line=file.readline()
		x, y = (int(i) for i in line.strip().split(' '))
		im.putpixel((x,y), ImageColor.getcolor('white', '1')) # or whatever color you wish	

im.save('image.png') 
