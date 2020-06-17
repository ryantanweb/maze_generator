from graphics import *
from gameboard import *
from pathway import *
"""
win = GraphWin("Maze Game", 1000, 1000)

#   *Draws the 400 tiles map
for x in range(20):
    drawVline(x * 50).draw(win)
for y in range(20):
    drawHline(y * 50).draw(win)
"""

#   *2d-representation array of the maze
maze_array = []
for x in range(20):
    for y in range(20):
        if y == 0:
            temprow_array = []
        temprow_array.append(False)
        if y == 19:
            maze_array.append(temprow_array)

#   *maze_array is now primed. False means there is an impassible wall.
visualize2DArray(maze_array)

#   *Click to close the opened window
win.getMouse()
