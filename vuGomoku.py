#1
'''
A *player* p is either 0 (drawn pink) or 1 (blue).

An *intersection* I is a pair (x,y) where x,y are integers and -9<=x,y<=9.

A *game state* G is a 6-member list in which:

    G[0] is {I:I is taken by player 0}.

    G[1] is {I:I is taken by player 1}.

    G[2] is either 0 or 1, indicating whose turn it is.

    G[3] is None. By adding G[3], I manipulate indicies of members of G to remind myself that
    G[0] is related to G[4] and G[1] to G[5].

    G[4] is the list of intersections taken by player 0 in order; G[4][0] is the last move

    G[5] is the list of intersections taken by player 1 in order; G[5][0] is the last move
'''

#2
def BoardFull():return\
    len(G[0]|G[1])==19**2

#3

def FiveRow(p):return\
    FiveRowH(p) or FiveRowV(p) or FiveRowDP(p) or FiveRowDN(p)

def FiveRowH(p):
    for x in range(-9,10):
        for y in range(-9,10):
            if rowSetH(x,y)<=G[p]:
                return True
    return False
def FiveRowV(p):
    for x in range(-9,10):
        for y in range(-9,10):
            if rowSetV(x,y)<=G[p]:
                return True
    return False
def FiveRowDP(p):
    for x in range(-9,10):
        for y in range(-9,10):
            if rowSetDP(x,y)<=G[p]:
                return True
    return False
def FiveRowDN(p):
    for x in range(-9,10):
        for y in range(-9,10):
            if rowSetDN(x,y)<=G[p]:
                return True
    return False

def rowSetH(x,y):return {(x,y),(x+1,y),(x+2,y),(x+3,y),(x+4,y)}
def rowSetV(x,y):return {(x,y),(x,y+1),(x,y+2),(x,y+3),(x,y+4)}
def rowSetDP(x,y):return {(x,y),(x+1,y+1),(x+2,y+2),(x+3,y+3),(x+4,y+4)}
def rowSetDN(x,y):return {(x,y),(x+1,y-1),(x+2,y-2),(x+3,y-3),(x+4,y-4)}

#4
def GameOver():return BoardFull() or FiveRow(0) or FiveRow(1)

#5
def Clicked(I):
    point=image(I)
    return (point[0]-mouseX)**2+(point[1]-mouseY)**2<radius**2 and\
           mouseDown and not oldMouseDown

######################################################################

from EaselLib import *

def windowDimensions():
    return (width,height)

def init():
    global G
    G=[set(),set(),0,None,[],[]]

def All():
    Set=set()
    for x in range(-9,10):
        for y in range(-9,10):
            Set=Set|{(x,y)}
    return Set

def Empty(G):return All()-G[0]|G[1]

def update():
    global G
    while undoClicked():
        if G[2]==1 and G[4]!=[]:
            G[0]=G[0]-{G[4][0]}
            G[4]=G[4][1:]
            G[2]=0
            break
        if G[2]==0 and G[5]!=[]:
            G[1]=G[1]-{G[5][0]}
            G[5]=G[5][1:]
            G[2]=1
            break
        break
    if resetClicked():return init()
    if not GameOver():
        if G[2]==0:
            for I in Empty(G):
                if Clicked(I):
                    G[0]=G[0]|{I}
                    G[2]=1
                    G[4]=[I]+G[4]
        if G[2]==1:
            for I in Empty(G):
                if Clicked(I):
                    G[1]=G[1]|{I}
                    G[2]=0
                    G[5]=[I]+G[5]

def undoClicked():
    x=5*scale
    y=9*scale+space/2
    return abs(mouseX-x)<space/2 and abs(mouseY-y)<space/3 and\
           mouseDown and not oldMouseDown

def resetClicked():
    x=8*scale
    y=9*scale+space/2
    return abs(mouseX-x)<space/2 and abs(mouseY-y)<space/3 and\
           mouseDown and not oldMouseDown

######################################################################

width=800
height=800
font=25
scale=35
radius=12
space=height/2-9*scale
black=(0,0,0)
pink=(255,102,255)
blue=(96,96,255)
color=[pink,blue]

