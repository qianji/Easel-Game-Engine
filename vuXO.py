from Easel import *
black = (0,0,0)
def grid():
    L1 = seg((-50,150),(-50,-150),black)
    L2 = seg((50,150),(50,-150),black)
    L3 = seg((-150,50),(150,50),black)
    L4 = seg((-150,-50),(150,-50),black)
    return [L1,L2,L3,L4]

#1 xImagePt: point -> sprite
def xImagePt(p):
    x=p[0]
    y=p[1]
    s1=seg((x-45,y-45),(x+45,y+45),black)
    s2=seg((x-45,y+45),(x+45,y-45),black)
    return [s1,s2]

#2 oImagePt: point -> sprite
def oImagePt(p):return [circ(p,45,black)]

#3 xCenter: cell -> int
def xCenter(c):return\
    -100 if c%3==1 else\
    0 if c%3==2 else\
    100

#4 yCenter: cell -> int
def yCenter(c):return\
    -100 if 7<=c<=9 else\
    0 if 4<=c<=6 else\
    100

#5 center: cell -> point
def center(c):return (xCenter(c),yCenter(c))

#6 xImageCell: cell -> sprite
def xImageCell(c):return xImagePt(center(c))

#7 oImageCell: cell -> sprite
def oImageCell(c): return oImagePt(center(c))

def display():return\
    grid()+xImageCell(1)+oImageCell(2)
