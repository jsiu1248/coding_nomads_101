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


## Functions
def printMaze(maze):
    for i in range(0, height):
        for j in range(0, width):
            if (maze[i][j] == 'u'): # what does this do?
                print(Fore.WHITE + str(maze[i][j]), end=" ") #if unvisited then white
            elif (maze[i][j] == 'c'):
                print(Fore.GREEN + str(maze[i][j]), end=" ") #if cell then green
            else:
                print(Fore.RED + str(maze[i][j]), end=" ") # if wall then red and what doe str(maze[i][i]) print?

        print('\n')

# Make the wall a passage and mark the unvisited cell as part of the maze
# Find number of surrounding cells
def surroundingCells(rand_wall):
    s_cells = 0
    if (maze[rand_wall[0] - 1][rand_wall[1]] == 'c'):
        s_cells += 1
    if (maze[rand_wall[0] + 1][rand_wall[1]] == 'c'):
        s_cells += 1
    if (maze[rand_wall[0]][rand_wall[1] - 1] == 'c'):
        s_cells += 1
    if (maze[rand_wall[0]][rand_wall[1] + 1] == 'c'):
        s_cells += 1

    return s_cells


## Main code
# Init variables
wall = 'w'
cell = 'c'
unvisited = 'u'
height = 4
width = 4
maze = []
wall=[]

# Initialize colorama
init() # why does this need to be initialized?

# Denote all cells as unvisited
for i in range(0, height):
    line = []
    for j in range(0, width):
        line.append(unvisited)
    maze.append(line)

# Randomize starting point and set it a cell
starting_height = int(random.random() * height)
starting_width = int(random.random() * width)
if (starting_height == 0):
    starting_height += 1
if (starting_height == height - 1):
    starting_height -= 1
if (starting_width == 0):
    starting_width += 1
if (starting_width == width - 1):
    starting_width -= 1

#pick a starting point
#top left is 0,0
#every adjacent cell is considered a wall
#assuming all the cells is a wall
#carving out the maze from the wall

#append list of walls
#append every adajecent cell to the starting point
#append x,y position to the list
#x -1, y and x



# Print final maze
printMaze(maze)

# a cell