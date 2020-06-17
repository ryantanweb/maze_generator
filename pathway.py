from random import *

def visualize2DArray(array):
    for a in array:
        print(a)

def pathway_map_start(maze_array, seed):
    seed(seed)
    start = randomInt(0,19)
    maze_array[start][1] = False


def rightHall():
    return null

def leftHall():
    return null

def upHall():
    return null

def downHall():
    return null
