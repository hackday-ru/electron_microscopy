#!/usr/bin/env python

import copy
import sys
from PIL import Image
from PIL import ImageFilter
from pprint import pprint
from time import sleep

def checkP(im, matrix, i, j):
    a = copy.deepcopy(i)
    b = copy.deepcopy(j)
    Flag = False
    P = 1
    dx = 0
    matrix[a][b] = 2
    im.putpixel((b,a), 200)
    qwe = 0
    while not Flag:
        Flag = True
        if b>0:
            if matrix[a][b-1] == 1:
                matrix[a][b-1] = 2
                b -= 1
                im.putpixel((b,a), 200)
                P += 1
                Flag = False
                if dx != 1:
                    P-=1
                dx = 1
    #    if b>0 and a<len(matrix)-2:
    #        if matrix[a+1][b-1] == 1 and Flag:
    #            matrix[a+1][b-1] = 2
    #            a+=1
    #            b-=1
    #            im.putpixel((b,a), 200)
    #            P+=1
    #            Flag = False
        if a<len(matrix)-2:
            if matrix[a+1][b] == 1 and Flag:
                matrix[a+1][b] = 2
                a += 1
                im.putpixel((b,a), 200)
                P += 1
                Flag = False
                if dx != 2:
                    P-=1
                dx = 2
    #    if b<len(matrix[0])-2 and a<len(matrix)-2:
    #        if matrix[a+1][b+1] == 1 and Flag:
    #            matrix[a+1][b+1] = 2
    #            P += 1
    #            a+=1
    #            b+=1
    #            im.putpixel((b,a), 200)
    #            Flag = False
        if b<len(matrix[0])-2:
            if matrix[a][b+1] == 1 and Flag:
                matrix[a][b+1] = 2
                b += 1
                im.putpixel((b,a), 200)
                P += 1
                Flag = False
                if dx != 3:
                    P-=1
                dx = 3
    #    if b<len(matrix[0])-2 and a>0:
    #        if matrix[a-1][b+1] == 1 and Flag:
    #            matrix[a-1][b+1] = 2
    #            b+=1
    #            a-=1
    #            P += 1
    #            im.putpixel((b,a), 200)
    #            Flag = False
        if a>0:
            if matrix[a-1][b] == 1 and Flag:
                matrix[a-1][b] = 2
                a -= 1
                im.putpixel((b,a), 200)
                P += 1
                Flag = False
                if dx != 4:
                    P-=1
                dx = 4
    #    if a>0 and b>0:
    #        if matrix[a-1][b-1] == 1 and Flag:
    #            matrix[a-1][b-1] = 2
    #            a-=1
    #            b-=1
    #            im.putpixel((b,a), 200)
    #            P+=1
    #            Flag = False
    return P

def searchForP(imageTrans):
    im = imageTrans

    x = 0
    y = 0
    matrix = []
    buf = []
    pixel_sektor = 1
    while y < im.size[1]:
        while x < im.size[0]:
            if im.getpixel((x,y)) == 0:
                buf.append(1)
            else:
                buf.append(0)
            x+=pixel_sektor
        x=0
        y+=pixel_sektor
        matrix.append(buf)
        buf = []
    #print len(matrix)
    #print len(matrix[0])
    i = 0
    j = 0
    objects = []
    flag = False
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                Per = checkP(im, matrix, i, j)
                objects.append(Per)
    #print len(objects)
    return objects
