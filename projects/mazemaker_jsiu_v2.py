# Challenge yourself and practice learning from outside resources
# by following this tutorial to build a maze generator:
# https://medium.com/swlh/fun-with-python-1-maze-generator-931639b4fb7e

# unvisited blocks will be 'u'

# Maze generator -- Randomized Prim Algorithm

## Imports
import random
import time
from colorama import init
from colorama import Fore, Back, Style

#def print maze
height = 4
width = 4
wall = 'w'
cell = 'c'
unvisited = 'u'
maze=[]

def printMaze(maze):
    for i in range(height):
        for j in range(width):
            print(maze[i][j], end=" ")
        print("\n")
    
#def surrounding cells
m=printMaze(maze)
