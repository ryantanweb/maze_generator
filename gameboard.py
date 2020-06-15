from graphics import *



def drawVline(x):
    pt1 = Point(x,0)
    pt2 = Point(x,1000)
    return Line(pt1, pt2)

def drawHline(y):
    pt1 = Point(0,y)
    pt2 = Point(1000,y)
    return Line(pt1, pt2)