def image(I):return (I[0]*scale,I[1]*scale)

def display():return\
    text()+board()+stones(0)+stones(1)+rowSprite(0)+rowSprite(1)

######################################################################

def text():return\
    title()+status()+undoButton()+resetButton()+credit()

def title():
    x=-8*scale
    y=9*scale+space/2
    return [txt('Gomoku',(x,y),font,black)]
def status():
    x=-5*scale
    y=9*scale+space/2
    if FiveRow(0):
        return [txt('Pink Wins',(x,y),font,pink)]
    if FiveRow(1):
        return [txt('Blue Wins',(x,y),font,blue)]
    if BoardFull():
        return [txt('Draw',(x,y),black)]
    else:
        return [txt(turn(),(x,y),font,color[G[2]])]
def undoButton():
    x=5*scale
    y=9*scale+space/2
    label=[txt('Undo',(x,y),font,black)]
    HL=[seg((x-space/2,y-space/3),(x+space/2,y-space/3),black)]
    HU=[seg((x-space/2,y+space/3),(x+space/2,y+space/3),black)]
    VL=[seg((x-space/2,y-space/3),(x-space/2,y+space/3),black)]
    VR=[seg((x+space/2,y-space/3),(x+space/2,y+space/3),black)]
    frame=HL+HU+VL+VR
    return label+frame
def resetButton():
    x=8*scale
    y=9*scale+space/2
    label=[txt('Reset',(x,y),font,black)]
    HL=[seg((x-space/2,y-space/3),(x+space/2,y-space/3),black)]
    HU=[seg((x-space/2,y+space/3),(x+space/2,y+space/3),black)]
    VL=[seg((x-space/2,y-space/3),(x-space/2,y+space/3),black)]
    VR=[seg((x+space/2,y-space/3),(x+space/2,y+space/3),black)]
    frame=HL+HU+VL+VR
    return label+frame
def credit():
    y=-9*scale-space/2
    return\
    [txt('Easel_PY: Dr. J. Nelson Rushton & Dr. Qianji Zheng. Gomoku: Vu Phan. TTU.',
         (0,y),font,black)]

def turn():
    if not GameOver():
        return "Pink's Turn" if G[2]==0 else\
               "Blue's Turn"

######################################################################

def board():return boardH()+boardV()

def boardH():
    sprite=[]
    for y in range(-9,10):
        sprite=sprite+[seg(image((-9,y)),image((9,y)),black)]
    return sprite
def boardV():
    sprite=[]
    for x in range(-9,10):
        sprite=sprite+[seg(image((x,-9)),image((x,9)),black)]
    return sprite

######################################################################

def stones(p):
    sprite=[]
    for I in G[p]:
        sprite=sprite+[disc(image(I),radius,color[p])]
    return sprite

######################################################################

def rowSprite(p):return rowSpriteH(p)+rowSpriteV(p)+rowSpriteDP(p)+rowSpriteDN(p)

def rowSpriteH(p):
    sprite=[]
    for x in range(-9,10):
        for y in range(-9,10):
            if rowSetH(x,y)<=G[p]:
                sprite=sprite+[seg(image((x,y)),image((x+4,y)),color[p])]
    return sprite
def rowSpriteV(p):
    sprite=[]
    for x in range(-9,10):
        for y in range(-9,10):
            if rowSetV(x,y)<=G[p]:
                sprite=sprite+[seg(image((x,y)),image((x,y+4)),color[p])]
    return sprite
def rowSpriteDP(p):
    sprite=[]
    for x in range(-9,10):
        for y in range(-9,10):
            if rowSetDP(x,y)<=G[p]:
                sprite=sprite+[seg(image((x,y)),image((x+4,y+4)),color[p])]
    return sprite
def rowSpriteDN(p):
    sprite=[]
    for x in range(-9,10):
        for y in range(-9,10):
            if rowSetDN(x,y)<=G[p]:
                sprite=sprite+[seg(image((x,y)),image((x+4,y-4)),color[p])]
    return sprite
