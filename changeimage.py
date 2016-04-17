#!/usr/bin/env python

from PIL import Image
from PIL import ImageFilter
from pprint import pprint
from operator import itemgetter

im = Image.open("ans.jpg")
im = im.convert("P")
im2 = Image.new("P", im.size, 0)

values = {}
his = im.histogram()
for i in range(256):
    if his[i] != 0:
        values[i] = his[i]

colors = sorted(values.items(), key=itemgetter(1), reverse=True)
pprint(colors)
bkgr = colors[0][0]
print "back: ", bkgr
temp = {}
"""
max = colors[0][1]
min = colors[len(colors)-1][1]
print max," ",min

mid = (max - min) / 2
print mid
sum = 0
j = 0
for i in range(mid):
	if colors[i][1] < mid:
		sum = sum + colors[i][1]
		j = j+1
porog = sum / j
print porog"""

for x in range(im.size[1]):
    for y in range(im.size[0]):
        pix = im.getpixel((y,x))
        temp[pix] = pix
        if pix >= bkgr-10 and pix <= bkgr+10:
            im2.putpixel((y,x),255)


im2 = im2.convert("RGB")

#im2 = im2.filter(ImageFilter.GaussianBlur(3))
#im2 = im2.filter(ImageFilter.CONTOUR)
im2 = im2.filter(ImageFilter.MedianFilter(5))
im2 = im2.filter(ImageFilter.MinFilter(3))
im2 = im2.filter(ImageFilter.MedianFilter(3))
im2 = im2.filter(ImageFilter.MinFilter(5))
#im2 = im2.filter(ImageFilter.MaxFilter(3))
im2 = im2.filter(ImageFilter.CONTOUR)

im2.save("images/output.jpg")
im2.show()