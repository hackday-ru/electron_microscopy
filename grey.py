#!/usr/bin/env python

import random
from PIL import Image, ImageFilter, ImageDraw
from pprint import pprint
from operator import itemgetter
import matplotlib.pyplot as plt

image = Image.open("images/test.jpg")
draw = ImageDraw.Draw(image)
width = image.size[0]
height = image.size[1]
pix = image.load()

for i in range(width):
	for j in range(height):
		a = pix[i, j][0]
		b = pix[i, j][1]
		c = pix[i, j][2]
		S = (a + b + c) // 3
		draw.point((i, j), (S, S, S))

del draw
image.save("ans.jpg")

image = Image.open("ans.jpg")
image.convert("P")

values = {}
his = image.histogram()
for i in range(256):
	values[i] = his[i]
#pprint(his)
#plt.hist(his,10)
#plt.show()
min = 10
max = 10
for i in range(256):
	if values[i] < min and values[i] != 0:
		min = values[i]
		minclr = i
	elif values[i] > max:
		max = values[i]
		maxclr = i

middle = (max - min)/2
sum = 0 
print middle
j=0
for i in range(256):
	if values[i] < middle and values[i] != 0:
		sum += values[i]
		j+=1
sum = sum / j

print "Min&Max&Sum: ",min," ",max," ",sum
#colors = sorted(values.items(), key=itemgetter(1), reverse=True)
#pprint(colors)
image.convert("P")
image2 = Image.new("P", image.size, 0)
for x in range(image.size[1]):
    for y in range(image.size[0]):
        pixel = image.getpixel((y,x))
        #print pixel
        if values[pixel] < sum:
            image2.putpixel((y,x),255)

image.show()
