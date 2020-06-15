from graphics import *
from gameboard import *

win = GraphWin("Maze Game", 1000, 1000)


for x in range(20):
    drawVline(x * 50).draw(win)
for y in range(20):
    drawHline(y * 50).draw(win)







#   *Click to close the opened window
win.getMouse()
