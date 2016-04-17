#!/usr/bin/env python
from PIL import Image
from operator import itemgetter

im = Image.open("images/test.jpg")
im = im.convert("P")
his = im.histogram()
print his
values = {}

for i in range(256):
  values[i] = his[i]

for j,k in sorted(values.items(), key=itemgetter(1), reverse=True)[:10]:
  print j,k
