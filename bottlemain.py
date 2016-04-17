#!/usr/bin/env python

from bottle import get,route, post, run, template, debug, request, static_file
from PIL import Image
from PIL import ImageFilter
from pprint import pprint
from operator import itemgetter
import os
import perimetr
import selectSquere
import igorcode


Image_Lst = []
@get('/reset')
def rst():
	image = Image_Lst[0]
	dlt()
	return image

@get('/')
def index():
	return template('index.html')

@get('/upload')
def upload_item():
	image = request.GET.get('pict', '').strip()
	return template('show_picture.tpl', image=image)

@get('/editgrey')
def edit_item():
	image = request.GET.get('pict', '').strip()
	image = grey(image)
	Image_Lst.append(image)
	pprint(Image_Lst)
	return template('show_picture.tpl', image=image)
	
@get('/editpik')
def edit_pik():
	image = request.GET.get('pict', '').strip()
	image = changeimage(image)
	Image_Lst.append(image)
	pprint(Image_Lst)
	return template('show_picture.tpl', image=image)
###############################################################
@get('/getmin')
def getmin():
	image = Image_Lst[len(Image_Lst)-1]
	image = Min(image,3)
	pprint(Image_Lst)
	return template('show_picture.tpl', image=image)

@get('/getmed')
def getmed():
	image = Image_Lst[len(Image_Lst)-1]
	image = Med(image,3)
	pprint(Image_Lst)
	return template('show_picture.tpl', image=image)

@get('/getmax')
def getmax():
	image = Image_Lst[len(Image_Lst)-1]
	image = Max(image,3)
	pprint(Image_Lst)
	return template('show_picture.tpl', image=image)

@get('/getcon')
def getcon():
	image = Image_Lst[len(Image_Lst)-1]
	image = Con(image)
	pprint(Image_Lst)
	return template('show_picture.tpl', image=image)

def dlt():
	dir = "images/"
	files = os.listdir(dir)
	for file in files:	
		if file.endswith("output.gif"):
			os.remove(os.path.join(dir,file))
################################################################
def changeimage(image):
	print image
	im1 = Image.open("images/"+image)
	im1 = im1.convert("P")
	im2 = Image.new("P", im1.size, 0)
	outputSrc = "output.gif"
	values = {}
	his = im1.histogram()
	for i in range(256):
		if his[i] != 0:
			values[i] = his[i]

	colors = sorted(values.items(), key=itemgetter(1), reverse=True)
	pprint(colors)
	bkgr = colors[0][0]
	print "back: ", bkgr
	temp = {}

	for x in range(im1.size[1]):
		for y in range(im1.size[0]):
			pix = im1.getpixel((y,x))
			temp[pix] = pix
			if pix >= bkgr-10 and pix <= bkgr+10:
				im2.putpixel((y,x),255)

	im2.save("images/output.gif")

	return outputSrc

def grey(image):
	im = Image.open("images/"+image)
	im = im.convert("L")

	width = im.size[0]
	height = im.size[1]
	pix = im.load()
	im = im.convert("P")
	outputSrc = "output.gif"
	values = {}
	his = im.histogram()
	for i in range(256):
		if his[i] != 0:
			print his[i]
			values[i] = his[i]

	average = 0
	gmin = values.keys()[0]
	gmax = values.keys()[-1:][0]
	average = (gmax + gmin) // 2

	for i in range(height):
		for j in range(width):
			pixel =  im.getpixel((j,i))
			if pixel <= average:
				im.putpixel((j,i),255)
			else:
				im.putpixel((j,i),0)

	#im = im.convert("RGB")
	#im = im.filter(ImageFilter.MaxFilter(3))
	#im = im.filter(ImageFilter.MinFilter(3))

	im.save("images/output.gif")

	return outputSrc

def Min(image, count):
	im = Image.open("images/"+image)
	im = im.convert("RGB")

	im = im.filter(ImageFilter.MinFilter(count))

	im.convert("P")
	number = len(Image_Lst)
	
	file = str(number)+"output.gif"
	im.save("images/"+file)
	Image_Lst.append(file)
	return 	file

def Med(image, count):
	im = Image.open("images/"+image)
	im = im.convert("RGB")

	im = im.filter(ImageFilter.MedianFilter(count))

	im.convert("P")
	number = len(Image_Lst)
	file = str(number)+"output.gif"
	im.save("images/"+file)
	Image_Lst.append(file)
	return 	file

def Max(image, count):
	im = Image.open("images/"+image)
	im = im.convert("RGB")

	im = im.filter(ImageFilter.MaxFilter(count))

	im.convert("P")
	number = len(Image_Lst)
	file = str(number)+"output.gif"
	im.save("images/"+file)
	Image_Lst.append(file)
	return 	file

def Con(image):
	im = Image.open("images/"+image)
	im = im.convert("RGB")

	im = im.filter(ImageFilter.CONTOUR)

	im.convert("P")
	number = len(Image_Lst)
	file = str(number)+"output.gif"
	im.save("images/"+file)
	Image_Lst.append(file)
	return 	file
##########################################################
@get('/stat')
def function():
	imageSquere = Image_Lst[0]
	imageSquere = Image.open("images/"+imageSquere)
	imageSquere = imageSquere.convert("RGB")
	imageSquere = imageSquere.filter(ImageFilter.MedianFilter(5))
	imageSquere = imageSquere.filter(ImageFilter.MinFilter(5))
	imageSquere = imageSquere.filter(ImageFilter.MedianFilter(5))
	imageSquere = imageSquere.filter(ImageFilter.MinFilter(5))
	imageSquere = imageSquere.convert("P")
	sque = selectSquere.selectSquere(imageSquere)
	imagePer = Image.open("images/"+Image_Lst[0])
	imagePer = imagePer.convert("RGB")
	imagePer = imagePer.filter(ImageFilter.MedianFilter(5))
	imagePer = imagePer.filter(ImageFilter.MinFilter(5))
	imagePer = imagePer.filter(ImageFilter.MedianFilter(5))
	imagePer = imagePer.filter(ImageFilter.MinFilter(5))
	imagePer = imagePer.filter(ImageFilter.CONTOUR)
	imagePer = imagePer.convert("P")
	peri = perimetr.searchForP(imagePer)
	igorcode.research(sque, peri)
	ima1 ="squarepie.png"
	ima2 ="squarecoloredhist.png"
	ima3 ="perimetercoloredhist.png"
	#ima1 = ima1.convert("P")
	#ima2 = ima2.convert("P")
	#ima3 = ima3.convert("P")
	return template ('three_images.tpl',image1=ima1, image2=ima2,image3=ima3)
##########################################################
# Static Routes
@get('/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
	return static_file(filename, root='images')

@get('/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='js')

@get('/<filename:re:.*\.(css|ttf)>')
def stylesheets(filename):
    return static_file(filename, root='css')

@route('/download/<filename:path>')
def download(filename):
    return static_file(filename, root='files', download=filename)

"""@get('/<filename:re:.*\.ttf>')
def fonts(filename):
    return static_file(filename, root='fonts')"""

debug(True)
run(host='localhost', port=8080, reloader=True)