import copy

import sys
from PIL import Image

class obj:
    points = []
    S = 0
    def checkExistance(self, ij):
        return self.points.count(ij)
    def selectObject(self, im, matrix, i, j):
        a = copy.deepcopy(i)
        b = copy.deepcopy(j)
        self.points.append((a,b))
        self.S += 25
        matrix[a][b] = 2
        im.putpixel((b*5,a*5), 100)
        if a < len(matrix)-2:
            if matrix[a+1][b] == 1 and self.checkExistance((a+1, b)) == 0:
                self.selectObject(im, matrix, a+1, b)
        if a > 0:
            if matrix[a-1][b] == 1 and self.checkExistance((a-1, b)) == 0:
                self.selectObject(im, matrix, a-1, b)
        if b < len(matrix[0])-2:
            if matrix[a][b+1] == 1 and self.checkExistance((a, b+1)) == 0:
                self.selectObject(im, matrix, a, b+1)
        if b > 0:
            if matrix[a][b-1] == 1 and self.checkExistance((a, b-1)) == 0:
                self.selectObject(im, matrix, a, b-1)
        return 0

def selectSquere(imageTrans):
    im = imageTrans

    x = 0
    y = 0
    matrix = []
    buf = []
    while y < im.size[1]:
        while x < im.size[0]:
            if im.getpixel((x,y)) == 0:
                buf.append(1)
            else:
                buf.append(0)
            x+=5
        x=0
        y+=5
        matrix.append(buf)
        buf = []
    i = 0
    j = 0
    objects = []
    objectsSquere = []
    backgr = 0
    flag = False
    #sys.setrecursionlimit(5000)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                for k in objects:
                    if k.checkExistance((i, j)) != 0:
                        flag = True
                if not flag:
                    objects.append(obj())
                    objects[len(objects)-1].selectObject(im, matrix, i, j)
                    #print "Object #", len(objects), " created!"
                    #print "His squere is ", objects[len(objects)-1].S
                    objectsSquere.append(objects[len(objects)-1].S)
                flag = False
            else:
                backgr+=25
    objectsSquere.append(backgr)
    return objectsSquere